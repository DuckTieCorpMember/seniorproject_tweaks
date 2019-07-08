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
  mounted: function () {
    this.getVisitors();

    setInterval(function () {
      this.getVisitors();
    }.bind(this), 1000); 
  },
  methods: {
    async getVisitors(){
      // eslint-disable-next-line
      console.log("A!")
      const responce = await axios.get({
        url: 'http://127.0.0.1:8000/visitors/',
        method: 'get'
      })
      // eslint-disable-next-line
      console.log(responce)
    }
  },
}
</script>

<style scoped>

</style>
