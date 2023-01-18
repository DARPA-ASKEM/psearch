<template>
    <div class="autocomplete">
      <Textarea
      rows="5" cols="30"
        v-model="search"
        @input="onChange"
      ></Textarea>

      <ul
        v-show="isOpen"
        class="autocomplete-results"
      >
        <li
          v-for="(result,i) in results"
          :key="i"
          @click="setResult(result)"
          class="autocomplete-result"
        >
          {{result}}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
import Textarea from 'primevue/textarea';

  export default {
    name: 'SearchAutocomplete',
    components:{
            Textarea,

        },
    props: {
      query:String,
      items: {
        type: Array,
        required: false,
        default: () => [],
      },
  },
    data(){
        return{
            search:this.query,
            isOpen: false,
            results:[]
        }
    },
    methods:{
      filterResults(){
              if (this.search.includes(':')){
                this.results = this.items.filter(item => item.toLowerCase().indexOf(this.search.split(":").at(-1).toLowerCase()) > -1);

              }

              if(this.search.charAt(this.search.length-1)==":"){
                this.isOpen = true;
              }
            },
      onChange(){
          this.filterResults();
          this.$emit('update:query', this.search)
        },
      setResult(result) {
        console.log(this.search.split(":"))
        this.search = this.search.split(":").slice(0, -1).join(":") + ":"+ result;
        this.isOpen = false;

         this.$emit('update:query', this.search)
     
    },
    
    },
    mounted() {
            this.search=this.query
        }
  };
  </script>

  <style>
  .autocomplete {
    position: relative;
  }

  .autocomplete-results {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    min-height: 1em;
    max-height: 6em;    
    overflow: auto;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>