### Test 1

- Question: Return count of all Simulation plans
- Query: `match (p:Plan) return count(p)`
- Success: Yes


### Test 2
- Question: What intermediates are related to models?
- Query:  `Match (m:Model)-[r *1..]->(i:Intermediate) Return m,r,i`
- Success: Kinda


### Test 3
- Question: poetry run psearch "Return the revision for the model with an id of 5"
- Query: `Match (rev:ModelRevision)-[r *1..]->(m:Model) where (m.id=5) return rev`
- Query(EXACT RERUN): `Match (mr:ModelRevision)<-[r:BEGINS_AT]-(m:Model) where (m.id=5) return mr`
- Success: No, almost
