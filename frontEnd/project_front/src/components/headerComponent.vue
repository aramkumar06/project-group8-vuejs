<template>

<div>
    <v-layout>
        <v-img
          :src="require('@/assets/logo.png')"
          class="mr-5"
          contain
          height="48"
          width="48"
          max-width="48"
          
        />
        <v-spacer />
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          :to="{ name: link.name, params: { cate: 123 }}"
          @click="onClick($event, link)"
          text
          large
        >
          {{ link.text }}
        </v-btn>
        <v-spacer />
        <v-text-field
          append-icon="mdi-magnify"
          flat
          hide-details
          solo-inverted
          style="max-width: 300px;"
        />
      </v-layout>
</div>

</template>


<script>

import {
    mapGetters
}from 'vuex'

export default {
    computed : {
        ...mapGetters(['links'])
    },
    methods: {
      
      onClick (e, item) {
        e.stopPropagation()

        console.log(item.text+ " " + item.to)
        if (item.to || !item.href) return

        //this.$vuetify.goTo(item.href)
      }
    },
    
}

</script>

<style scoped>

#header {
    background-color : #999999;
    position : absolute;
    

}

</style>