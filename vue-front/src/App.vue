<template>
  <v-app>
    <v-container>
      <v-layout row>
        <v-flex shrink pa-1>
          <v-card dark color="green darken-3">
            <v-list two-line subheader>
              <v-list-tile
                v-for="item in items"
                :key="item.title"
                avatar
                v-on:="">

                <v-list-tile-avatar>
                  <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
                </v-list-tile-avatar>

                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
                </v-list-tile-content>

              </v-list-tile>
              </v-list>
          </v-card>
        </v-flex>
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
export default {
  name: 'App',
  components: {

  },
  data () {
    return {
      items: [
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos'},
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes'},
          { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work'}
        ],
        dirs: [],
    }
  },
  computed: {

  },
  methods: {

  },
}
</script>

<style scoped>

</style>
