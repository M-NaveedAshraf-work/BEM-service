<template>
  <v-app>
    <v-app-bar
      app
      color="teal darken-4"
      dark
    >
      <v-toolbar-title>BEM Interactive Dashboard</v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="text-center">
        <v-btn>
          <router-link to="/">Input</router-link>
        </v-btn>
       <v-btn>
          <router-link to="/CapX_Cal">CapX and Calibration</router-link>
        </v-btn>
        <v-btn>
          <router-link to="/UQ">UQ</router-link>
        </v-btn>
        <v-btn>
          <router-link to="/Output">Output</router-link>
        </v-btn>
      </div>
      
      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
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

  data: () => ({
    //
  }),
};
</script>
