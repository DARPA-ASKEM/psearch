<template>
    <div>   
        <h1>Ask openai to generate a cypher query for you</h1>

        <Textarea  v-model="value" rows="5" cols="30" ></Textarea>
        <h3>Latest query: <span class="query" >{{this.latestQuery}}</span></h3>
        <br/>
        
        <Button label="Send" @click="sendToOpenAi($event)"></Button>

        <div class="main-container">
            <div class="graph-renderer" id="viz"></div>
        </div>
    </div>
 
</template>

<script>
    import NeoVis from 'neovis.js';
    import graphConfig from '../assets/config'
    import Button from 'primevue/button';
    import Textarea from 'primevue/textarea';
    import axios from "axios"


    let neovisInstance;
    export default {
        name: "GraphVisualizer",
        components:{
            Textarea,
            Button,
        },
        data() {
        return {
            latestQuery: "hi",
            };
        },
        
       
        methods: {
            
            renderGraph(config_v=null) {
                let config;
                if (config_v==null){
                    config = graphConfig()
                }else{
                    config=config_v
                }
                    
                this.latestQuery=config.initialCypher
                neovisInstance = new NeoVis(config);
                neovisInstance.render();
            },
            sendToOpenAi(event){

                if (this.value.toLowerCase().includes("delete")){
                        alert("Unable to delete nodes or edges")
                        return
                    }
                if (this.value.toLowerCase().includes("create")){
                    alert("Unable to create nodes or edges")
                    return
                }
                axios.get("http://localhost:8001/experimental/cql?query="+this.value).then((resp) => {
                    let config;
                    config = graphConfig()
                    if (resp.data.toLowerCase().includes("delete")){
                        alert("Unable to delete nodes or edges")
                        return
                    }
                    if (resp.data.toLowerCase().includes("create")){
                        alert("Unable to create nodes or edges")
                        return
                    }
                    config.initialCypher=resp.data
                    this.renderGraph(config)
                
                    })

        }
            
        },
        mounted() {
            this.renderGraph(this.config);
        }
    }
</script>

<style scoped>
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
</style>