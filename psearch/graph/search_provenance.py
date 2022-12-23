from neo4j import Driver

from typing import Optional


class SearchProvenance:
    def __init__(self,  graph_db: Optional[Driver] = None):
        self.graph_db = graph_db
    
    
    
    def send_generated_query(self,query_string):
        
        with self.graph_db.session() as session:            

            query = (
                f"{query_string}"
            )

            response = session.run(query)

            return [
                { "node": res.data()}
                for res in response
            ]

    
