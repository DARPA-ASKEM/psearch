// import NeoVis from 'neovis.js';
function graphConfig () {
  return {
    containerId: 'viz',
    neo4j: {
      serverUrl: process.env.NEO4J_URI || 'bolt://localhost:7687',
      serverUser: process.env.NEO4J_USER || 'neo4j',
      serverPassword: process.env.NEO4J_PASSWORD || 'password'
    },
    visConfig: {
      clickToUse: true,
      layout: {
          improvedLayout: true,
          hierarchical: {
            enabled: false,
            direction: 'UD',
            sortMethod: 'hubsize',
            parentCentralization: false,
            blockShifting: true,
            edgeMinimization: false
          }
        },
        interaction: {
          dragNodes: true,
          navigationButtons: true,
          multiselect: true,
          hover: true,
          hoverConnectedEdges: true,
          tooltipDelay: 300
        },
      nodes: {
        borderWidth:2,
      },
      
    },
    labels: {
      Publication: {
        title: "id",
        label:"name",
        value:"id",
        caption:"id",
        group: "name",
        },
      Dataset: {
          title: "id",
          label:"name",
          value:"id",
          caption:"id",
          group: "name",
          color:"#d5726e",
          },
      Intermediate: {
        title: "id",
        value:"id",
        label: "name",
        caption:"id",
        group: "name",
        color:"#ff0000"
        },
      Model: {
          title: "id",
          label:"name",
          caption:"id",
          value:"id",
          group: "name",
          color:"#02a353",
          shape:"square"
          },
      Simulation_run: {
        title: "id",
        label:"name",
        caption:"id",
        value:"id",
        group: "name",
        color:"#4e87b5",
        shape:"ellipse"
        },
      Plan: {
        title: "id",
        label:"name",
        caption:'id',
        value:"id",
        group: "name",
        color:"#00c2fe",
        },
      Model_revision:{
        title: "id",
        label:"name",
        caption:"id",
        value:"id",
        group: "name",
        color:"#f3ec4b",
        shape:"square"
      }
  },
  relationships: {
      EDITED_FROM: {
          "label": "name",
      },
      EXTRACTED_FROM: {
          "label": "name",
      },
      REINTERPRETS: {
          "label": "name",
      },
      BEGINS_AT: {
          "label": "name",
      },
      COPIED_FROM:{
        "label":"name"
      },
      CITES:{
        "label":"name"
      },
      USES:{
        "label":"name"
      },
      EQUIVALENT_OF:{
        "label":"name"
      },
      GENERATED_BY:{
        "label":"name"
      },
      DECOMPOSED_FROM:{
        "label":"name"
      },
      GLUED_FROM:{
        "label":"name"
      },
      STRATIFIED_FROM:{
        "label":"name"
      },
  },
    initialCypher: "MATCH (n)-[r]-() RETURN * LIMIT 300"}}
 

export default graphConfig
