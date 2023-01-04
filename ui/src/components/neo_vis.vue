<template>
    <div>   
        <h1>Semantically search the TERArium provenance graph</h1>
        <div class="rowquery">
            <div class="columnquery">
                <Textarea  v-model="value" rows="5" cols="34" ></Textarea>
                <Button  label="Send" @click="sendToOpenAi()">Convert to Query</Button>
            </div>
            <div class="columnquery">
                <SearchAutocomplete
                    :key="conponentKey"
                    @clicked="clicked_show"
                    :items="[
                        'BEGINS_AT',
                        'CITES',
                        'COMBINED_FROM',
                        'COPIED_FROM',
                        'Dataset',
                        'DECOMPOSED_FROM',
                        'EDITED_FROM',
                        'EXTRACTED_FROM',
                        'GENERATED_BY',
                        'GLUED_FROM',
                        'Intermediate',
                        'Model',
                        'ModelRevision',
                        'Plan',
                        'Publication',
                        'REINTERPRETS',
                        'SimulationRun',
                        'STRATIFIED_FROM',
                        'USES',
                    ]"
                    v-model:query="currentQuery"
            />
        <Button class="update_button" label="Send" @click="update_graph()">Run Query</Button>
            </div>
        
        </div>
        <br/>

        <h3>Last query: <span class="query" >{{this.lastQuery}}</span></h3>
        
        <div class="main-container">
            <div class="graph-renderer" id="viz"></div>
        </div>
        <br/>
        <div class="row">
            <div class="column">
            Types of nodes:
                <ul>
                    <li>Publication</li>
                    <li>Intermediate</li>
                    <li>Model</li>
                    <li>ModelRevision</li>
                    <li>Plan</li>
                    <li>SimulationRun</li>
                    <li>Dataset</li>
                </ul>
            </div>
            <div class="column">

            Types of edges:
                <ul>
                    <li>CITES</li>
                    <li>COPIED_FROM</li>
                    <li>COMBINED_FROM</li>
                    <li>EDITED_FROM</li>
                    <li>DECOMPOSED_FROM</li>
                    <li>GLUED_FROM</li>
                    <li>STRATIFIED_FROM</li>
                    <li>USES</li>
                    <li>EQUIVALENT_OF</li>
                    <li>EXTRACTED_FROM</li>
                    <li>REINTERPRETS</li>
                    <li>GENERATED_BY</li>
                    <li>BEGINS_AT</li>
                </ul>
            </div>
            <div class="column">

            Allowed connections:
                <ul>
                    <li>CITES</li>
                        <ul>
                            <li>Publication -> Publication</li>
                        </ul>
                    <li>COPIED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>COMBINED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>EDITED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>DECOMPOSED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>GLUED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>STRATIFIED_FROM</li>
                        <ul>
                            <li>ModelRevision -> ModelRevision</li>
                        </ul>
                    <li>USES</li>
                        <ul>
                            <li>Plan -> ModelRevision</li>
                        </ul>
           
                    <li>EXTRACTED_FROM</li>
                        <ul>
                            <li>Intermediate -> Publication</li>
                            <li>Dataset -> Publication</li>
                        </ul>
                    <li>REINTERPRETS</li>
                        <ul>
                            <li>Dataset -> SimulationRun</li>
                        </ul>
                    <li>GENERATED_BY</li>
                        <ul>
                            <li>SimulationRun -> Plan</li>
                        </ul>
                    <li>BEGINS_AT</li>
                        <ul>
                            <li>Model -> ModelRevision</li>
                        </ul>
                </ul>
            </div>


        </div>

        
    </div>
 
</template>

<script>
    import NeoVis from 'neovis.js';
    import graphConfig from '../assets/config'
    import Button from 'primevue/button';
    import Textarea from 'primevue/textarea';
    import axios from "axios"
    import SearchAutocomplete from './autocomplete.vue'
 

    let neovisInstance;
    export default {
        name: "GraphVisualizer",
        components:{
            Textarea,
            Button,
            SearchAutocomplete
        },
        data() {
        return {
            lastQuery:"",
            currentQuery: "",
            value:null,
            conponentKey:0
            };
        },
        
       
        methods: {
            forceRerender(){
                this.conponentKey += 1;
            },
            clicked_show(query){
                this.currentQuery=query
                console.log(this.currentQuery)
            },
            
            renderGraph(config_v=null) {
                let config;
                if (config_v==null){
                    config = graphConfig()
                }else{
                    config=config_v
                }
                    
                this.lastQuery=config.initialCypher
                neovisInstance = new NeoVis(config);
                neovisInstance.render();
            },
           
            sendToOpenAi(){

                if (this.value.toLowerCase().includes("delete")){
                        alert("Unable to delete nodes or edges")
                        return
                    }

                axios.get("http://localhost:8001/experimental/cql?query="+this.value).then((resp) => {
                    
                    if (resp.data.toLowerCase().includes("delete")){
                        alert("Unable to delete nodes or edges")
                        return
                    }
                    if (resp.data.toLowerCase().includes("create")){
                        alert("Unable to create nodes or edges")
                        return
                    }
                    this.currentQuery=resp.data
                    this.forceRerender()
                
                    })

        },
        update_graph(){
            let config;
            config = graphConfig()
            config.initialCypher=this.currentQuery
            this.renderGraph(config)
        }
            
        },
        mounted() {
            this.renderGraph(this.config);
        }
    }
</script>

<style scoped>
    .update_button{
        background-color: #4CAF50;
    }
    .main-container {
        height: 600px;
    }
    .query{
        color: red;
    }
    #viz  {
        background: #fff;
        border-radius: 15px;
        height: calc(100% - 84px) !important;
        padding: 20px;
        overflow: hidden;
        max-height: 766px;
    }

    .column {
  float: left;
  width: 33.33%;
  background-clip: content-box;

  background-color: #D3D3D3;
  padding:5px
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.columnquery {
  float: left;
  width: 33.33%;

  padding:5px
}

/* Clear floats after the columns */
.rowquery:after {
  content: "";
  display: table;
  clear: both;
}
</style>