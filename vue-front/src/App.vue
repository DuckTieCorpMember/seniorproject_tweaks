<template>
  <v-app>
    <v-container>
      <v-layout row>
        <list-view :items="items" />
        <v-flex grow pa-1>
          <v-card dark color="green">
            <v-card-text>Banana</v-card-text> 
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import ListView from './views/ListView.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    ListView,
  },
  data () {
    return {
      items: [
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos'},
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes'},
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work'}
        ],
    }
  },
  mounted: function (){
    this.getVisitors();
  },
  computed: {

  },
  methods: {
    async getVisitors(){
      axios.get('http://127.0.0.1:8000/visitors/').then(res => {
        const items = res.data;
        this.items=[];
        items.forEach(element => {
          this.items.push({
            icon: 'folder',
            iconClass: 'grey lighten-1 white--text',
            title: element.visitorName,
          });
        });
      })
    }
  },
}
</script>

<style scoped>

</style>
