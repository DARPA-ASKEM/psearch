from fastapi import FastAPI  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/")   
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import json

import requests

from fastapi import  Depends, HTTPException, Query, Response, status
from fastapi.logger import logger
from graph.neo4j import request_engine as request_graph_db
from graph.search_provenance import SearchProvenance

import sys

import openai

from psearch.env import token

openai.api_key = token

ostensible_db_def = """
I will type "Question:" followed by a question or command in English like "Question: Count all Publications" and you will return a 
single line print "Query:" Followed by an openCypher query like "Query: `match (p:publication) return count(p)`

Question: Match all nodes in the database
Query: `Match (n) return n`

Question: Which composed models are derived from Paper with ID of 1?
Query: `Match (m:model)-[r *1..]-> (i:intermediate)- [r2:EXTRACTED_FROM]->(p:publication) where p.id=1 return m`

Question: Which datasets are associated with which model primitives?
Query: `match (d:dataset)-[r *1..]-(i:intermediate) return labels(d),d,i`

Question: Return simulators that rely on Primitive with ID of 12 or 4
Query: `match (p:plan)-[r *1..]->(i:intermediate) where i.id=4 or i.id=12 return p,r,i`

Question: Which simulators were created by User with ID 999?
Query: `match (p:plan)-[r:USES]->(mr:model_revision) where r.user_id=999 return p`

Question: What are prior versions of this composed model with id 5?
Query: `Match (rev:model_revision)<-[r:BEGINS_AT]-(m:model) where (m.id=5) match (rev2:model_revision)<-[r2 *1.. ]-(rev) return rev,rev2`
"""



@app.post("/neo4j_query")
def model_opt(
    payload: dict,
    graph_db=Depends(request_graph_db),
) -> Response:

    search_handler = SearchProvenance( graph_db=graph_db)
    
    preamble = ostensible_db_def
    user_query = f"""
    Question: {payload.get('user_query')}
    Query: 
    """
    prompt = preamble + "\n" + user_query
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=64)
    print(completion.choices[0].text.lower())
    query=completion.choices[0].text.lower().strip()[1:-1]
    data=search_handler.send_generated_query(query_string=query)
    logger.info("new model created: %i", id)
    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"query":query,"data":data}),
    )


@app.get("/search") 
def search_provenance():    

  return {"message": "Hey, It is me Goku"}