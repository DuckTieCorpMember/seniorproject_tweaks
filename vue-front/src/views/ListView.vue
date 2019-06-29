<template>
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
</template>

<script>
export default {
    props: {
        items: {
            type: Array,
            default: null,
            required: true,
        }
    }
}
</script>

<style scoped>

</style>
