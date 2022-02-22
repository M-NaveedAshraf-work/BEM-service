<template>

  <!-- Top Portion with file inputs, building info, and running the BEM -->

  <v-container grid-list-md>
    <v-row no-gutters>
      <v-col
        md="5">
        <v-card>
          <v-card-title>Input Files</v-card-title>
          <v-card-text>Upload Weather File</v-card-text>
          <v-file-input
            accept="xls/*"
            label="Weather File"
          ></v-file-input>
          <v-card-text>Upload Building JSON File</v-card-text>
          <v-file-input
            accept="json/*"
            label="Building File"
          ></v-file-input>
        </v-card>
        <v-card outlined color="transparent">
          <v-card-title>     </v-card-title>
        </v-card>
        <v-card>
          <v-card-title>Run the BEM</v-card-title>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-select
                :items="output_period"
                label="Output Period"
                outlined
                dense
                ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
            >
              <v-btn
                align="center"
                depressed
                color="primary"
              >
              Run BEM
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col
        md="5"
        offset-md="2"
        >
        <v-card>
          <v-card-title
            align="center"
            >Building
          </v-card-title>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-text-field
                label="Building Name"
                outlined
                dense
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-text-field
                label="Building Location"
                outlined
                dense
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-select
                :items="terrain_class"
                label="Terrain Class"
                outlined
                dense
                ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="8"
              offset-md="1"
              >
              <v-text-field
                label="Building Ventilated Volume (m^3)"
                outlined
                dense
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="8"
              offset-md="1"
              >
              <v-text-field
                label="Building Height (m)"
                outlined
                dense
                type="number"
                ></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        Hello
      </v-col>
      <v-col>
        Hello
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

export default {
  data: () => ({
    terrain_class: ['Open Terrain', 'Country', 'Urban / City'],
    output_period: ['Hourly', 'Daily', 'Monthly'],
  }),
}
</script>
