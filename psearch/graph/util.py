
q="match (p:plan) return p"
q="match(i:intermediates)<-[r *1..]-(m:models)"+\
    "return i,m"
q="match(d:datasets)-[r *1..]-(i:intermediates)"+\
    "return d,r,i"
def dyanmic_id_mapping(query):
    id_node_types={}
    if "(" in query:
        split_query=query.split('(')
        for item in split_query:
            if ")" in item:
                key_value=item.split(")")[0]
                if ":" in key_value:
                    id_node_types[key_value.split(':')[0]]=key_value.split(':')[1]
    return id_node_types

def query_return_types(query,mapping):
    print(query)
    types_returned={}
    if "return" in query:
        return_types=query.split('return')[1]
        print(return_types)
        for type in return_types.split(','):
            types_returned[type.strip()]=mapping[type.strip()]
    return types_returned
mapping=dyanmic_id_mapping(q)
print(mapping)
types_returned=query_return_types(query=q,mapping=mapping)
print('h')
print(types_returned)