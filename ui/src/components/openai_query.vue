<template>

    <div >
        <h1>Ask openai to generate a cypher query for you</h1>

        <Textarea  v-model="value" rows="5" cols="30" ></Textarea>
        <br/>
        
        <Button label="Send" @click="sendToOpenAi($event)"></Button>

        <div>
        <DataTable :value="nodes" responsiveLayout="scroll">
            <Column field="id" header="ID"></Column>
         
        </DataTable>
    </div>
    </div>

  </template>
  
  <script>
  import Textarea from 'primevue/textarea';
  import Button from 'primevue/button';
  import DataTable from 'primevue/datatable'
  import Column from 'primevue/column'
  import axios from "axios"
  
  export default {
    name: 'OpenaiQuery',
    data() {
    return { value: "",
            nodes:[{"id":1},{"id":2}]
     } 
    },
    components:{
        Textarea,
        Button,
        DataTable,
        Column
    },
    methods:{
        sendToOpenAi(event){
            console.log(event)
            console.log(this.value)
            axios.post("http://localhost:8000/neo4j_query",{
                  user_query: this.value,
                  }).then((resp) => {
                console.log(resp)
                console.log(resp.data)
                let array_of_nodes=[]
                for(let node_ in resp.data['data']){
                  console.log(node_)
                  for (const [key, value] of Object.entries(resp.data['data'][node_]['node'])) {
                    console.log(key, value);
                    array_of_nodes.push({"id":value['id']})
                  }


                  
                }
                console.log('after')
                console.log(array_of_nodes)
                this.nodes=array_of_nodes
             
                })

        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  