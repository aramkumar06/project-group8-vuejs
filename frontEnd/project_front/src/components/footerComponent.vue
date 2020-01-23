<template>
 <v-footer
    class="py-4"
    dark
    height="auto"
  >
    <v-container mx-auto>
      <v-layout wrap>
        <v-flex xs9>
            <h1> 김주희, 김태민, 박진홍, 이상민, 홍기환 </h1>
        </v-flex>
        <v-spacer />
        <v-btn
          class="mr-0"
          square
          
          @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-chevron-up</v-icon>
        </v-btn>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<script>
export default {
    data: () => ({
      items: [
        {
          href: '#!',
          icon: 'mdi-twitter'
        },
        {
          href: '#!',
          icon: 'mdi-instagram'
        },
        {
          href: '#!',
          icon: 'mdi-facebook'
        },
        {
          href: '#!',
          icon: 'mdi-google-plus'
        },
        {
          href: '#!',
          icon: 'mdi-reddit'
        },
        {
          href: '#!',
          icon: 'mdi-discord'
        },
        {
          href: '#!',
          icon: 'mdi-pinterest'
        }
      ]
    })
}
</script>

<style scoped>

</style>