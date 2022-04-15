<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <v-app-bar
      app
      color="teal darken-4"
      dark
    >
      <v-toolbar-title>BEM Interactive Dashboard</v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="text-center">
        <v-btn to="/">
          Input
        </v-btn >
        <v-btn to="/UQ">
          Uncertainty Quantification
        </v-btn>
        <v-btn to="/CapX_Cal">
          CapX and Calibration
        </v-btn>
        <v-btn to="/Output">
          Output Graphs
        </v-btn>
      </div>
      
      <v-spacer></v-spacer>

      <v-btn
        href="https://www.joulea.com/"
        target="_blank"
        text
      >
        <span class="mr-2">Joulea Website</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

  export default {
    name: 'App',

    computed: {
      theme(){
        return (this.$vuetify.theme.light) ? 'dark' : 'light'
      }
    },

    data: () => ({
    }),
  };
</script>
