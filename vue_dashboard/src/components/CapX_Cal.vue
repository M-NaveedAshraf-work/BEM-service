<template>
  <v-container grid-list-md>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Genetic Algorithm Inputs</v-card-title>
              <v-col offset-md="1" md="10">
                <div>
                  <v-expansion-panels multiple>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Edit Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.population_size"
                            label = "Population Size [ea]"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.crossover_rate"
                            label = "Crossover Rate"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.mutation_rate"
                            label = "Mutation Rate"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.random_seed"
                            label = "Random Seed"
                            outlined
                            dense
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.max_time"
                            label = "Maximum Code Execution Time [min]"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="GASettings.top_percentage"
                            label = "Top Percentage of Selection"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </div>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-card-title>Calibration Setting Inputs</v-card-title>
              <v-col offset-md="1" md="10">
                <div>
                  <v-expansion-panels>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Edit Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-select
                            v-model="calSettings.data_interval"
                            :items="dateInterval"
                            label = "Calibration Data Interval"
                            outlined
                            dense
                          ></v-select>
                        </v-row>
                        <v-row>
                          <v-select
                            v-model="calSettings.electricity_data"
                            :items="ynBool"
                            label = "Electricity Data"
                            outlined
                            dense
                          ></v-select>
                        </v-row>
                        <v-row>
                          <v-select
                            v-model="calSettings.natural_gas_data"
                            :items="ynBool"
                            label = "Natural Gas Data"
                            outlined
                            dense
                          ></v-select>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="calSettings.cvrmse_criterion"
                            label = "cvRMSE Criterion [%]"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="calSettings.convergence_diff"
                            label = "Convergence Difference"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="calSettings.n_times_converge"
                            label = "N Times of Convergence"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </div>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>Schedule Calibration Parameters</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="scheduleHeaders"
                    :items="scheduleParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialogSchedule"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add Schedule Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editScheduleForm.name"
                                      :items='scheduleOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editScheduleForm.day"
                                      :items="dayType"
                                      label="Data Type"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editScheduleForm.min_hour"
                                      type="number"
                                      label="Minimum Hour"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editScheduleForm.max_hour"
                                      label="Maximum Hour"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editScheduleForm.min"
                                      label="Minimum Value"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editScheduleForm.max"
                                      label="Maximum Value"
                                    ></v-text-field>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="scheduleClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="scheduleSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDeleteSchedule" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="scheduleCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirmSchedule">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItemSchedule(item)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItemSchedule(item)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="getMessage"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>Monthly Internal Heat Gains</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="heatHeaders"
                    :items="heatParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialogHeat"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add Heat Gain Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.name"
                                      :items='heatOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.day"
                                      :items="floatInt"
                                      label="Data Type"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editHeatForm.min"
                                      type="number"
                                      label="Minimum Hour"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editHeatForm.max"
                                      label="Maximum Hour"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.min_month"
                                      :items="months"
                                      label="Minimum Value"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.max_month"
                                      :items="months"
                                      label="Maximum Value"
                                    ></v-select>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="heatClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="heatSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDeleteHeat" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="heatCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirmHeat">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItemHeat(item)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItemHeat(item)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="getMessage"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>Calibration Parameters</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="calHeaders"
                    :items="calParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-toolbar-title>My Calibration Parameters</v-toolbar-title>
                        <v-divider
                          class="mx-4"
                          inset
                          vertical
                        ></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialog"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add Calibration Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editCalForm.name"
                                      :items='calOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editCalForm.data"
                                      :items="floatInt"
                                      label="Data Type"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editCalForm.min"
                                      type="number"
                                      label="Minimum Value"
                                    ></v-text-field>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-text-field
                                      v-model="editCalForm.max"
                                      label="Maximum Value"
                                    ></v-text-field>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="calClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="calSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDelete" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="calCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItem(item)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItem(item)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="getMessage"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
              <v-row justify="center">
                <v-col>
                  <v-btn 
                    class = "ma-2"
                    align="center"
                    depressed
                    color="red"
                    v-on:click="combineCalibration();"
                  >Load Calibration Inputs</v-btn>
                </v-col>
                <v-col>
                  <v-btn 
                    class = "ma-2"
                    :loading= loading
                    :disabled= loading
                    align="center"
                    depressed
                    color="green"
                    v-on:click="runCalibration(); loadState();"
                  >Run Calibration</v-btn>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <div id="Cal">
                <div id="calchart" style="width: 800px;height:500px;"></div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
    <v-row>
      <v-container></v-container>
    </v-row>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Energy Star Inputs</v-card-title>
              <v-col offset-md="1" md="10">
                <v-row>
                  <v-expansion-panels>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Energy Star Score Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.grossArea"
                            label = "Non-Scoreble Gross Floor Area"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.dataGrossArea"
                            label = "Data Center Gross Area"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.officeGrossArea"
                            label = "Scoreable Gross Area"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.weeklyOperation"
                            label = "Weekly Operating Hours"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.workers"
                            label = "Number of Main Shift Workers"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.computers"
                            label = "Number of Computers"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.percentCooled"
                            label = "% of the Building that can be Cooled"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.coolingDays"
                            label = "Cooling Degree Days"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.heatingDays"
                            label = "Heating Degree Days"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.siteEUI"
                            label = "EUI of Site"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.sourceEUI"
                            label = "EUI of Source"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.siteConsumption"
                            label = "Energy Consuption of Site (kBTU)"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.score.sourceConsumption"
                            label = "Energy Consumption of Source (kBTU)"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Energystar Target Score Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.targetScore.current"
                            label = "Current EUI Score"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.targetScore.target"
                            label = "Target Energystar Score"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.targetScore.area"
                            label = "Scoreable Gross Floor Area"
                            outlined
                            dense
                            type="number"
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-select
                            v-model="energystarData.targetScore.unit"
                            :items="convertOptions"
                            label = "Converts Units form KBTU to kWh"
                            outlined
                            dense
                          ></v-select>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Benchmarking Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.benchmarkInput.minSQFT"
                            label = "Minimum Square Feet"
                            outlined
                            type="number"
                            dense
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.benchmarkInput.maxSQFT"
                            label = "Maximum Square Feet"
                            outlined
                            type="number"
                            dense
                          ></v-text-field>
                        </v-row>
                        <v-row>
                          <v-text-field
                            v-model="energystarData.benchmarkInput.minYear"
                            label = "Minium Year Database Building was Built"
                            outlined
                            type="number"
                            dense
                          ></v-text-field>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </v-row>
                <v-row>
                  <v-btn
                  class = "ma-2"
                  align="center"
                  depressed
                  color="primary"
                  v-on:click="sendEnergystar(); getEnergystar();"
                  >Run Energystar Calculation</v-btn>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-card-title>Energy Star Outputs</v-card-title>
              <v-container full-height>
                <v-row>
                  <h1>Score</h1>
                </v-row>
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="energystarData.score.score"
                      label = "Energystar Score"
                      outlined
                      :readonly="true"
                      dense
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="energystarData.score.predictEUI"
                      label = "Predicted EUI"
                      outlined
                      :readonly="true"
                      dense
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="energystarData.score.adjustedEUI"
                      label = "Adjusted EUI"
                      outlined
                      :readonly="true"
                      dense
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <h1>Target Score</h1>
                </v-row>
                <v-row>
                  <v-text-field
                    v-model="energystarData.targetScore.usage"
                    label = "Energy Savings Needed to Meet Target Score"
                    outlined
                    :readonly="true"
                    dense
                  ></v-text-field>
                </v-row>
                <v-row>
                  <v-text-field
                    v-model="energystarData.targetScore.targetEUI"
                    label = "Source EUI Needed to Meet Target Score"
                    outlined
                    :readonly="true"
                    dense
                  ></v-text-field>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Graphs</v-card-title>
              <v-row>
                <v-col>
                  <div id="energystarchart" style="width: 700px;height:500px;"></div>
                </v-col>
                <v-col>
                  <div id="energystarpie" style="width: 600px;height:500px;"></div>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
    <v-row>
      <v-container></v-container>
    </v-row>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>CapX Settings</v-card-title>
              <v-col offset-md="1" md="10">
                <div>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.discount_rate"
                      label = "Discount Rate"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.period_analysis"
                      label = "Period of Analysis [years]"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.energy_eff_budget"
                      label = "Energy Efficient Measure Budget Restriction [$]"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.energy_del_restriction"
                      label = "Total Delivered Energy Restrictions [kWh/m2/yr]"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.electricity_cost"
                      label = "Electricity Cost [$/kWh]"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="capxSettings.natural_gas_cost"
                      label = "Natural Gas Cost [$/kWh]"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-row>
                </div>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-card-title>CapX Parameter Values</v-card-title>
              <v-col offset-md="1" md="10">
                <div>
                  <v-expansion-panels>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Heating Efficiency (COP)</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric Water Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.electricWaterBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.electricWaterBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Gas Water Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.gasWaterBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.gasWaterBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Oil Water Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.oilWaterBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.oilWaterBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric Steam Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.electricSteamBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.electricSteamBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Gas Steam Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.gasSteamBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.gasSteamBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Oil Steam Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.oilSteamBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingEfficiency.oilSteamBoiler.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Cooling Efficiency (COP)</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Reciprocating Air Chiller
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.reciprocatingAirChiller.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.reciprocatingAirChiller.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Reciprocating Water Chiller
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.reciprocatingWaterChiller.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.reciprocatingWaterChiller.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Centrifugal Water Chiller
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.centrifugalWaterChiller.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.centrifugalWaterChiller.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Absorption Water Chiller
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.absorptionWaterChiller.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.coolingEfficiency.absorptionWaterChiller.param1"
                              label = "COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Heating and Cooling Plants Efficiencies (COP)</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter 1
                          </v-col>
                          <v-col>
                            Parameter 2
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Heat Pump air-air
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpAA.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpAA.param1"
                              label = "Heating COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpAA.param2"
                              label = "Cooling COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Heat Pump water-air
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpWA.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpWA.param1"
                              label = "Heating COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatingCoolingEfficiency.heatPumpWA.param2"
                              label = "Cooling COP"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Heat Recovery Type</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            No Heat Revcovery
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.None.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.None.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Heat Exchange Plates
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.heatExchangePlates.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.heatExchangePlates.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Two Element HX (Shell and Tube)
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.twoElement.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.twoElement.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Heat Exchange Pipes
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.heatExchangePipes.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.heatExchangePipes.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Rotation Intermittent HX
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.rotation.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.heatRecovery.rotation.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Building Air Leakage Level</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Minimum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.airLeakage.minimum.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.airLeakage.minimum.param1"
                              label = "Airflow m3/hr per floor area"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Maximum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.airLeakage.maximum.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.airLeakage.maximum.param1"
                              label = "Airflow m3/hr per floor area"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Specific Fan Power</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                          <v-col>
                            kW of Fans
                          </v-col>
                          <v-col>
                            CFM Value
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Inline Centrifugal
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.inlineCentrifugal.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.inlineCentrifugal.kw"
                              label = "Specific Fan Power"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.inlineCentrifugal.CFM"
                              label = "kW of Fans"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.inlineCentrifugal.param1"
                              label = "CFM Value"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Blower
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.blower.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.blower.kw"
                              label = "Specific Fan Power"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.blower.CFM"
                              label = "kW of Fans"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.blower.param1"
                              label = "CFM Value"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Axial
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.specificFanPower.axial.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                            v-model="capxParameterValues.specificFanPower.axial.kw"
                              label = "Specific Fan Power"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                            v-model="capxParameterValues.specificFanPower.axial.CFM"
                              label = "kW of Fans"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                            v-model="capxParameterValues.specificFanPower.axial.param1"
                              label = "CFM Value"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>DHW Generation System</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.electric.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.electric.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            VR-Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.VRBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.VRBoiler.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Gas Boiler, HR-Boiler
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.gasBoiler.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.gasBoiler.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Co-Generation
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.coGeneration.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.coGeneration.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            District Heating
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.districtHeating.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.districtHeating.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Heat Pump
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.heatPump.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.heatPump.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Steam
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.steam.cost"
                              label = "Cost"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.DHWGenerationSystem.steam.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>PV Module</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Minimum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.PVModule.minimum.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.PVModule.minimum.param1"
                              label = "Performance Factor"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Maximum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.PVModule.maximum.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.PVModule.maximum.param1"
                              label = "Performance Factor"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Solar Collector</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Minimum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.solarCollector.minimum.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.solarCollector.minimum.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Maximum Value
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.solarCollector.maximum.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.solarCollector.maximum.param1"
                              label = "Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Appliance</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Energy-Star Baseline
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarBaseline.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarBaseline.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Energy-Star Top 10%
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarTop10.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarTop10.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Energy-Star Top 5%
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarTop5.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.appliance.eStarTop5.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Lighting</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            100% CFL
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.allCFL.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.allCFL.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.allCFL.fixtures"
                              label = "Number of Fixtures"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            LED and CFL Combo
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LEDCFL.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LEDCFL.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LEDCFL.fixtures"
                              label = "Number of Fixtures"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            LED
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LED.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LED.param1"
                              label = "W/m^2"
                              outlined
                              dense
                              disabled
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lighting.LED.fixtures"
                              label = "Number of Fixtures"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Wind Turbine</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Minimum Diameter
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.windTurbine.minimumDiameter.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.windTurbine.minimumDiameter.param1"
                              label = "Diameter"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Maximum Diameter
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.windTurbine.maximumDiameter.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.windTurbine.maximumDiameter.param1"
                              label = "Diameter"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Natural Ventilation</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter 1
                          </v-col>
                          <v-col>
                            Parameter 2
                          </v-col>
                          <v-col>
                            Parameter 3
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            NV Baseline
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.baseline.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.baseline.param1"
                              label = "Width [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.baseline.param2"
                              label = "Height [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.baseline.param3"
                              label = "Angle [degree]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            NV Improvement 1
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve1.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve1.param1"
                              label = "Width [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve1.param2"
                              label = "Height [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve1.param3"
                              label = "Angle [degree]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            NV Improvement 2
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve2.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve2.param1"
                              label = "Width [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve2.param2"
                              label = "Height [m]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.naturalVentilation.improve2.param3"
                              label = "Angle [degree]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Electric Battery</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter 1
                          </v-col>
                          <v-col>
                            Parameter 2
                          </v-col>
                          <v-col>
                            Parameter 3
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric Battery Baseline
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.baseline.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.baseline.param1"
                              label = "Battery Capacity [kWh]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.baseline.param2"
                              label = "Charging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.baseline.param3"
                              label = "Discharging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric Battery Improvement 1
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve1.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve1.param1"
                              label = "Battery Capacity [kWh]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve1.param2"
                              label = "Charging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve1.param3"
                              label = "Discharging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Electric Battery Improvement 2
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve2.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve2.param1"
                              label = "Battery Capacity [kWh]"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve2.param2"
                              label = "Charging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.electricBattery.improve2.param3"
                              label = "Discharging Efficiency"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Lighting Dimmer</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            Technology Levels
                          </v-col>
                          <v-col>
                            Cost ($)
                          </v-col>
                          <v-col>
                            Parameter
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Minimum Number of Dimmer
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lightingDimmer.minimumDimmer.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lightingDimmer.minimumDimmer.param1"
                              label = "Number of Dimmers"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            Maximum Number of Dimmer
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lightingDimmer.maximumDimmer.cost"
                              label = "Cost"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                          <v-col>
                            <v-text-field
                              v-model="capxParameterValues.lightingDimmer.maximumDimmer.param1"
                              label = "Number of Dimmers"
                              outlined
                              dense
                              type="number"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Table Inputs</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col>
                            <v-btn>Overhang</v-btn>
                          </v-col>
                          <v-col>
                            <v-btn>Fin</v-btn>
                          </v-col>
                          <v-col>
                            <v-btn>Window SRF</v-btn>
                          </v-col>
                        </v-row>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </div>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>CapX Parameters</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="capxHeaders"
                    :items="capxParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-toolbar-title>My CapX Parameters</v-toolbar-title>
                        <v-divider
                          class="mx-4"
                          inset
                          vertical
                        ></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialogCapx"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add CapX Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editCapxForm.name"
                                      :items='capxOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editCapxForm.data"
                                      :items="disCont"
                                      label="Data Type"
                                    ></v-select>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="capxClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="capxSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDeleteCapx" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="capxCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirmCapx">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItemCapx(item)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItemCapx(item)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="sendMessage()"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
              <v-row justify="center">
                <v-col>
                  <v-btn 
                    class = "ma-2"
                    align="center"
                    depressed
                    color="red"
                    v-on:click="combineCapx()"
                  >Load CapX Settings</v-btn>
                </v-col>
                <v-col>
                  <v-btn 
                    class = "ma-2"
                    :loading= loading2
                    :disabled= loading2
                    align="center"
                    depressed
                    color="green"
                    v-on:click="runCapx(); loadState2();"
                  >Run CapX</v-btn>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <div id="CapX">
                <div id="capxchart" style="width: 800px;height:500px;"></div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </v-container>
</template>

<script>
import axios from 'axios'
import blank_estar from '../../../backend/New_BEM_Code/Input/blank_estar.json'
import blank_cal from '../../../backend/New_BEM_Code/Input/blank_example_calibration.json'

export default{
  name: "CapX_Cal",

  data: () => {

    return {

      calCapBool: ['CapX', 'Calibration'],
      dateInterval: ['Monthly', 'Hourly'],
      ynBool: ['Yes', 'No'],
      months: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      dialog: false,
      dialogDelete: false,
      loader: null,
      loading: false,

      dialogCapx: false,
      dialogDeleteCapx: false,
      loading2: false,

      dialogSchedule: false,
      dialogDeleteSchedule: false,

      dialogHeat: false,
      dialogDeleteHeat: false,

      max25chars: v => v.length <= 25 || 'Input too long!',
      pagination: {},
      calBool:false,
      calColor: '',
      calText: '',
      floatInt: ['Float', 'Integer'],
      disCont: ['Discrete', 'Continuous'],
      dayType: ['Weekday', 'Weekend'],
      heatOptions: ['Occupancy', 'Appliance', 'Lighting'],
      scheduleOptions: ['Occupancy Schedule',
                        'Appliance Schedule',
                        'Lighting Schedule',
                        'Heating Temperature Setpoint',
                        'Cooling Temperature Setpoint'
                        ],
      calOptions: ['Heating COP',
                  'Cooling COP',
                  'Extra ventilation above fresh air supply',
                  'Heat Recovery Type',
                  'Exhaust Air Recirculation Percentage',
                  'Building air leakage level',
                  'Specific Fan Power',
                  'Fan Control Factor',
                  'DHW Generation System',
                  'Occupancy',
                  'Appliance',
                  'Lighting',
                  'Outdoor Air',
                  'DHW',
                  'Roof1 Uvalue',
                  'Roof1 Absorption coefficient',
                  'Roof1 Emissivity',
                  'Opaque1 Uvalue',
                  'Opaque1 Absorption coefficient',
                  'Opaque1 Emissivity',
                  'Window1 Uvalue',
                  'Window1 Emissivity',
                  'Window1 Solar transmittance',
                  'Window1 SRF_S',
                  'Window1 SRF_SE',
                  'Window1 SRF_E',
                  'Window1 SRF_NE',
                  'Window1 SRF_N',
                  'Window1 SRF_NW',
                  'Window1 SRF_W',
                  'Window1 SRF_SW',
                  'Retail Refri Capacity',
                  'EV Charger Power',
                  'Garage Appliance', 
                  'Garage Lighting',
                  'Lighting Dimmer Weekday',
                  'Lighting Dimmer Weekend',
                  'Occupancy Monthly',
                  'Appliance Monthly',
                  'Lighting Monthly',
                  'Window1 SRF All',
                  ],
      capxOptions: ['Heating COP',
                    'Cooling COP',
                    'Heating & Cooling COPs',
                    'Heat Recovery Type',
                    'Building air leakage level',
                    'Specifiec fan power',
                    'DHW Generation System',
                    'PV module Area',
                    'SHW Collector Area',
                    'Appliance',
                    'Lighting',
                    'Roof1',
                    'Opaque1',
                    'Window1',
                    'Window1 Overhang Angle_S',
                    'Window1 Overhang Angle_SE',
                    'Window1 Overhang Angle_E',
                    'Window1 Overhang Angle_NE',
                    'Window1 Overhang Angle_N',
                    'Window1 Overhang Angle_NW',
                    'Window1 Overhang Angle_W',
                    'Window1 Overhang Angle_SW',
                    'Window1 Fin Angle_S',
                    'Window1 Fin Angle_SE',
                    'Window1 Fin Angle_E',
                    'Window1 Fin Angle_NE',
                    'Window1 Fin Angle_N',
                    'Window1 Fin Angle_NW',
                    'Window1 Fin Angle_W',
                    'Window1 Fin Angle_SW',
                    'Wind Turbine',
                    'Natural Ventilation',
                    'Electric Battery',
                    'Lighting Dimmer',
                    'Window1 SRF_S',
                    'Window1 SRF_SE',
                    'Window1 SRF_E',
                    'Window1 SRF_NE',
                    'Window1 SRF_N',
                    'Window1 SRF_NW',
                    'Window1 SRF_W',
                    'Window1 SRF_SW',
                    'Window1 SRF_Roof',
                    'Window1 SRF All',
                    ],

      convertOptions: ['kBTU', 'kWh'],
      
      heatHeaders: [
        {
          text: 'Heat Parameters',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Day Type', value: 'day'},
        { text: 'Min', value: 'min'},
        { text: 'Max', value: 'max'},
        { text: 'Min Month', value: 'min_month'},
        { text: 'Max Month', value: 'max_month'},
        { text: 'Actions', value: 'actions',sortable: false },
      ],

      heatParams: [],
      editedIndex4: -1,

      editHeatForm: {
        name: '',
        day: '',
        min: '',
        max: '',
        min_month: '',
        max_month: '',
      },

      defaultHeatForm: {
        name: '',
        day: '',
        min: '',
        max: '',
        min_month: '',
        max_month: '',
      },

      scheduleHeaders: [
        {
          text: 'Schedule Parameters',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Day Type', value: 'day'},
        { text: 'Min Hour', value: 'min_hour'},
        { text: 'Max Hour', value: 'max_hour'},
        { text: 'Min', value: 'min'},
        { text: 'Max', value: 'max'},
        { text: 'Actions', value: 'actions',sortable: false },
      ],

      scheduleParams: [],
      editedIndex3: -1,

      editScheduleForm: {
        name: '',
        day: '',
        min_hour: '',
        max_hour: '',
        min: '',
        max: '',
      },

      defaultScheduleForm: {
        name: '',
        day: '',
        min_hour: '',
        max_hour: '',
        min: '',
        max: '',
      },

      calHeaders: [
        {
          text: 'Calibration Parameters',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Type', value: 'data' },
        { text: 'Minimum', value: 'min' },
        { text: 'Maximum', value: 'max' },
        { text: 'Actions', value: 'actions',sortable: false },
      ],

      calParams: [],

      // calParams: blank_cal.calibration_parameters,
      // scheduleParams: blank_cal.schedule_parameters,
      // heatParams: blank_cal.monthly_internal,
      GASettings: blank_cal.ga_settings,
      calSettings: blank_cal.calibration_settings,
      type: blank_cal.type,
      // capxParams: blank_cal.capxParameters,
      capxParameterValues: blank_cal.capxParameterValues,
      capxSettings: blank_cal.capxSettings,

      editedIndex: -1,

      editCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },
      defaultCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },

      capxHeaders: [
        {
          text: 'CapX Parameters',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Type', value: 'data' },
        { text: 'Actions', value: 'actions',sortable: false },
      ],

      capxParams: [],
      editedIndex2: -1,

      editCapxForm: {
        name: '',
        data: '',
      },
      defaultCapxForm: {
        name: '',
        data: '',
      },

      // GASettings: [],
      // calSettings: [],
      // calCombine: [],
      // type: 'Calibration',

      // capxParameterValues: null,
      // capxSettings: [],


      dataInterval: "Monthly",
      monthlySchedule: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      hourlySchedule: ["1/1/19 12:00 PM", "1/1/19 1:00 PM", "1/1/19 2:00 PM", "1/1/19 3:00 PM", "1/1/19 4:00 PM", "1/1/19 5:00 PM", "1/1/19 6:00 PM", "1/1/19 7:00 PM", "1/1/19 8:00 PM", "1/1/19 9:00 PM", "1/1/19 10:00 PM", "1/1/19 11:00 PM", "1/2/19 12:00 AM", "1/2/19 1:00 AM", "1/2/19 2:00 AM", "1/2/19 3:00 AM", "1/2/19 4:00 AM", "1/2/19 5:00 AM", "1/2/19 6:00 AM", "1/2/19 7:00 AM", "1/2/19 8:00 AM", "1/2/19 9:00 AM", "1/2/19 10:00 AM", "1/2/19 11:00 AM", "1/2/19 12:00 PM", "1/2/19 1:00 PM", "1/2/19 2:00 PM", "1/2/19 3:00 PM", "1/2/19 4:00 PM", "1/2/19 5:00 PM", "1/2/19 6:00 PM", "1/2/19 7:00 PM", "1/2/19 8:00 PM", "1/2/19 9:00 PM", "1/2/19 10:00 PM", "1/2/19 11:00 PM", "1/3/19 12:00 AM", "1/3/19 1:00 AM", "1/3/19 2:00 AM", "1/3/19 3:00 AM", "1/3/19 4:00 AM", "1/3/19 5:00 AM", "1/3/19 6:00 AM", "1/3/19 7:00 AM", "1/3/19 8:00 AM", "1/3/19 9:00 AM", "1/3/19 10:00 AM", "1/3/19 11:00 AM", "1/3/19 12:00 PM", "1/3/19 1:00 PM", "1/3/19 2:00 PM", "1/3/19 3:00 PM", "1/3/19 4:00 PM", "1/3/19 5:00 PM", "1/3/19 6:00 PM", "1/3/19 7:00 PM", "1/3/19 8:00 PM", "1/3/19 9:00 PM", "1/3/19 10:00 PM", "1/3/19 11:00 PM", "1/4/19 12:00 AM", "1/4/19 1:00 AM", "1/4/19 2:00 AM", "1/4/19 3:00 AM", "1/4/19 4:00 AM", "1/4/19 5:00 AM", "1/4/19 6:00 AM", "1/4/19 7:00 AM", "1/4/19 8:00 AM", "1/4/19 9:00 AM", "1/4/19 10:00 AM", "1/4/19 11:00 AM", "1/4/19 12:00 PM", "1/4/19 1:00 PM", "1/4/19 2:00 PM", "1/4/19 3:00 PM", "1/4/19 4:00 PM", "1/4/19 5:00 PM", "1/4/19 6:00 PM", "1/4/19 7:00 PM", "1/4/19 8:00 PM", "1/4/19 9:00 PM", "1/4/19 10:00 PM", "1/4/19 11:00 PM", "1/5/19 12:00 AM", "1/5/19 1:00 AM", "1/5/19 2:00 AM", "1/5/19 3:00 AM", "1/5/19 4:00 AM", "1/5/19 5:00 AM", "1/5/19 6:00 AM", "1/5/19 7:00 AM", "1/5/19 8:00 AM", "1/5/19 9:00 AM", "1/5/19 10:00 AM", "1/5/19 11:00 AM", "1/5/19 12:00 PM", "1/5/19 1:00 PM", "1/5/19 2:00 PM", "1/5/19 3:00 PM", "1/5/19 4:00 PM", "1/5/19 5:00 PM", "1/5/19 6:00 PM", "1/5/19 7:00 PM", "1/5/19 8:00 PM", "1/5/19 9:00 PM", "1/5/19 10:00 PM", "1/5/19 11:00 PM", "1/6/19 12:00 AM", "1/6/19 1:00 AM", "1/6/19 2:00 AM", "1/6/19 3:00 AM", "1/6/19 4:00 AM", "1/6/19 5:00 AM", "1/6/19 6:00 AM", "1/6/19 7:00 AM", "1/6/19 8:00 AM", "1/6/19 9:00 AM", "1/6/19 10:00 AM", "1/6/19 11:00 AM", "1/6/19 12:00 PM", "1/6/19 1:00 PM", "1/6/19 2:00 PM", "1/6/19 3:00 PM", "1/6/19 4:00 PM", "1/6/19 5:00 PM", "1/6/19 6:00 PM", "1/6/19 7:00 PM", "1/6/19 8:00 PM", "1/6/19 9:00 PM", "1/6/19 10:00 PM", "1/6/19 11:00 PM", "1/7/19 12:00 AM", "1/7/19 1:00 AM", "1/7/19 2:00 AM", "1/7/19 3:00 AM", "1/7/19 4:00 AM", "1/7/19 5:00 AM", "1/7/19 6:00 AM", "1/7/19 7:00 AM", "1/7/19 8:00 AM", "1/7/19 9:00 AM", "1/7/19 10:00 AM", "1/7/19 11:00 AM", "1/7/19 12:00 PM", "1/7/19 1:00 PM", "1/7/19 2:00 PM", "1/7/19 3:00 PM", "1/7/19 4:00 PM", "1/7/19 5:00 PM", "1/7/19 6:00 PM", "1/7/19 7:00 PM", "1/7/19 8:00 PM", "1/7/19 9:00 PM", "1/7/19 10:00 PM", "1/7/19 11:00 PM", "1/8/19 12:00 AM", "1/8/19 1:00 AM", "1/8/19 2:00 AM", "1/8/19 3:00 AM", "1/8/19 4:00 AM", "1/8/19 5:00 AM", "1/8/19 6:00 AM", "1/8/19 7:00 AM", "1/8/19 8:00 AM", "1/8/19 9:00 AM", "1/8/19 10:00 AM", "1/8/19 11:00 AM", "1/8/19 12:00 PM", "1/8/19 1:00 PM", "1/8/19 2:00 PM", "1/8/19 3:00 PM", "1/8/19 4:00 PM", "1/8/19 5:00 PM", "1/8/19 6:00 PM", "1/8/19 7:00 PM", "1/8/19 8:00 PM", "1/8/19 9:00 PM", "1/8/19 10:00 PM", "1/8/19 11:00 PM", "1/9/19 12:00 AM", "1/9/19 1:00 AM", "1/9/19 2:00 AM", "1/9/19 3:00 AM", "1/9/19 4:00 AM", "1/9/19 5:00 AM", "1/9/19 6:00 AM", "1/9/19 7:00 AM", "1/9/19 8:00 AM", "1/9/19 9:00 AM", "1/9/19 10:00 AM", "1/9/19 11:00 AM", "1/9/19 12:00 PM", "1/9/19 1:00 PM", "1/9/19 2:00 PM", "1/9/19 3:00 PM", "1/9/19 4:00 PM", "1/9/19 5:00 PM", "1/9/19 6:00 PM", "1/9/19 7:00 PM", "1/9/19 8:00 PM", "1/9/19 9:00 PM", "1/9/19 10:00 PM", "1/9/19 11:00 PM", "1/10/19 12:00 AM", "1/10/19 1:00 AM", "1/10/19 2:00 AM", "1/10/19 3:00 AM", "1/10/19 4:00 AM", "1/10/19 5:00 AM", "1/10/19 6:00 AM", "1/10/19 7:00 AM", "1/10/19 8:00 AM", "1/10/19 9:00 AM", "1/10/19 10:00 AM", "1/10/19 11:00 AM", "1/10/19 12:00 PM", "1/10/19 1:00 PM", "1/10/19 2:00 PM", "1/10/19 3:00 PM", "1/10/19 4:00 PM", "1/10/19 5:00 PM", "1/10/19 6:00 PM", "1/10/19 7:00 PM", "1/10/19 8:00 PM", "1/10/19 9:00 PM", "1/10/19 10:00 PM", "1/10/19 11:00 PM", "1/11/19 12:00 AM", "1/11/19 1:00 AM", "1/11/19 2:00 AM", "1/11/19 3:00 AM", "1/11/19 4:00 AM", "1/11/19 5:00 AM", "1/11/19 6:00 AM", "1/11/19 7:00 AM", "1/11/19 8:00 AM", "1/11/19 9:00 AM", "1/11/19 10:00 AM", "1/11/19 11:00 AM", "1/11/19 12:00 PM", "1/11/19 1:00 PM", "1/11/19 2:00 PM", "1/11/19 3:00 PM", "1/11/19 4:00 PM", "1/11/19 5:00 PM", "1/11/19 6:00 PM", "1/11/19 7:00 PM", "1/11/19 8:00 PM", "1/11/19 9:00 PM", "1/11/19 10:00 PM", "1/11/19 11:00 PM", "1/12/19 12:00 AM", "1/12/19 1:00 AM", "1/12/19 2:00 AM", "1/12/19 3:00 AM", "1/12/19 4:00 AM", "1/12/19 5:00 AM", "1/12/19 6:00 AM", "1/12/19 7:00 AM", "1/12/19 8:00 AM", "1/12/19 9:00 AM", "1/12/19 10:00 AM", "1/12/19 11:00 AM", "1/12/19 12:00 PM", "1/12/19 1:00 PM", "1/12/19 2:00 PM", "1/12/19 3:00 PM", "1/12/19 4:00 PM", "1/12/19 5:00 PM", "1/12/19 6:00 PM", "1/12/19 7:00 PM", "1/12/19 8:00 PM", "1/12/19 9:00 PM", "1/12/19 10:00 PM", "1/12/19 11:00 PM", "1/13/19 12:00 AM", "1/13/19 1:00 AM", "1/13/19 2:00 AM", "1/13/19 3:00 AM", "1/13/19 4:00 AM", "1/13/19 5:00 AM", "1/13/19 6:00 AM", "1/13/19 7:00 AM", "1/13/19 8:00 AM", "1/13/19 9:00 AM", "1/13/19 10:00 AM", "1/13/19 11:00 AM", "1/13/19 12:00 PM", "1/13/19 1:00 PM", "1/13/19 2:00 PM", "1/13/19 3:00 PM", "1/13/19 4:00 PM", "1/13/19 5:00 PM", "1/13/19 6:00 PM", "1/13/19 7:00 PM", "1/13/19 8:00 PM", "1/13/19 9:00 PM", "1/13/19 10:00 PM", "1/13/19 11:00 PM", "1/14/19 12:00 AM", "1/14/19 1:00 AM", "1/14/19 2:00 AM", "1/14/19 3:00 AM", "1/14/19 4:00 AM", "1/14/19 5:00 AM", "1/14/19 6:00 AM", "1/14/19 7:00 AM", "1/14/19 8:00 AM", "1/14/19 9:00 AM", "1/14/19 10:00 AM", "1/14/19 11:00 AM", "1/14/19 12:00 PM", "1/14/19 1:00 PM", "1/14/19 2:00 PM", "1/14/19 3:00 PM", "1/14/19 4:00 PM", "1/14/19 5:00 PM", "1/14/19 6:00 PM", "1/14/19 7:00 PM", "1/14/19 8:00 PM", "1/14/19 9:00 PM", "1/14/19 10:00 PM", "1/14/19 11:00 PM", "1/15/19 12:00 AM", "1/15/19 1:00 AM", "1/15/19 2:00 AM", "1/15/19 3:00 AM", "1/15/19 4:00 AM", "1/15/19 5:00 AM", "1/15/19 6:00 AM", "1/15/19 7:00 AM", "1/15/19 8:00 AM", "1/15/19 9:00 AM", "1/15/19 10:00 AM", "1/15/19 11:00 AM", "1/15/19 12:00 PM", "1/15/19 1:00 PM", "1/15/19 2:00 PM", "1/15/19 3:00 PM", "1/15/19 4:00 PM", "1/15/19 5:00 PM", "1/15/19 6:00 PM", "1/15/19 7:00 PM", "1/15/19 8:00 PM", "1/15/19 9:00 PM", "1/15/19 10:00 PM", "1/15/19 11:00 PM", "1/16/19 12:00 AM", "1/16/19 1:00 AM", "1/16/19 2:00 AM", "1/16/19 3:00 AM", "1/16/19 4:00 AM", "1/16/19 5:00 AM", "1/16/19 6:00 AM", "1/16/19 7:00 AM", "1/16/19 8:00 AM", "1/16/19 9:00 AM", "1/16/19 10:00 AM", "1/16/19 11:00 AM", "1/16/19 12:00 PM", "1/16/19 1:00 PM", "1/16/19 2:00 PM", "1/16/19 3:00 PM", "1/16/19 4:00 PM", "1/16/19 5:00 PM", "1/16/19 6:00 PM", "1/16/19 7:00 PM", "1/16/19 8:00 PM", "1/16/19 9:00 PM", "1/16/19 10:00 PM", "1/16/19 11:00 PM", "1/17/19 12:00 AM", "1/17/19 1:00 AM", "1/17/19 2:00 AM", "1/17/19 3:00 AM", "1/17/19 4:00 AM", "1/17/19 5:00 AM", "1/17/19 6:00 AM", "1/17/19 7:00 AM", "1/17/19 8:00 AM", "1/17/19 9:00 AM", "1/17/19 10:00 AM", "1/17/19 11:00 AM", "1/17/19 12:00 PM", "1/17/19 1:00 PM", "1/17/19 2:00 PM", "1/17/19 3:00 PM", "1/17/19 4:00 PM", "1/17/19 5:00 PM", "1/17/19 6:00 PM", "1/17/19 7:00 PM", "1/17/19 8:00 PM", "1/17/19 9:00 PM", "1/17/19 10:00 PM", "1/17/19 11:00 PM", "1/18/19 12:00 AM", "1/18/19 1:00 AM", "1/18/19 2:00 AM", "1/18/19 3:00 AM", "1/18/19 4:00 AM", "1/18/19 5:00 AM", "1/18/19 6:00 AM", "1/18/19 7:00 AM", "1/18/19 8:00 AM", "1/18/19 9:00 AM", "1/18/19 10:00 AM", "1/18/19 11:00 AM", "1/18/19 12:00 PM", "1/18/19 1:00 PM", "1/18/19 2:00 PM", "1/18/19 3:00 PM", "1/18/19 4:00 PM", "1/18/19 5:00 PM", "1/18/19 6:00 PM", "1/18/19 7:00 PM", "1/18/19 8:00 PM", "1/18/19 9:00 PM", "1/18/19 10:00 PM", "1/18/19 11:00 PM", "1/19/19 12:00 AM", "1/19/19 1:00 AM", "1/19/19 2:00 AM", "1/19/19 3:00 AM", "1/19/19 4:00 AM", "1/19/19 5:00 AM", "1/19/19 6:00 AM", "1/19/19 7:00 AM", "1/19/19 8:00 AM", "1/19/19 9:00 AM", "1/19/19 10:00 AM", "1/19/19 11:00 AM", "1/19/19 12:00 PM", "1/19/19 1:00 PM", "1/19/19 2:00 PM", "1/19/19 3:00 PM", "1/19/19 4:00 PM", "1/19/19 5:00 PM", "1/19/19 6:00 PM", "1/19/19 7:00 PM", "1/19/19 8:00 PM", "1/19/19 9:00 PM", "1/19/19 10:00 PM", "1/19/19 11:00 PM", "1/20/19 12:00 AM", "1/20/19 1:00 AM", "1/20/19 2:00 AM", "1/20/19 3:00 AM", "1/20/19 4:00 AM", "1/20/19 5:00 AM", "1/20/19 6:00 AM", "1/20/19 7:00 AM", "1/20/19 8:00 AM", "1/20/19 9:00 AM", "1/20/19 10:00 AM", "1/20/19 11:00 AM", "1/20/19 12:00 PM", "1/20/19 1:00 PM", "1/20/19 2:00 PM", "1/20/19 3:00 PM", "1/20/19 4:00 PM", "1/20/19 5:00 PM", "1/20/19 6:00 PM", "1/20/19 7:00 PM", "1/20/19 8:00 PM", "1/20/19 9:00 PM", "1/20/19 10:00 PM", "1/20/19 11:00 PM", "1/21/19 12:00 AM", "1/21/19 1:00 AM", "1/21/19 2:00 AM", "1/21/19 3:00 AM", "1/21/19 4:00 AM", "1/21/19 5:00 AM", "1/21/19 6:00 AM", "1/21/19 7:00 AM", "1/21/19 8:00 AM", "1/21/19 9:00 AM", "1/21/19 10:00 AM", "1/21/19 11:00 AM", "1/21/19 12:00 PM", "1/21/19 1:00 PM", "1/21/19 2:00 PM", "1/21/19 3:00 PM", "1/21/19 4:00 PM", "1/21/19 5:00 PM", "1/21/19 6:00 PM", "1/21/19 7:00 PM", "1/21/19 8:00 PM", "1/21/19 9:00 PM", "1/21/19 10:00 PM", "1/21/19 11:00 PM", "1/22/19 12:00 AM", "1/22/19 1:00 AM", "1/22/19 2:00 AM", "1/22/19 3:00 AM", "1/22/19 4:00 AM", "1/22/19 5:00 AM", "1/22/19 6:00 AM", "1/22/19 7:00 AM", "1/22/19 8:00 AM", "1/22/19 9:00 AM", "1/22/19 10:00 AM", "1/22/19 11:00 AM", "1/22/19 12:00 PM", "1/22/19 1:00 PM", "1/22/19 2:00 PM", "1/22/19 3:00 PM", "1/22/19 4:00 PM", "1/22/19 5:00 PM", "1/22/19 6:00 PM", "1/22/19 7:00 PM", "1/22/19 8:00 PM", "1/22/19 9:00 PM", "1/22/19 10:00 PM", "1/22/19 11:00 PM", "1/23/19 12:00 AM", "1/23/19 1:00 AM", "1/23/19 2:00 AM", "1/23/19 3:00 AM", "1/23/19 4:00 AM", "1/23/19 5:00 AM", "1/23/19 6:00 AM", "1/23/19 7:00 AM", "1/23/19 8:00 AM", "1/23/19 9:00 AM", "1/23/19 10:00 AM", "1/23/19 11:00 AM", "1/23/19 12:00 PM", "1/23/19 1:00 PM", "1/23/19 2:00 PM", "1/23/19 3:00 PM", "1/23/19 4:00 PM", "1/23/19 5:00 PM", "1/23/19 6:00 PM", "1/23/19 7:00 PM", "1/23/19 8:00 PM", "1/23/19 9:00 PM", "1/23/19 10:00 PM", "1/23/19 11:00 PM", "1/24/19 12:00 AM", "1/24/19 1:00 AM", "1/24/19 2:00 AM", "1/24/19 3:00 AM", "1/24/19 4:00 AM", "1/24/19 5:00 AM", "1/24/19 6:00 AM", "1/24/19 7:00 AM", "1/24/19 8:00 AM", "1/24/19 9:00 AM", "1/24/19 10:00 AM", "1/24/19 11:00 AM", "1/24/19 12:00 PM", "1/24/19 1:00 PM", "1/24/19 2:00 PM", "1/24/19 3:00 PM", "1/24/19 4:00 PM", "1/24/19 5:00 PM", "1/24/19 6:00 PM", "1/24/19 7:00 PM", "1/24/19 8:00 PM", "1/24/19 9:00 PM", "1/24/19 10:00 PM", "1/24/19 11:00 PM", "1/25/19 12:00 AM", "1/25/19 1:00 AM", "1/25/19 2:00 AM", "1/25/19 3:00 AM", "1/25/19 4:00 AM", "1/25/19 5:00 AM", "1/25/19 6:00 AM", "1/25/19 7:00 AM", "1/25/19 8:00 AM", "1/25/19 9:00 AM", "1/25/19 10:00 AM", "1/25/19 11:00 AM", "1/25/19 12:00 PM", "1/25/19 1:00 PM", "1/25/19 2:00 PM", "1/25/19 3:00 PM", "1/25/19 4:00 PM", "1/25/19 5:00 PM", "1/25/19 6:00 PM", "1/25/19 7:00 PM", "1/25/19 8:00 PM", "1/25/19 9:00 PM", "1/25/19 10:00 PM", "1/25/19 11:00 PM", "1/26/19 12:00 AM", "1/26/19 1:00 AM", "1/26/19 2:00 AM", "1/26/19 3:00 AM", "1/26/19 4:00 AM", "1/26/19 5:00 AM", "1/26/19 6:00 AM", "1/26/19 7:00 AM", "1/26/19 8:00 AM", "1/26/19 9:00 AM", "1/26/19 10:00 AM", "1/26/19 11:00 AM", "1/26/19 12:00 PM", "1/26/19 1:00 PM", "1/26/19 2:00 PM", "1/26/19 3:00 PM", "1/26/19 4:00 PM", "1/26/19 5:00 PM", "1/26/19 6:00 PM", "1/26/19 7:00 PM", "1/26/19 8:00 PM", "1/26/19 9:00 PM", "1/26/19 10:00 PM", "1/26/19 11:00 PM", "1/27/19 12:00 AM", "1/27/19 1:00 AM", "1/27/19 2:00 AM", "1/27/19 3:00 AM", "1/27/19 4:00 AM", "1/27/19 5:00 AM", "1/27/19 6:00 AM", "1/27/19 7:00 AM", "1/27/19 8:00 AM", "1/27/19 9:00 AM", "1/27/19 10:00 AM", "1/27/19 11:00 AM", "1/27/19 12:00 PM", "1/27/19 1:00 PM", "1/27/19 2:00 PM", "1/27/19 3:00 PM", "1/27/19 4:00 PM", "1/27/19 5:00 PM", "1/27/19 6:00 PM", "1/27/19 7:00 PM", "1/27/19 8:00 PM", "1/27/19 9:00 PM", "1/27/19 10:00 PM", "1/27/19 11:00 PM", "1/28/19 12:00 AM", "1/28/19 1:00 AM", "1/28/19 2:00 AM", "1/28/19 3:00 AM", "1/28/19 4:00 AM", "1/28/19 5:00 AM", "1/28/19 6:00 AM", "1/28/19 7:00 AM", "1/28/19 8:00 AM", "1/28/19 9:00 AM", "1/28/19 10:00 AM", "1/28/19 11:00 AM", "1/28/19 12:00 PM", "1/28/19 1:00 PM", "1/28/19 2:00 PM", "1/28/19 3:00 PM", "1/28/19 4:00 PM", "1/28/19 5:00 PM", "1/28/19 6:00 PM", "1/28/19 7:00 PM", "1/28/19 8:00 PM", "1/28/19 9:00 PM", "1/28/19 10:00 PM", "1/28/19 11:00 PM", "1/29/19 12:00 AM", "1/29/19 1:00 AM", "1/29/19 2:00 AM", "1/29/19 3:00 AM", "1/29/19 4:00 AM", "1/29/19 5:00 AM", "1/29/19 6:00 AM", "1/29/19 7:00 AM", "1/29/19 8:00 AM", "1/29/19 9:00 AM", "1/29/19 10:00 AM", "1/29/19 11:00 AM", "1/29/19 12:00 PM", "1/29/19 1:00 PM", "1/29/19 2:00 PM", "1/29/19 3:00 PM", "1/29/19 4:00 PM", "1/29/19 5:00 PM", "1/29/19 6:00 PM", "1/29/19 7:00 PM", "1/29/19 8:00 PM", "1/29/19 9:00 PM", "1/29/19 10:00 PM", "1/29/19 11:00 PM", "1/30/19 12:00 AM", "1/30/19 1:00 AM", "1/30/19 2:00 AM", "1/30/19 3:00 AM", "1/30/19 4:00 AM", "1/30/19 5:00 AM", "1/30/19 6:00 AM", "1/30/19 7:00 AM", "1/30/19 8:00 AM", "1/30/19 9:00 AM", "1/30/19 10:00 AM", "1/30/19 11:00 AM", "1/30/19 12:00 PM", "1/30/19 1:00 PM", "1/30/19 2:00 PM", "1/30/19 3:00 PM", "1/30/19 4:00 PM", "1/30/19 5:00 PM", "1/30/19 6:00 PM", "1/30/19 7:00 PM", "1/30/19 8:00 PM", "1/30/19 9:00 PM", "1/30/19 10:00 PM", "1/30/19 11:00 PM", "1/31/19 12:00 AM", "1/31/19 1:00 AM", "1/31/19 2:00 AM", "1/31/19 3:00 AM", "1/31/19 4:00 AM", "1/31/19 5:00 AM", "1/31/19 6:00 AM", "1/31/19 7:00 AM", "1/31/19 8:00 AM", "1/31/19 9:00 AM", "1/31/19 10:00 AM", "1/31/19 11:00 AM", "1/31/19 12:00 PM", "1/31/19 1:00 PM", "1/31/19 2:00 PM", "1/31/19 3:00 PM", "1/31/19 4:00 PM", "1/31/19 5:00 PM", "1/31/19 6:00 PM", "1/31/19 7:00 PM", "1/31/19 8:00 PM", "1/31/19 9:00 PM", "1/31/19 10:00 PM", "1/31/19 11:00 PM", "2/1/19 12:00 AM", "2/1/19 1:00 AM", "2/1/19 2:00 AM", "2/1/19 3:00 AM", "2/1/19 4:00 AM", "2/1/19 5:00 AM", "2/1/19 6:00 AM", "2/1/19 7:00 AM", "2/1/19 8:00 AM", "2/1/19 9:00 AM", "2/1/19 10:00 AM", "2/1/19 11:00 AM", "2/1/19 12:00 PM", "2/1/19 1:00 PM", "2/1/19 2:00 PM", "2/1/19 3:00 PM", "2/1/19 4:00 PM", "2/1/19 5:00 PM", "2/1/19 6:00 PM", "2/1/19 7:00 PM", "2/1/19 8:00 PM", "2/1/19 9:00 PM", "2/1/19 10:00 PM", "2/1/19 11:00 PM", "2/2/19 12:00 AM", "2/2/19 1:00 AM", "2/2/19 2:00 AM", "2/2/19 3:00 AM", "2/2/19 4:00 AM", "2/2/19 5:00 AM", "2/2/19 6:00 AM", "2/2/19 7:00 AM", "2/2/19 8:00 AM", "2/2/19 9:00 AM", "2/2/19 10:00 AM", "2/2/19 11:00 AM", "2/2/19 12:00 PM", "2/2/19 1:00 PM", "2/2/19 2:00 PM", "2/2/19 3:00 PM", "2/2/19 4:00 PM", "2/2/19 5:00 PM", "2/2/19 6:00 PM", "2/2/19 7:00 PM", "2/2/19 8:00 PM", "2/2/19 9:00 PM", "2/2/19 10:00 PM", "2/2/19 11:00 PM", "2/3/19 12:00 AM", "2/3/19 1:00 AM", "2/3/19 2:00 AM", "2/3/19 3:00 AM", "2/3/19 4:00 AM", "2/3/19 5:00 AM", "2/3/19 6:00 AM", "2/3/19 7:00 AM", "2/3/19 8:00 AM", "2/3/19 9:00 AM", "2/3/19 10:00 AM", "2/3/19 11:00 AM", "2/3/19 12:00 PM", "2/3/19 1:00 PM", "2/3/19 2:00 PM", "2/3/19 3:00 PM", "2/3/19 4:00 PM", "2/3/19 5:00 PM", "2/3/19 6:00 PM", "2/3/19 7:00 PM", "2/3/19 8:00 PM", "2/3/19 9:00 PM", "2/3/19 10:00 PM", "2/3/19 11:00 PM", "2/4/19 12:00 AM", "2/4/19 1:00 AM", "2/4/19 2:00 AM", "2/4/19 3:00 AM", "2/4/19 4:00 AM", "2/4/19 5:00 AM", "2/4/19 6:00 AM", "2/4/19 7:00 AM", "2/4/19 8:00 AM", "2/4/19 9:00 AM", "2/4/19 10:00 AM", "2/4/19 11:00 AM", "2/4/19 12:00 PM", "2/4/19 1:00 PM", "2/4/19 2:00 PM", "2/4/19 3:00 PM", "2/4/19 4:00 PM", "2/4/19 5:00 PM", "2/4/19 6:00 PM", "2/4/19 7:00 PM", "2/4/19 8:00 PM", "2/4/19 9:00 PM", "2/4/19 10:00 PM", "2/4/19 11:00 PM", "2/5/19 12:00 AM", "2/5/19 1:00 AM", "2/5/19 2:00 AM", "2/5/19 3:00 AM", "2/5/19 4:00 AM", "2/5/19 5:00 AM", "2/5/19 6:00 AM", "2/5/19 7:00 AM", "2/5/19 8:00 AM", "2/5/19 9:00 AM", "2/5/19 10:00 AM", "2/5/19 11:00 AM", "2/5/19 12:00 PM", "2/5/19 1:00 PM", "2/5/19 2:00 PM", "2/5/19 3:00 PM", "2/5/19 4:00 PM", "2/5/19 5:00 PM", "2/5/19 6:00 PM", "2/5/19 7:00 PM", "2/5/19 8:00 PM", "2/5/19 9:00 PM", "2/5/19 10:00 PM", "2/5/19 11:00 PM", "2/6/19 12:00 AM", "2/6/19 1:00 AM", "2/6/19 2:00 AM", "2/6/19 3:00 AM", "2/6/19 4:00 AM", "2/6/19 5:00 AM", "2/6/19 6:00 AM", "2/6/19 7:00 AM", "2/6/19 8:00 AM", "2/6/19 9:00 AM", "2/6/19 10:00 AM", "2/6/19 11:00 AM", "2/6/19 12:00 PM", "2/6/19 1:00 PM", "2/6/19 2:00 PM", "2/6/19 3:00 PM", "2/6/19 4:00 PM", "2/6/19 5:00 PM", "2/6/19 6:00 PM", "2/6/19 7:00 PM", "2/6/19 8:00 PM", "2/6/19 9:00 PM", "2/6/19 10:00 PM", "2/6/19 11:00 PM", "2/7/19 12:00 AM", "2/7/19 1:00 AM", "2/7/19 2:00 AM", "2/7/19 3:00 AM", "2/7/19 4:00 AM", "2/7/19 5:00 AM", "2/7/19 6:00 AM", "2/7/19 7:00 AM", "2/7/19 8:00 AM", "2/7/19 9:00 AM", "2/7/19 10:00 AM", "2/7/19 11:00 AM", "2/7/19 12:00 PM", "2/7/19 1:00 PM", "2/7/19 2:00 PM", "2/7/19 3:00 PM", "2/7/19 4:00 PM", "2/7/19 5:00 PM", "2/7/19 6:00 PM", "2/7/19 7:00 PM", "2/7/19 8:00 PM", "2/7/19 9:00 PM", "2/7/19 10:00 PM", "2/7/19 11:00 PM", "2/8/19 12:00 AM", "2/8/19 1:00 AM", "2/8/19 2:00 AM", "2/8/19 3:00 AM", "2/8/19 4:00 AM", "2/8/19 5:00 AM", "2/8/19 6:00 AM", "2/8/19 7:00 AM", "2/8/19 8:00 AM", "2/8/19 9:00 AM", "2/8/19 10:00 AM", "2/8/19 11:00 AM", "2/8/19 12:00 PM", "2/8/19 1:00 PM", "2/8/19 2:00 PM", "2/8/19 3:00 PM", "2/8/19 4:00 PM", "2/8/19 5:00 PM", "2/8/19 6:00 PM", "2/8/19 7:00 PM", "2/8/19 8:00 PM", "2/8/19 9:00 PM", "2/8/19 10:00 PM", "2/8/19 11:00 PM", "2/9/19 12:00 AM", "2/9/19 1:00 AM", "2/9/19 2:00 AM", "2/9/19 3:00 AM", "2/9/19 4:00 AM", "2/9/19 5:00 AM", "2/9/19 6:00 AM", "2/9/19 7:00 AM", "2/9/19 8:00 AM", "2/9/19 9:00 AM", "2/9/19 10:00 AM", "2/9/19 11:00 AM", "2/9/19 12:00 PM", "2/9/19 1:00 PM", "2/9/19 2:00 PM", "2/9/19 3:00 PM", "2/9/19 4:00 PM", "2/9/19 5:00 PM", "2/9/19 6:00 PM", "2/9/19 7:00 PM", "2/9/19 8:00 PM", "2/9/19 9:00 PM", "2/9/19 10:00 PM", "2/9/19 11:00 PM", "2/10/19 12:00 AM", "2/10/19 1:00 AM", "2/10/19 2:00 AM", "2/10/19 3:00 AM", "2/10/19 4:00 AM", "2/10/19 5:00 AM", "2/10/19 6:00 AM", "2/10/19 7:00 AM", "2/10/19 8:00 AM", "2/10/19 9:00 AM", "2/10/19 10:00 AM", "2/10/19 11:00 AM", "2/10/19 12:00 PM", "2/10/19 1:00 PM", "2/10/19 2:00 PM", "2/10/19 3:00 PM", "2/10/19 4:00 PM", "2/10/19 5:00 PM", "2/10/19 6:00 PM", "2/10/19 7:00 PM", "2/10/19 8:00 PM", "2/10/19 9:00 PM", "2/10/19 10:00 PM", "2/10/19 11:00 PM", "2/11/19 12:00 AM", "2/11/19 1:00 AM", "2/11/19 2:00 AM", "2/11/19 3:00 AM", "2/11/19 4:00 AM", "2/11/19 5:00 AM", "2/11/19 6:00 AM", "2/11/19 7:00 AM", "2/11/19 8:00 AM", "2/11/19 9:00 AM", "2/11/19 10:00 AM", "2/11/19 11:00 AM", "2/11/19 12:00 PM", "2/11/19 1:00 PM", "2/11/19 2:00 PM", "2/11/19 3:00 PM", "2/11/19 4:00 PM", "2/11/19 5:00 PM", "2/11/19 6:00 PM", "2/11/19 7:00 PM", "2/11/19 8:00 PM", "2/11/19 9:00 PM", "2/11/19 10:00 PM", "2/11/19 11:00 PM", "2/12/19 12:00 AM", "2/12/19 1:00 AM", "2/12/19 2:00 AM", "2/12/19 3:00 AM", "2/12/19 4:00 AM", "2/12/19 5:00 AM", "2/12/19 6:00 AM", "2/12/19 7:00 AM", "2/12/19 8:00 AM", "2/12/19 9:00 AM", "2/12/19 10:00 AM", "2/12/19 11:00 AM", "2/12/19 12:00 PM", "2/12/19 1:00 PM", "2/12/19 2:00 PM", "2/12/19 3:00 PM", "2/12/19 4:00 PM", "2/12/19 5:00 PM", "2/12/19 6:00 PM", "2/12/19 7:00 PM", "2/12/19 8:00 PM", "2/12/19 9:00 PM", "2/12/19 10:00 PM", "2/12/19 11:00 PM", "2/13/19 12:00 AM", "2/13/19 1:00 AM", "2/13/19 2:00 AM", "2/13/19 3:00 AM", "2/13/19 4:00 AM", "2/13/19 5:00 AM", "2/13/19 6:00 AM", "2/13/19 7:00 AM", "2/13/19 8:00 AM", "2/13/19 9:00 AM", "2/13/19 10:00 AM", "2/13/19 11:00 AM", "2/13/19 12:00 PM", "2/13/19 1:00 PM", "2/13/19 2:00 PM", "2/13/19 3:00 PM", "2/13/19 4:00 PM", "2/13/19 5:00 PM", "2/13/19 6:00 PM", "2/13/19 7:00 PM", "2/13/19 8:00 PM", "2/13/19 9:00 PM", "2/13/19 10:00 PM", "2/13/19 11:00 PM", "2/14/19 12:00 AM", "2/14/19 1:00 AM", "2/14/19 2:00 AM", "2/14/19 3:00 AM", "2/14/19 4:00 AM", "2/14/19 5:00 AM", "2/14/19 6:00 AM", "2/14/19 7:00 AM", "2/14/19 8:00 AM", "2/14/19 9:00 AM", "2/14/19 10:00 AM", "2/14/19 11:00 AM", "2/14/19 12:00 PM", "2/14/19 1:00 PM", "2/14/19 2:00 PM", "2/14/19 3:00 PM", "2/14/19 4:00 PM", "2/14/19 5:00 PM", "2/14/19 6:00 PM", "2/14/19 7:00 PM", "2/14/19 8:00 PM", "2/14/19 9:00 PM", "2/14/19 10:00 PM", "2/14/19 11:00 PM", "2/15/19 12:00 AM", "2/15/19 1:00 AM", "2/15/19 2:00 AM", "2/15/19 3:00 AM", "2/15/19 4:00 AM", "2/15/19 5:00 AM", "2/15/19 6:00 AM", "2/15/19 7:00 AM", "2/15/19 8:00 AM", "2/15/19 9:00 AM", "2/15/19 10:00 AM", "2/15/19 11:00 AM", "2/15/19 12:00 PM", "2/15/19 1:00 PM", "2/15/19 2:00 PM", "2/15/19 3:00 PM", "2/15/19 4:00 PM", "2/15/19 5:00 PM", "2/15/19 6:00 PM", "2/15/19 7:00 PM", "2/15/19 8:00 PM", "2/15/19 9:00 PM", "2/15/19 10:00 PM", "2/15/19 11:00 PM", "2/16/19 12:00 AM", "2/16/19 1:00 AM", "2/16/19 2:00 AM", "2/16/19 3:00 AM", "2/16/19 4:00 AM", "2/16/19 5:00 AM", "2/16/19 6:00 AM", "2/16/19 7:00 AM", "2/16/19 8:00 AM", "2/16/19 9:00 AM", "2/16/19 10:00 AM", "2/16/19 11:00 AM", "2/16/19 12:00 PM", "2/16/19 1:00 PM", "2/16/19 2:00 PM", "2/16/19 3:00 PM", "2/16/19 4:00 PM", "2/16/19 5:00 PM", "2/16/19 6:00 PM", "2/16/19 7:00 PM", "2/16/19 8:00 PM", "2/16/19 9:00 PM", "2/16/19 10:00 PM", "2/16/19 11:00 PM", "2/17/19 12:00 AM", "2/17/19 1:00 AM", "2/17/19 2:00 AM", "2/17/19 3:00 AM", "2/17/19 4:00 AM", "2/17/19 5:00 AM", "2/17/19 6:00 AM", "2/17/19 7:00 AM", "2/17/19 8:00 AM", "2/17/19 9:00 AM", "2/17/19 10:00 AM", "2/17/19 11:00 AM", "2/17/19 12:00 PM", "2/17/19 1:00 PM", "2/17/19 2:00 PM", "2/17/19 3:00 PM", "2/17/19 4:00 PM", "2/17/19 5:00 PM", "2/17/19 6:00 PM", "2/17/19 7:00 PM", "2/17/19 8:00 PM", "2/17/19 9:00 PM", "2/17/19 10:00 PM", "2/17/19 11:00 PM", "2/18/19 12:00 AM", "2/18/19 1:00 AM", "2/18/19 2:00 AM", "2/18/19 3:00 AM", "2/18/19 4:00 AM", "2/18/19 5:00 AM", "2/18/19 6:00 AM", "2/18/19 7:00 AM", "2/18/19 8:00 AM", "2/18/19 9:00 AM", "2/18/19 10:00 AM", "2/18/19 11:00 AM", "2/18/19 12:00 PM", "2/18/19 1:00 PM", "2/18/19 2:00 PM", "2/18/19 3:00 PM", "2/18/19 4:00 PM", "2/18/19 5:00 PM", "2/18/19 6:00 PM", "2/18/19 7:00 PM", "2/18/19 8:00 PM", "2/18/19 9:00 PM", "2/18/19 10:00 PM", "2/18/19 11:00 PM", "2/19/19 12:00 AM", "2/19/19 1:00 AM", "2/19/19 2:00 AM", "2/19/19 3:00 AM", "2/19/19 4:00 AM", "2/19/19 5:00 AM", "2/19/19 6:00 AM", "2/19/19 7:00 AM", "2/19/19 8:00 AM", "2/19/19 9:00 AM", "2/19/19 10:00 AM", "2/19/19 11:00 AM", "2/19/19 12:00 PM", "2/19/19 1:00 PM", "2/19/19 2:00 PM", "2/19/19 3:00 PM", "2/19/19 4:00 PM", "2/19/19 5:00 PM", "2/19/19 6:00 PM", "2/19/19 7:00 PM", "2/19/19 8:00 PM", "2/19/19 9:00 PM", "2/19/19 10:00 PM", "2/19/19 11:00 PM", "2/20/19 12:00 AM", "2/20/19 1:00 AM", "2/20/19 2:00 AM", "2/20/19 3:00 AM", "2/20/19 4:00 AM", "2/20/19 5:00 AM", "2/20/19 6:00 AM", "2/20/19 7:00 AM", "2/20/19 8:00 AM", "2/20/19 9:00 AM", "2/20/19 10:00 AM", "2/20/19 11:00 AM", "2/20/19 12:00 PM", "2/20/19 1:00 PM", "2/20/19 2:00 PM", "2/20/19 3:00 PM", "2/20/19 4:00 PM", "2/20/19 5:00 PM", "2/20/19 6:00 PM", "2/20/19 7:00 PM", "2/20/19 8:00 PM", "2/20/19 9:00 PM", "2/20/19 10:00 PM", "2/20/19 11:00 PM", "2/21/19 12:00 AM", "2/21/19 1:00 AM", "2/21/19 2:00 AM", "2/21/19 3:00 AM", "2/21/19 4:00 AM", "2/21/19 5:00 AM", "2/21/19 6:00 AM", "2/21/19 7:00 AM", "2/21/19 8:00 AM", "2/21/19 9:00 AM", "2/21/19 10:00 AM", "2/21/19 11:00 AM", "2/21/19 12:00 PM", "2/21/19 1:00 PM", "2/21/19 2:00 PM", "2/21/19 3:00 PM", "2/21/19 4:00 PM", "2/21/19 5:00 PM", "2/21/19 6:00 PM", "2/21/19 7:00 PM", "2/21/19 8:00 PM", "2/21/19 9:00 PM", "2/21/19 10:00 PM", "2/21/19 11:00 PM", "2/22/19 12:00 AM", "2/22/19 1:00 AM", "2/22/19 2:00 AM", "2/22/19 3:00 AM", "2/22/19 4:00 AM", "2/22/19 5:00 AM", "2/22/19 6:00 AM", "2/22/19 7:00 AM", "2/22/19 8:00 AM", "2/22/19 9:00 AM", "2/22/19 10:00 AM", "2/22/19 11:00 AM", "2/22/19 12:00 PM", "2/22/19 1:00 PM", "2/22/19 2:00 PM", "2/22/19 3:00 PM", "2/22/19 4:00 PM", "2/22/19 5:00 PM", "2/22/19 6:00 PM", "2/22/19 7:00 PM", "2/22/19 8:00 PM", "2/22/19 9:00 PM", "2/22/19 10:00 PM", "2/22/19 11:00 PM", "2/23/19 12:00 AM", "2/23/19 1:00 AM", "2/23/19 2:00 AM", "2/23/19 3:00 AM", "2/23/19 4:00 AM", "2/23/19 5:00 AM", "2/23/19 6:00 AM", "2/23/19 7:00 AM", "2/23/19 8:00 AM", "2/23/19 9:00 AM", "2/23/19 10:00 AM", "2/23/19 11:00 AM", "2/23/19 12:00 PM", "2/23/19 1:00 PM", "2/23/19 2:00 PM", "2/23/19 3:00 PM", "2/23/19 4:00 PM", "2/23/19 5:00 PM", "2/23/19 6:00 PM", "2/23/19 7:00 PM", "2/23/19 8:00 PM", "2/23/19 9:00 PM", "2/23/19 10:00 PM", "2/23/19 11:00 PM", "2/24/19 12:00 AM", "2/24/19 1:00 AM", "2/24/19 2:00 AM", "2/24/19 3:00 AM", "2/24/19 4:00 AM", "2/24/19 5:00 AM", "2/24/19 6:00 AM", "2/24/19 7:00 AM", "2/24/19 8:00 AM", "2/24/19 9:00 AM", "2/24/19 10:00 AM", "2/24/19 11:00 AM", "2/24/19 12:00 PM", "2/24/19 1:00 PM", "2/24/19 2:00 PM", "2/24/19 3:00 PM", "2/24/19 4:00 PM", "2/24/19 5:00 PM", "2/24/19 6:00 PM", "2/24/19 7:00 PM", "2/24/19 8:00 PM", "2/24/19 9:00 PM", "2/24/19 10:00 PM", "2/24/19 11:00 PM", "2/25/19 12:00 AM", "2/25/19 1:00 AM", "2/25/19 2:00 AM", "2/25/19 3:00 AM", "2/25/19 4:00 AM", "2/25/19 5:00 AM", "2/25/19 6:00 AM", "2/25/19 7:00 AM", "2/25/19 8:00 AM", "2/25/19 9:00 AM", "2/25/19 10:00 AM", "2/25/19 11:00 AM", "2/25/19 12:00 PM", "2/25/19 1:00 PM", "2/25/19 2:00 PM", "2/25/19 3:00 PM", "2/25/19 4:00 PM", "2/25/19 5:00 PM", "2/25/19 6:00 PM", "2/25/19 7:00 PM", "2/25/19 8:00 PM", "2/25/19 9:00 PM", "2/25/19 10:00 PM", "2/25/19 11:00 PM", "2/26/19 12:00 AM", "2/26/19 1:00 AM", "2/26/19 2:00 AM", "2/26/19 3:00 AM", "2/26/19 4:00 AM", "2/26/19 5:00 AM", "2/26/19 6:00 AM", "2/26/19 7:00 AM", "2/26/19 8:00 AM", "2/26/19 9:00 AM", "2/26/19 10:00 AM", "2/26/19 11:00 AM", "2/26/19 12:00 PM", "2/26/19 1:00 PM", "2/26/19 2:00 PM", "2/26/19 3:00 PM", "2/26/19 4:00 PM", "2/26/19 5:00 PM", "2/26/19 6:00 PM", "2/26/19 7:00 PM", "2/26/19 8:00 PM", "2/26/19 9:00 PM", "2/26/19 10:00 PM", "2/26/19 11:00 PM", "2/27/19 12:00 AM", "2/27/19 1:00 AM", "2/27/19 2:00 AM", "2/27/19 3:00 AM", "2/27/19 4:00 AM", "2/27/19 5:00 AM", "2/27/19 6:00 AM", "2/27/19 7:00 AM", "2/27/19 8:00 AM", "2/27/19 9:00 AM", "2/27/19 10:00 AM", "2/27/19 11:00 AM", "2/27/19 12:00 PM", "2/27/19 1:00 PM", "2/27/19 2:00 PM", "2/27/19 3:00 PM", "2/27/19 4:00 PM", "2/27/19 5:00 PM", "2/27/19 6:00 PM", "2/27/19 7:00 PM", "2/27/19 8:00 PM", "2/27/19 9:00 PM", "2/27/19 10:00 PM", "2/27/19 11:00 PM", "2/28/19 12:00 AM", "2/28/19 1:00 AM", "2/28/19 2:00 AM", "2/28/19 3:00 AM", "2/28/19 4:00 AM", "2/28/19 5:00 AM", "2/28/19 6:00 AM", "2/28/19 7:00 AM", "2/28/19 8:00 AM", "2/28/19 9:00 AM", "2/28/19 10:00 AM", "2/28/19 11:00 AM", "2/28/19 12:00 PM", "2/28/19 1:00 PM", "2/28/19 2:00 PM", "2/28/19 3:00 PM", "2/28/19 4:00 PM", "2/28/19 5:00 PM", "2/28/19 6:00 PM", "2/28/19 7:00 PM", "2/28/19 8:00 PM", "2/28/19 9:00 PM", "2/28/19 10:00 PM", "2/28/19 11:00 PM", "3/1/19 12:00 AM", "3/1/19 1:00 AM", "3/1/19 2:00 AM", "3/1/19 3:00 AM", "3/1/19 4:00 AM", "3/1/19 5:00 AM", "3/1/19 6:00 AM", "3/1/19 7:00 AM", "3/1/19 8:00 AM", "3/1/19 9:00 AM", "3/1/19 10:00 AM", "3/1/19 11:00 AM", "3/1/19 12:00 PM", "3/1/19 1:00 PM", "3/1/19 2:00 PM", "3/1/19 3:00 PM", "3/1/19 4:00 PM", "3/1/19 5:00 PM", "3/1/19 6:00 PM", "3/1/19 7:00 PM", "3/1/19 8:00 PM", "3/1/19 9:00 PM", "3/1/19 10:00 PM", "3/1/19 11:00 PM", "3/2/19 12:00 AM", "3/2/19 1:00 AM", "3/2/19 2:00 AM", "3/2/19 3:00 AM", "3/2/19 4:00 AM", "3/2/19 5:00 AM", "3/2/19 6:00 AM", "3/2/19 7:00 AM", "3/2/19 8:00 AM", "3/2/19 9:00 AM", "3/2/19 10:00 AM", "3/2/19 11:00 AM", "3/2/19 12:00 PM", "3/2/19 1:00 PM", "3/2/19 2:00 PM", "3/2/19 3:00 PM", "3/2/19 4:00 PM", "3/2/19 5:00 PM", "3/2/19 6:00 PM", "3/2/19 7:00 PM", "3/2/19 8:00 PM", "3/2/19 9:00 PM", "3/2/19 10:00 PM", "3/2/19 11:00 PM", "3/3/19 12:00 AM", "3/3/19 1:00 AM", "3/3/19 2:00 AM", "3/3/19 3:00 AM", "3/3/19 4:00 AM", "3/3/19 5:00 AM", "3/3/19 6:00 AM", "3/3/19 7:00 AM", "3/3/19 8:00 AM", "3/3/19 9:00 AM", "3/3/19 10:00 AM", "3/3/19 11:00 AM", "3/3/19 12:00 PM", "3/3/19 1:00 PM", "3/3/19 2:00 PM", "3/3/19 3:00 PM", "3/3/19 4:00 PM", "3/3/19 5:00 PM", "3/3/19 6:00 PM", "3/3/19 7:00 PM", "3/3/19 8:00 PM", "3/3/19 9:00 PM", "3/3/19 10:00 PM", "3/3/19 11:00 PM", "3/4/19 12:00 AM", "3/4/19 1:00 AM", "3/4/19 2:00 AM", "3/4/19 3:00 AM", "3/4/19 4:00 AM", "3/4/19 5:00 AM", "3/4/19 6:00 AM", "3/4/19 7:00 AM", "3/4/19 8:00 AM", "3/4/19 9:00 AM", "3/4/19 10:00 AM", "3/4/19 11:00 AM", "3/4/19 12:00 PM", "3/4/19 1:00 PM", "3/4/19 2:00 PM", "3/4/19 3:00 PM", "3/4/19 4:00 PM", "3/4/19 5:00 PM", "3/4/19 6:00 PM", "3/4/19 7:00 PM", "3/4/19 8:00 PM", "3/4/19 9:00 PM", "3/4/19 10:00 PM", "3/4/19 11:00 PM", "3/5/19 12:00 AM", "3/5/19 1:00 AM", "3/5/19 2:00 AM", "3/5/19 3:00 AM", "3/5/19 4:00 AM", "3/5/19 5:00 AM", "3/5/19 6:00 AM", "3/5/19 7:00 AM", "3/5/19 8:00 AM", "3/5/19 9:00 AM", "3/5/19 10:00 AM", "3/5/19 11:00 AM", "3/5/19 12:00 PM", "3/5/19 1:00 PM", "3/5/19 2:00 PM", "3/5/19 3:00 PM", "3/5/19 4:00 PM", "3/5/19 5:00 PM", "3/5/19 6:00 PM", "3/5/19 7:00 PM", "3/5/19 8:00 PM", "3/5/19 9:00 PM", "3/5/19 10:00 PM", "3/5/19 11:00 PM", "3/6/19 12:00 AM", "3/6/19 1:00 AM", "3/6/19 2:00 AM", "3/6/19 3:00 AM", "3/6/19 4:00 AM", "3/6/19 5:00 AM", "3/6/19 6:00 AM", "3/6/19 7:00 AM", "3/6/19 8:00 AM", "3/6/19 9:00 AM", "3/6/19 10:00 AM", "3/6/19 11:00 AM", "3/6/19 12:00 PM", "3/6/19 1:00 PM", "3/6/19 2:00 PM", "3/6/19 3:00 PM", "3/6/19 4:00 PM", "3/6/19 5:00 PM", "3/6/19 6:00 PM", "3/6/19 7:00 PM", "3/6/19 8:00 PM", "3/6/19 9:00 PM", "3/6/19 10:00 PM", "3/6/19 11:00 PM", "3/7/19 12:00 AM", "3/7/19 1:00 AM", "3/7/19 2:00 AM", "3/7/19 3:00 AM", "3/7/19 4:00 AM", "3/7/19 5:00 AM", "3/7/19 6:00 AM", "3/7/19 7:00 AM", "3/7/19 8:00 AM", "3/7/19 9:00 AM", "3/7/19 10:00 AM", "3/7/19 11:00 AM", "3/7/19 12:00 PM", "3/7/19 1:00 PM", "3/7/19 2:00 PM", "3/7/19 3:00 PM", "3/7/19 4:00 PM", "3/7/19 5:00 PM", "3/7/19 6:00 PM", "3/7/19 7:00 PM", "3/7/19 8:00 PM", "3/7/19 9:00 PM", "3/7/19 10:00 PM", "3/7/19 11:00 PM", "3/8/19 12:00 AM", "3/8/19 1:00 AM", "3/8/19 2:00 AM", "3/8/19 3:00 AM", "3/8/19 4:00 AM", "3/8/19 5:00 AM", "3/8/19 6:00 AM", "3/8/19 7:00 AM", "3/8/19 8:00 AM", "3/8/19 9:00 AM", "3/8/19 10:00 AM", "3/8/19 11:00 AM", "3/8/19 12:00 PM", "3/8/19 1:00 PM", "3/8/19 2:00 PM", "3/8/19 3:00 PM", "3/8/19 4:00 PM", "3/8/19 5:00 PM", "3/8/19 6:00 PM", "3/8/19 7:00 PM", "3/8/19 8:00 PM", "3/8/19 9:00 PM", "3/8/19 10:00 PM", "3/8/19 11:00 PM", "3/9/19 12:00 AM", "3/9/19 1:00 AM", "3/9/19 2:00 AM", "3/9/19 3:00 AM", "3/9/19 4:00 AM", "3/9/19 5:00 AM", "3/9/19 6:00 AM", "3/9/19 7:00 AM", "3/9/19 8:00 AM", "3/9/19 9:00 AM", "3/9/19 10:00 AM", "3/9/19 11:00 AM", "3/9/19 12:00 PM", "3/9/19 1:00 PM", "3/9/19 2:00 PM", "3/9/19 3:00 PM", "3/9/19 4:00 PM", "3/9/19 5:00 PM", "3/9/19 6:00 PM", "3/9/19 7:00 PM", "3/9/19 8:00 PM", "3/9/19 9:00 PM", "3/9/19 10:00 PM", "3/9/19 11:00 PM", "3/10/19 12:00 AM", "3/10/19 1:00 AM", "3/10/19 2:00 AM", "3/10/19 3:00 AM", "3/10/19 4:00 AM", "3/10/19 5:00 AM", "3/10/19 6:00 AM", "3/10/19 7:00 AM", "3/10/19 8:00 AM", "3/10/19 9:00 AM", "3/10/19 10:00 AM", "3/10/19 11:00 AM", "3/10/19 12:00 PM", "3/10/19 1:00 PM", "3/10/19 2:00 PM", "3/10/19 3:00 PM", "3/10/19 4:00 PM", "3/10/19 5:00 PM", "3/10/19 6:00 PM", "3/10/19 7:00 PM", "3/10/19 8:00 PM", "3/10/19 9:00 PM", "3/10/19 10:00 PM", "3/10/19 11:00 PM", "3/11/19 12:00 AM", "3/11/19 1:00 AM", "3/11/19 2:00 AM", "3/11/19 3:00 AM", "3/11/19 4:00 AM", "3/11/19 5:00 AM", "3/11/19 6:00 AM", "3/11/19 7:00 AM", "3/11/19 8:00 AM", "3/11/19 9:00 AM", "3/11/19 10:00 AM", "3/11/19 11:00 AM", "3/11/19 12:00 PM", "3/11/19 1:00 PM", "3/11/19 2:00 PM", "3/11/19 3:00 PM", "3/11/19 4:00 PM", "3/11/19 5:00 PM", "3/11/19 6:00 PM", "3/11/19 7:00 PM", "3/11/19 8:00 PM", "3/11/19 9:00 PM", "3/11/19 10:00 PM", "3/11/19 11:00 PM", "3/12/19 12:00 AM", "3/12/19 1:00 AM", "3/12/19 2:00 AM", "3/12/19 3:00 AM", "3/12/19 4:00 AM", "3/12/19 5:00 AM", "3/12/19 6:00 AM", "3/12/19 7:00 AM", "3/12/19 8:00 AM", "3/12/19 9:00 AM", "3/12/19 10:00 AM", "3/12/19 11:00 AM", "3/12/19 12:00 PM", "3/12/19 1:00 PM", "3/12/19 2:00 PM", "3/12/19 3:00 PM", "3/12/19 4:00 PM", "3/12/19 5:00 PM", "3/12/19 6:00 PM", "3/12/19 7:00 PM", "3/12/19 8:00 PM", "3/12/19 9:00 PM", "3/12/19 10:00 PM", "3/12/19 11:00 PM", "3/13/19 12:00 AM", "3/13/19 1:00 AM", "3/13/19 2:00 AM", "3/13/19 3:00 AM", "3/13/19 4:00 AM", "3/13/19 5:00 AM", "3/13/19 6:00 AM", "3/13/19 7:00 AM", "3/13/19 8:00 AM", "3/13/19 9:00 AM", "3/13/19 10:00 AM", "3/13/19 11:00 AM", "3/13/19 12:00 PM", "3/13/19 1:00 PM", "3/13/19 2:00 PM", "3/13/19 3:00 PM", "3/13/19 4:00 PM", "3/13/19 5:00 PM", "3/13/19 6:00 PM", "3/13/19 7:00 PM", "3/13/19 8:00 PM", "3/13/19 9:00 PM", "3/13/19 10:00 PM", "3/13/19 11:00 PM", "3/14/19 12:00 AM", "3/14/19 1:00 AM", "3/14/19 2:00 AM", "3/14/19 3:00 AM", "3/14/19 4:00 AM", "3/14/19 5:00 AM", "3/14/19 6:00 AM", "3/14/19 7:00 AM", "3/14/19 8:00 AM", "3/14/19 9:00 AM", "3/14/19 10:00 AM", "3/14/19 11:00 AM", "3/14/19 12:00 PM", "3/14/19 1:00 PM", "3/14/19 2:00 PM", "3/14/19 3:00 PM", "3/14/19 4:00 PM", "3/14/19 5:00 PM", "3/14/19 6:00 PM", "3/14/19 7:00 PM", "3/14/19 8:00 PM", "3/14/19 9:00 PM", "3/14/19 10:00 PM", "3/14/19 11:00 PM", "3/15/19 12:00 AM", "3/15/19 1:00 AM", "3/15/19 2:00 AM", "3/15/19 3:00 AM", "3/15/19 4:00 AM", "3/15/19 5:00 AM", "3/15/19 6:00 AM", "3/15/19 7:00 AM", "3/15/19 8:00 AM", "3/15/19 9:00 AM", "3/15/19 10:00 AM", "3/15/19 11:00 AM", "3/15/19 12:00 PM", "3/15/19 1:00 PM", "3/15/19 2:00 PM", "3/15/19 3:00 PM", "3/15/19 4:00 PM", "3/15/19 5:00 PM", "3/15/19 6:00 PM", "3/15/19 7:00 PM", "3/15/19 8:00 PM", "3/15/19 9:00 PM", "3/15/19 10:00 PM", "3/15/19 11:00 PM", "3/16/19 12:00 AM", "3/16/19 1:00 AM", "3/16/19 2:00 AM", "3/16/19 3:00 AM", "3/16/19 4:00 AM", "3/16/19 5:00 AM", "3/16/19 6:00 AM", "3/16/19 7:00 AM", "3/16/19 8:00 AM", "3/16/19 9:00 AM", "3/16/19 10:00 AM", "3/16/19 11:00 AM", "3/16/19 12:00 PM", "3/16/19 1:00 PM", "3/16/19 2:00 PM", "3/16/19 3:00 PM", "3/16/19 4:00 PM", "3/16/19 5:00 PM", "3/16/19 6:00 PM", "3/16/19 7:00 PM", "3/16/19 8:00 PM", "3/16/19 9:00 PM", "3/16/19 10:00 PM", "3/16/19 11:00 PM", "3/17/19 12:00 AM", "3/17/19 1:00 AM", "3/17/19 2:00 AM", "3/17/19 3:00 AM", "3/17/19 4:00 AM", "3/17/19 5:00 AM", "3/17/19 6:00 AM", "3/17/19 7:00 AM", "3/17/19 8:00 AM", "3/17/19 9:00 AM", "3/17/19 10:00 AM", "3/17/19 11:00 AM", "3/17/19 12:00 PM", "3/17/19 1:00 PM", "3/17/19 2:00 PM", "3/17/19 3:00 PM", "3/17/19 4:00 PM", "3/17/19 5:00 PM", "3/17/19 6:00 PM", "3/17/19 7:00 PM", "3/17/19 8:00 PM", "3/17/19 9:00 PM", "3/17/19 10:00 PM", "3/17/19 11:00 PM", "3/18/19 12:00 AM", "3/18/19 1:00 AM", "3/18/19 2:00 AM", "3/18/19 3:00 AM", "3/18/19 4:00 AM", "3/18/19 5:00 AM", "3/18/19 6:00 AM", "3/18/19 7:00 AM", "3/18/19 8:00 AM", "3/18/19 9:00 AM", "3/18/19 10:00 AM", "3/18/19 11:00 AM", "3/18/19 12:00 PM", "3/18/19 1:00 PM", "3/18/19 2:00 PM", "3/18/19 3:00 PM", "3/18/19 4:00 PM", "3/18/19 5:00 PM", "3/18/19 6:00 PM", "3/18/19 7:00 PM", "3/18/19 8:00 PM", "3/18/19 9:00 PM", "3/18/19 10:00 PM", "3/18/19 11:00 PM", "3/19/19 12:00 AM", "3/19/19 1:00 AM", "3/19/19 2:00 AM", "3/19/19 3:00 AM", "3/19/19 4:00 AM", "3/19/19 5:00 AM", "3/19/19 6:00 AM", "3/19/19 7:00 AM", "3/19/19 8:00 AM", "3/19/19 9:00 AM", "3/19/19 10:00 AM", "3/19/19 11:00 AM", "3/19/19 12:00 PM", "3/19/19 1:00 PM", "3/19/19 2:00 PM", "3/19/19 3:00 PM", "3/19/19 4:00 PM", "3/19/19 5:00 PM", "3/19/19 6:00 PM", "3/19/19 7:00 PM", "3/19/19 8:00 PM", "3/19/19 9:00 PM", "3/19/19 10:00 PM", "3/19/19 11:00 PM", "3/20/19 12:00 AM", "3/20/19 1:00 AM", "3/20/19 2:00 AM", "3/20/19 3:00 AM", "3/20/19 4:00 AM", "3/20/19 5:00 AM", "3/20/19 6:00 AM", "3/20/19 7:00 AM", "3/20/19 8:00 AM", "3/20/19 9:00 AM", "3/20/19 10:00 AM", "3/20/19 11:00 AM", "3/20/19 12:00 PM", "3/20/19 1:00 PM", "3/20/19 2:00 PM", "3/20/19 3:00 PM", "3/20/19 4:00 PM", "3/20/19 5:00 PM", "3/20/19 6:00 PM", "3/20/19 7:00 PM", "3/20/19 8:00 PM", "3/20/19 9:00 PM", "3/20/19 10:00 PM", "3/20/19 11:00 PM", "3/21/19 12:00 AM", "3/21/19 1:00 AM", "3/21/19 2:00 AM", "3/21/19 3:00 AM", "3/21/19 4:00 AM", "3/21/19 5:00 AM", "3/21/19 6:00 AM", "3/21/19 7:00 AM", "3/21/19 8:00 AM", "3/21/19 9:00 AM", "3/21/19 10:00 AM", "3/21/19 11:00 AM", "3/21/19 12:00 PM", "3/21/19 1:00 PM", "3/21/19 2:00 PM", "3/21/19 3:00 PM", "3/21/19 4:00 PM", "3/21/19 5:00 PM", "3/21/19 6:00 PM", "3/21/19 7:00 PM", "3/21/19 8:00 PM", "3/21/19 9:00 PM", "3/21/19 10:00 PM", "3/21/19 11:00 PM", "3/22/19 12:00 AM", "3/22/19 1:00 AM", "3/22/19 2:00 AM", "3/22/19 3:00 AM", "3/22/19 4:00 AM", "3/22/19 5:00 AM", "3/22/19 6:00 AM", "3/22/19 7:00 AM", "3/22/19 8:00 AM", "3/22/19 9:00 AM", "3/22/19 10:00 AM", "3/22/19 11:00 AM", "3/22/19 12:00 PM", "3/22/19 1:00 PM", "3/22/19 2:00 PM", "3/22/19 3:00 PM", "3/22/19 4:00 PM", "3/22/19 5:00 PM", "3/22/19 6:00 PM", "3/22/19 7:00 PM", "3/22/19 8:00 PM", "3/22/19 9:00 PM", "3/22/19 10:00 PM", "3/22/19 11:00 PM", "3/23/19 12:00 AM", "3/23/19 1:00 AM", "3/23/19 2:00 AM", "3/23/19 3:00 AM", "3/23/19 4:00 AM", "3/23/19 5:00 AM", "3/23/19 6:00 AM", "3/23/19 7:00 AM", "3/23/19 8:00 AM", "3/23/19 9:00 AM", "3/23/19 10:00 AM", "3/23/19 11:00 AM", "3/23/19 12:00 PM", "3/23/19 1:00 PM", "3/23/19 2:00 PM", "3/23/19 3:00 PM", "3/23/19 4:00 PM", "3/23/19 5:00 PM", "3/23/19 6:00 PM", "3/23/19 7:00 PM", "3/23/19 8:00 PM", "3/23/19 9:00 PM", "3/23/19 10:00 PM", "3/23/19 11:00 PM", "3/24/19 12:00 AM", "3/24/19 1:00 AM", "3/24/19 2:00 AM", "3/24/19 3:00 AM", "3/24/19 4:00 AM", "3/24/19 5:00 AM", "3/24/19 6:00 AM", "3/24/19 7:00 AM", "3/24/19 8:00 AM", "3/24/19 9:00 AM", "3/24/19 10:00 AM", "3/24/19 11:00 AM", "3/24/19 12:00 PM", "3/24/19 1:00 PM", "3/24/19 2:00 PM", "3/24/19 3:00 PM", "3/24/19 4:00 PM", "3/24/19 5:00 PM", "3/24/19 6:00 PM", "3/24/19 7:00 PM", "3/24/19 8:00 PM", "3/24/19 9:00 PM", "3/24/19 10:00 PM", "3/24/19 11:00 PM", "3/25/19 12:00 AM", "3/25/19 1:00 AM", "3/25/19 2:00 AM", "3/25/19 3:00 AM", "3/25/19 4:00 AM", "3/25/19 5:00 AM", "3/25/19 6:00 AM", "3/25/19 7:00 AM", "3/25/19 8:00 AM", "3/25/19 9:00 AM", "3/25/19 10:00 AM", "3/25/19 11:00 AM", "3/25/19 12:00 PM", "3/25/19 1:00 PM", "3/25/19 2:00 PM", "3/25/19 3:00 PM", "3/25/19 4:00 PM", "3/25/19 5:00 PM", "3/25/19 6:00 PM", "3/25/19 7:00 PM", "3/25/19 8:00 PM", "3/25/19 9:00 PM", "3/25/19 10:00 PM", "3/25/19 11:00 PM", "3/26/19 12:00 AM", "3/26/19 1:00 AM", "3/26/19 2:00 AM", "3/26/19 3:00 AM", "3/26/19 4:00 AM", "3/26/19 5:00 AM", "3/26/19 6:00 AM", "3/26/19 7:00 AM", "3/26/19 8:00 AM", "3/26/19 9:00 AM", "3/26/19 10:00 AM", "3/26/19 11:00 AM", "3/26/19 12:00 PM", "3/26/19 1:00 PM", "3/26/19 2:00 PM", "3/26/19 3:00 PM", "3/26/19 4:00 PM", "3/26/19 5:00 PM", "3/26/19 6:00 PM", "3/26/19 7:00 PM", "3/26/19 8:00 PM", "3/26/19 9:00 PM", "3/26/19 10:00 PM", "3/26/19 11:00 PM", "3/27/19 12:00 AM", "3/27/19 1:00 AM", "3/27/19 2:00 AM", "3/27/19 3:00 AM", "3/27/19 4:00 AM", "3/27/19 5:00 AM", "3/27/19 6:00 AM", "3/27/19 7:00 AM", "3/27/19 8:00 AM", "3/27/19 9:00 AM", "3/27/19 10:00 AM", "3/27/19 11:00 AM", "3/27/19 12:00 PM", "3/27/19 1:00 PM", "3/27/19 2:00 PM", "3/27/19 3:00 PM", "3/27/19 4:00 PM", "3/27/19 5:00 PM", "3/27/19 6:00 PM", "3/27/19 7:00 PM", "3/27/19 8:00 PM", "3/27/19 9:00 PM", "3/27/19 10:00 PM", "3/27/19 11:00 PM", "3/28/19 12:00 AM", "3/28/19 1:00 AM", "3/28/19 2:00 AM", "3/28/19 3:00 AM", "3/28/19 4:00 AM", "3/28/19 5:00 AM", "3/28/19 6:00 AM", "3/28/19 7:00 AM", "3/28/19 8:00 AM", "3/28/19 9:00 AM", "3/28/19 10:00 AM", "3/28/19 11:00 AM", "3/28/19 12:00 PM", "3/28/19 1:00 PM", "3/28/19 2:00 PM", "3/28/19 3:00 PM", "3/28/19 4:00 PM", "3/28/19 5:00 PM", "3/28/19 6:00 PM", "3/28/19 7:00 PM", "3/28/19 8:00 PM", "3/28/19 9:00 PM", "3/28/19 10:00 PM", "3/28/19 11:00 PM", "3/29/19 12:00 AM", "3/29/19 1:00 AM", "3/29/19 2:00 AM", "3/29/19 3:00 AM", "3/29/19 4:00 AM", "3/29/19 5:00 AM", "3/29/19 6:00 AM", "3/29/19 7:00 AM", "3/29/19 8:00 AM", "3/29/19 9:00 AM", "3/29/19 10:00 AM", "3/29/19 11:00 AM", "3/29/19 12:00 PM", "3/29/19 1:00 PM", "3/29/19 2:00 PM", "3/29/19 3:00 PM", "3/29/19 4:00 PM", "3/29/19 5:00 PM", "3/29/19 6:00 PM", "3/29/19 7:00 PM", "3/29/19 8:00 PM", "3/29/19 9:00 PM", "3/29/19 10:00 PM", "3/29/19 11:00 PM", "3/30/19 12:00 AM", "3/30/19 1:00 AM", "3/30/19 2:00 AM", "3/30/19 3:00 AM", "3/30/19 4:00 AM", "3/30/19 5:00 AM", "3/30/19 6:00 AM", "3/30/19 7:00 AM", "3/30/19 8:00 AM", "3/30/19 9:00 AM", "3/30/19 10:00 AM", "3/30/19 11:00 AM", "3/30/19 12:00 PM", "3/30/19 1:00 PM", "3/30/19 2:00 PM", "3/30/19 3:00 PM", "3/30/19 4:00 PM", "3/30/19 5:00 PM", "3/30/19 6:00 PM", "3/30/19 7:00 PM", "3/30/19 8:00 PM", "3/30/19 9:00 PM", "3/30/19 10:00 PM", "3/30/19 11:00 PM", "3/31/19 12:00 AM", "3/31/19 1:00 AM", "3/31/19 2:00 AM", "3/31/19 3:00 AM", "3/31/19 4:00 AM", "3/31/19 5:00 AM", "3/31/19 6:00 AM", "3/31/19 7:00 AM", "3/31/19 8:00 AM", "3/31/19 9:00 AM", "3/31/19 10:00 AM", "3/31/19 11:00 AM", "3/31/19 12:00 PM", "3/31/19 1:00 PM", "3/31/19 2:00 PM", "3/31/19 3:00 PM", "3/31/19 4:00 PM", "3/31/19 5:00 PM", "3/31/19 6:00 PM", "3/31/19 7:00 PM", "3/31/19 8:00 PM", "3/31/19 9:00 PM", "3/31/19 10:00 PM", "3/31/19 11:00 PM", "4/1/19 12:00 AM", "4/1/19 1:00 AM", "4/1/19 2:00 AM", "4/1/19 3:00 AM", "4/1/19 4:00 AM", "4/1/19 5:00 AM", "4/1/19 6:00 AM", "4/1/19 7:00 AM", "4/1/19 8:00 AM", "4/1/19 9:00 AM", "4/1/19 10:00 AM", "4/1/19 11:00 AM", "4/1/19 12:00 PM", "4/1/19 1:00 PM", "4/1/19 2:00 PM", "4/1/19 3:00 PM", "4/1/19 4:00 PM", "4/1/19 5:00 PM", "4/1/19 6:00 PM", "4/1/19 7:00 PM", "4/1/19 8:00 PM", "4/1/19 9:00 PM", "4/1/19 10:00 PM", "4/1/19 11:00 PM", "4/2/19 12:00 AM", "4/2/19 1:00 AM", "4/2/19 2:00 AM", "4/2/19 3:00 AM", "4/2/19 4:00 AM", "4/2/19 5:00 AM", "4/2/19 6:00 AM", "4/2/19 7:00 AM", "4/2/19 8:00 AM", "4/2/19 9:00 AM", "4/2/19 10:00 AM", "4/2/19 11:00 AM", "4/2/19 12:00 PM", "4/2/19 1:00 PM", "4/2/19 2:00 PM", "4/2/19 3:00 PM", "4/2/19 4:00 PM", "4/2/19 5:00 PM", "4/2/19 6:00 PM", "4/2/19 7:00 PM", "4/2/19 8:00 PM", "4/2/19 9:00 PM", "4/2/19 10:00 PM", "4/2/19 11:00 PM", "4/3/19 12:00 AM", "4/3/19 1:00 AM", "4/3/19 2:00 AM", "4/3/19 3:00 AM", "4/3/19 4:00 AM", "4/3/19 5:00 AM", "4/3/19 6:00 AM", "4/3/19 7:00 AM", "4/3/19 8:00 AM", "4/3/19 9:00 AM", "4/3/19 10:00 AM", "4/3/19 11:00 AM", "4/3/19 12:00 PM", "4/3/19 1:00 PM", "4/3/19 2:00 PM", "4/3/19 3:00 PM", "4/3/19 4:00 PM", "4/3/19 5:00 PM", "4/3/19 6:00 PM", "4/3/19 7:00 PM", "4/3/19 8:00 PM", "4/3/19 9:00 PM", "4/3/19 10:00 PM", "4/3/19 11:00 PM", "4/4/19 12:00 AM", "4/4/19 1:00 AM", "4/4/19 2:00 AM", "4/4/19 3:00 AM", "4/4/19 4:00 AM", "4/4/19 5:00 AM", "4/4/19 6:00 AM", "4/4/19 7:00 AM", "4/4/19 8:00 AM", "4/4/19 9:00 AM", "4/4/19 10:00 AM", "4/4/19 11:00 AM", "4/4/19 12:00 PM", "4/4/19 1:00 PM", "4/4/19 2:00 PM", "4/4/19 3:00 PM", "4/4/19 4:00 PM", "4/4/19 5:00 PM", "4/4/19 6:00 PM", "4/4/19 7:00 PM", "4/4/19 8:00 PM", "4/4/19 9:00 PM", "4/4/19 10:00 PM", "4/4/19 11:00 PM", "4/5/19 12:00 AM", "4/5/19 1:00 AM", "4/5/19 2:00 AM", "4/5/19 3:00 AM", "4/5/19 4:00 AM", "4/5/19 5:00 AM", "4/5/19 6:00 AM", "4/5/19 7:00 AM", "4/5/19 8:00 AM", "4/5/19 9:00 AM", "4/5/19 10:00 AM", "4/5/19 11:00 AM", "4/5/19 12:00 PM", "4/5/19 1:00 PM", "4/5/19 2:00 PM", "4/5/19 3:00 PM", "4/5/19 4:00 PM", "4/5/19 5:00 PM", "4/5/19 6:00 PM", "4/5/19 7:00 PM", "4/5/19 8:00 PM", "4/5/19 9:00 PM", "4/5/19 10:00 PM", "4/5/19 11:00 PM", "4/6/19 12:00 AM", "4/6/19 1:00 AM", "4/6/19 2:00 AM", "4/6/19 3:00 AM", "4/6/19 4:00 AM", "4/6/19 5:00 AM", "4/6/19 6:00 AM", "4/6/19 7:00 AM", "4/6/19 8:00 AM", "4/6/19 9:00 AM", "4/6/19 10:00 AM", "4/6/19 11:00 AM", "4/6/19 12:00 PM", "4/6/19 1:00 PM", "4/6/19 2:00 PM", "4/6/19 3:00 PM", "4/6/19 4:00 PM", "4/6/19 5:00 PM", "4/6/19 6:00 PM", "4/6/19 7:00 PM", "4/6/19 8:00 PM", "4/6/19 9:00 PM", "4/6/19 10:00 PM", "4/6/19 11:00 PM", "4/7/19 12:00 AM", "4/7/19 1:00 AM", "4/7/19 2:00 AM", "4/7/19 3:00 AM", "4/7/19 4:00 AM", "4/7/19 5:00 AM", "4/7/19 6:00 AM", "4/7/19 7:00 AM", "4/7/19 8:00 AM", "4/7/19 9:00 AM", "4/7/19 10:00 AM", "4/7/19 11:00 AM", "4/7/19 12:00 PM", "4/7/19 1:00 PM", "4/7/19 2:00 PM", "4/7/19 3:00 PM", "4/7/19 4:00 PM", "4/7/19 5:00 PM", "4/7/19 6:00 PM", "4/7/19 7:00 PM", "4/7/19 8:00 PM", "4/7/19 9:00 PM", "4/7/19 10:00 PM", "4/7/19 11:00 PM", "4/8/19 12:00 AM", "4/8/19 1:00 AM", "4/8/19 2:00 AM", "4/8/19 3:00 AM", "4/8/19 4:00 AM", "4/8/19 5:00 AM", "4/8/19 6:00 AM", "4/8/19 7:00 AM", "4/8/19 8:00 AM", "4/8/19 9:00 AM", "4/8/19 10:00 AM", "4/8/19 11:00 AM", "4/8/19 12:00 PM", "4/8/19 1:00 PM", "4/8/19 2:00 PM", "4/8/19 3:00 PM", "4/8/19 4:00 PM", "4/8/19 5:00 PM", "4/8/19 6:00 PM", "4/8/19 7:00 PM", "4/8/19 8:00 PM", "4/8/19 9:00 PM", "4/8/19 10:00 PM", "4/8/19 11:00 PM", "4/9/19 12:00 AM", "4/9/19 1:00 AM", "4/9/19 2:00 AM", "4/9/19 3:00 AM", "4/9/19 4:00 AM", "4/9/19 5:00 AM", "4/9/19 6:00 AM", "4/9/19 7:00 AM", "4/9/19 8:00 AM", "4/9/19 9:00 AM", "4/9/19 10:00 AM", "4/9/19 11:00 AM", "4/9/19 12:00 PM", "4/9/19 1:00 PM", "4/9/19 2:00 PM", "4/9/19 3:00 PM", "4/9/19 4:00 PM", "4/9/19 5:00 PM", "4/9/19 6:00 PM", "4/9/19 7:00 PM", "4/9/19 8:00 PM", "4/9/19 9:00 PM", "4/9/19 10:00 PM", "4/9/19 11:00 PM", "4/10/19 12:00 AM", "4/10/19 1:00 AM", "4/10/19 2:00 AM", "4/10/19 3:00 AM", "4/10/19 4:00 AM", "4/10/19 5:00 AM", "4/10/19 6:00 AM", "4/10/19 7:00 AM", "4/10/19 8:00 AM", "4/10/19 9:00 AM", "4/10/19 10:00 AM", "4/10/19 11:00 AM", "4/10/19 12:00 PM", "4/10/19 1:00 PM", "4/10/19 2:00 PM", "4/10/19 3:00 PM", "4/10/19 4:00 PM", "4/10/19 5:00 PM", "4/10/19 6:00 PM", "4/10/19 7:00 PM", "4/10/19 8:00 PM", "4/10/19 9:00 PM", "4/10/19 10:00 PM", "4/10/19 11:00 PM", "4/11/19 12:00 AM", "4/11/19 1:00 AM", "4/11/19 2:00 AM", "4/11/19 3:00 AM", "4/11/19 4:00 AM", "4/11/19 5:00 AM", "4/11/19 6:00 AM", "4/11/19 7:00 AM", "4/11/19 8:00 AM", "4/11/19 9:00 AM", "4/11/19 10:00 AM", "4/11/19 11:00 AM", "4/11/19 12:00 PM", "4/11/19 1:00 PM", "4/11/19 2:00 PM", "4/11/19 3:00 PM", "4/11/19 4:00 PM", "4/11/19 5:00 PM", "4/11/19 6:00 PM", "4/11/19 7:00 PM", "4/11/19 8:00 PM", "4/11/19 9:00 PM", "4/11/19 10:00 PM", "4/11/19 11:00 PM", "4/12/19 12:00 AM", "4/12/19 1:00 AM", "4/12/19 2:00 AM", "4/12/19 3:00 AM", "4/12/19 4:00 AM", "4/12/19 5:00 AM", "4/12/19 6:00 AM", "4/12/19 7:00 AM", "4/12/19 8:00 AM", "4/12/19 9:00 AM", "4/12/19 10:00 AM", "4/12/19 11:00 AM", "4/12/19 12:00 PM", "4/12/19 1:00 PM", "4/12/19 2:00 PM", "4/12/19 3:00 PM", "4/12/19 4:00 PM", "4/12/19 5:00 PM", "4/12/19 6:00 PM", "4/12/19 7:00 PM", "4/12/19 8:00 PM", "4/12/19 9:00 PM", "4/12/19 10:00 PM", "4/12/19 11:00 PM", "4/13/19 12:00 AM", "4/13/19 1:00 AM", "4/13/19 2:00 AM", "4/13/19 3:00 AM", "4/13/19 4:00 AM", "4/13/19 5:00 AM", "4/13/19 6:00 AM", "4/13/19 7:00 AM", "4/13/19 8:00 AM", "4/13/19 9:00 AM", "4/13/19 10:00 AM", "4/13/19 11:00 AM", "4/13/19 12:00 PM", "4/13/19 1:00 PM", "4/13/19 2:00 PM", "4/13/19 3:00 PM", "4/13/19 4:00 PM", "4/13/19 5:00 PM", "4/13/19 6:00 PM", "4/13/19 7:00 PM", "4/13/19 8:00 PM", "4/13/19 9:00 PM", "4/13/19 10:00 PM", "4/13/19 11:00 PM", "4/14/19 12:00 AM", "4/14/19 1:00 AM", "4/14/19 2:00 AM", "4/14/19 3:00 AM", "4/14/19 4:00 AM", "4/14/19 5:00 AM", "4/14/19 6:00 AM", "4/14/19 7:00 AM", "4/14/19 8:00 AM", "4/14/19 9:00 AM", "4/14/19 10:00 AM", "4/14/19 11:00 AM", "4/14/19 12:00 PM", "4/14/19 1:00 PM", "4/14/19 2:00 PM", "4/14/19 3:00 PM", "4/14/19 4:00 PM", "4/14/19 5:00 PM", "4/14/19 6:00 PM", "4/14/19 7:00 PM", "4/14/19 8:00 PM", "4/14/19 9:00 PM", "4/14/19 10:00 PM", "4/14/19 11:00 PM", "4/15/19 12:00 AM", "4/15/19 1:00 AM", "4/15/19 2:00 AM", "4/15/19 3:00 AM", "4/15/19 4:00 AM", "4/15/19 5:00 AM", "4/15/19 6:00 AM", "4/15/19 7:00 AM", "4/15/19 8:00 AM", "4/15/19 9:00 AM", "4/15/19 10:00 AM", "4/15/19 11:00 AM", "4/15/19 12:00 PM", "4/15/19 1:00 PM", "4/15/19 2:00 PM", "4/15/19 3:00 PM", "4/15/19 4:00 PM", "4/15/19 5:00 PM", "4/15/19 6:00 PM", "4/15/19 7:00 PM", "4/15/19 8:00 PM", "4/15/19 9:00 PM", "4/15/19 10:00 PM", "4/15/19 11:00 PM", "4/16/19 12:00 AM", "4/16/19 1:00 AM", "4/16/19 2:00 AM", "4/16/19 3:00 AM", "4/16/19 4:00 AM", "4/16/19 5:00 AM", "4/16/19 6:00 AM", "4/16/19 7:00 AM", "4/16/19 8:00 AM", "4/16/19 9:00 AM", "4/16/19 10:00 AM", "4/16/19 11:00 AM", "4/16/19 12:00 PM", "4/16/19 1:00 PM", "4/16/19 2:00 PM", "4/16/19 3:00 PM", "4/16/19 4:00 PM", "4/16/19 5:00 PM", "4/16/19 6:00 PM", "4/16/19 7:00 PM", "4/16/19 8:00 PM", "4/16/19 9:00 PM", "4/16/19 10:00 PM", "4/16/19 11:00 PM", "4/17/19 12:00 AM", "4/17/19 1:00 AM", "4/17/19 2:00 AM", "4/17/19 3:00 AM", "4/17/19 4:00 AM", "4/17/19 5:00 AM", "4/17/19 6:00 AM", "4/17/19 7:00 AM", "4/17/19 8:00 AM", "4/17/19 9:00 AM", "4/17/19 10:00 AM", "4/17/19 11:00 AM", "4/17/19 12:00 PM", "4/17/19 1:00 PM", "4/17/19 2:00 PM", "4/17/19 3:00 PM", "4/17/19 4:00 PM", "4/17/19 5:00 PM", "4/17/19 6:00 PM", "4/17/19 7:00 PM", "4/17/19 8:00 PM", "4/17/19 9:00 PM", "4/17/19 10:00 PM", "4/17/19 11:00 PM", "4/18/19 12:00 AM", "4/18/19 1:00 AM", "4/18/19 2:00 AM", "4/18/19 3:00 AM", "4/18/19 4:00 AM", "4/18/19 5:00 AM", "4/18/19 6:00 AM", "4/18/19 7:00 AM", "4/18/19 8:00 AM", "4/18/19 9:00 AM", "4/18/19 10:00 AM", "4/18/19 11:00 AM", "4/18/19 12:00 PM", "4/18/19 1:00 PM", "4/18/19 2:00 PM", "4/18/19 3:00 PM", "4/18/19 4:00 PM", "4/18/19 5:00 PM", "4/18/19 6:00 PM", "4/18/19 7:00 PM", "4/18/19 8:00 PM", "4/18/19 9:00 PM", "4/18/19 10:00 PM", "4/18/19 11:00 PM", "4/19/19 12:00 AM", "4/19/19 1:00 AM", "4/19/19 2:00 AM", "4/19/19 3:00 AM", "4/19/19 4:00 AM", "4/19/19 5:00 AM", "4/19/19 6:00 AM", "4/19/19 7:00 AM", "4/19/19 8:00 AM", "4/19/19 9:00 AM", "4/19/19 10:00 AM", "4/19/19 11:00 AM", "4/19/19 12:00 PM", "4/19/19 1:00 PM", "4/19/19 2:00 PM", "4/19/19 3:00 PM", "4/19/19 4:00 PM", "4/19/19 5:00 PM", "4/19/19 6:00 PM", "4/19/19 7:00 PM", "4/19/19 8:00 PM", "4/19/19 9:00 PM", "4/19/19 10:00 PM", "4/19/19 11:00 PM", "4/20/19 12:00 AM", "4/20/19 1:00 AM", "4/20/19 2:00 AM", "4/20/19 3:00 AM", "4/20/19 4:00 AM", "4/20/19 5:00 AM", "4/20/19 6:00 AM", "4/20/19 7:00 AM", "4/20/19 8:00 AM", "4/20/19 9:00 AM", "4/20/19 10:00 AM", "4/20/19 11:00 AM", "4/20/19 12:00 PM", "4/20/19 1:00 PM", "4/20/19 2:00 PM", "4/20/19 3:00 PM", "4/20/19 4:00 PM", "4/20/19 5:00 PM", "4/20/19 6:00 PM", "4/20/19 7:00 PM", "4/20/19 8:00 PM", "4/20/19 9:00 PM", "4/20/19 10:00 PM", "4/20/19 11:00 PM", "4/21/19 12:00 AM", "4/21/19 1:00 AM", "4/21/19 2:00 AM", "4/21/19 3:00 AM", "4/21/19 4:00 AM", "4/21/19 5:00 AM", "4/21/19 6:00 AM", "4/21/19 7:00 AM", "4/21/19 8:00 AM", "4/21/19 9:00 AM", "4/21/19 10:00 AM", "4/21/19 11:00 AM", "4/21/19 12:00 PM", "4/21/19 1:00 PM", "4/21/19 2:00 PM", "4/21/19 3:00 PM", "4/21/19 4:00 PM", "4/21/19 5:00 PM", "4/21/19 6:00 PM", "4/21/19 7:00 PM", "4/21/19 8:00 PM", "4/21/19 9:00 PM", "4/21/19 10:00 PM", "4/21/19 11:00 PM", "4/22/19 12:00 AM", "4/22/19 1:00 AM", "4/22/19 2:00 AM", "4/22/19 3:00 AM", "4/22/19 4:00 AM", "4/22/19 5:00 AM", "4/22/19 6:00 AM", "4/22/19 7:00 AM", "4/22/19 8:00 AM", "4/22/19 9:00 AM", "4/22/19 10:00 AM", "4/22/19 11:00 AM", "4/22/19 12:00 PM", "4/22/19 1:00 PM", "4/22/19 2:00 PM", "4/22/19 3:00 PM", "4/22/19 4:00 PM", "4/22/19 5:00 PM", "4/22/19 6:00 PM", "4/22/19 7:00 PM", "4/22/19 8:00 PM", "4/22/19 9:00 PM", "4/22/19 10:00 PM", "4/22/19 11:00 PM", "4/23/19 12:00 AM", "4/23/19 1:00 AM", "4/23/19 2:00 AM", "4/23/19 3:00 AM", "4/23/19 4:00 AM", "4/23/19 5:00 AM", "4/23/19 6:00 AM", "4/23/19 7:00 AM", "4/23/19 8:00 AM", "4/23/19 9:00 AM", "4/23/19 10:00 AM", "4/23/19 11:00 AM", "4/23/19 12:00 PM", "4/23/19 1:00 PM", "4/23/19 2:00 PM", "4/23/19 3:00 PM", "4/23/19 4:00 PM", "4/23/19 5:00 PM", "4/23/19 6:00 PM", "4/23/19 7:00 PM", "4/23/19 8:00 PM", "4/23/19 9:00 PM", "4/23/19 10:00 PM", "4/23/19 11:00 PM", "4/24/19 12:00 AM", "4/24/19 1:00 AM", "4/24/19 2:00 AM", "4/24/19 3:00 AM", "4/24/19 4:00 AM", "4/24/19 5:00 AM", "4/24/19 6:00 AM", "4/24/19 7:00 AM", "4/24/19 8:00 AM", "4/24/19 9:00 AM", "4/24/19 10:00 AM", "4/24/19 11:00 AM", "4/24/19 12:00 PM", "4/24/19 1:00 PM", "4/24/19 2:00 PM", "4/24/19 3:00 PM", "4/24/19 4:00 PM", "4/24/19 5:00 PM", "4/24/19 6:00 PM", "4/24/19 7:00 PM", "4/24/19 8:00 PM", "4/24/19 9:00 PM", "4/24/19 10:00 PM", "4/24/19 11:00 PM", "4/25/19 12:00 AM", "4/25/19 1:00 AM", "4/25/19 2:00 AM", "4/25/19 3:00 AM", "4/25/19 4:00 AM", "4/25/19 5:00 AM", "4/25/19 6:00 AM", "4/25/19 7:00 AM", "4/25/19 8:00 AM", "4/25/19 9:00 AM", "4/25/19 10:00 AM", "4/25/19 11:00 AM", "4/25/19 12:00 PM", "4/25/19 1:00 PM", "4/25/19 2:00 PM", "4/25/19 3:00 PM", "4/25/19 4:00 PM", "4/25/19 5:00 PM", "4/25/19 6:00 PM", "4/25/19 7:00 PM", "4/25/19 8:00 PM", "4/25/19 9:00 PM", "4/25/19 10:00 PM", "4/25/19 11:00 PM", "4/26/19 12:00 AM", "4/26/19 1:00 AM", "4/26/19 2:00 AM", "4/26/19 3:00 AM", "4/26/19 4:00 AM", "4/26/19 5:00 AM", "4/26/19 6:00 AM", "4/26/19 7:00 AM", "4/26/19 8:00 AM", "4/26/19 9:00 AM", "4/26/19 10:00 AM", "4/26/19 11:00 AM", "4/26/19 12:00 PM", "4/26/19 1:00 PM", "4/26/19 2:00 PM", "4/26/19 3:00 PM", "4/26/19 4:00 PM", "4/26/19 5:00 PM", "4/26/19 6:00 PM", "4/26/19 7:00 PM", "4/26/19 8:00 PM", "4/26/19 9:00 PM", "4/26/19 10:00 PM", "4/26/19 11:00 PM", "4/27/19 12:00 AM", "4/27/19 1:00 AM", "4/27/19 2:00 AM", "4/27/19 3:00 AM", "4/27/19 4:00 AM", "4/27/19 5:00 AM", "4/27/19 6:00 AM", "4/27/19 7:00 AM", "4/27/19 8:00 AM", "4/27/19 9:00 AM", "4/27/19 10:00 AM", "4/27/19 11:00 AM", "4/27/19 12:00 PM", "4/27/19 1:00 PM", "4/27/19 2:00 PM", "4/27/19 3:00 PM", "4/27/19 4:00 PM", "4/27/19 5:00 PM", "4/27/19 6:00 PM", "4/27/19 7:00 PM", "4/27/19 8:00 PM", "4/27/19 9:00 PM", "4/27/19 10:00 PM", "4/27/19 11:00 PM", "4/28/19 12:00 AM", "4/28/19 1:00 AM", "4/28/19 2:00 AM", "4/28/19 3:00 AM", "4/28/19 4:00 AM", "4/28/19 5:00 AM", "4/28/19 6:00 AM", "4/28/19 7:00 AM", "4/28/19 8:00 AM", "4/28/19 9:00 AM", "4/28/19 10:00 AM", "4/28/19 11:00 AM", "4/28/19 12:00 PM", "4/28/19 1:00 PM", "4/28/19 2:00 PM", "4/28/19 3:00 PM", "4/28/19 4:00 PM", "4/28/19 5:00 PM", "4/28/19 6:00 PM", "4/28/19 7:00 PM", "4/28/19 8:00 PM", "4/28/19 9:00 PM", "4/28/19 10:00 PM", "4/28/19 11:00 PM", "4/29/19 12:00 AM", "4/29/19 1:00 AM", "4/29/19 2:00 AM", "4/29/19 3:00 AM", "4/29/19 4:00 AM", "4/29/19 5:00 AM", "4/29/19 6:00 AM", "4/29/19 7:00 AM", "4/29/19 8:00 AM", "4/29/19 9:00 AM", "4/29/19 10:00 AM", "4/29/19 11:00 AM", "4/29/19 12:00 PM", "4/29/19 1:00 PM", "4/29/19 2:00 PM", "4/29/19 3:00 PM", "4/29/19 4:00 PM", "4/29/19 5:00 PM", "4/29/19 6:00 PM", "4/29/19 7:00 PM", "4/29/19 8:00 PM", "4/29/19 9:00 PM", "4/29/19 10:00 PM", "4/29/19 11:00 PM", "4/30/19 12:00 AM", "4/30/19 1:00 AM", "4/30/19 2:00 AM", "4/30/19 3:00 AM", "4/30/19 4:00 AM", "4/30/19 5:00 AM", "4/30/19 6:00 AM", "4/30/19 7:00 AM", "4/30/19 8:00 AM", "4/30/19 9:00 AM", "4/30/19 10:00 AM", "4/30/19 11:00 AM", "4/30/19 12:00 PM", "4/30/19 1:00 PM", "4/30/19 2:00 PM", "4/30/19 3:00 PM", "4/30/19 4:00 PM", "4/30/19 5:00 PM", "4/30/19 6:00 PM", "4/30/19 7:00 PM", "4/30/19 8:00 PM", "4/30/19 9:00 PM", "4/30/19 10:00 PM", "4/30/19 11:00 PM", "5/1/19 12:00 AM", "5/1/19 1:00 AM", "5/1/19 2:00 AM", "5/1/19 3:00 AM", "5/1/19 4:00 AM", "5/1/19 5:00 AM", "5/1/19 6:00 AM", "5/1/19 7:00 AM", "5/1/19 8:00 AM", "5/1/19 9:00 AM", "5/1/19 10:00 AM", "5/1/19 11:00 AM", "5/1/19 12:00 PM", "5/1/19 1:00 PM", "5/1/19 2:00 PM", "5/1/19 3:00 PM", "5/1/19 4:00 PM", "5/1/19 5:00 PM", "5/1/19 6:00 PM", "5/1/19 7:00 PM", "5/1/19 8:00 PM", "5/1/19 9:00 PM", "5/1/19 10:00 PM", "5/1/19 11:00 PM", "5/2/19 12:00 AM", "5/2/19 1:00 AM", "5/2/19 2:00 AM", "5/2/19 3:00 AM", "5/2/19 4:00 AM", "5/2/19 5:00 AM", "5/2/19 6:00 AM", "5/2/19 7:00 AM", "5/2/19 8:00 AM", "5/2/19 9:00 AM", "5/2/19 10:00 AM", "5/2/19 11:00 AM", "5/2/19 12:00 PM", "5/2/19 1:00 PM", "5/2/19 2:00 PM", "5/2/19 3:00 PM", "5/2/19 4:00 PM", "5/2/19 5:00 PM", "5/2/19 6:00 PM", "5/2/19 7:00 PM", "5/2/19 8:00 PM", "5/2/19 9:00 PM", "5/2/19 10:00 PM", "5/2/19 11:00 PM", "5/3/19 12:00 AM", "5/3/19 1:00 AM", "5/3/19 2:00 AM", "5/3/19 3:00 AM", "5/3/19 4:00 AM", "5/3/19 5:00 AM", "5/3/19 6:00 AM", "5/3/19 7:00 AM", "5/3/19 8:00 AM", "5/3/19 9:00 AM", "5/3/19 10:00 AM", "5/3/19 11:00 AM", "5/3/19 12:00 PM", "5/3/19 1:00 PM", "5/3/19 2:00 PM", "5/3/19 3:00 PM", "5/3/19 4:00 PM", "5/3/19 5:00 PM", "5/3/19 6:00 PM", "5/3/19 7:00 PM", "5/3/19 8:00 PM", "5/3/19 9:00 PM", "5/3/19 10:00 PM", "5/3/19 11:00 PM", "5/4/19 12:00 AM", "5/4/19 1:00 AM", "5/4/19 2:00 AM", "5/4/19 3:00 AM", "5/4/19 4:00 AM", "5/4/19 5:00 AM", "5/4/19 6:00 AM", "5/4/19 7:00 AM", "5/4/19 8:00 AM", "5/4/19 9:00 AM", "5/4/19 10:00 AM", "5/4/19 11:00 AM", "5/4/19 12:00 PM", "5/4/19 1:00 PM", "5/4/19 2:00 PM", "5/4/19 3:00 PM", "5/4/19 4:00 PM", "5/4/19 5:00 PM", "5/4/19 6:00 PM", "5/4/19 7:00 PM", "5/4/19 8:00 PM", "5/4/19 9:00 PM", "5/4/19 10:00 PM", "5/4/19 11:00 PM", "5/5/19 12:00 AM", "5/5/19 1:00 AM", "5/5/19 2:00 AM", "5/5/19 3:00 AM", "5/5/19 4:00 AM", "5/5/19 5:00 AM", "5/5/19 6:00 AM", "5/5/19 7:00 AM", "5/5/19 8:00 AM", "5/5/19 9:00 AM", "5/5/19 10:00 AM", "5/5/19 11:00 AM", "5/5/19 12:00 PM", "5/5/19 1:00 PM", "5/5/19 2:00 PM", "5/5/19 3:00 PM", "5/5/19 4:00 PM", "5/5/19 5:00 PM", "5/5/19 6:00 PM", "5/5/19 7:00 PM", "5/5/19 8:00 PM", "5/5/19 9:00 PM", "5/5/19 10:00 PM", "5/5/19 11:00 PM", "5/6/19 12:00 AM", "5/6/19 1:00 AM", "5/6/19 2:00 AM", "5/6/19 3:00 AM", "5/6/19 4:00 AM", "5/6/19 5:00 AM", "5/6/19 6:00 AM", "5/6/19 7:00 AM", "5/6/19 8:00 AM", "5/6/19 9:00 AM", "5/6/19 10:00 AM", "5/6/19 11:00 AM", "5/6/19 12:00 PM", "5/6/19 1:00 PM", "5/6/19 2:00 PM", "5/6/19 3:00 PM", "5/6/19 4:00 PM", "5/6/19 5:00 PM", "5/6/19 6:00 PM", "5/6/19 7:00 PM", "5/6/19 8:00 PM", "5/6/19 9:00 PM", "5/6/19 10:00 PM", "5/6/19 11:00 PM", "5/7/19 12:00 AM", "5/7/19 1:00 AM", "5/7/19 2:00 AM", "5/7/19 3:00 AM", "5/7/19 4:00 AM", "5/7/19 5:00 AM", "5/7/19 6:00 AM", "5/7/19 7:00 AM", "5/7/19 8:00 AM", "5/7/19 9:00 AM", "5/7/19 10:00 AM", "5/7/19 11:00 AM", "5/7/19 12:00 PM", "5/7/19 1:00 PM", "5/7/19 2:00 PM", "5/7/19 3:00 PM", "5/7/19 4:00 PM", "5/7/19 5:00 PM", "5/7/19 6:00 PM", "5/7/19 7:00 PM", "5/7/19 8:00 PM", "5/7/19 9:00 PM", "5/7/19 10:00 PM", "5/7/19 11:00 PM", "5/8/19 12:00 AM", "5/8/19 1:00 AM", "5/8/19 2:00 AM", "5/8/19 3:00 AM", "5/8/19 4:00 AM", "5/8/19 5:00 AM", "5/8/19 6:00 AM", "5/8/19 7:00 AM", "5/8/19 8:00 AM", "5/8/19 9:00 AM", "5/8/19 10:00 AM", "5/8/19 11:00 AM", "5/8/19 12:00 PM", "5/8/19 1:00 PM", "5/8/19 2:00 PM", "5/8/19 3:00 PM", "5/8/19 4:00 PM", "5/8/19 5:00 PM", "5/8/19 6:00 PM", "5/8/19 7:00 PM", "5/8/19 8:00 PM", "5/8/19 9:00 PM", "5/8/19 10:00 PM", "5/8/19 11:00 PM", "5/9/19 12:00 AM", "5/9/19 1:00 AM", "5/9/19 2:00 AM", "5/9/19 3:00 AM", "5/9/19 4:00 AM", "5/9/19 5:00 AM", "5/9/19 6:00 AM", "5/9/19 7:00 AM", "5/9/19 8:00 AM", "5/9/19 9:00 AM", "5/9/19 10:00 AM", "5/9/19 11:00 AM", "5/9/19 12:00 PM", "5/9/19 1:00 PM", "5/9/19 2:00 PM", "5/9/19 3:00 PM", "5/9/19 4:00 PM", "5/9/19 5:00 PM", "5/9/19 6:00 PM", "5/9/19 7:00 PM", "5/9/19 8:00 PM", "5/9/19 9:00 PM", "5/9/19 10:00 PM", "5/9/19 11:00 PM", "5/10/19 12:00 AM", "5/10/19 1:00 AM", "5/10/19 2:00 AM", "5/10/19 3:00 AM", "5/10/19 4:00 AM", "5/10/19 5:00 AM", "5/10/19 6:00 AM", "5/10/19 7:00 AM", "5/10/19 8:00 AM", "5/10/19 9:00 AM", "5/10/19 10:00 AM", "5/10/19 11:00 AM", "5/10/19 12:00 PM", "5/10/19 1:00 PM", "5/10/19 2:00 PM", "5/10/19 3:00 PM", "5/10/19 4:00 PM", "5/10/19 5:00 PM", "5/10/19 6:00 PM", "5/10/19 7:00 PM", "5/10/19 8:00 PM", "5/10/19 9:00 PM", "5/10/19 10:00 PM", "5/10/19 11:00 PM", "5/11/19 12:00 AM", "5/11/19 1:00 AM", "5/11/19 2:00 AM", "5/11/19 3:00 AM", "5/11/19 4:00 AM", "5/11/19 5:00 AM", "5/11/19 6:00 AM", "5/11/19 7:00 AM", "5/11/19 8:00 AM", "5/11/19 9:00 AM", "5/11/19 10:00 AM", "5/11/19 11:00 AM", "5/11/19 12:00 PM", "5/11/19 1:00 PM", "5/11/19 2:00 PM", "5/11/19 3:00 PM", "5/11/19 4:00 PM", "5/11/19 5:00 PM", "5/11/19 6:00 PM", "5/11/19 7:00 PM", "5/11/19 8:00 PM", "5/11/19 9:00 PM", "5/11/19 10:00 PM", "5/11/19 11:00 PM", "5/12/19 12:00 AM", "5/12/19 1:00 AM", "5/12/19 2:00 AM", "5/12/19 3:00 AM", "5/12/19 4:00 AM", "5/12/19 5:00 AM", "5/12/19 6:00 AM", "5/12/19 7:00 AM", "5/12/19 8:00 AM", "5/12/19 9:00 AM", "5/12/19 10:00 AM", "5/12/19 11:00 AM", "5/12/19 12:00 PM", "5/12/19 1:00 PM", "5/12/19 2:00 PM", "5/12/19 3:00 PM", "5/12/19 4:00 PM", "5/12/19 5:00 PM", "5/12/19 6:00 PM", "5/12/19 7:00 PM", "5/12/19 8:00 PM", "5/12/19 9:00 PM", "5/12/19 10:00 PM", "5/12/19 11:00 PM", "5/13/19 12:00 AM", "5/13/19 1:00 AM", "5/13/19 2:00 AM", "5/13/19 3:00 AM", "5/13/19 4:00 AM", "5/13/19 5:00 AM", "5/13/19 6:00 AM", "5/13/19 7:00 AM", "5/13/19 8:00 AM", "5/13/19 9:00 AM", "5/13/19 10:00 AM", "5/13/19 11:00 AM", "5/13/19 12:00 PM", "5/13/19 1:00 PM", "5/13/19 2:00 PM", "5/13/19 3:00 PM", "5/13/19 4:00 PM", "5/13/19 5:00 PM", "5/13/19 6:00 PM", "5/13/19 7:00 PM", "5/13/19 8:00 PM", "5/13/19 9:00 PM", "5/13/19 10:00 PM", "5/13/19 11:00 PM", "5/14/19 12:00 AM", "5/14/19 1:00 AM", "5/14/19 2:00 AM", "5/14/19 3:00 AM", "5/14/19 4:00 AM", "5/14/19 5:00 AM", "5/14/19 6:00 AM", "5/14/19 7:00 AM", "5/14/19 8:00 AM", "5/14/19 9:00 AM", "5/14/19 10:00 AM", "5/14/19 11:00 AM", "5/14/19 12:00 PM", "5/14/19 1:00 PM", "5/14/19 2:00 PM", "5/14/19 3:00 PM", "5/14/19 4:00 PM", "5/14/19 5:00 PM", "5/14/19 6:00 PM", "5/14/19 7:00 PM", "5/14/19 8:00 PM", "5/14/19 9:00 PM", "5/14/19 10:00 PM", "5/14/19 11:00 PM", "5/15/19 12:00 AM", "5/15/19 1:00 AM", "5/15/19 2:00 AM", "5/15/19 3:00 AM", "5/15/19 4:00 AM", "5/15/19 5:00 AM", "5/15/19 6:00 AM", "5/15/19 7:00 AM", "5/15/19 8:00 AM", "5/15/19 9:00 AM", "5/15/19 10:00 AM", "5/15/19 11:00 AM", "5/15/19 12:00 PM", "5/15/19 1:00 PM", "5/15/19 2:00 PM", "5/15/19 3:00 PM", "5/15/19 4:00 PM", "5/15/19 5:00 PM", "5/15/19 6:00 PM", "5/15/19 7:00 PM", "5/15/19 8:00 PM", "5/15/19 9:00 PM", "5/15/19 10:00 PM", "5/15/19 11:00 PM", "5/16/19 12:00 AM", "5/16/19 1:00 AM", "5/16/19 2:00 AM", "5/16/19 3:00 AM", "5/16/19 4:00 AM", "5/16/19 5:00 AM", "5/16/19 6:00 AM", "5/16/19 7:00 AM", "5/16/19 8:00 AM", "5/16/19 9:00 AM", "5/16/19 10:00 AM", "5/16/19 11:00 AM", "5/16/19 12:00 PM", "5/16/19 1:00 PM", "5/16/19 2:00 PM", "5/16/19 3:00 PM", "5/16/19 4:00 PM", "5/16/19 5:00 PM", "5/16/19 6:00 PM", "5/16/19 7:00 PM", "5/16/19 8:00 PM", "5/16/19 9:00 PM", "5/16/19 10:00 PM", "5/16/19 11:00 PM", "5/17/19 12:00 AM", "5/17/19 1:00 AM", "5/17/19 2:00 AM", "5/17/19 3:00 AM", "5/17/19 4:00 AM", "5/17/19 5:00 AM", "5/17/19 6:00 AM", "5/17/19 7:00 AM", "5/17/19 8:00 AM", "5/17/19 9:00 AM", "5/17/19 10:00 AM", "5/17/19 11:00 AM", "5/17/19 12:00 PM", "5/17/19 1:00 PM", "5/17/19 2:00 PM", "5/17/19 3:00 PM", "5/17/19 4:00 PM", "5/17/19 5:00 PM", "5/17/19 6:00 PM", "5/17/19 7:00 PM", "5/17/19 8:00 PM", "5/17/19 9:00 PM", "5/17/19 10:00 PM", "5/17/19 11:00 PM", "5/18/19 12:00 AM", "5/18/19 1:00 AM", "5/18/19 2:00 AM", "5/18/19 3:00 AM", "5/18/19 4:00 AM", "5/18/19 5:00 AM", "5/18/19 6:00 AM", "5/18/19 7:00 AM", "5/18/19 8:00 AM", "5/18/19 9:00 AM", "5/18/19 10:00 AM", "5/18/19 11:00 AM", "5/18/19 12:00 PM", "5/18/19 1:00 PM", "5/18/19 2:00 PM", "5/18/19 3:00 PM", "5/18/19 4:00 PM", "5/18/19 5:00 PM", "5/18/19 6:00 PM", "5/18/19 7:00 PM", "5/18/19 8:00 PM", "5/18/19 9:00 PM", "5/18/19 10:00 PM", "5/18/19 11:00 PM", "5/19/19 12:00 AM", "5/19/19 1:00 AM", "5/19/19 2:00 AM", "5/19/19 3:00 AM", "5/19/19 4:00 AM", "5/19/19 5:00 AM", "5/19/19 6:00 AM", "5/19/19 7:00 AM", "5/19/19 8:00 AM", "5/19/19 9:00 AM", "5/19/19 10:00 AM", "5/19/19 11:00 AM", "5/19/19 12:00 PM", "5/19/19 1:00 PM", "5/19/19 2:00 PM", "5/19/19 3:00 PM", "5/19/19 4:00 PM", "5/19/19 5:00 PM", "5/19/19 6:00 PM", "5/19/19 7:00 PM", "5/19/19 8:00 PM", "5/19/19 9:00 PM", "5/19/19 10:00 PM", "5/19/19 11:00 PM", "5/20/19 12:00 AM", "5/20/19 1:00 AM", "5/20/19 2:00 AM", "5/20/19 3:00 AM", "5/20/19 4:00 AM", "5/20/19 5:00 AM", "5/20/19 6:00 AM", "5/20/19 7:00 AM", "5/20/19 8:00 AM", "5/20/19 9:00 AM", "5/20/19 10:00 AM", "5/20/19 11:00 AM", "5/20/19 12:00 PM", "5/20/19 1:00 PM", "5/20/19 2:00 PM", "5/20/19 3:00 PM", "5/20/19 4:00 PM", "5/20/19 5:00 PM", "5/20/19 6:00 PM", "5/20/19 7:00 PM", "5/20/19 8:00 PM", "5/20/19 9:00 PM", "5/20/19 10:00 PM", "5/20/19 11:00 PM", "5/21/19 12:00 AM", "5/21/19 1:00 AM", "5/21/19 2:00 AM", "5/21/19 3:00 AM", "5/21/19 4:00 AM", "5/21/19 5:00 AM", "5/21/19 6:00 AM", "5/21/19 7:00 AM", "5/21/19 8:00 AM", "5/21/19 9:00 AM", "5/21/19 10:00 AM", "5/21/19 11:00 AM", "5/21/19 12:00 PM", "5/21/19 1:00 PM", "5/21/19 2:00 PM", "5/21/19 3:00 PM", "5/21/19 4:00 PM", "5/21/19 5:00 PM", "5/21/19 6:00 PM", "5/21/19 7:00 PM", "5/21/19 8:00 PM", "5/21/19 9:00 PM", "5/21/19 10:00 PM", "5/21/19 11:00 PM", "5/22/19 12:00 AM", "5/22/19 1:00 AM", "5/22/19 2:00 AM", "5/22/19 3:00 AM", "5/22/19 4:00 AM", "5/22/19 5:00 AM", "5/22/19 6:00 AM", "5/22/19 7:00 AM", "5/22/19 8:00 AM", "5/22/19 9:00 AM", "5/22/19 10:00 AM", "5/22/19 11:00 AM", "5/22/19 12:00 PM", "5/22/19 1:00 PM", "5/22/19 2:00 PM", "5/22/19 3:00 PM", "5/22/19 4:00 PM", "5/22/19 5:00 PM", "5/22/19 6:00 PM", "5/22/19 7:00 PM", "5/22/19 8:00 PM", "5/22/19 9:00 PM", "5/22/19 10:00 PM", "5/22/19 11:00 PM", "5/23/19 12:00 AM", "5/23/19 1:00 AM", "5/23/19 2:00 AM", "5/23/19 3:00 AM", "5/23/19 4:00 AM", "5/23/19 5:00 AM", "5/23/19 6:00 AM", "5/23/19 7:00 AM", "5/23/19 8:00 AM", "5/23/19 9:00 AM", "5/23/19 10:00 AM", "5/23/19 11:00 AM", "5/23/19 12:00 PM", "5/23/19 1:00 PM", "5/23/19 2:00 PM", "5/23/19 3:00 PM", "5/23/19 4:00 PM", "5/23/19 5:00 PM", "5/23/19 6:00 PM", "5/23/19 7:00 PM", "5/23/19 8:00 PM", "5/23/19 9:00 PM", "5/23/19 10:00 PM", "5/23/19 11:00 PM", "5/24/19 12:00 AM", "5/24/19 1:00 AM", "5/24/19 2:00 AM", "5/24/19 3:00 AM", "5/24/19 4:00 AM", "5/24/19 5:00 AM", "5/24/19 6:00 AM", "5/24/19 7:00 AM", "5/24/19 8:00 AM", "5/24/19 9:00 AM", "5/24/19 10:00 AM", "5/24/19 11:00 AM", "5/24/19 12:00 PM", "5/24/19 1:00 PM", "5/24/19 2:00 PM", "5/24/19 3:00 PM", "5/24/19 4:00 PM", "5/24/19 5:00 PM", "5/24/19 6:00 PM", "5/24/19 7:00 PM", "5/24/19 8:00 PM", "5/24/19 9:00 PM", "5/24/19 10:00 PM", "5/24/19 11:00 PM", "5/25/19 12:00 AM", "5/25/19 1:00 AM", "5/25/19 2:00 AM", "5/25/19 3:00 AM", "5/25/19 4:00 AM", "5/25/19 5:00 AM", "5/25/19 6:00 AM", "5/25/19 7:00 AM", "5/25/19 8:00 AM", "5/25/19 9:00 AM", "5/25/19 10:00 AM", "5/25/19 11:00 AM", "5/25/19 12:00 PM", "5/25/19 1:00 PM", "5/25/19 2:00 PM", "5/25/19 3:00 PM", "5/25/19 4:00 PM", "5/25/19 5:00 PM", "5/25/19 6:00 PM", "5/25/19 7:00 PM", "5/25/19 8:00 PM", "5/25/19 9:00 PM", "5/25/19 10:00 PM", "5/25/19 11:00 PM", "5/26/19 12:00 AM", "5/26/19 1:00 AM", "5/26/19 2:00 AM", "5/26/19 3:00 AM", "5/26/19 4:00 AM", "5/26/19 5:00 AM", "5/26/19 6:00 AM", "5/26/19 7:00 AM", "5/26/19 8:00 AM", "5/26/19 9:00 AM", "5/26/19 10:00 AM", "5/26/19 11:00 AM", "5/26/19 12:00 PM", "5/26/19 1:00 PM", "5/26/19 2:00 PM", "5/26/19 3:00 PM", "5/26/19 4:00 PM", "5/26/19 5:00 PM", "5/26/19 6:00 PM", "5/26/19 7:00 PM", "5/26/19 8:00 PM", "5/26/19 9:00 PM", "5/26/19 10:00 PM", "5/26/19 11:00 PM", "5/27/19 12:00 AM", "5/27/19 1:00 AM", "5/27/19 2:00 AM", "5/27/19 3:00 AM", "5/27/19 4:00 AM", "5/27/19 5:00 AM", "5/27/19 6:00 AM", "5/27/19 7:00 AM", "5/27/19 8:00 AM", "5/27/19 9:00 AM", "5/27/19 10:00 AM", "5/27/19 11:00 AM", "5/27/19 12:00 PM", "5/27/19 1:00 PM", "5/27/19 2:00 PM", "5/27/19 3:00 PM", "5/27/19 4:00 PM", "5/27/19 5:00 PM", "5/27/19 6:00 PM", "5/27/19 7:00 PM", "5/27/19 8:00 PM", "5/27/19 9:00 PM", "5/27/19 10:00 PM", "5/27/19 11:00 PM", "5/28/19 12:00 AM", "5/28/19 1:00 AM", "5/28/19 2:00 AM", "5/28/19 3:00 AM", "5/28/19 4:00 AM", "5/28/19 5:00 AM", "5/28/19 6:00 AM", "5/28/19 7:00 AM", "5/28/19 8:00 AM", "5/28/19 9:00 AM", "5/28/19 10:00 AM", "5/28/19 11:00 AM", "5/28/19 12:00 PM", "5/28/19 1:00 PM", "5/28/19 2:00 PM", "5/28/19 3:00 PM", "5/28/19 4:00 PM", "5/28/19 5:00 PM", "5/28/19 6:00 PM", "5/28/19 7:00 PM", "5/28/19 8:00 PM", "5/28/19 9:00 PM", "5/28/19 10:00 PM", "5/28/19 11:00 PM", "5/29/19 12:00 AM", "5/29/19 1:00 AM", "5/29/19 2:00 AM", "5/29/19 3:00 AM", "5/29/19 4:00 AM", "5/29/19 5:00 AM", "5/29/19 6:00 AM", "5/29/19 7:00 AM", "5/29/19 8:00 AM", "5/29/19 9:00 AM", "5/29/19 10:00 AM", "5/29/19 11:00 AM", "5/29/19 12:00 PM", "5/29/19 1:00 PM", "5/29/19 2:00 PM", "5/29/19 3:00 PM", "5/29/19 4:00 PM", "5/29/19 5:00 PM", "5/29/19 6:00 PM", "5/29/19 7:00 PM", "5/29/19 8:00 PM", "5/29/19 9:00 PM", "5/29/19 10:00 PM", "5/29/19 11:00 PM", "5/30/19 12:00 AM", "5/30/19 1:00 AM", "5/30/19 2:00 AM", "5/30/19 3:00 AM", "5/30/19 4:00 AM", "5/30/19 5:00 AM", "5/30/19 6:00 AM", "5/30/19 7:00 AM", "5/30/19 8:00 AM", "5/30/19 9:00 AM", "5/30/19 10:00 AM", "5/30/19 11:00 AM", "5/30/19 12:00 PM", "5/30/19 1:00 PM", "5/30/19 2:00 PM", "5/30/19 3:00 PM", "5/30/19 4:00 PM", "5/30/19 5:00 PM", "5/30/19 6:00 PM", "5/30/19 7:00 PM", "5/30/19 8:00 PM", "5/30/19 9:00 PM", "5/30/19 10:00 PM", "5/30/19 11:00 PM", "5/31/19 12:00 AM", "5/31/19 1:00 AM", "5/31/19 2:00 AM", "5/31/19 3:00 AM", "5/31/19 4:00 AM", "5/31/19 5:00 AM", "5/31/19 6:00 AM", "5/31/19 7:00 AM", "5/31/19 8:00 AM", "5/31/19 9:00 AM", "5/31/19 10:00 AM", "5/31/19 11:00 AM", "5/31/19 12:00 PM", "5/31/19 1:00 PM", "5/31/19 2:00 PM", "5/31/19 3:00 PM", "5/31/19 4:00 PM", "5/31/19 5:00 PM", "5/31/19 6:00 PM", "5/31/19 7:00 PM", "5/31/19 8:00 PM", "5/31/19 9:00 PM", "5/31/19 10:00 PM", "5/31/19 11:00 PM", "6/1/19 12:00 AM", "6/1/19 1:00 AM", "6/1/19 2:00 AM", "6/1/19 3:00 AM", "6/1/19 4:00 AM", "6/1/19 5:00 AM", "6/1/19 6:00 AM", "6/1/19 7:00 AM", "6/1/19 8:00 AM", "6/1/19 9:00 AM", "6/1/19 10:00 AM", "6/1/19 11:00 AM", "6/1/19 12:00 PM", "6/1/19 1:00 PM", "6/1/19 2:00 PM", "6/1/19 3:00 PM", "6/1/19 4:00 PM", "6/1/19 5:00 PM", "6/1/19 6:00 PM", "6/1/19 7:00 PM", "6/1/19 8:00 PM", "6/1/19 9:00 PM", "6/1/19 10:00 PM", "6/1/19 11:00 PM", "6/2/19 12:00 AM", "6/2/19 1:00 AM", "6/2/19 2:00 AM", "6/2/19 3:00 AM", "6/2/19 4:00 AM", "6/2/19 5:00 AM", "6/2/19 6:00 AM", "6/2/19 7:00 AM", "6/2/19 8:00 AM", "6/2/19 9:00 AM", "6/2/19 10:00 AM", "6/2/19 11:00 AM", "6/2/19 12:00 PM", "6/2/19 1:00 PM", "6/2/19 2:00 PM", "6/2/19 3:00 PM", "6/2/19 4:00 PM", "6/2/19 5:00 PM", "6/2/19 6:00 PM", "6/2/19 7:00 PM", "6/2/19 8:00 PM", "6/2/19 9:00 PM", "6/2/19 10:00 PM", "6/2/19 11:00 PM", "6/3/19 12:00 AM", "6/3/19 1:00 AM", "6/3/19 2:00 AM", "6/3/19 3:00 AM", "6/3/19 4:00 AM", "6/3/19 5:00 AM", "6/3/19 6:00 AM", "6/3/19 7:00 AM", "6/3/19 8:00 AM", "6/3/19 9:00 AM", "6/3/19 10:00 AM", "6/3/19 11:00 AM", "6/3/19 12:00 PM", "6/3/19 1:00 PM", "6/3/19 2:00 PM", "6/3/19 3:00 PM", "6/3/19 4:00 PM", "6/3/19 5:00 PM", "6/3/19 6:00 PM", "6/3/19 7:00 PM", "6/3/19 8:00 PM", "6/3/19 9:00 PM", "6/3/19 10:00 PM", "6/3/19 11:00 PM", "6/4/19 12:00 AM", "6/4/19 1:00 AM", "6/4/19 2:00 AM", "6/4/19 3:00 AM", "6/4/19 4:00 AM", "6/4/19 5:00 AM", "6/4/19 6:00 AM", "6/4/19 7:00 AM", "6/4/19 8:00 AM", "6/4/19 9:00 AM", "6/4/19 10:00 AM", "6/4/19 11:00 AM", "6/4/19 12:00 PM", "6/4/19 1:00 PM", "6/4/19 2:00 PM", "6/4/19 3:00 PM", "6/4/19 4:00 PM", "6/4/19 5:00 PM", "6/4/19 6:00 PM", "6/4/19 7:00 PM", "6/4/19 8:00 PM", "6/4/19 9:00 PM", "6/4/19 10:00 PM", "6/4/19 11:00 PM", "6/5/19 12:00 AM", "6/5/19 1:00 AM", "6/5/19 2:00 AM", "6/5/19 3:00 AM", "6/5/19 4:00 AM", "6/5/19 5:00 AM", "6/5/19 6:00 AM", "6/5/19 7:00 AM", "6/5/19 8:00 AM", "6/5/19 9:00 AM", "6/5/19 10:00 AM", "6/5/19 11:00 AM", "6/5/19 12:00 PM", "6/5/19 1:00 PM", "6/5/19 2:00 PM", "6/5/19 3:00 PM", "6/5/19 4:00 PM", "6/5/19 5:00 PM", "6/5/19 6:00 PM", "6/5/19 7:00 PM", "6/5/19 8:00 PM", "6/5/19 9:00 PM", "6/5/19 10:00 PM", "6/5/19 11:00 PM", "6/6/19 12:00 AM", "6/6/19 1:00 AM", "6/6/19 2:00 AM", "6/6/19 3:00 AM", "6/6/19 4:00 AM", "6/6/19 5:00 AM", "6/6/19 6:00 AM", "6/6/19 7:00 AM", "6/6/19 8:00 AM", "6/6/19 9:00 AM", "6/6/19 10:00 AM", "6/6/19 11:00 AM", "6/6/19 12:00 PM", "6/6/19 1:00 PM", "6/6/19 2:00 PM", "6/6/19 3:00 PM", "6/6/19 4:00 PM", "6/6/19 5:00 PM", "6/6/19 6:00 PM", "6/6/19 7:00 PM", "6/6/19 8:00 PM", "6/6/19 9:00 PM", "6/6/19 10:00 PM", "6/6/19 11:00 PM", "6/7/19 12:00 AM", "6/7/19 1:00 AM", "6/7/19 2:00 AM", "6/7/19 3:00 AM", "6/7/19 4:00 AM", "6/7/19 5:00 AM", "6/7/19 6:00 AM", "6/7/19 7:00 AM", "6/7/19 8:00 AM", "6/7/19 9:00 AM", "6/7/19 10:00 AM", "6/7/19 11:00 AM", "6/7/19 12:00 PM", "6/7/19 1:00 PM", "6/7/19 2:00 PM", "6/7/19 3:00 PM", "6/7/19 4:00 PM", "6/7/19 5:00 PM", "6/7/19 6:00 PM", "6/7/19 7:00 PM", "6/7/19 8:00 PM", "6/7/19 9:00 PM", "6/7/19 10:00 PM", "6/7/19 11:00 PM", "6/8/19 12:00 AM", "6/8/19 1:00 AM", "6/8/19 2:00 AM", "6/8/19 3:00 AM", "6/8/19 4:00 AM", "6/8/19 5:00 AM", "6/8/19 6:00 AM", "6/8/19 7:00 AM", "6/8/19 8:00 AM", "6/8/19 9:00 AM", "6/8/19 10:00 AM", "6/8/19 11:00 AM", "6/8/19 12:00 PM", "6/8/19 1:00 PM", "6/8/19 2:00 PM", "6/8/19 3:00 PM", "6/8/19 4:00 PM", "6/8/19 5:00 PM", "6/8/19 6:00 PM", "6/8/19 7:00 PM", "6/8/19 8:00 PM", "6/8/19 9:00 PM", "6/8/19 10:00 PM", "6/8/19 11:00 PM", "6/9/19 12:00 AM", "6/9/19 1:00 AM", "6/9/19 2:00 AM", "6/9/19 3:00 AM", "6/9/19 4:00 AM", "6/9/19 5:00 AM", "6/9/19 6:00 AM", "6/9/19 7:00 AM", "6/9/19 8:00 AM", "6/9/19 9:00 AM", "6/9/19 10:00 AM", "6/9/19 11:00 AM", "6/9/19 12:00 PM", "6/9/19 1:00 PM", "6/9/19 2:00 PM", "6/9/19 3:00 PM", "6/9/19 4:00 PM", "6/9/19 5:00 PM", "6/9/19 6:00 PM", "6/9/19 7:00 PM", "6/9/19 8:00 PM", "6/9/19 9:00 PM", "6/9/19 10:00 PM", "6/9/19 11:00 PM", "6/10/19 12:00 AM", "6/10/19 1:00 AM", "6/10/19 2:00 AM", "6/10/19 3:00 AM", "6/10/19 4:00 AM", "6/10/19 5:00 AM", "6/10/19 6:00 AM", "6/10/19 7:00 AM", "6/10/19 8:00 AM", "6/10/19 9:00 AM", "6/10/19 10:00 AM", "6/10/19 11:00 AM", "6/10/19 12:00 PM", "6/10/19 1:00 PM", "6/10/19 2:00 PM", "6/10/19 3:00 PM", "6/10/19 4:00 PM", "6/10/19 5:00 PM", "6/10/19 6:00 PM", "6/10/19 7:00 PM", "6/10/19 8:00 PM", "6/10/19 9:00 PM", "6/10/19 10:00 PM", "6/10/19 11:00 PM", "6/11/19 12:00 AM", "6/11/19 1:00 AM", "6/11/19 2:00 AM", "6/11/19 3:00 AM", "6/11/19 4:00 AM", "6/11/19 5:00 AM", "6/11/19 6:00 AM", "6/11/19 7:00 AM", "6/11/19 8:00 AM", "6/11/19 9:00 AM", "6/11/19 10:00 AM", "6/11/19 11:00 AM", "6/11/19 12:00 PM", "6/11/19 1:00 PM", "6/11/19 2:00 PM", "6/11/19 3:00 PM", "6/11/19 4:00 PM", "6/11/19 5:00 PM", "6/11/19 6:00 PM", "6/11/19 7:00 PM", "6/11/19 8:00 PM", "6/11/19 9:00 PM", "6/11/19 10:00 PM", "6/11/19 11:00 PM", "6/12/19 12:00 AM", "6/12/19 1:00 AM", "6/12/19 2:00 AM", "6/12/19 3:00 AM", "6/12/19 4:00 AM", "6/12/19 5:00 AM", "6/12/19 6:00 AM", "6/12/19 7:00 AM", "6/12/19 8:00 AM", "6/12/19 9:00 AM", "6/12/19 10:00 AM", "6/12/19 11:00 AM", "6/12/19 12:00 PM", "6/12/19 1:00 PM", "6/12/19 2:00 PM", "6/12/19 3:00 PM", "6/12/19 4:00 PM", "6/12/19 5:00 PM", "6/12/19 6:00 PM", "6/12/19 7:00 PM", "6/12/19 8:00 PM", "6/12/19 9:00 PM", "6/12/19 10:00 PM", "6/12/19 11:00 PM", "6/13/19 12:00 AM", "6/13/19 1:00 AM", "6/13/19 2:00 AM", "6/13/19 3:00 AM", "6/13/19 4:00 AM", "6/13/19 5:00 AM", "6/13/19 6:00 AM", "6/13/19 7:00 AM", "6/13/19 8:00 AM", "6/13/19 9:00 AM", "6/13/19 10:00 AM", "6/13/19 11:00 AM", "6/13/19 12:00 PM", "6/13/19 1:00 PM", "6/13/19 2:00 PM", "6/13/19 3:00 PM", "6/13/19 4:00 PM", "6/13/19 5:00 PM", "6/13/19 6:00 PM", "6/13/19 7:00 PM", "6/13/19 8:00 PM", "6/13/19 9:00 PM", "6/13/19 10:00 PM", "6/13/19 11:00 PM", "6/14/19 12:00 AM", "6/14/19 1:00 AM", "6/14/19 2:00 AM", "6/14/19 3:00 AM", "6/14/19 4:00 AM", "6/14/19 5:00 AM", "6/14/19 6:00 AM", "6/14/19 7:00 AM", "6/14/19 8:00 AM", "6/14/19 9:00 AM", "6/14/19 10:00 AM", "6/14/19 11:00 AM", "6/14/19 12:00 PM", "6/14/19 1:00 PM", "6/14/19 2:00 PM", "6/14/19 3:00 PM", "6/14/19 4:00 PM", "6/14/19 5:00 PM", "6/14/19 6:00 PM", "6/14/19 7:00 PM", "6/14/19 8:00 PM", "6/14/19 9:00 PM", "6/14/19 10:00 PM", "6/14/19 11:00 PM", "6/15/19 12:00 AM", "6/15/19 1:00 AM", "6/15/19 2:00 AM", "6/15/19 3:00 AM", "6/15/19 4:00 AM", "6/15/19 5:00 AM", "6/15/19 6:00 AM", "6/15/19 7:00 AM", "6/15/19 8:00 AM", "6/15/19 9:00 AM", "6/15/19 10:00 AM", "6/15/19 11:00 AM", "6/15/19 12:00 PM", "6/15/19 1:00 PM", "6/15/19 2:00 PM", "6/15/19 3:00 PM", "6/15/19 4:00 PM", "6/15/19 5:00 PM", "6/15/19 6:00 PM", "6/15/19 7:00 PM", "6/15/19 8:00 PM", "6/15/19 9:00 PM", "6/15/19 10:00 PM", "6/15/19 11:00 PM", "6/16/19 12:00 AM", "6/16/19 1:00 AM", "6/16/19 2:00 AM", "6/16/19 3:00 AM", "6/16/19 4:00 AM", "6/16/19 5:00 AM", "6/16/19 6:00 AM", "6/16/19 7:00 AM", "6/16/19 8:00 AM", "6/16/19 9:00 AM", "6/16/19 10:00 AM", "6/16/19 11:00 AM", "6/16/19 12:00 PM", "6/16/19 1:00 PM", "6/16/19 2:00 PM", "6/16/19 3:00 PM", "6/16/19 4:00 PM", "6/16/19 5:00 PM", "6/16/19 6:00 PM", "6/16/19 7:00 PM", "6/16/19 8:00 PM", "6/16/19 9:00 PM", "6/16/19 10:00 PM", "6/16/19 11:00 PM", "6/17/19 12:00 AM", "6/17/19 1:00 AM", "6/17/19 2:00 AM", "6/17/19 3:00 AM", "6/17/19 4:00 AM", "6/17/19 5:00 AM", "6/17/19 6:00 AM", "6/17/19 7:00 AM", "6/17/19 8:00 AM", "6/17/19 9:00 AM", "6/17/19 10:00 AM", "6/17/19 11:00 AM", "6/17/19 12:00 PM", "6/17/19 1:00 PM", "6/17/19 2:00 PM", "6/17/19 3:00 PM", "6/17/19 4:00 PM", "6/17/19 5:00 PM", "6/17/19 6:00 PM", "6/17/19 7:00 PM", "6/17/19 8:00 PM", "6/17/19 9:00 PM", "6/17/19 10:00 PM", "6/17/19 11:00 PM", "6/18/19 12:00 AM", "6/18/19 1:00 AM", "6/18/19 2:00 AM", "6/18/19 3:00 AM", "6/18/19 4:00 AM", "6/18/19 5:00 AM", "6/18/19 6:00 AM", "6/18/19 7:00 AM", "6/18/19 8:00 AM", "6/18/19 9:00 AM", "6/18/19 10:00 AM", "6/18/19 11:00 AM", "6/18/19 12:00 PM", "6/18/19 1:00 PM", "6/18/19 2:00 PM", "6/18/19 3:00 PM", "6/18/19 4:00 PM", "6/18/19 5:00 PM", "6/18/19 6:00 PM", "6/18/19 7:00 PM", "6/18/19 8:00 PM", "6/18/19 9:00 PM", "6/18/19 10:00 PM", "6/18/19 11:00 PM", "6/19/19 12:00 AM", "6/19/19 1:00 AM", "6/19/19 2:00 AM", "6/19/19 3:00 AM", "6/19/19 4:00 AM", "6/19/19 5:00 AM", "6/19/19 6:00 AM", "6/19/19 7:00 AM", "6/19/19 8:00 AM", "6/19/19 9:00 AM", "6/19/19 10:00 AM", "6/19/19 11:00 AM", "6/19/19 12:00 PM", "6/19/19 1:00 PM", "6/19/19 2:00 PM", "6/19/19 3:00 PM", "6/19/19 4:00 PM", "6/19/19 5:00 PM", "6/19/19 6:00 PM", "6/19/19 7:00 PM", "6/19/19 8:00 PM", "6/19/19 9:00 PM", "6/19/19 10:00 PM", "6/19/19 11:00 PM", "6/20/19 12:00 AM", "6/20/19 1:00 AM", "6/20/19 2:00 AM", "6/20/19 3:00 AM", "6/20/19 4:00 AM", "6/20/19 5:00 AM", "6/20/19 6:00 AM", "6/20/19 7:00 AM", "6/20/19 8:00 AM", "6/20/19 9:00 AM", "6/20/19 10:00 AM", "6/20/19 11:00 AM", "6/20/19 12:00 PM", "6/20/19 1:00 PM", "6/20/19 2:00 PM", "6/20/19 3:00 PM", "6/20/19 4:00 PM", "6/20/19 5:00 PM", "6/20/19 6:00 PM", "6/20/19 7:00 PM", "6/20/19 8:00 PM", "6/20/19 9:00 PM", "6/20/19 10:00 PM", "6/20/19 11:00 PM", "6/21/19 12:00 AM", "6/21/19 1:00 AM", "6/21/19 2:00 AM", "6/21/19 3:00 AM", "6/21/19 4:00 AM", "6/21/19 5:00 AM", "6/21/19 6:00 AM", "6/21/19 7:00 AM", "6/21/19 8:00 AM", "6/21/19 9:00 AM", "6/21/19 10:00 AM", "6/21/19 11:00 AM", "6/21/19 12:00 PM", "6/21/19 1:00 PM", "6/21/19 2:00 PM", "6/21/19 3:00 PM", "6/21/19 4:00 PM", "6/21/19 5:00 PM", "6/21/19 6:00 PM", "6/21/19 7:00 PM", "6/21/19 8:00 PM", "6/21/19 9:00 PM", "6/21/19 10:00 PM", "6/21/19 11:00 PM", "6/22/19 12:00 AM", "6/22/19 1:00 AM", "6/22/19 2:00 AM", "6/22/19 3:00 AM", "6/22/19 4:00 AM", "6/22/19 5:00 AM", "6/22/19 6:00 AM", "6/22/19 7:00 AM", "6/22/19 8:00 AM", "6/22/19 9:00 AM", "6/22/19 10:00 AM", "6/22/19 11:00 AM", "6/22/19 12:00 PM", "6/22/19 1:00 PM", "6/22/19 2:00 PM", "6/22/19 3:00 PM", "6/22/19 4:00 PM", "6/22/19 5:00 PM", "6/22/19 6:00 PM", "6/22/19 7:00 PM", "6/22/19 8:00 PM", "6/22/19 9:00 PM", "6/22/19 10:00 PM", "6/22/19 11:00 PM", "6/23/19 12:00 AM", "6/23/19 1:00 AM", "6/23/19 2:00 AM", "6/23/19 3:00 AM", "6/23/19 4:00 AM", "6/23/19 5:00 AM", "6/23/19 6:00 AM", "6/23/19 7:00 AM", "6/23/19 8:00 AM", "6/23/19 9:00 AM", "6/23/19 10:00 AM", "6/23/19 11:00 AM", "6/23/19 12:00 PM", "6/23/19 1:00 PM", "6/23/19 2:00 PM", "6/23/19 3:00 PM", "6/23/19 4:00 PM", "6/23/19 5:00 PM", "6/23/19 6:00 PM", "6/23/19 7:00 PM", "6/23/19 8:00 PM", "6/23/19 9:00 PM", "6/23/19 10:00 PM", "6/23/19 11:00 PM", "6/24/19 12:00 AM", "6/24/19 1:00 AM", "6/24/19 2:00 AM", "6/24/19 3:00 AM", "6/24/19 4:00 AM", "6/24/19 5:00 AM", "6/24/19 6:00 AM", "6/24/19 7:00 AM", "6/24/19 8:00 AM", "6/24/19 9:00 AM", "6/24/19 10:00 AM", "6/24/19 11:00 AM", "6/24/19 12:00 PM", "6/24/19 1:00 PM", "6/24/19 2:00 PM", "6/24/19 3:00 PM", "6/24/19 4:00 PM", "6/24/19 5:00 PM", "6/24/19 6:00 PM", "6/24/19 7:00 PM", "6/24/19 8:00 PM", "6/24/19 9:00 PM", "6/24/19 10:00 PM", "6/24/19 11:00 PM", "6/25/19 12:00 AM", "6/25/19 1:00 AM", "6/25/19 2:00 AM", "6/25/19 3:00 AM", "6/25/19 4:00 AM", "6/25/19 5:00 AM", "6/25/19 6:00 AM", "6/25/19 7:00 AM", "6/25/19 8:00 AM", "6/25/19 9:00 AM", "6/25/19 10:00 AM", "6/25/19 11:00 AM", "6/25/19 12:00 PM", "6/25/19 1:00 PM", "6/25/19 2:00 PM", "6/25/19 3:00 PM", "6/25/19 4:00 PM", "6/25/19 5:00 PM", "6/25/19 6:00 PM", "6/25/19 7:00 PM", "6/25/19 8:00 PM", "6/25/19 9:00 PM", "6/25/19 10:00 PM", "6/25/19 11:00 PM", "6/26/19 12:00 AM", "6/26/19 1:00 AM", "6/26/19 2:00 AM", "6/26/19 3:00 AM", "6/26/19 4:00 AM", "6/26/19 5:00 AM", "6/26/19 6:00 AM", "6/26/19 7:00 AM", "6/26/19 8:00 AM", "6/26/19 9:00 AM", "6/26/19 10:00 AM", "6/26/19 11:00 AM", "6/26/19 12:00 PM", "6/26/19 1:00 PM", "6/26/19 2:00 PM", "6/26/19 3:00 PM", "6/26/19 4:00 PM", "6/26/19 5:00 PM", "6/26/19 6:00 PM", "6/26/19 7:00 PM", "6/26/19 8:00 PM", "6/26/19 9:00 PM", "6/26/19 10:00 PM", "6/26/19 11:00 PM", "6/27/19 12:00 AM", "6/27/19 1:00 AM", "6/27/19 2:00 AM", "6/27/19 3:00 AM", "6/27/19 4:00 AM", "6/27/19 5:00 AM", "6/27/19 6:00 AM", "6/27/19 7:00 AM", "6/27/19 8:00 AM", "6/27/19 9:00 AM", "6/27/19 10:00 AM", "6/27/19 11:00 AM", "6/27/19 12:00 PM", "6/27/19 1:00 PM", "6/27/19 2:00 PM", "6/27/19 3:00 PM", "6/27/19 4:00 PM", "6/27/19 5:00 PM", "6/27/19 6:00 PM", "6/27/19 7:00 PM", "6/27/19 8:00 PM", "6/27/19 9:00 PM", "6/27/19 10:00 PM", "6/27/19 11:00 PM", "6/28/19 12:00 AM", "6/28/19 1:00 AM", "6/28/19 2:00 AM", "6/28/19 3:00 AM", "6/28/19 4:00 AM", "6/28/19 5:00 AM", "6/28/19 6:00 AM", "6/28/19 7:00 AM", "6/28/19 8:00 AM", "6/28/19 9:00 AM", "6/28/19 10:00 AM", "6/28/19 11:00 AM", "6/28/19 12:00 PM", "6/28/19 1:00 PM", "6/28/19 2:00 PM", "6/28/19 3:00 PM", "6/28/19 4:00 PM", "6/28/19 5:00 PM", "6/28/19 6:00 PM", "6/28/19 7:00 PM", "6/28/19 8:00 PM", "6/28/19 9:00 PM", "6/28/19 10:00 PM", "6/28/19 11:00 PM", "6/29/19 12:00 AM", "6/29/19 1:00 AM", "6/29/19 2:00 AM", "6/29/19 3:00 AM", "6/29/19 4:00 AM", "6/29/19 5:00 AM", "6/29/19 6:00 AM", "6/29/19 7:00 AM", "6/29/19 8:00 AM", "6/29/19 9:00 AM", "6/29/19 10:00 AM", "6/29/19 11:00 AM", "6/29/19 12:00 PM", "6/29/19 1:00 PM", "6/29/19 2:00 PM", "6/29/19 3:00 PM", "6/29/19 4:00 PM", "6/29/19 5:00 PM", "6/29/19 6:00 PM", "6/29/19 7:00 PM", "6/29/19 8:00 PM", "6/29/19 9:00 PM", "6/29/19 10:00 PM", "6/29/19 11:00 PM", "6/30/19 12:00 AM", "6/30/19 1:00 AM", "6/30/19 2:00 AM", "6/30/19 3:00 AM", "6/30/19 4:00 AM", "6/30/19 5:00 AM", "6/30/19 6:00 AM", "6/30/19 7:00 AM", "6/30/19 8:00 AM", "6/30/19 9:00 AM", "6/30/19 10:00 AM", "6/30/19 11:00 AM", "6/30/19 12:00 PM", "6/30/19 1:00 PM", "6/30/19 2:00 PM", "6/30/19 3:00 PM", "6/30/19 4:00 PM", "6/30/19 5:00 PM", "6/30/19 6:00 PM", "6/30/19 7:00 PM", "6/30/19 8:00 PM", "6/30/19 9:00 PM", "6/30/19 10:00 PM", "6/30/19 11:00 PM", "7/1/19 12:00 AM", "7/1/19 1:00 AM", "7/1/19 2:00 AM", "7/1/19 3:00 AM", "7/1/19 4:00 AM", "7/1/19 5:00 AM", "7/1/19 6:00 AM", "7/1/19 7:00 AM", "7/1/19 8:00 AM", "7/1/19 9:00 AM", "7/1/19 10:00 AM", "7/1/19 11:00 AM", "7/1/19 12:00 PM", "7/1/19 1:00 PM", "7/1/19 2:00 PM", "7/1/19 3:00 PM", "7/1/19 4:00 PM", "7/1/19 5:00 PM", "7/1/19 6:00 PM", "7/1/19 7:00 PM", "7/1/19 8:00 PM", "7/1/19 9:00 PM", "7/1/19 10:00 PM", "7/1/19 11:00 PM", "7/2/19 12:00 AM", "7/2/19 1:00 AM", "7/2/19 2:00 AM", "7/2/19 3:00 AM", "7/2/19 4:00 AM", "7/2/19 5:00 AM", "7/2/19 6:00 AM", "7/2/19 7:00 AM", "7/2/19 8:00 AM", "7/2/19 9:00 AM", "7/2/19 10:00 AM", "7/2/19 11:00 AM", "7/2/19 12:00 PM", "7/2/19 1:00 PM", "7/2/19 2:00 PM", "7/2/19 3:00 PM", "7/2/19 4:00 PM", "7/2/19 5:00 PM", "7/2/19 6:00 PM", "7/2/19 7:00 PM", "7/2/19 8:00 PM", "7/2/19 9:00 PM", "7/2/19 10:00 PM", "7/2/19 11:00 PM", "7/3/19 12:00 AM", "7/3/19 1:00 AM", "7/3/19 2:00 AM", "7/3/19 3:00 AM", "7/3/19 4:00 AM", "7/3/19 5:00 AM", "7/3/19 6:00 AM", "7/3/19 7:00 AM", "7/3/19 8:00 AM", "7/3/19 9:00 AM", "7/3/19 10:00 AM", "7/3/19 11:00 AM", "7/3/19 12:00 PM", "7/3/19 1:00 PM", "7/3/19 2:00 PM", "7/3/19 3:00 PM", "7/3/19 4:00 PM", "7/3/19 5:00 PM", "7/3/19 6:00 PM", "7/3/19 7:00 PM", "7/3/19 8:00 PM", "7/3/19 9:00 PM", "7/3/19 10:00 PM", "7/3/19 11:00 PM", "7/4/19 12:00 AM", "7/4/19 1:00 AM", "7/4/19 2:00 AM", "7/4/19 3:00 AM", "7/4/19 4:00 AM", "7/4/19 5:00 AM", "7/4/19 6:00 AM", "7/4/19 7:00 AM", "7/4/19 8:00 AM", "7/4/19 9:00 AM", "7/4/19 10:00 AM", "7/4/19 11:00 AM", "7/4/19 12:00 PM", "7/4/19 1:00 PM", "7/4/19 2:00 PM", "7/4/19 3:00 PM", "7/4/19 4:00 PM", "7/4/19 5:00 PM", "7/4/19 6:00 PM", "7/4/19 7:00 PM", "7/4/19 8:00 PM", "7/4/19 9:00 PM", "7/4/19 10:00 PM", "7/4/19 11:00 PM", "7/5/19 12:00 AM", "7/5/19 1:00 AM", "7/5/19 2:00 AM", "7/5/19 3:00 AM", "7/5/19 4:00 AM", "7/5/19 5:00 AM", "7/5/19 6:00 AM", "7/5/19 7:00 AM", "7/5/19 8:00 AM", "7/5/19 9:00 AM", "7/5/19 10:00 AM", "7/5/19 11:00 AM", "7/5/19 12:00 PM", "7/5/19 1:00 PM", "7/5/19 2:00 PM", "7/5/19 3:00 PM", "7/5/19 4:00 PM", "7/5/19 5:00 PM", "7/5/19 6:00 PM", "7/5/19 7:00 PM", "7/5/19 8:00 PM", "7/5/19 9:00 PM", "7/5/19 10:00 PM", "7/5/19 11:00 PM", "7/6/19 12:00 AM", "7/6/19 1:00 AM", "7/6/19 2:00 AM", "7/6/19 3:00 AM", "7/6/19 4:00 AM", "7/6/19 5:00 AM", "7/6/19 6:00 AM", "7/6/19 7:00 AM", "7/6/19 8:00 AM", "7/6/19 9:00 AM", "7/6/19 10:00 AM", "7/6/19 11:00 AM", "7/6/19 12:00 PM", "7/6/19 1:00 PM", "7/6/19 2:00 PM", "7/6/19 3:00 PM", "7/6/19 4:00 PM", "7/6/19 5:00 PM", "7/6/19 6:00 PM", "7/6/19 7:00 PM", "7/6/19 8:00 PM", "7/6/19 9:00 PM", "7/6/19 10:00 PM", "7/6/19 11:00 PM", "7/7/19 12:00 AM", "7/7/19 1:00 AM", "7/7/19 2:00 AM", "7/7/19 3:00 AM", "7/7/19 4:00 AM", "7/7/19 5:00 AM", "7/7/19 6:00 AM", "7/7/19 7:00 AM", "7/7/19 8:00 AM", "7/7/19 9:00 AM", "7/7/19 10:00 AM", "7/7/19 11:00 AM", "7/7/19 12:00 PM", "7/7/19 1:00 PM", "7/7/19 2:00 PM", "7/7/19 3:00 PM", "7/7/19 4:00 PM", "7/7/19 5:00 PM", "7/7/19 6:00 PM", "7/7/19 7:00 PM", "7/7/19 8:00 PM", "7/7/19 9:00 PM", "7/7/19 10:00 PM", "7/7/19 11:00 PM", "7/8/19 12:00 AM", "7/8/19 1:00 AM", "7/8/19 2:00 AM", "7/8/19 3:00 AM", "7/8/19 4:00 AM", "7/8/19 5:00 AM", "7/8/19 6:00 AM", "7/8/19 7:00 AM", "7/8/19 8:00 AM", "7/8/19 9:00 AM", "7/8/19 10:00 AM", "7/8/19 11:00 AM", "7/8/19 12:00 PM", "7/8/19 1:00 PM", "7/8/19 2:00 PM", "7/8/19 3:00 PM", "7/8/19 4:00 PM", "7/8/19 5:00 PM", "7/8/19 6:00 PM", "7/8/19 7:00 PM", "7/8/19 8:00 PM", "7/8/19 9:00 PM", "7/8/19 10:00 PM", "7/8/19 11:00 PM", "7/9/19 12:00 AM", "7/9/19 1:00 AM", "7/9/19 2:00 AM", "7/9/19 3:00 AM", "7/9/19 4:00 AM", "7/9/19 5:00 AM", "7/9/19 6:00 AM", "7/9/19 7:00 AM", "7/9/19 8:00 AM", "7/9/19 9:00 AM", "7/9/19 10:00 AM", "7/9/19 11:00 AM", "7/9/19 12:00 PM", "7/9/19 1:00 PM", "7/9/19 2:00 PM", "7/9/19 3:00 PM", "7/9/19 4:00 PM", "7/9/19 5:00 PM", "7/9/19 6:00 PM", "7/9/19 7:00 PM", "7/9/19 8:00 PM", "7/9/19 9:00 PM", "7/9/19 10:00 PM", "7/9/19 11:00 PM", "7/10/19 12:00 AM", "7/10/19 1:00 AM", "7/10/19 2:00 AM", "7/10/19 3:00 AM", "7/10/19 4:00 AM", "7/10/19 5:00 AM", "7/10/19 6:00 AM", "7/10/19 7:00 AM", "7/10/19 8:00 AM", "7/10/19 9:00 AM", "7/10/19 10:00 AM", "7/10/19 11:00 AM", "7/10/19 12:00 PM", "7/10/19 1:00 PM", "7/10/19 2:00 PM", "7/10/19 3:00 PM", "7/10/19 4:00 PM", "7/10/19 5:00 PM", "7/10/19 6:00 PM", "7/10/19 7:00 PM", "7/10/19 8:00 PM", "7/10/19 9:00 PM", "7/10/19 10:00 PM", "7/10/19 11:00 PM", "7/11/19 12:00 AM", "7/11/19 1:00 AM", "7/11/19 2:00 AM", "7/11/19 3:00 AM", "7/11/19 4:00 AM", "7/11/19 5:00 AM", "7/11/19 6:00 AM", "7/11/19 7:00 AM", "7/11/19 8:00 AM", "7/11/19 9:00 AM", "7/11/19 10:00 AM", "7/11/19 11:00 AM", "7/11/19 12:00 PM", "7/11/19 1:00 PM", "7/11/19 2:00 PM", "7/11/19 3:00 PM", "7/11/19 4:00 PM", "7/11/19 5:00 PM", "7/11/19 6:00 PM", "7/11/19 7:00 PM", "7/11/19 8:00 PM", "7/11/19 9:00 PM", "7/11/19 10:00 PM", "7/11/19 11:00 PM", "7/12/19 12:00 AM", "7/12/19 1:00 AM", "7/12/19 2:00 AM", "7/12/19 3:00 AM", "7/12/19 4:00 AM", "7/12/19 5:00 AM", "7/12/19 6:00 AM", "7/12/19 7:00 AM", "7/12/19 8:00 AM", "7/12/19 9:00 AM", "7/12/19 10:00 AM", "7/12/19 11:00 AM", "7/12/19 12:00 PM", "7/12/19 1:00 PM", "7/12/19 2:00 PM", "7/12/19 3:00 PM", "7/12/19 4:00 PM", "7/12/19 5:00 PM", "7/12/19 6:00 PM", "7/12/19 7:00 PM", "7/12/19 8:00 PM", "7/12/19 9:00 PM", "7/12/19 10:00 PM", "7/12/19 11:00 PM", "7/13/19 12:00 AM", "7/13/19 1:00 AM", "7/13/19 2:00 AM", "7/13/19 3:00 AM", "7/13/19 4:00 AM", "7/13/19 5:00 AM", "7/13/19 6:00 AM", "7/13/19 7:00 AM", "7/13/19 8:00 AM", "7/13/19 9:00 AM", "7/13/19 10:00 AM", "7/13/19 11:00 AM", "7/13/19 12:00 PM", "7/13/19 1:00 PM", "7/13/19 2:00 PM", "7/13/19 3:00 PM", "7/13/19 4:00 PM", "7/13/19 5:00 PM", "7/13/19 6:00 PM", "7/13/19 7:00 PM", "7/13/19 8:00 PM", "7/13/19 9:00 PM", "7/13/19 10:00 PM", "7/13/19 11:00 PM", "7/14/19 12:00 AM", "7/14/19 1:00 AM", "7/14/19 2:00 AM", "7/14/19 3:00 AM", "7/14/19 4:00 AM", "7/14/19 5:00 AM", "7/14/19 6:00 AM", "7/14/19 7:00 AM", "7/14/19 8:00 AM", "7/14/19 9:00 AM", "7/14/19 10:00 AM", "7/14/19 11:00 AM", "7/14/19 12:00 PM", "7/14/19 1:00 PM", "7/14/19 2:00 PM", "7/14/19 3:00 PM", "7/14/19 4:00 PM", "7/14/19 5:00 PM", "7/14/19 6:00 PM", "7/14/19 7:00 PM", "7/14/19 8:00 PM", "7/14/19 9:00 PM", "7/14/19 10:00 PM", "7/14/19 11:00 PM", "7/15/19 12:00 AM", "7/15/19 1:00 AM", "7/15/19 2:00 AM", "7/15/19 3:00 AM", "7/15/19 4:00 AM", "7/15/19 5:00 AM", "7/15/19 6:00 AM", "7/15/19 7:00 AM", "7/15/19 8:00 AM", "7/15/19 9:00 AM", "7/15/19 10:00 AM", "7/15/19 11:00 AM", "7/15/19 12:00 PM", "7/15/19 1:00 PM", "7/15/19 2:00 PM", "7/15/19 3:00 PM", "7/15/19 4:00 PM", "7/15/19 5:00 PM", "7/15/19 6:00 PM", "7/15/19 7:00 PM", "7/15/19 8:00 PM", "7/15/19 9:00 PM", "7/15/19 10:00 PM", "7/15/19 11:00 PM", "7/16/19 12:00 AM", "7/16/19 1:00 AM", "7/16/19 2:00 AM", "7/16/19 3:00 AM", "7/16/19 4:00 AM", "7/16/19 5:00 AM", "7/16/19 6:00 AM", "7/16/19 7:00 AM", "7/16/19 8:00 AM", "7/16/19 9:00 AM", "7/16/19 10:00 AM", "7/16/19 11:00 AM", "7/16/19 12:00 PM", "7/16/19 1:00 PM", "7/16/19 2:00 PM", "7/16/19 3:00 PM", "7/16/19 4:00 PM", "7/16/19 5:00 PM", "7/16/19 6:00 PM", "7/16/19 7:00 PM", "7/16/19 8:00 PM", "7/16/19 9:00 PM", "7/16/19 10:00 PM", "7/16/19 11:00 PM", "7/17/19 12:00 AM", "7/17/19 1:00 AM", "7/17/19 2:00 AM", "7/17/19 3:00 AM", "7/17/19 4:00 AM", "7/17/19 5:00 AM", "7/17/19 6:00 AM", "7/17/19 7:00 AM", "7/17/19 8:00 AM", "7/17/19 9:00 AM", "7/17/19 10:00 AM", "7/17/19 11:00 AM", "7/17/19 12:00 PM", "7/17/19 1:00 PM", "7/17/19 2:00 PM", "7/17/19 3:00 PM", "7/17/19 4:00 PM", "7/17/19 5:00 PM", "7/17/19 6:00 PM", "7/17/19 7:00 PM", "7/17/19 8:00 PM", "7/17/19 9:00 PM", "7/17/19 10:00 PM", "7/17/19 11:00 PM", "7/18/19 12:00 AM", "7/18/19 1:00 AM", "7/18/19 2:00 AM", "7/18/19 3:00 AM", "7/18/19 4:00 AM", "7/18/19 5:00 AM", "7/18/19 6:00 AM", "7/18/19 7:00 AM", "7/18/19 8:00 AM", "7/18/19 9:00 AM", "7/18/19 10:00 AM", "7/18/19 11:00 AM", "7/18/19 12:00 PM", "7/18/19 1:00 PM", "7/18/19 2:00 PM", "7/18/19 3:00 PM", "7/18/19 4:00 PM", "7/18/19 5:00 PM", "7/18/19 6:00 PM", "7/18/19 7:00 PM", "7/18/19 8:00 PM", "7/18/19 9:00 PM", "7/18/19 10:00 PM", "7/18/19 11:00 PM", "7/19/19 12:00 AM", "7/19/19 1:00 AM", "7/19/19 2:00 AM", "7/19/19 3:00 AM", "7/19/19 4:00 AM", "7/19/19 5:00 AM", "7/19/19 6:00 AM", "7/19/19 7:00 AM", "7/19/19 8:00 AM", "7/19/19 9:00 AM", "7/19/19 10:00 AM", "7/19/19 11:00 AM", "7/19/19 12:00 PM", "7/19/19 1:00 PM", "7/19/19 2:00 PM", "7/19/19 3:00 PM", "7/19/19 4:00 PM", "7/19/19 5:00 PM", "7/19/19 6:00 PM", "7/19/19 7:00 PM", "7/19/19 8:00 PM", "7/19/19 9:00 PM", "7/19/19 10:00 PM", "7/19/19 11:00 PM", "7/20/19 12:00 AM", "7/20/19 1:00 AM", "7/20/19 2:00 AM", "7/20/19 3:00 AM", "7/20/19 4:00 AM", "7/20/19 5:00 AM", "7/20/19 6:00 AM", "7/20/19 7:00 AM", "7/20/19 8:00 AM", "7/20/19 9:00 AM", "7/20/19 10:00 AM", "7/20/19 11:00 AM", "7/20/19 12:00 PM", "7/20/19 1:00 PM", "7/20/19 2:00 PM", "7/20/19 3:00 PM", "7/20/19 4:00 PM", "7/20/19 5:00 PM", "7/20/19 6:00 PM", "7/20/19 7:00 PM", "7/20/19 8:00 PM", "7/20/19 9:00 PM", "7/20/19 10:00 PM", "7/20/19 11:00 PM", "7/21/19 12:00 AM", "7/21/19 1:00 AM", "7/21/19 2:00 AM", "7/21/19 3:00 AM", "7/21/19 4:00 AM", "7/21/19 5:00 AM", "7/21/19 6:00 AM", "7/21/19 7:00 AM", "7/21/19 8:00 AM", "7/21/19 9:00 AM", "7/21/19 10:00 AM", "7/21/19 11:00 AM", "7/21/19 12:00 PM", "7/21/19 1:00 PM", "7/21/19 2:00 PM", "7/21/19 3:00 PM", "7/21/19 4:00 PM", "7/21/19 5:00 PM", "7/21/19 6:00 PM", "7/21/19 7:00 PM", "7/21/19 8:00 PM", "7/21/19 9:00 PM", "7/21/19 10:00 PM", "7/21/19 11:00 PM", "7/22/19 12:00 AM", "7/22/19 1:00 AM", "7/22/19 2:00 AM", "7/22/19 3:00 AM", "7/22/19 4:00 AM", "7/22/19 5:00 AM", "7/22/19 6:00 AM", "7/22/19 7:00 AM", "7/22/19 8:00 AM", "7/22/19 9:00 AM", "7/22/19 10:00 AM", "7/22/19 11:00 AM", "7/22/19 12:00 PM", "7/22/19 1:00 PM", "7/22/19 2:00 PM", "7/22/19 3:00 PM", "7/22/19 4:00 PM", "7/22/19 5:00 PM", "7/22/19 6:00 PM", "7/22/19 7:00 PM", "7/22/19 8:00 PM", "7/22/19 9:00 PM", "7/22/19 10:00 PM", "7/22/19 11:00 PM", "7/23/19 12:00 AM", "7/23/19 1:00 AM", "7/23/19 2:00 AM", "7/23/19 3:00 AM", "7/23/19 4:00 AM", "7/23/19 5:00 AM", "7/23/19 6:00 AM", "7/23/19 7:00 AM", "7/23/19 8:00 AM", "7/23/19 9:00 AM", "7/23/19 10:00 AM", "7/23/19 11:00 AM", "7/23/19 12:00 PM", "7/23/19 1:00 PM", "7/23/19 2:00 PM", "7/23/19 3:00 PM", "7/23/19 4:00 PM", "7/23/19 5:00 PM", "7/23/19 6:00 PM", "7/23/19 7:00 PM", "7/23/19 8:00 PM", "7/23/19 9:00 PM", "7/23/19 10:00 PM", "7/23/19 11:00 PM", "7/24/19 12:00 AM", "7/24/19 1:00 AM", "7/24/19 2:00 AM", "7/24/19 3:00 AM", "7/24/19 4:00 AM", "7/24/19 5:00 AM", "7/24/19 6:00 AM", "7/24/19 7:00 AM", "7/24/19 8:00 AM", "7/24/19 9:00 AM", "7/24/19 10:00 AM", "7/24/19 11:00 AM", "7/24/19 12:00 PM", "7/24/19 1:00 PM", "7/24/19 2:00 PM", "7/24/19 3:00 PM", "7/24/19 4:00 PM", "7/24/19 5:00 PM", "7/24/19 6:00 PM", "7/24/19 7:00 PM", "7/24/19 8:00 PM", "7/24/19 9:00 PM", "7/24/19 10:00 PM", "7/24/19 11:00 PM", "7/25/19 12:00 AM", "7/25/19 1:00 AM", "7/25/19 2:00 AM", "7/25/19 3:00 AM", "7/25/19 4:00 AM", "7/25/19 5:00 AM", "7/25/19 6:00 AM", "7/25/19 7:00 AM", "7/25/19 8:00 AM", "7/25/19 9:00 AM", "7/25/19 10:00 AM", "7/25/19 11:00 AM", "7/25/19 12:00 PM", "7/25/19 1:00 PM", "7/25/19 2:00 PM", "7/25/19 3:00 PM", "7/25/19 4:00 PM", "7/25/19 5:00 PM", "7/25/19 6:00 PM", "7/25/19 7:00 PM", "7/25/19 8:00 PM", "7/25/19 9:00 PM", "7/25/19 10:00 PM", "7/25/19 11:00 PM", "7/26/19 12:00 AM", "7/26/19 1:00 AM", "7/26/19 2:00 AM", "7/26/19 3:00 AM", "7/26/19 4:00 AM", "7/26/19 5:00 AM", "7/26/19 6:00 AM", "7/26/19 7:00 AM", "7/26/19 8:00 AM", "7/26/19 9:00 AM", "7/26/19 10:00 AM", "7/26/19 11:00 AM", "7/26/19 12:00 PM", "7/26/19 1:00 PM", "7/26/19 2:00 PM", "7/26/19 3:00 PM", "7/26/19 4:00 PM", "7/26/19 5:00 PM", "7/26/19 6:00 PM", "7/26/19 7:00 PM", "7/26/19 8:00 PM", "7/26/19 9:00 PM", "7/26/19 10:00 PM", "7/26/19 11:00 PM", "7/27/19 12:00 AM", "7/27/19 1:00 AM", "7/27/19 2:00 AM", "7/27/19 3:00 AM", "7/27/19 4:00 AM", "7/27/19 5:00 AM", "7/27/19 6:00 AM", "7/27/19 7:00 AM", "7/27/19 8:00 AM", "7/27/19 9:00 AM", "7/27/19 10:00 AM", "7/27/19 11:00 AM", "7/27/19 12:00 PM", "7/27/19 1:00 PM", "7/27/19 2:00 PM", "7/27/19 3:00 PM", "7/27/19 4:00 PM", "7/27/19 5:00 PM", "7/27/19 6:00 PM", "7/27/19 7:00 PM", "7/27/19 8:00 PM", "7/27/19 9:00 PM", "7/27/19 10:00 PM", "7/27/19 11:00 PM", "7/28/19 12:00 AM", "7/28/19 1:00 AM", "7/28/19 2:00 AM", "7/28/19 3:00 AM", "7/28/19 4:00 AM", "7/28/19 5:00 AM", "7/28/19 6:00 AM", "7/28/19 7:00 AM", "7/28/19 8:00 AM", "7/28/19 9:00 AM", "7/28/19 10:00 AM", "7/28/19 11:00 AM", "7/28/19 12:00 PM", "7/28/19 1:00 PM", "7/28/19 2:00 PM", "7/28/19 3:00 PM", "7/28/19 4:00 PM", "7/28/19 5:00 PM", "7/28/19 6:00 PM", "7/28/19 7:00 PM", "7/28/19 8:00 PM", "7/28/19 9:00 PM", "7/28/19 10:00 PM", "7/28/19 11:00 PM", "7/29/19 12:00 AM", "7/29/19 1:00 AM", "7/29/19 2:00 AM", "7/29/19 3:00 AM", "7/29/19 4:00 AM", "7/29/19 5:00 AM", "7/29/19 6:00 AM", "7/29/19 7:00 AM", "7/29/19 8:00 AM", "7/29/19 9:00 AM", "7/29/19 10:00 AM", "7/29/19 11:00 AM", "7/29/19 12:00 PM", "7/29/19 1:00 PM", "7/29/19 2:00 PM", "7/29/19 3:00 PM", "7/29/19 4:00 PM", "7/29/19 5:00 PM", "7/29/19 6:00 PM", "7/29/19 7:00 PM", "7/29/19 8:00 PM", "7/29/19 9:00 PM", "7/29/19 10:00 PM", "7/29/19 11:00 PM", "7/30/19 12:00 AM", "7/30/19 1:00 AM", "7/30/19 2:00 AM", "7/30/19 3:00 AM", "7/30/19 4:00 AM", "7/30/19 5:00 AM", "7/30/19 6:00 AM", "7/30/19 7:00 AM", "7/30/19 8:00 AM", "7/30/19 9:00 AM", "7/30/19 10:00 AM", "7/30/19 11:00 AM", "7/30/19 12:00 PM", "7/30/19 1:00 PM", "7/30/19 2:00 PM", "7/30/19 3:00 PM", "7/30/19 4:00 PM", "7/30/19 5:00 PM", "7/30/19 6:00 PM", "7/30/19 7:00 PM", "7/30/19 8:00 PM", "7/30/19 9:00 PM", "7/30/19 10:00 PM", "7/30/19 11:00 PM", "7/31/19 12:00 AM", "7/31/19 1:00 AM", "7/31/19 2:00 AM", "7/31/19 3:00 AM", "7/31/19 4:00 AM", "7/31/19 5:00 AM", "7/31/19 6:00 AM", "7/31/19 7:00 AM", "7/31/19 8:00 AM", "7/31/19 9:00 AM", "7/31/19 10:00 AM", "7/31/19 11:00 AM", "7/31/19 12:00 PM", "7/31/19 1:00 PM", "7/31/19 2:00 PM", "7/31/19 3:00 PM", "7/31/19 4:00 PM", "7/31/19 5:00 PM", "7/31/19 6:00 PM", "7/31/19 7:00 PM", "7/31/19 8:00 PM", "7/31/19 9:00 PM", "7/31/19 10:00 PM", "7/31/19 11:00 PM", "8/1/19 12:00 AM", "8/1/19 1:00 AM", "8/1/19 2:00 AM", "8/1/19 3:00 AM", "8/1/19 4:00 AM", "8/1/19 5:00 AM", "8/1/19 6:00 AM", "8/1/19 7:00 AM", "8/1/19 8:00 AM", "8/1/19 9:00 AM", "8/1/19 10:00 AM", "8/1/19 11:00 AM", "8/1/19 12:00 PM", "8/1/19 1:00 PM", "8/1/19 2:00 PM", "8/1/19 3:00 PM", "8/1/19 4:00 PM", "8/1/19 5:00 PM", "8/1/19 6:00 PM", "8/1/19 7:00 PM", "8/1/19 8:00 PM", "8/1/19 9:00 PM", "8/1/19 10:00 PM", "8/1/19 11:00 PM", "8/2/19 12:00 AM", "8/2/19 1:00 AM", "8/2/19 2:00 AM", "8/2/19 3:00 AM", "8/2/19 4:00 AM", "8/2/19 5:00 AM", "8/2/19 6:00 AM", "8/2/19 7:00 AM", "8/2/19 8:00 AM", "8/2/19 9:00 AM", "8/2/19 10:00 AM", "8/2/19 11:00 AM", "8/2/19 12:00 PM", "8/2/19 1:00 PM", "8/2/19 2:00 PM", "8/2/19 3:00 PM", "8/2/19 4:00 PM", "8/2/19 5:00 PM", "8/2/19 6:00 PM", "8/2/19 7:00 PM", "8/2/19 8:00 PM", "8/2/19 9:00 PM", "8/2/19 10:00 PM", "8/2/19 11:00 PM", "8/3/19 12:00 AM", "8/3/19 1:00 AM", "8/3/19 2:00 AM", "8/3/19 3:00 AM", "8/3/19 4:00 AM", "8/3/19 5:00 AM", "8/3/19 6:00 AM", "8/3/19 7:00 AM", "8/3/19 8:00 AM", "8/3/19 9:00 AM", "8/3/19 10:00 AM", "8/3/19 11:00 AM", "8/3/19 12:00 PM", "8/3/19 1:00 PM", "8/3/19 2:00 PM", "8/3/19 3:00 PM", "8/3/19 4:00 PM", "8/3/19 5:00 PM", "8/3/19 6:00 PM", "8/3/19 7:00 PM", "8/3/19 8:00 PM", "8/3/19 9:00 PM", "8/3/19 10:00 PM", "8/3/19 11:00 PM", "8/4/19 12:00 AM", "8/4/19 1:00 AM", "8/4/19 2:00 AM", "8/4/19 3:00 AM", "8/4/19 4:00 AM", "8/4/19 5:00 AM", "8/4/19 6:00 AM", "8/4/19 7:00 AM", "8/4/19 8:00 AM", "8/4/19 9:00 AM", "8/4/19 10:00 AM", "8/4/19 11:00 AM", "8/4/19 12:00 PM", "8/4/19 1:00 PM", "8/4/19 2:00 PM", "8/4/19 3:00 PM", "8/4/19 4:00 PM", "8/4/19 5:00 PM", "8/4/19 6:00 PM", "8/4/19 7:00 PM", "8/4/19 8:00 PM", "8/4/19 9:00 PM", "8/4/19 10:00 PM", "8/4/19 11:00 PM", "8/5/19 12:00 AM", "8/5/19 1:00 AM", "8/5/19 2:00 AM", "8/5/19 3:00 AM", "8/5/19 4:00 AM", "8/5/19 5:00 AM", "8/5/19 6:00 AM", "8/5/19 7:00 AM", "8/5/19 8:00 AM", "8/5/19 9:00 AM", "8/5/19 10:00 AM", "8/5/19 11:00 AM", "8/5/19 12:00 PM", "8/5/19 1:00 PM", "8/5/19 2:00 PM", "8/5/19 3:00 PM", "8/5/19 4:00 PM", "8/5/19 5:00 PM", "8/5/19 6:00 PM", "8/5/19 7:00 PM", "8/5/19 8:00 PM", "8/5/19 9:00 PM", "8/5/19 10:00 PM", "8/5/19 11:00 PM", "8/6/19 12:00 AM", "8/6/19 1:00 AM", "8/6/19 2:00 AM", "8/6/19 3:00 AM", "8/6/19 4:00 AM", "8/6/19 5:00 AM", "8/6/19 6:00 AM", "8/6/19 7:00 AM", "8/6/19 8:00 AM", "8/6/19 9:00 AM", "8/6/19 10:00 AM", "8/6/19 11:00 AM", "8/6/19 12:00 PM", "8/6/19 1:00 PM", "8/6/19 2:00 PM", "8/6/19 3:00 PM", "8/6/19 4:00 PM", "8/6/19 5:00 PM", "8/6/19 6:00 PM", "8/6/19 7:00 PM", "8/6/19 8:00 PM", "8/6/19 9:00 PM", "8/6/19 10:00 PM", "8/6/19 11:00 PM", "8/7/19 12:00 AM", "8/7/19 1:00 AM", "8/7/19 2:00 AM", "8/7/19 3:00 AM", "8/7/19 4:00 AM", "8/7/19 5:00 AM", "8/7/19 6:00 AM", "8/7/19 7:00 AM", "8/7/19 8:00 AM", "8/7/19 9:00 AM", "8/7/19 10:00 AM", "8/7/19 11:00 AM", "8/7/19 12:00 PM", "8/7/19 1:00 PM", "8/7/19 2:00 PM", "8/7/19 3:00 PM", "8/7/19 4:00 PM", "8/7/19 5:00 PM", "8/7/19 6:00 PM", "8/7/19 7:00 PM", "8/7/19 8:00 PM", "8/7/19 9:00 PM", "8/7/19 10:00 PM", "8/7/19 11:00 PM", "8/8/19 12:00 AM", "8/8/19 1:00 AM", "8/8/19 2:00 AM", "8/8/19 3:00 AM", "8/8/19 4:00 AM", "8/8/19 5:00 AM", "8/8/19 6:00 AM", "8/8/19 7:00 AM", "8/8/19 8:00 AM", "8/8/19 9:00 AM", "8/8/19 10:00 AM", "8/8/19 11:00 AM", "8/8/19 12:00 PM", "8/8/19 1:00 PM", "8/8/19 2:00 PM", "8/8/19 3:00 PM", "8/8/19 4:00 PM", "8/8/19 5:00 PM", "8/8/19 6:00 PM", "8/8/19 7:00 PM", "8/8/19 8:00 PM", "8/8/19 9:00 PM", "8/8/19 10:00 PM", "8/8/19 11:00 PM", "8/9/19 12:00 AM", "8/9/19 1:00 AM", "8/9/19 2:00 AM", "8/9/19 3:00 AM", "8/9/19 4:00 AM", "8/9/19 5:00 AM", "8/9/19 6:00 AM", "8/9/19 7:00 AM", "8/9/19 8:00 AM", "8/9/19 9:00 AM", "8/9/19 10:00 AM", "8/9/19 11:00 AM", "8/9/19 12:00 PM", "8/9/19 1:00 PM", "8/9/19 2:00 PM", "8/9/19 3:00 PM", "8/9/19 4:00 PM", "8/9/19 5:00 PM", "8/9/19 6:00 PM", "8/9/19 7:00 PM", "8/9/19 8:00 PM", "8/9/19 9:00 PM", "8/9/19 10:00 PM", "8/9/19 11:00 PM", "8/10/19 12:00 AM", "8/10/19 1:00 AM", "8/10/19 2:00 AM", "8/10/19 3:00 AM", "8/10/19 4:00 AM", "8/10/19 5:00 AM", "8/10/19 6:00 AM", "8/10/19 7:00 AM", "8/10/19 8:00 AM", "8/10/19 9:00 AM", "8/10/19 10:00 AM", "8/10/19 11:00 AM", "8/10/19 12:00 PM", "8/10/19 1:00 PM", "8/10/19 2:00 PM", "8/10/19 3:00 PM", "8/10/19 4:00 PM", "8/10/19 5:00 PM", "8/10/19 6:00 PM", "8/10/19 7:00 PM", "8/10/19 8:00 PM", "8/10/19 9:00 PM", "8/10/19 10:00 PM", "8/10/19 11:00 PM", "8/11/19 12:00 AM", "8/11/19 1:00 AM", "8/11/19 2:00 AM", "8/11/19 3:00 AM", "8/11/19 4:00 AM", "8/11/19 5:00 AM", "8/11/19 6:00 AM", "8/11/19 7:00 AM", "8/11/19 8:00 AM", "8/11/19 9:00 AM", "8/11/19 10:00 AM", "8/11/19 11:00 AM", "8/11/19 12:00 PM", "8/11/19 1:00 PM", "8/11/19 2:00 PM", "8/11/19 3:00 PM", "8/11/19 4:00 PM", "8/11/19 5:00 PM", "8/11/19 6:00 PM", "8/11/19 7:00 PM", "8/11/19 8:00 PM", "8/11/19 9:00 PM", "8/11/19 10:00 PM", "8/11/19 11:00 PM", "8/12/19 12:00 AM", "8/12/19 1:00 AM", "8/12/19 2:00 AM", "8/12/19 3:00 AM", "8/12/19 4:00 AM", "8/12/19 5:00 AM", "8/12/19 6:00 AM", "8/12/19 7:00 AM", "8/12/19 8:00 AM", "8/12/19 9:00 AM", "8/12/19 10:00 AM", "8/12/19 11:00 AM", "8/12/19 12:00 PM", "8/12/19 1:00 PM", "8/12/19 2:00 PM", "8/12/19 3:00 PM", "8/12/19 4:00 PM", "8/12/19 5:00 PM", "8/12/19 6:00 PM", "8/12/19 7:00 PM", "8/12/19 8:00 PM", "8/12/19 9:00 PM", "8/12/19 10:00 PM", "8/12/19 11:00 PM", "8/13/19 12:00 AM", "8/13/19 1:00 AM", "8/13/19 2:00 AM", "8/13/19 3:00 AM", "8/13/19 4:00 AM", "8/13/19 5:00 AM", "8/13/19 6:00 AM", "8/13/19 7:00 AM", "8/13/19 8:00 AM", "8/13/19 9:00 AM", "8/13/19 10:00 AM", "8/13/19 11:00 AM", "8/13/19 12:00 PM", "8/13/19 1:00 PM", "8/13/19 2:00 PM", "8/13/19 3:00 PM", "8/13/19 4:00 PM", "8/13/19 5:00 PM", "8/13/19 6:00 PM", "8/13/19 7:00 PM", "8/13/19 8:00 PM", "8/13/19 9:00 PM", "8/13/19 10:00 PM", "8/13/19 11:00 PM", "8/14/19 12:00 AM", "8/14/19 1:00 AM", "8/14/19 2:00 AM", "8/14/19 3:00 AM", "8/14/19 4:00 AM", "8/14/19 5:00 AM", "8/14/19 6:00 AM", "8/14/19 7:00 AM", "8/14/19 8:00 AM", "8/14/19 9:00 AM", "8/14/19 10:00 AM", "8/14/19 11:00 AM", "8/14/19 12:00 PM", "8/14/19 1:00 PM", "8/14/19 2:00 PM", "8/14/19 3:00 PM", "8/14/19 4:00 PM", "8/14/19 5:00 PM", "8/14/19 6:00 PM", "8/14/19 7:00 PM", "8/14/19 8:00 PM", "8/14/19 9:00 PM", "8/14/19 10:00 PM", "8/14/19 11:00 PM", "8/15/19 12:00 AM", "8/15/19 1:00 AM", "8/15/19 2:00 AM", "8/15/19 3:00 AM", "8/15/19 4:00 AM", "8/15/19 5:00 AM", "8/15/19 6:00 AM", "8/15/19 7:00 AM", "8/15/19 8:00 AM", "8/15/19 9:00 AM", "8/15/19 10:00 AM", "8/15/19 11:00 AM", "8/15/19 12:00 PM", "8/15/19 1:00 PM", "8/15/19 2:00 PM", "8/15/19 3:00 PM", "8/15/19 4:00 PM", "8/15/19 5:00 PM", "8/15/19 6:00 PM", "8/15/19 7:00 PM", "8/15/19 8:00 PM", "8/15/19 9:00 PM", "8/15/19 10:00 PM", "8/15/19 11:00 PM", "8/16/19 12:00 AM", "8/16/19 1:00 AM", "8/16/19 2:00 AM", "8/16/19 3:00 AM", "8/16/19 4:00 AM", "8/16/19 5:00 AM", "8/16/19 6:00 AM", "8/16/19 7:00 AM", "8/16/19 8:00 AM", "8/16/19 9:00 AM", "8/16/19 10:00 AM", "8/16/19 11:00 AM", "8/16/19 12:00 PM", "8/16/19 1:00 PM", "8/16/19 2:00 PM", "8/16/19 3:00 PM", "8/16/19 4:00 PM", "8/16/19 5:00 PM", "8/16/19 6:00 PM", "8/16/19 7:00 PM", "8/16/19 8:00 PM", "8/16/19 9:00 PM", "8/16/19 10:00 PM", "8/16/19 11:00 PM", "8/17/19 12:00 AM", "8/17/19 1:00 AM", "8/17/19 2:00 AM", "8/17/19 3:00 AM", "8/17/19 4:00 AM", "8/17/19 5:00 AM", "8/17/19 6:00 AM", "8/17/19 7:00 AM", "8/17/19 8:00 AM", "8/17/19 9:00 AM", "8/17/19 10:00 AM", "8/17/19 11:00 AM", "8/17/19 12:00 PM", "8/17/19 1:00 PM", "8/17/19 2:00 PM", "8/17/19 3:00 PM", "8/17/19 4:00 PM", "8/17/19 5:00 PM", "8/17/19 6:00 PM", "8/17/19 7:00 PM", "8/17/19 8:00 PM", "8/17/19 9:00 PM", "8/17/19 10:00 PM", "8/17/19 11:00 PM", "8/18/19 12:00 AM", "8/18/19 1:00 AM", "8/18/19 2:00 AM", "8/18/19 3:00 AM", "8/18/19 4:00 AM", "8/18/19 5:00 AM", "8/18/19 6:00 AM", "8/18/19 7:00 AM", "8/18/19 8:00 AM", "8/18/19 9:00 AM", "8/18/19 10:00 AM", "8/18/19 11:00 AM", "8/18/19 12:00 PM", "8/18/19 1:00 PM", "8/18/19 2:00 PM", "8/18/19 3:00 PM", "8/18/19 4:00 PM", "8/18/19 5:00 PM", "8/18/19 6:00 PM", "8/18/19 7:00 PM", "8/18/19 8:00 PM", "8/18/19 9:00 PM", "8/18/19 10:00 PM", "8/18/19 11:00 PM", "8/19/19 12:00 AM", "8/19/19 1:00 AM", "8/19/19 2:00 AM", "8/19/19 3:00 AM", "8/19/19 4:00 AM", "8/19/19 5:00 AM", "8/19/19 6:00 AM", "8/19/19 7:00 AM", "8/19/19 8:00 AM", "8/19/19 9:00 AM", "8/19/19 10:00 AM", "8/19/19 11:00 AM", "8/19/19 12:00 PM", "8/19/19 1:00 PM", "8/19/19 2:00 PM", "8/19/19 3:00 PM", "8/19/19 4:00 PM", "8/19/19 5:00 PM", "8/19/19 6:00 PM", "8/19/19 7:00 PM", "8/19/19 8:00 PM", "8/19/19 9:00 PM", "8/19/19 10:00 PM", "8/19/19 11:00 PM", "8/20/19 12:00 AM", "8/20/19 1:00 AM", "8/20/19 2:00 AM", "8/20/19 3:00 AM", "8/20/19 4:00 AM", "8/20/19 5:00 AM", "8/20/19 6:00 AM", "8/20/19 7:00 AM", "8/20/19 8:00 AM", "8/20/19 9:00 AM", "8/20/19 10:00 AM", "8/20/19 11:00 AM", "8/20/19 12:00 PM", "8/20/19 1:00 PM", "8/20/19 2:00 PM", "8/20/19 3:00 PM", "8/20/19 4:00 PM", "8/20/19 5:00 PM", "8/20/19 6:00 PM", "8/20/19 7:00 PM", "8/20/19 8:00 PM", "8/20/19 9:00 PM", "8/20/19 10:00 PM", "8/20/19 11:00 PM", "8/21/19 12:00 AM", "8/21/19 1:00 AM", "8/21/19 2:00 AM", "8/21/19 3:00 AM", "8/21/19 4:00 AM", "8/21/19 5:00 AM", "8/21/19 6:00 AM", "8/21/19 7:00 AM", "8/21/19 8:00 AM", "8/21/19 9:00 AM", "8/21/19 10:00 AM", "8/21/19 11:00 AM", "8/21/19 12:00 PM", "8/21/19 1:00 PM", "8/21/19 2:00 PM", "8/21/19 3:00 PM", "8/21/19 4:00 PM", "8/21/19 5:00 PM", "8/21/19 6:00 PM", "8/21/19 7:00 PM", "8/21/19 8:00 PM", "8/21/19 9:00 PM", "8/21/19 10:00 PM", "8/21/19 11:00 PM", "8/22/19 12:00 AM", "8/22/19 1:00 AM", "8/22/19 2:00 AM", "8/22/19 3:00 AM", "8/22/19 4:00 AM", "8/22/19 5:00 AM", "8/22/19 6:00 AM", "8/22/19 7:00 AM", "8/22/19 8:00 AM", "8/22/19 9:00 AM", "8/22/19 10:00 AM", "8/22/19 11:00 AM", "8/22/19 12:00 PM", "8/22/19 1:00 PM", "8/22/19 2:00 PM", "8/22/19 3:00 PM", "8/22/19 4:00 PM", "8/22/19 5:00 PM", "8/22/19 6:00 PM", "8/22/19 7:00 PM", "8/22/19 8:00 PM", "8/22/19 9:00 PM", "8/22/19 10:00 PM", "8/22/19 11:00 PM", "8/23/19 12:00 AM", "8/23/19 1:00 AM", "8/23/19 2:00 AM", "8/23/19 3:00 AM", "8/23/19 4:00 AM", "8/23/19 5:00 AM", "8/23/19 6:00 AM", "8/23/19 7:00 AM", "8/23/19 8:00 AM", "8/23/19 9:00 AM", "8/23/19 10:00 AM", "8/23/19 11:00 AM", "8/23/19 12:00 PM", "8/23/19 1:00 PM", "8/23/19 2:00 PM", "8/23/19 3:00 PM", "8/23/19 4:00 PM", "8/23/19 5:00 PM", "8/23/19 6:00 PM", "8/23/19 7:00 PM", "8/23/19 8:00 PM", "8/23/19 9:00 PM", "8/23/19 10:00 PM", "8/23/19 11:00 PM", "8/24/19 12:00 AM", "8/24/19 1:00 AM", "8/24/19 2:00 AM", "8/24/19 3:00 AM", "8/24/19 4:00 AM", "8/24/19 5:00 AM", "8/24/19 6:00 AM", "8/24/19 7:00 AM", "8/24/19 8:00 AM", "8/24/19 9:00 AM", "8/24/19 10:00 AM", "8/24/19 11:00 AM", "8/24/19 12:00 PM", "8/24/19 1:00 PM", "8/24/19 2:00 PM", "8/24/19 3:00 PM", "8/24/19 4:00 PM", "8/24/19 5:00 PM", "8/24/19 6:00 PM", "8/24/19 7:00 PM", "8/24/19 8:00 PM", "8/24/19 9:00 PM", "8/24/19 10:00 PM", "8/24/19 11:00 PM", "8/25/19 12:00 AM", "8/25/19 1:00 AM", "8/25/19 2:00 AM", "8/25/19 3:00 AM", "8/25/19 4:00 AM", "8/25/19 5:00 AM", "8/25/19 6:00 AM", "8/25/19 7:00 AM", "8/25/19 8:00 AM", "8/25/19 9:00 AM", "8/25/19 10:00 AM", "8/25/19 11:00 AM", "8/25/19 12:00 PM", "8/25/19 1:00 PM", "8/25/19 2:00 PM", "8/25/19 3:00 PM", "8/25/19 4:00 PM", "8/25/19 5:00 PM", "8/25/19 6:00 PM", "8/25/19 7:00 PM", "8/25/19 8:00 PM", "8/25/19 9:00 PM", "8/25/19 10:00 PM", "8/25/19 11:00 PM", "8/26/19 12:00 AM", "8/26/19 1:00 AM", "8/26/19 2:00 AM", "8/26/19 3:00 AM", "8/26/19 4:00 AM", "8/26/19 5:00 AM", "8/26/19 6:00 AM", "8/26/19 7:00 AM", "8/26/19 8:00 AM", "8/26/19 9:00 AM", "8/26/19 10:00 AM", "8/26/19 11:00 AM", "8/26/19 12:00 PM", "8/26/19 1:00 PM", "8/26/19 2:00 PM", "8/26/19 3:00 PM", "8/26/19 4:00 PM", "8/26/19 5:00 PM", "8/26/19 6:00 PM", "8/26/19 7:00 PM", "8/26/19 8:00 PM", "8/26/19 9:00 PM", "8/26/19 10:00 PM", "8/26/19 11:00 PM", "8/27/19 12:00 AM", "8/27/19 1:00 AM", "8/27/19 2:00 AM", "8/27/19 3:00 AM", "8/27/19 4:00 AM", "8/27/19 5:00 AM", "8/27/19 6:00 AM", "8/27/19 7:00 AM", "8/27/19 8:00 AM", "8/27/19 9:00 AM", "8/27/19 10:00 AM", "8/27/19 11:00 AM", "8/27/19 12:00 PM", "8/27/19 1:00 PM", "8/27/19 2:00 PM", "8/27/19 3:00 PM", "8/27/19 4:00 PM", "8/27/19 5:00 PM", "8/27/19 6:00 PM", "8/27/19 7:00 PM", "8/27/19 8:00 PM", "8/27/19 9:00 PM", "8/27/19 10:00 PM", "8/27/19 11:00 PM", "8/28/19 12:00 AM", "8/28/19 1:00 AM", "8/28/19 2:00 AM", "8/28/19 3:00 AM", "8/28/19 4:00 AM", "8/28/19 5:00 AM", "8/28/19 6:00 AM", "8/28/19 7:00 AM", "8/28/19 8:00 AM", "8/28/19 9:00 AM", "8/28/19 10:00 AM", "8/28/19 11:00 AM", "8/28/19 12:00 PM", "8/28/19 1:00 PM", "8/28/19 2:00 PM", "8/28/19 3:00 PM", "8/28/19 4:00 PM", "8/28/19 5:00 PM", "8/28/19 6:00 PM", "8/28/19 7:00 PM", "8/28/19 8:00 PM", "8/28/19 9:00 PM", "8/28/19 10:00 PM", "8/28/19 11:00 PM", "8/29/19 12:00 AM", "8/29/19 1:00 AM", "8/29/19 2:00 AM", "8/29/19 3:00 AM", "8/29/19 4:00 AM", "8/29/19 5:00 AM", "8/29/19 6:00 AM", "8/29/19 7:00 AM", "8/29/19 8:00 AM", "8/29/19 9:00 AM", "8/29/19 10:00 AM", "8/29/19 11:00 AM", "8/29/19 12:00 PM", "8/29/19 1:00 PM", "8/29/19 2:00 PM", "8/29/19 3:00 PM", "8/29/19 4:00 PM", "8/29/19 5:00 PM", "8/29/19 6:00 PM", "8/29/19 7:00 PM", "8/29/19 8:00 PM", "8/29/19 9:00 PM", "8/29/19 10:00 PM", "8/29/19 11:00 PM", "8/30/19 12:00 AM", "8/30/19 1:00 AM", "8/30/19 2:00 AM", "8/30/19 3:00 AM", "8/30/19 4:00 AM", "8/30/19 5:00 AM", "8/30/19 6:00 AM", "8/30/19 7:00 AM", "8/30/19 8:00 AM", "8/30/19 9:00 AM", "8/30/19 10:00 AM", "8/30/19 11:00 AM", "8/30/19 12:00 PM", "8/30/19 1:00 PM", "8/30/19 2:00 PM", "8/30/19 3:00 PM", "8/30/19 4:00 PM", "8/30/19 5:00 PM", "8/30/19 6:00 PM", "8/30/19 7:00 PM", "8/30/19 8:00 PM", "8/30/19 9:00 PM", "8/30/19 10:00 PM", "8/30/19 11:00 PM", "8/31/19 12:00 AM", "8/31/19 1:00 AM", "8/31/19 2:00 AM", "8/31/19 3:00 AM", "8/31/19 4:00 AM", "8/31/19 5:00 AM", "8/31/19 6:00 AM", "8/31/19 7:00 AM", "8/31/19 8:00 AM", "8/31/19 9:00 AM", "8/31/19 10:00 AM", "8/31/19 11:00 AM", "8/31/19 12:00 PM", "8/31/19 1:00 PM", "8/31/19 2:00 PM", "8/31/19 3:00 PM", "8/31/19 4:00 PM", "8/31/19 5:00 PM", "8/31/19 6:00 PM", "8/31/19 7:00 PM", "8/31/19 8:00 PM", "8/31/19 9:00 PM", "8/31/19 10:00 PM", "8/31/19 11:00 PM", "9/1/19 12:00 AM", "9/1/19 1:00 AM", "9/1/19 2:00 AM", "9/1/19 3:00 AM", "9/1/19 4:00 AM", "9/1/19 5:00 AM", "9/1/19 6:00 AM", "9/1/19 7:00 AM", "9/1/19 8:00 AM", "9/1/19 9:00 AM", "9/1/19 10:00 AM", "9/1/19 11:00 AM", "9/1/19 12:00 PM", "9/1/19 1:00 PM", "9/1/19 2:00 PM", "9/1/19 3:00 PM", "9/1/19 4:00 PM", "9/1/19 5:00 PM", "9/1/19 6:00 PM", "9/1/19 7:00 PM", "9/1/19 8:00 PM", "9/1/19 9:00 PM", "9/1/19 10:00 PM", "9/1/19 11:00 PM", "9/2/19 12:00 AM", "9/2/19 1:00 AM", "9/2/19 2:00 AM", "9/2/19 3:00 AM", "9/2/19 4:00 AM", "9/2/19 5:00 AM", "9/2/19 6:00 AM", "9/2/19 7:00 AM", "9/2/19 8:00 AM", "9/2/19 9:00 AM", "9/2/19 10:00 AM", "9/2/19 11:00 AM", "9/2/19 12:00 PM", "9/2/19 1:00 PM", "9/2/19 2:00 PM", "9/2/19 3:00 PM", "9/2/19 4:00 PM", "9/2/19 5:00 PM", "9/2/19 6:00 PM", "9/2/19 7:00 PM", "9/2/19 8:00 PM", "9/2/19 9:00 PM", "9/2/19 10:00 PM", "9/2/19 11:00 PM", "9/3/19 12:00 AM", "9/3/19 1:00 AM", "9/3/19 2:00 AM", "9/3/19 3:00 AM", "9/3/19 4:00 AM", "9/3/19 5:00 AM", "9/3/19 6:00 AM", "9/3/19 7:00 AM", "9/3/19 8:00 AM", "9/3/19 9:00 AM", "9/3/19 10:00 AM", "9/3/19 11:00 AM", "9/3/19 12:00 PM", "9/3/19 1:00 PM", "9/3/19 2:00 PM", "9/3/19 3:00 PM", "9/3/19 4:00 PM", "9/3/19 5:00 PM", "9/3/19 6:00 PM", "9/3/19 7:00 PM", "9/3/19 8:00 PM", "9/3/19 9:00 PM", "9/3/19 10:00 PM", "9/3/19 11:00 PM", "9/4/19 12:00 AM", "9/4/19 1:00 AM", "9/4/19 2:00 AM", "9/4/19 3:00 AM", "9/4/19 4:00 AM", "9/4/19 5:00 AM", "9/4/19 6:00 AM", "9/4/19 7:00 AM", "9/4/19 8:00 AM", "9/4/19 9:00 AM", "9/4/19 10:00 AM", "9/4/19 11:00 AM", "9/4/19 12:00 PM", "9/4/19 1:00 PM", "9/4/19 2:00 PM", "9/4/19 3:00 PM", "9/4/19 4:00 PM", "9/4/19 5:00 PM", "9/4/19 6:00 PM", "9/4/19 7:00 PM", "9/4/19 8:00 PM", "9/4/19 9:00 PM", "9/4/19 10:00 PM", "9/4/19 11:00 PM", "9/5/19 12:00 AM", "9/5/19 1:00 AM", "9/5/19 2:00 AM", "9/5/19 3:00 AM", "9/5/19 4:00 AM", "9/5/19 5:00 AM", "9/5/19 6:00 AM", "9/5/19 7:00 AM", "9/5/19 8:00 AM", "9/5/19 9:00 AM", "9/5/19 10:00 AM", "9/5/19 11:00 AM", "9/5/19 12:00 PM", "9/5/19 1:00 PM", "9/5/19 2:00 PM", "9/5/19 3:00 PM", "9/5/19 4:00 PM", "9/5/19 5:00 PM", "9/5/19 6:00 PM", "9/5/19 7:00 PM", "9/5/19 8:00 PM", "9/5/19 9:00 PM", "9/5/19 10:00 PM", "9/5/19 11:00 PM", "9/6/19 12:00 AM", "9/6/19 1:00 AM", "9/6/19 2:00 AM", "9/6/19 3:00 AM", "9/6/19 4:00 AM", "9/6/19 5:00 AM", "9/6/19 6:00 AM", "9/6/19 7:00 AM", "9/6/19 8:00 AM", "9/6/19 9:00 AM", "9/6/19 10:00 AM", "9/6/19 11:00 AM", "9/6/19 12:00 PM", "9/6/19 1:00 PM", "9/6/19 2:00 PM", "9/6/19 3:00 PM", "9/6/19 4:00 PM", "9/6/19 5:00 PM", "9/6/19 6:00 PM", "9/6/19 7:00 PM", "9/6/19 8:00 PM", "9/6/19 9:00 PM", "9/6/19 10:00 PM", "9/6/19 11:00 PM", "9/7/19 12:00 AM", "9/7/19 1:00 AM", "9/7/19 2:00 AM", "9/7/19 3:00 AM", "9/7/19 4:00 AM", "9/7/19 5:00 AM", "9/7/19 6:00 AM", "9/7/19 7:00 AM", "9/7/19 8:00 AM", "9/7/19 9:00 AM", "9/7/19 10:00 AM", "9/7/19 11:00 AM", "9/7/19 12:00 PM", "9/7/19 1:00 PM", "9/7/19 2:00 PM", "9/7/19 3:00 PM", "9/7/19 4:00 PM", "9/7/19 5:00 PM", "9/7/19 6:00 PM", "9/7/19 7:00 PM", "9/7/19 8:00 PM", "9/7/19 9:00 PM", "9/7/19 10:00 PM", "9/7/19 11:00 PM", "9/8/19 12:00 AM", "9/8/19 1:00 AM", "9/8/19 2:00 AM", "9/8/19 3:00 AM", "9/8/19 4:00 AM", "9/8/19 5:00 AM", "9/8/19 6:00 AM", "9/8/19 7:00 AM", "9/8/19 8:00 AM", "9/8/19 9:00 AM", "9/8/19 10:00 AM", "9/8/19 11:00 AM", "9/8/19 12:00 PM", "9/8/19 1:00 PM", "9/8/19 2:00 PM", "9/8/19 3:00 PM", "9/8/19 4:00 PM", "9/8/19 5:00 PM", "9/8/19 6:00 PM", "9/8/19 7:00 PM", "9/8/19 8:00 PM", "9/8/19 9:00 PM", "9/8/19 10:00 PM", "9/8/19 11:00 PM", "9/9/19 12:00 AM", "9/9/19 1:00 AM", "9/9/19 2:00 AM", "9/9/19 3:00 AM", "9/9/19 4:00 AM", "9/9/19 5:00 AM", "9/9/19 6:00 AM", "9/9/19 7:00 AM", "9/9/19 8:00 AM", "9/9/19 9:00 AM", "9/9/19 10:00 AM", "9/9/19 11:00 AM", "9/9/19 12:00 PM", "9/9/19 1:00 PM", "9/9/19 2:00 PM", "9/9/19 3:00 PM", "9/9/19 4:00 PM", "9/9/19 5:00 PM", "9/9/19 6:00 PM", "9/9/19 7:00 PM", "9/9/19 8:00 PM", "9/9/19 9:00 PM", "9/9/19 10:00 PM", "9/9/19 11:00 PM", "9/10/19 12:00 AM", "9/10/19 1:00 AM", "9/10/19 2:00 AM", "9/10/19 3:00 AM", "9/10/19 4:00 AM", "9/10/19 5:00 AM", "9/10/19 6:00 AM", "9/10/19 7:00 AM", "9/10/19 8:00 AM", "9/10/19 9:00 AM", "9/10/19 10:00 AM", "9/10/19 11:00 AM", "9/10/19 12:00 PM", "9/10/19 1:00 PM", "9/10/19 2:00 PM", "9/10/19 3:00 PM", "9/10/19 4:00 PM", "9/10/19 5:00 PM", "9/10/19 6:00 PM", "9/10/19 7:00 PM", "9/10/19 8:00 PM", "9/10/19 9:00 PM", "9/10/19 10:00 PM", "9/10/19 11:00 PM", "9/11/19 12:00 AM", "9/11/19 1:00 AM", "9/11/19 2:00 AM", "9/11/19 3:00 AM", "9/11/19 4:00 AM", "9/11/19 5:00 AM", "9/11/19 6:00 AM", "9/11/19 7:00 AM", "9/11/19 8:00 AM", "9/11/19 9:00 AM", "9/11/19 10:00 AM", "9/11/19 11:00 AM", "9/11/19 12:00 PM", "9/11/19 1:00 PM", "9/11/19 2:00 PM", "9/11/19 3:00 PM", "9/11/19 4:00 PM", "9/11/19 5:00 PM", "9/11/19 6:00 PM", "9/11/19 7:00 PM", "9/11/19 8:00 PM", "9/11/19 9:00 PM", "9/11/19 10:00 PM", "9/11/19 11:00 PM", "9/12/19 12:00 AM", "9/12/19 1:00 AM", "9/12/19 2:00 AM", "9/12/19 3:00 AM", "9/12/19 4:00 AM", "9/12/19 5:00 AM", "9/12/19 6:00 AM", "9/12/19 7:00 AM", "9/12/19 8:00 AM", "9/12/19 9:00 AM", "9/12/19 10:00 AM", "9/12/19 11:00 AM", "9/12/19 12:00 PM", "9/12/19 1:00 PM", "9/12/19 2:00 PM", "9/12/19 3:00 PM", "9/12/19 4:00 PM", "9/12/19 5:00 PM", "9/12/19 6:00 PM", "9/12/19 7:00 PM", "9/12/19 8:00 PM", "9/12/19 9:00 PM", "9/12/19 10:00 PM", "9/12/19 11:00 PM", "9/13/19 12:00 AM", "9/13/19 1:00 AM", "9/13/19 2:00 AM", "9/13/19 3:00 AM", "9/13/19 4:00 AM", "9/13/19 5:00 AM", "9/13/19 6:00 AM", "9/13/19 7:00 AM", "9/13/19 8:00 AM", "9/13/19 9:00 AM", "9/13/19 10:00 AM", "9/13/19 11:00 AM", "9/13/19 12:00 PM", "9/13/19 1:00 PM", "9/13/19 2:00 PM", "9/13/19 3:00 PM", "9/13/19 4:00 PM", "9/13/19 5:00 PM", "9/13/19 6:00 PM", "9/13/19 7:00 PM", "9/13/19 8:00 PM", "9/13/19 9:00 PM", "9/13/19 10:00 PM", "9/13/19 11:00 PM", "9/14/19 12:00 AM", "9/14/19 1:00 AM", "9/14/19 2:00 AM", "9/14/19 3:00 AM", "9/14/19 4:00 AM", "9/14/19 5:00 AM", "9/14/19 6:00 AM", "9/14/19 7:00 AM", "9/14/19 8:00 AM", "9/14/19 9:00 AM", "9/14/19 10:00 AM", "9/14/19 11:00 AM", "9/14/19 12:00 PM", "9/14/19 1:00 PM", "9/14/19 2:00 PM", "9/14/19 3:00 PM", "9/14/19 4:00 PM", "9/14/19 5:00 PM", "9/14/19 6:00 PM", "9/14/19 7:00 PM", "9/14/19 8:00 PM", "9/14/19 9:00 PM", "9/14/19 10:00 PM", "9/14/19 11:00 PM", "9/15/19 12:00 AM", "9/15/19 1:00 AM", "9/15/19 2:00 AM", "9/15/19 3:00 AM", "9/15/19 4:00 AM", "9/15/19 5:00 AM", "9/15/19 6:00 AM", "9/15/19 7:00 AM", "9/15/19 8:00 AM", "9/15/19 9:00 AM", "9/15/19 10:00 AM", "9/15/19 11:00 AM", "9/15/19 12:00 PM", "9/15/19 1:00 PM", "9/15/19 2:00 PM", "9/15/19 3:00 PM", "9/15/19 4:00 PM", "9/15/19 5:00 PM", "9/15/19 6:00 PM", "9/15/19 7:00 PM", "9/15/19 8:00 PM", "9/15/19 9:00 PM", "9/15/19 10:00 PM", "9/15/19 11:00 PM", "9/16/19 12:00 AM", "9/16/19 1:00 AM", "9/16/19 2:00 AM", "9/16/19 3:00 AM", "9/16/19 4:00 AM", "9/16/19 5:00 AM", "9/16/19 6:00 AM", "9/16/19 7:00 AM", "9/16/19 8:00 AM", "9/16/19 9:00 AM", "9/16/19 10:00 AM", "9/16/19 11:00 AM", "9/16/19 12:00 PM", "9/16/19 1:00 PM", "9/16/19 2:00 PM", "9/16/19 3:00 PM", "9/16/19 4:00 PM", "9/16/19 5:00 PM", "9/16/19 6:00 PM", "9/16/19 7:00 PM", "9/16/19 8:00 PM", "9/16/19 9:00 PM", "9/16/19 10:00 PM", "9/16/19 11:00 PM", "9/17/19 12:00 AM", "9/17/19 1:00 AM", "9/17/19 2:00 AM", "9/17/19 3:00 AM", "9/17/19 4:00 AM", "9/17/19 5:00 AM", "9/17/19 6:00 AM", "9/17/19 7:00 AM", "9/17/19 8:00 AM", "9/17/19 9:00 AM", "9/17/19 10:00 AM", "9/17/19 11:00 AM", "9/17/19 12:00 PM", "9/17/19 1:00 PM", "9/17/19 2:00 PM", "9/17/19 3:00 PM", "9/17/19 4:00 PM", "9/17/19 5:00 PM", "9/17/19 6:00 PM", "9/17/19 7:00 PM", "9/17/19 8:00 PM", "9/17/19 9:00 PM", "9/17/19 10:00 PM", "9/17/19 11:00 PM", "9/18/19 12:00 AM", "9/18/19 1:00 AM", "9/18/19 2:00 AM", "9/18/19 3:00 AM", "9/18/19 4:00 AM", "9/18/19 5:00 AM", "9/18/19 6:00 AM", "9/18/19 7:00 AM", "9/18/19 8:00 AM", "9/18/19 9:00 AM", "9/18/19 10:00 AM", "9/18/19 11:00 AM", "9/18/19 12:00 PM", "9/18/19 1:00 PM", "9/18/19 2:00 PM", "9/18/19 3:00 PM", "9/18/19 4:00 PM", "9/18/19 5:00 PM", "9/18/19 6:00 PM", "9/18/19 7:00 PM", "9/18/19 8:00 PM", "9/18/19 9:00 PM", "9/18/19 10:00 PM", "9/18/19 11:00 PM", "9/19/19 12:00 AM", "9/19/19 1:00 AM", "9/19/19 2:00 AM", "9/19/19 3:00 AM", "9/19/19 4:00 AM", "9/19/19 5:00 AM", "9/19/19 6:00 AM", "9/19/19 7:00 AM", "9/19/19 8:00 AM", "9/19/19 9:00 AM", "9/19/19 10:00 AM", "9/19/19 11:00 AM", "9/19/19 12:00 PM", "9/19/19 1:00 PM", "9/19/19 2:00 PM", "9/19/19 3:00 PM", "9/19/19 4:00 PM", "9/19/19 5:00 PM", "9/19/19 6:00 PM", "9/19/19 7:00 PM", "9/19/19 8:00 PM", "9/19/19 9:00 PM", "9/19/19 10:00 PM", "9/19/19 11:00 PM", "9/20/19 12:00 AM", "9/20/19 1:00 AM", "9/20/19 2:00 AM", "9/20/19 3:00 AM", "9/20/19 4:00 AM", "9/20/19 5:00 AM", "9/20/19 6:00 AM", "9/20/19 7:00 AM", "9/20/19 8:00 AM", "9/20/19 9:00 AM", "9/20/19 10:00 AM", "9/20/19 11:00 AM", "9/20/19 12:00 PM", "9/20/19 1:00 PM", "9/20/19 2:00 PM", "9/20/19 3:00 PM", "9/20/19 4:00 PM", "9/20/19 5:00 PM", "9/20/19 6:00 PM", "9/20/19 7:00 PM", "9/20/19 8:00 PM", "9/20/19 9:00 PM", "9/20/19 10:00 PM", "9/20/19 11:00 PM", "9/21/19 12:00 AM", "9/21/19 1:00 AM", "9/21/19 2:00 AM", "9/21/19 3:00 AM", "9/21/19 4:00 AM", "9/21/19 5:00 AM", "9/21/19 6:00 AM", "9/21/19 7:00 AM", "9/21/19 8:00 AM", "9/21/19 9:00 AM", "9/21/19 10:00 AM", "9/21/19 11:00 AM", "9/21/19 12:00 PM", "9/21/19 1:00 PM", "9/21/19 2:00 PM", "9/21/19 3:00 PM", "9/21/19 4:00 PM", "9/21/19 5:00 PM", "9/21/19 6:00 PM", "9/21/19 7:00 PM", "9/21/19 8:00 PM", "9/21/19 9:00 PM", "9/21/19 10:00 PM", "9/21/19 11:00 PM", "9/22/19 12:00 AM", "9/22/19 1:00 AM", "9/22/19 2:00 AM", "9/22/19 3:00 AM", "9/22/19 4:00 AM", "9/22/19 5:00 AM", "9/22/19 6:00 AM", "9/22/19 7:00 AM", "9/22/19 8:00 AM", "9/22/19 9:00 AM", "9/22/19 10:00 AM", "9/22/19 11:00 AM", "9/22/19 12:00 PM", "9/22/19 1:00 PM", "9/22/19 2:00 PM", "9/22/19 3:00 PM", "9/22/19 4:00 PM", "9/22/19 5:00 PM", "9/22/19 6:00 PM", "9/22/19 7:00 PM", "9/22/19 8:00 PM", "9/22/19 9:00 PM", "9/22/19 10:00 PM", "9/22/19 11:00 PM", "9/23/19 12:00 AM", "9/23/19 1:00 AM", "9/23/19 2:00 AM", "9/23/19 3:00 AM", "9/23/19 4:00 AM", "9/23/19 5:00 AM", "9/23/19 6:00 AM", "9/23/19 7:00 AM", "9/23/19 8:00 AM", "9/23/19 9:00 AM", "9/23/19 10:00 AM", "9/23/19 11:00 AM", "9/23/19 12:00 PM", "9/23/19 1:00 PM", "9/23/19 2:00 PM", "9/23/19 3:00 PM", "9/23/19 4:00 PM", "9/23/19 5:00 PM", "9/23/19 6:00 PM", "9/23/19 7:00 PM", "9/23/19 8:00 PM", "9/23/19 9:00 PM", "9/23/19 10:00 PM", "9/23/19 11:00 PM", "9/24/19 12:00 AM", "9/24/19 1:00 AM", "9/24/19 2:00 AM", "9/24/19 3:00 AM", "9/24/19 4:00 AM", "9/24/19 5:00 AM", "9/24/19 6:00 AM", "9/24/19 7:00 AM", "9/24/19 8:00 AM", "9/24/19 9:00 AM", "9/24/19 10:00 AM", "9/24/19 11:00 AM", "9/24/19 12:00 PM", "9/24/19 1:00 PM", "9/24/19 2:00 PM", "9/24/19 3:00 PM", "9/24/19 4:00 PM", "9/24/19 5:00 PM", "9/24/19 6:00 PM", "9/24/19 7:00 PM", "9/24/19 8:00 PM", "9/24/19 9:00 PM", "9/24/19 10:00 PM", "9/24/19 11:00 PM", "9/25/19 12:00 AM", "9/25/19 1:00 AM", "9/25/19 2:00 AM", "9/25/19 3:00 AM", "9/25/19 4:00 AM", "9/25/19 5:00 AM", "9/25/19 6:00 AM", "9/25/19 7:00 AM", "9/25/19 8:00 AM", "9/25/19 9:00 AM", "9/25/19 10:00 AM", "9/25/19 11:00 AM", "9/25/19 12:00 PM", "9/25/19 1:00 PM", "9/25/19 2:00 PM", "9/25/19 3:00 PM", "9/25/19 4:00 PM", "9/25/19 5:00 PM", "9/25/19 6:00 PM", "9/25/19 7:00 PM", "9/25/19 8:00 PM", "9/25/19 9:00 PM", "9/25/19 10:00 PM", "9/25/19 11:00 PM", "9/26/19 12:00 AM", "9/26/19 1:00 AM", "9/26/19 2:00 AM", "9/26/19 3:00 AM", "9/26/19 4:00 AM", "9/26/19 5:00 AM", "9/26/19 6:00 AM", "9/26/19 7:00 AM", "9/26/19 8:00 AM", "9/26/19 9:00 AM", "9/26/19 10:00 AM", "9/26/19 11:00 AM", "9/26/19 12:00 PM", "9/26/19 1:00 PM", "9/26/19 2:00 PM", "9/26/19 3:00 PM", "9/26/19 4:00 PM", "9/26/19 5:00 PM", "9/26/19 6:00 PM", "9/26/19 7:00 PM", "9/26/19 8:00 PM", "9/26/19 9:00 PM", "9/26/19 10:00 PM", "9/26/19 11:00 PM", "9/27/19 12:00 AM", "9/27/19 1:00 AM", "9/27/19 2:00 AM", "9/27/19 3:00 AM", "9/27/19 4:00 AM", "9/27/19 5:00 AM", "9/27/19 6:00 AM", "9/27/19 7:00 AM", "9/27/19 8:00 AM", "9/27/19 9:00 AM", "9/27/19 10:00 AM", "9/27/19 11:00 AM", "9/27/19 12:00 PM", "9/27/19 1:00 PM", "9/27/19 2:00 PM", "9/27/19 3:00 PM", "9/27/19 4:00 PM", "9/27/19 5:00 PM", "9/27/19 6:00 PM", "9/27/19 7:00 PM", "9/27/19 8:00 PM", "9/27/19 9:00 PM", "9/27/19 10:00 PM", "9/27/19 11:00 PM", "9/28/19 12:00 AM", "9/28/19 1:00 AM", "9/28/19 2:00 AM", "9/28/19 3:00 AM", "9/28/19 4:00 AM", "9/28/19 5:00 AM", "9/28/19 6:00 AM", "9/28/19 7:00 AM", "9/28/19 8:00 AM", "9/28/19 9:00 AM", "9/28/19 10:00 AM", "9/28/19 11:00 AM", "9/28/19 12:00 PM", "9/28/19 1:00 PM", "9/28/19 2:00 PM", "9/28/19 3:00 PM", "9/28/19 4:00 PM", "9/28/19 5:00 PM", "9/28/19 6:00 PM", "9/28/19 7:00 PM", "9/28/19 8:00 PM", "9/28/19 9:00 PM", "9/28/19 10:00 PM", "9/28/19 11:00 PM", "9/29/19 12:00 AM", "9/29/19 1:00 AM", "9/29/19 2:00 AM", "9/29/19 3:00 AM", "9/29/19 4:00 AM", "9/29/19 5:00 AM", "9/29/19 6:00 AM", "9/29/19 7:00 AM", "9/29/19 8:00 AM", "9/29/19 9:00 AM", "9/29/19 10:00 AM", "9/29/19 11:00 AM", "9/29/19 12:00 PM", "9/29/19 1:00 PM", "9/29/19 2:00 PM", "9/29/19 3:00 PM", "9/29/19 4:00 PM", "9/29/19 5:00 PM", "9/29/19 6:00 PM", "9/29/19 7:00 PM", "9/29/19 8:00 PM", "9/29/19 9:00 PM", "9/29/19 10:00 PM", "9/29/19 11:00 PM", "9/30/19 12:00 AM", "9/30/19 1:00 AM", "9/30/19 2:00 AM", "9/30/19 3:00 AM", "9/30/19 4:00 AM", "9/30/19 5:00 AM", "9/30/19 6:00 AM", "9/30/19 7:00 AM", "9/30/19 8:00 AM", "9/30/19 9:00 AM", "9/30/19 10:00 AM", "9/30/19 11:00 AM", "9/30/19 12:00 PM", "9/30/19 1:00 PM", "9/30/19 2:00 PM", "9/30/19 3:00 PM", "9/30/19 4:00 PM", "9/30/19 5:00 PM", "9/30/19 6:00 PM", "9/30/19 7:00 PM", "9/30/19 8:00 PM", "9/30/19 9:00 PM", "9/30/19 10:00 PM", "9/30/19 11:00 PM", "10/1/19 12:00 AM", "10/1/19 1:00 AM", "10/1/19 2:00 AM", "10/1/19 3:00 AM", "10/1/19 4:00 AM", "10/1/19 5:00 AM", "10/1/19 6:00 AM", "10/1/19 7:00 AM", "10/1/19 8:00 AM", "10/1/19 9:00 AM", "10/1/19 10:00 AM", "10/1/19 11:00 AM", "10/1/19 12:00 PM", "10/1/19 1:00 PM", "10/1/19 2:00 PM", "10/1/19 3:00 PM", "10/1/19 4:00 PM", "10/1/19 5:00 PM", "10/1/19 6:00 PM", "10/1/19 7:00 PM", "10/1/19 8:00 PM", "10/1/19 9:00 PM", "10/1/19 10:00 PM", "10/1/19 11:00 PM", "10/2/19 12:00 AM", "10/2/19 1:00 AM", "10/2/19 2:00 AM", "10/2/19 3:00 AM", "10/2/19 4:00 AM", "10/2/19 5:00 AM", "10/2/19 6:00 AM", "10/2/19 7:00 AM", "10/2/19 8:00 AM", "10/2/19 9:00 AM", "10/2/19 10:00 AM", "10/2/19 11:00 AM", "10/2/19 12:00 PM", "10/2/19 1:00 PM", "10/2/19 2:00 PM", "10/2/19 3:00 PM", "10/2/19 4:00 PM", "10/2/19 5:00 PM", "10/2/19 6:00 PM", "10/2/19 7:00 PM", "10/2/19 8:00 PM", "10/2/19 9:00 PM", "10/2/19 10:00 PM", "10/2/19 11:00 PM", "10/3/19 12:00 AM", "10/3/19 1:00 AM", "10/3/19 2:00 AM", "10/3/19 3:00 AM", "10/3/19 4:00 AM", "10/3/19 5:00 AM", "10/3/19 6:00 AM", "10/3/19 7:00 AM", "10/3/19 8:00 AM", "10/3/19 9:00 AM", "10/3/19 10:00 AM", "10/3/19 11:00 AM", "10/3/19 12:00 PM", "10/3/19 1:00 PM", "10/3/19 2:00 PM", "10/3/19 3:00 PM", "10/3/19 4:00 PM", "10/3/19 5:00 PM", "10/3/19 6:00 PM", "10/3/19 7:00 PM", "10/3/19 8:00 PM", "10/3/19 9:00 PM", "10/3/19 10:00 PM", "10/3/19 11:00 PM", "10/4/19 12:00 AM", "10/4/19 1:00 AM", "10/4/19 2:00 AM", "10/4/19 3:00 AM", "10/4/19 4:00 AM", "10/4/19 5:00 AM", "10/4/19 6:00 AM", "10/4/19 7:00 AM", "10/4/19 8:00 AM", "10/4/19 9:00 AM", "10/4/19 10:00 AM", "10/4/19 11:00 AM", "10/4/19 12:00 PM", "10/4/19 1:00 PM", "10/4/19 2:00 PM", "10/4/19 3:00 PM", "10/4/19 4:00 PM", "10/4/19 5:00 PM", "10/4/19 6:00 PM", "10/4/19 7:00 PM", "10/4/19 8:00 PM", "10/4/19 9:00 PM", "10/4/19 10:00 PM", "10/4/19 11:00 PM", "10/5/19 12:00 AM", "10/5/19 1:00 AM", "10/5/19 2:00 AM", "10/5/19 3:00 AM", "10/5/19 4:00 AM", "10/5/19 5:00 AM", "10/5/19 6:00 AM", "10/5/19 7:00 AM", "10/5/19 8:00 AM", "10/5/19 9:00 AM", "10/5/19 10:00 AM", "10/5/19 11:00 AM", "10/5/19 12:00 PM", "10/5/19 1:00 PM", "10/5/19 2:00 PM", "10/5/19 3:00 PM", "10/5/19 4:00 PM", "10/5/19 5:00 PM", "10/5/19 6:00 PM", "10/5/19 7:00 PM", "10/5/19 8:00 PM", "10/5/19 9:00 PM", "10/5/19 10:00 PM", "10/5/19 11:00 PM", "10/6/19 12:00 AM", "10/6/19 1:00 AM", "10/6/19 2:00 AM", "10/6/19 3:00 AM", "10/6/19 4:00 AM", "10/6/19 5:00 AM", "10/6/19 6:00 AM", "10/6/19 7:00 AM", "10/6/19 8:00 AM", "10/6/19 9:00 AM", "10/6/19 10:00 AM", "10/6/19 11:00 AM", "10/6/19 12:00 PM", "10/6/19 1:00 PM", "10/6/19 2:00 PM", "10/6/19 3:00 PM", "10/6/19 4:00 PM", "10/6/19 5:00 PM", "10/6/19 6:00 PM", "10/6/19 7:00 PM", "10/6/19 8:00 PM", "10/6/19 9:00 PM", "10/6/19 10:00 PM", "10/6/19 11:00 PM", "10/7/19 12:00 AM", "10/7/19 1:00 AM", "10/7/19 2:00 AM", "10/7/19 3:00 AM", "10/7/19 4:00 AM", "10/7/19 5:00 AM", "10/7/19 6:00 AM", "10/7/19 7:00 AM", "10/7/19 8:00 AM", "10/7/19 9:00 AM", "10/7/19 10:00 AM", "10/7/19 11:00 AM", "10/7/19 12:00 PM", "10/7/19 1:00 PM", "10/7/19 2:00 PM", "10/7/19 3:00 PM", "10/7/19 4:00 PM", "10/7/19 5:00 PM", "10/7/19 6:00 PM", "10/7/19 7:00 PM", "10/7/19 8:00 PM", "10/7/19 9:00 PM", "10/7/19 10:00 PM", "10/7/19 11:00 PM", "10/8/19 12:00 AM", "10/8/19 1:00 AM", "10/8/19 2:00 AM", "10/8/19 3:00 AM", "10/8/19 4:00 AM", "10/8/19 5:00 AM", "10/8/19 6:00 AM", "10/8/19 7:00 AM", "10/8/19 8:00 AM", "10/8/19 9:00 AM", "10/8/19 10:00 AM", "10/8/19 11:00 AM", "10/8/19 12:00 PM", "10/8/19 1:00 PM", "10/8/19 2:00 PM", "10/8/19 3:00 PM", "10/8/19 4:00 PM", "10/8/19 5:00 PM", "10/8/19 6:00 PM", "10/8/19 7:00 PM", "10/8/19 8:00 PM", "10/8/19 9:00 PM", "10/8/19 10:00 PM", "10/8/19 11:00 PM", "10/9/19 12:00 AM", "10/9/19 1:00 AM", "10/9/19 2:00 AM", "10/9/19 3:00 AM", "10/9/19 4:00 AM", "10/9/19 5:00 AM", "10/9/19 6:00 AM", "10/9/19 7:00 AM", "10/9/19 8:00 AM", "10/9/19 9:00 AM", "10/9/19 10:00 AM", "10/9/19 11:00 AM", "10/9/19 12:00 PM", "10/9/19 1:00 PM", "10/9/19 2:00 PM", "10/9/19 3:00 PM", "10/9/19 4:00 PM", "10/9/19 5:00 PM", "10/9/19 6:00 PM", "10/9/19 7:00 PM", "10/9/19 8:00 PM", "10/9/19 9:00 PM", "10/9/19 10:00 PM", "10/9/19 11:00 PM", "10/10/19 12:00 AM", "10/10/19 1:00 AM", "10/10/19 2:00 AM", "10/10/19 3:00 AM", "10/10/19 4:00 AM", "10/10/19 5:00 AM", "10/10/19 6:00 AM", "10/10/19 7:00 AM", "10/10/19 8:00 AM", "10/10/19 9:00 AM", "10/10/19 10:00 AM", "10/10/19 11:00 AM", "10/10/19 12:00 PM", "10/10/19 1:00 PM", "10/10/19 2:00 PM", "10/10/19 3:00 PM", "10/10/19 4:00 PM", "10/10/19 5:00 PM", "10/10/19 6:00 PM", "10/10/19 7:00 PM", "10/10/19 8:00 PM", "10/10/19 9:00 PM", "10/10/19 10:00 PM", "10/10/19 11:00 PM", "10/11/19 12:00 AM", "10/11/19 1:00 AM", "10/11/19 2:00 AM", "10/11/19 3:00 AM", "10/11/19 4:00 AM", "10/11/19 5:00 AM", "10/11/19 6:00 AM", "10/11/19 7:00 AM", "10/11/19 8:00 AM", "10/11/19 9:00 AM", "10/11/19 10:00 AM", "10/11/19 11:00 AM", "10/11/19 12:00 PM", "10/11/19 1:00 PM", "10/11/19 2:00 PM", "10/11/19 3:00 PM", "10/11/19 4:00 PM", "10/11/19 5:00 PM", "10/11/19 6:00 PM", "10/11/19 7:00 PM", "10/11/19 8:00 PM", "10/11/19 9:00 PM", "10/11/19 10:00 PM", "10/11/19 11:00 PM", "10/12/19 12:00 AM", "10/12/19 1:00 AM", "10/12/19 2:00 AM", "10/12/19 3:00 AM", "10/12/19 4:00 AM", "10/12/19 5:00 AM", "10/12/19 6:00 AM", "10/12/19 7:00 AM", "10/12/19 8:00 AM", "10/12/19 9:00 AM", "10/12/19 10:00 AM", "10/12/19 11:00 AM", "10/12/19 12:00 PM", "10/12/19 1:00 PM", "10/12/19 2:00 PM", "10/12/19 3:00 PM", "10/12/19 4:00 PM", "10/12/19 5:00 PM", "10/12/19 6:00 PM", "10/12/19 7:00 PM", "10/12/19 8:00 PM", "10/12/19 9:00 PM", "10/12/19 10:00 PM", "10/12/19 11:00 PM", "10/13/19 12:00 AM", "10/13/19 1:00 AM", "10/13/19 2:00 AM", "10/13/19 3:00 AM", "10/13/19 4:00 AM", "10/13/19 5:00 AM", "10/13/19 6:00 AM", "10/13/19 7:00 AM", "10/13/19 8:00 AM", "10/13/19 9:00 AM", "10/13/19 10:00 AM", "10/13/19 11:00 AM", "10/13/19 12:00 PM", "10/13/19 1:00 PM", "10/13/19 2:00 PM", "10/13/19 3:00 PM", "10/13/19 4:00 PM", "10/13/19 5:00 PM", "10/13/19 6:00 PM", "10/13/19 7:00 PM", "10/13/19 8:00 PM", "10/13/19 9:00 PM", "10/13/19 10:00 PM", "10/13/19 11:00 PM", "10/14/19 12:00 AM", "10/14/19 1:00 AM", "10/14/19 2:00 AM", "10/14/19 3:00 AM", "10/14/19 4:00 AM", "10/14/19 5:00 AM", "10/14/19 6:00 AM", "10/14/19 7:00 AM", "10/14/19 8:00 AM", "10/14/19 9:00 AM", "10/14/19 10:00 AM", "10/14/19 11:00 AM", "10/14/19 12:00 PM", "10/14/19 1:00 PM", "10/14/19 2:00 PM", "10/14/19 3:00 PM", "10/14/19 4:00 PM", "10/14/19 5:00 PM", "10/14/19 6:00 PM", "10/14/19 7:00 PM", "10/14/19 8:00 PM", "10/14/19 9:00 PM", "10/14/19 10:00 PM", "10/14/19 11:00 PM", "10/15/19 12:00 AM", "10/15/19 1:00 AM", "10/15/19 2:00 AM", "10/15/19 3:00 AM", "10/15/19 4:00 AM", "10/15/19 5:00 AM", "10/15/19 6:00 AM", "10/15/19 7:00 AM", "10/15/19 8:00 AM", "10/15/19 9:00 AM", "10/15/19 10:00 AM", "10/15/19 11:00 AM", "10/15/19 12:00 PM", "10/15/19 1:00 PM", "10/15/19 2:00 PM", "10/15/19 3:00 PM", "10/15/19 4:00 PM", "10/15/19 5:00 PM", "10/15/19 6:00 PM", "10/15/19 7:00 PM", "10/15/19 8:00 PM", "10/15/19 9:00 PM", "10/15/19 10:00 PM", "10/15/19 11:00 PM", "10/16/19 12:00 AM", "10/16/19 1:00 AM", "10/16/19 2:00 AM", "10/16/19 3:00 AM", "10/16/19 4:00 AM", "10/16/19 5:00 AM", "10/16/19 6:00 AM", "10/16/19 7:00 AM", "10/16/19 8:00 AM", "10/16/19 9:00 AM", "10/16/19 10:00 AM", "10/16/19 11:00 AM", "10/16/19 12:00 PM", "10/16/19 1:00 PM", "10/16/19 2:00 PM", "10/16/19 3:00 PM", "10/16/19 4:00 PM", "10/16/19 5:00 PM", "10/16/19 6:00 PM", "10/16/19 7:00 PM", "10/16/19 8:00 PM", "10/16/19 9:00 PM", "10/16/19 10:00 PM", "10/16/19 11:00 PM", "10/17/19 12:00 AM", "10/17/19 1:00 AM", "10/17/19 2:00 AM", "10/17/19 3:00 AM", "10/17/19 4:00 AM", "10/17/19 5:00 AM", "10/17/19 6:00 AM", "10/17/19 7:00 AM", "10/17/19 8:00 AM", "10/17/19 9:00 AM", "10/17/19 10:00 AM", "10/17/19 11:00 AM", "10/17/19 12:00 PM", "10/17/19 1:00 PM", "10/17/19 2:00 PM", "10/17/19 3:00 PM", "10/17/19 4:00 PM", "10/17/19 5:00 PM", "10/17/19 6:00 PM", "10/17/19 7:00 PM", "10/17/19 8:00 PM", "10/17/19 9:00 PM", "10/17/19 10:00 PM", "10/17/19 11:00 PM", "10/18/19 12:00 AM", "10/18/19 1:00 AM", "10/18/19 2:00 AM", "10/18/19 3:00 AM", "10/18/19 4:00 AM", "10/18/19 5:00 AM", "10/18/19 6:00 AM", "10/18/19 7:00 AM", "10/18/19 8:00 AM", "10/18/19 9:00 AM", "10/18/19 10:00 AM", "10/18/19 11:00 AM", "10/18/19 12:00 PM", "10/18/19 1:00 PM", "10/18/19 2:00 PM", "10/18/19 3:00 PM", "10/18/19 4:00 PM", "10/18/19 5:00 PM", "10/18/19 6:00 PM", "10/18/19 7:00 PM", "10/18/19 8:00 PM", "10/18/19 9:00 PM", "10/18/19 10:00 PM", "10/18/19 11:00 PM", "10/19/19 12:00 AM", "10/19/19 1:00 AM", "10/19/19 2:00 AM", "10/19/19 3:00 AM", "10/19/19 4:00 AM", "10/19/19 5:00 AM", "10/19/19 6:00 AM", "10/19/19 7:00 AM", "10/19/19 8:00 AM", "10/19/19 9:00 AM", "10/19/19 10:00 AM", "10/19/19 11:00 AM", "10/19/19 12:00 PM", "10/19/19 1:00 PM", "10/19/19 2:00 PM", "10/19/19 3:00 PM", "10/19/19 4:00 PM", "10/19/19 5:00 PM", "10/19/19 6:00 PM", "10/19/19 7:00 PM", "10/19/19 8:00 PM", "10/19/19 9:00 PM", "10/19/19 10:00 PM", "10/19/19 11:00 PM", "10/20/19 12:00 AM", "10/20/19 1:00 AM", "10/20/19 2:00 AM", "10/20/19 3:00 AM", "10/20/19 4:00 AM", "10/20/19 5:00 AM", "10/20/19 6:00 AM", "10/20/19 7:00 AM", "10/20/19 8:00 AM", "10/20/19 9:00 AM", "10/20/19 10:00 AM", "10/20/19 11:00 AM", "10/20/19 12:00 PM", "10/20/19 1:00 PM", "10/20/19 2:00 PM", "10/20/19 3:00 PM", "10/20/19 4:00 PM", "10/20/19 5:00 PM", "10/20/19 6:00 PM", "10/20/19 7:00 PM", "10/20/19 8:00 PM", "10/20/19 9:00 PM", "10/20/19 10:00 PM", "10/20/19 11:00 PM", "10/21/19 12:00 AM", "10/21/19 1:00 AM", "10/21/19 2:00 AM", "10/21/19 3:00 AM", "10/21/19 4:00 AM", "10/21/19 5:00 AM", "10/21/19 6:00 AM", "10/21/19 7:00 AM", "10/21/19 8:00 AM", "10/21/19 9:00 AM", "10/21/19 10:00 AM", "10/21/19 11:00 AM", "10/21/19 12:00 PM", "10/21/19 1:00 PM", "10/21/19 2:00 PM", "10/21/19 3:00 PM", "10/21/19 4:00 PM", "10/21/19 5:00 PM", "10/21/19 6:00 PM", "10/21/19 7:00 PM", "10/21/19 8:00 PM", "10/21/19 9:00 PM", "10/21/19 10:00 PM", "10/21/19 11:00 PM", "10/22/19 12:00 AM", "10/22/19 1:00 AM", "10/22/19 2:00 AM", "10/22/19 3:00 AM", "10/22/19 4:00 AM", "10/22/19 5:00 AM", "10/22/19 6:00 AM", "10/22/19 7:00 AM", "10/22/19 8:00 AM", "10/22/19 9:00 AM", "10/22/19 10:00 AM", "10/22/19 11:00 AM", "10/22/19 12:00 PM", "10/22/19 1:00 PM", "10/22/19 2:00 PM", "10/22/19 3:00 PM", "10/22/19 4:00 PM", "10/22/19 5:00 PM", "10/22/19 6:00 PM", "10/22/19 7:00 PM", "10/22/19 8:00 PM", "10/22/19 9:00 PM", "10/22/19 10:00 PM", "10/22/19 11:00 PM", "10/23/19 12:00 AM", "10/23/19 1:00 AM", "10/23/19 2:00 AM", "10/23/19 3:00 AM", "10/23/19 4:00 AM", "10/23/19 5:00 AM", "10/23/19 6:00 AM", "10/23/19 7:00 AM", "10/23/19 8:00 AM", "10/23/19 9:00 AM", "10/23/19 10:00 AM", "10/23/19 11:00 AM", "10/23/19 12:00 PM", "10/23/19 1:00 PM", "10/23/19 2:00 PM", "10/23/19 3:00 PM", "10/23/19 4:00 PM", "10/23/19 5:00 PM", "10/23/19 6:00 PM", "10/23/19 7:00 PM", "10/23/19 8:00 PM", "10/23/19 9:00 PM", "10/23/19 10:00 PM", "10/23/19 11:00 PM", "10/24/19 12:00 AM", "10/24/19 1:00 AM", "10/24/19 2:00 AM", "10/24/19 3:00 AM", "10/24/19 4:00 AM", "10/24/19 5:00 AM", "10/24/19 6:00 AM", "10/24/19 7:00 AM", "10/24/19 8:00 AM", "10/24/19 9:00 AM", "10/24/19 10:00 AM", "10/24/19 11:00 AM", "10/24/19 12:00 PM", "10/24/19 1:00 PM", "10/24/19 2:00 PM", "10/24/19 3:00 PM", "10/24/19 4:00 PM", "10/24/19 5:00 PM", "10/24/19 6:00 PM", "10/24/19 7:00 PM", "10/24/19 8:00 PM", "10/24/19 9:00 PM", "10/24/19 10:00 PM", "10/24/19 11:00 PM", "10/25/19 12:00 AM", "10/25/19 1:00 AM", "10/25/19 2:00 AM", "10/25/19 3:00 AM", "10/25/19 4:00 AM", "10/25/19 5:00 AM", "10/25/19 6:00 AM", "10/25/19 7:00 AM", "10/25/19 8:00 AM", "10/25/19 9:00 AM", "10/25/19 10:00 AM", "10/25/19 11:00 AM", "10/25/19 12:00 PM", "10/25/19 1:00 PM", "10/25/19 2:00 PM", "10/25/19 3:00 PM", "10/25/19 4:00 PM", "10/25/19 5:00 PM", "10/25/19 6:00 PM", "10/25/19 7:00 PM", "10/25/19 8:00 PM", "10/25/19 9:00 PM", "10/25/19 10:00 PM", "10/25/19 11:00 PM", "10/26/19 12:00 AM", "10/26/19 1:00 AM", "10/26/19 2:00 AM", "10/26/19 3:00 AM", "10/26/19 4:00 AM", "10/26/19 5:00 AM", "10/26/19 6:00 AM", "10/26/19 7:00 AM", "10/26/19 8:00 AM", "10/26/19 9:00 AM", "10/26/19 10:00 AM", "10/26/19 11:00 AM", "10/26/19 12:00 PM", "10/26/19 1:00 PM", "10/26/19 2:00 PM", "10/26/19 3:00 PM", "10/26/19 4:00 PM", "10/26/19 5:00 PM", "10/26/19 6:00 PM", "10/26/19 7:00 PM", "10/26/19 8:00 PM", "10/26/19 9:00 PM", "10/26/19 10:00 PM", "10/26/19 11:00 PM", "10/27/19 12:00 AM", "10/27/19 1:00 AM", "10/27/19 2:00 AM", "10/27/19 3:00 AM", "10/27/19 4:00 AM", "10/27/19 5:00 AM", "10/27/19 6:00 AM", "10/27/19 7:00 AM", "10/27/19 8:00 AM", "10/27/19 9:00 AM", "10/27/19 10:00 AM", "10/27/19 11:00 AM", "10/27/19 12:00 PM", "10/27/19 1:00 PM", "10/27/19 2:00 PM", "10/27/19 3:00 PM", "10/27/19 4:00 PM", "10/27/19 5:00 PM", "10/27/19 6:00 PM", "10/27/19 7:00 PM", "10/27/19 8:00 PM", "10/27/19 9:00 PM", "10/27/19 10:00 PM", "10/27/19 11:00 PM", "10/28/19 12:00 AM", "10/28/19 1:00 AM", "10/28/19 2:00 AM", "10/28/19 3:00 AM", "10/28/19 4:00 AM", "10/28/19 5:00 AM", "10/28/19 6:00 AM", "10/28/19 7:00 AM", "10/28/19 8:00 AM", "10/28/19 9:00 AM", "10/28/19 10:00 AM", "10/28/19 11:00 AM", "10/28/19 12:00 PM", "10/28/19 1:00 PM", "10/28/19 2:00 PM", "10/28/19 3:00 PM", "10/28/19 4:00 PM", "10/28/19 5:00 PM", "10/28/19 6:00 PM", "10/28/19 7:00 PM", "10/28/19 8:00 PM", "10/28/19 9:00 PM", "10/28/19 10:00 PM", "10/28/19 11:00 PM", "10/29/19 12:00 AM", "10/29/19 1:00 AM", "10/29/19 2:00 AM", "10/29/19 3:00 AM", "10/29/19 4:00 AM", "10/29/19 5:00 AM", "10/29/19 6:00 AM", "10/29/19 7:00 AM", "10/29/19 8:00 AM", "10/29/19 9:00 AM", "10/29/19 10:00 AM", "10/29/19 11:00 AM", "10/29/19 12:00 PM", "10/29/19 1:00 PM", "10/29/19 2:00 PM", "10/29/19 3:00 PM", "10/29/19 4:00 PM", "10/29/19 5:00 PM", "10/29/19 6:00 PM", "10/29/19 7:00 PM", "10/29/19 8:00 PM", "10/29/19 9:00 PM", "10/29/19 10:00 PM", "10/29/19 11:00 PM", "10/30/19 12:00 AM", "10/30/19 1:00 AM", "10/30/19 2:00 AM", "10/30/19 3:00 AM", "10/30/19 4:00 AM", "10/30/19 5:00 AM", "10/30/19 6:00 AM", "10/30/19 7:00 AM", "10/30/19 8:00 AM", "10/30/19 9:00 AM", "10/30/19 10:00 AM", "10/30/19 11:00 AM", "10/30/19 12:00 PM", "10/30/19 1:00 PM", "10/30/19 2:00 PM", "10/30/19 3:00 PM", "10/30/19 4:00 PM", "10/30/19 5:00 PM", "10/30/19 6:00 PM", "10/30/19 7:00 PM", "10/30/19 8:00 PM", "10/30/19 9:00 PM", "10/30/19 10:00 PM", "10/30/19 11:00 PM", "10/31/19 12:00 AM", "10/31/19 1:00 AM", "10/31/19 2:00 AM", "10/31/19 3:00 AM", "10/31/19 4:00 AM", "10/31/19 5:00 AM", "10/31/19 6:00 AM", "10/31/19 7:00 AM", "10/31/19 8:00 AM", "10/31/19 9:00 AM", "10/31/19 10:00 AM", "10/31/19 11:00 AM", "10/31/19 12:00 PM", "10/31/19 1:00 PM", "10/31/19 2:00 PM", "10/31/19 3:00 PM", "10/31/19 4:00 PM", "10/31/19 5:00 PM", "10/31/19 6:00 PM", "10/31/19 7:00 PM", "10/31/19 8:00 PM", "10/31/19 9:00 PM", "10/31/19 10:00 PM", "10/31/19 11:00 PM", "11/1/19 12:00 AM", "11/1/19 1:00 AM", "11/1/19 2:00 AM", "11/1/19 3:00 AM", "11/1/19 4:00 AM", "11/1/19 5:00 AM", "11/1/19 6:00 AM", "11/1/19 7:00 AM", "11/1/19 8:00 AM", "11/1/19 9:00 AM", "11/1/19 10:00 AM", "11/1/19 11:00 AM", "11/1/19 12:00 PM", "11/1/19 1:00 PM", "11/1/19 2:00 PM", "11/1/19 3:00 PM", "11/1/19 4:00 PM", "11/1/19 5:00 PM", "11/1/19 6:00 PM", "11/1/19 7:00 PM", "11/1/19 8:00 PM", "11/1/19 9:00 PM", "11/1/19 10:00 PM", "11/1/19 11:00 PM", "11/2/19 12:00 AM", "11/2/19 1:00 AM", "11/2/19 2:00 AM", "11/2/19 3:00 AM", "11/2/19 4:00 AM", "11/2/19 5:00 AM", "11/2/19 6:00 AM", "11/2/19 7:00 AM", "11/2/19 8:00 AM", "11/2/19 9:00 AM", "11/2/19 10:00 AM", "11/2/19 11:00 AM", "11/2/19 12:00 PM", "11/2/19 1:00 PM", "11/2/19 2:00 PM", "11/2/19 3:00 PM", "11/2/19 4:00 PM", "11/2/19 5:00 PM", "11/2/19 6:00 PM", "11/2/19 7:00 PM", "11/2/19 8:00 PM", "11/2/19 9:00 PM", "11/2/19 10:00 PM", "11/2/19 11:00 PM", "11/3/19 12:00 AM", "11/3/19 1:00 AM", "11/3/19 2:00 AM", "11/3/19 3:00 AM", "11/3/19 4:00 AM", "11/3/19 5:00 AM", "11/3/19 6:00 AM", "11/3/19 7:00 AM", "11/3/19 8:00 AM", "11/3/19 9:00 AM", "11/3/19 10:00 AM", "11/3/19 11:00 AM", "11/3/19 12:00 PM", "11/3/19 1:00 PM", "11/3/19 2:00 PM", "11/3/19 3:00 PM", "11/3/19 4:00 PM", "11/3/19 5:00 PM", "11/3/19 6:00 PM", "11/3/19 7:00 PM", "11/3/19 8:00 PM", "11/3/19 9:00 PM", "11/3/19 10:00 PM", "11/3/19 11:00 PM", "11/4/19 12:00 AM", "11/4/19 1:00 AM", "11/4/19 2:00 AM", "11/4/19 3:00 AM", "11/4/19 4:00 AM", "11/4/19 5:00 AM", "11/4/19 6:00 AM", "11/4/19 7:00 AM", "11/4/19 8:00 AM", "11/4/19 9:00 AM", "11/4/19 10:00 AM", "11/4/19 11:00 AM", "11/4/19 12:00 PM", "11/4/19 1:00 PM", "11/4/19 2:00 PM", "11/4/19 3:00 PM", "11/4/19 4:00 PM", "11/4/19 5:00 PM", "11/4/19 6:00 PM", "11/4/19 7:00 PM", "11/4/19 8:00 PM", "11/4/19 9:00 PM", "11/4/19 10:00 PM", "11/4/19 11:00 PM", "11/5/19 12:00 AM", "11/5/19 1:00 AM", "11/5/19 2:00 AM", "11/5/19 3:00 AM", "11/5/19 4:00 AM", "11/5/19 5:00 AM", "11/5/19 6:00 AM", "11/5/19 7:00 AM", "11/5/19 8:00 AM", "11/5/19 9:00 AM", "11/5/19 10:00 AM", "11/5/19 11:00 AM", "11/5/19 12:00 PM", "11/5/19 1:00 PM", "11/5/19 2:00 PM", "11/5/19 3:00 PM", "11/5/19 4:00 PM", "11/5/19 5:00 PM", "11/5/19 6:00 PM", "11/5/19 7:00 PM", "11/5/19 8:00 PM", "11/5/19 9:00 PM", "11/5/19 10:00 PM", "11/5/19 11:00 PM", "11/6/19 12:00 AM", "11/6/19 1:00 AM", "11/6/19 2:00 AM", "11/6/19 3:00 AM", "11/6/19 4:00 AM", "11/6/19 5:00 AM", "11/6/19 6:00 AM", "11/6/19 7:00 AM", "11/6/19 8:00 AM", "11/6/19 9:00 AM", "11/6/19 10:00 AM", "11/6/19 11:00 AM", "11/6/19 12:00 PM", "11/6/19 1:00 PM", "11/6/19 2:00 PM", "11/6/19 3:00 PM", "11/6/19 4:00 PM", "11/6/19 5:00 PM", "11/6/19 6:00 PM", "11/6/19 7:00 PM", "11/6/19 8:00 PM", "11/6/19 9:00 PM", "11/6/19 10:00 PM", "11/6/19 11:00 PM", "11/7/19 12:00 AM", "11/7/19 1:00 AM", "11/7/19 2:00 AM", "11/7/19 3:00 AM", "11/7/19 4:00 AM", "11/7/19 5:00 AM", "11/7/19 6:00 AM", "11/7/19 7:00 AM", "11/7/19 8:00 AM", "11/7/19 9:00 AM", "11/7/19 10:00 AM", "11/7/19 11:00 AM", "11/7/19 12:00 PM", "11/7/19 1:00 PM", "11/7/19 2:00 PM", "11/7/19 3:00 PM", "11/7/19 4:00 PM", "11/7/19 5:00 PM", "11/7/19 6:00 PM", "11/7/19 7:00 PM", "11/7/19 8:00 PM", "11/7/19 9:00 PM", "11/7/19 10:00 PM", "11/7/19 11:00 PM", "11/8/19 12:00 AM", "11/8/19 1:00 AM", "11/8/19 2:00 AM", "11/8/19 3:00 AM", "11/8/19 4:00 AM", "11/8/19 5:00 AM", "11/8/19 6:00 AM", "11/8/19 7:00 AM", "11/8/19 8:00 AM", "11/8/19 9:00 AM", "11/8/19 10:00 AM", "11/8/19 11:00 AM", "11/8/19 12:00 PM", "11/8/19 1:00 PM", "11/8/19 2:00 PM", "11/8/19 3:00 PM", "11/8/19 4:00 PM", "11/8/19 5:00 PM", "11/8/19 6:00 PM", "11/8/19 7:00 PM", "11/8/19 8:00 PM", "11/8/19 9:00 PM", "11/8/19 10:00 PM", "11/8/19 11:00 PM", "11/9/19 12:00 AM", "11/9/19 1:00 AM", "11/9/19 2:00 AM", "11/9/19 3:00 AM", "11/9/19 4:00 AM", "11/9/19 5:00 AM", "11/9/19 6:00 AM", "11/9/19 7:00 AM", "11/9/19 8:00 AM", "11/9/19 9:00 AM", "11/9/19 10:00 AM", "11/9/19 11:00 AM", "11/9/19 12:00 PM", "11/9/19 1:00 PM", "11/9/19 2:00 PM", "11/9/19 3:00 PM", "11/9/19 4:00 PM", "11/9/19 5:00 PM", "11/9/19 6:00 PM", "11/9/19 7:00 PM", "11/9/19 8:00 PM", "11/9/19 9:00 PM", "11/9/19 10:00 PM", "11/9/19 11:00 PM", "11/10/19 12:00 AM", "11/10/19 1:00 AM", "11/10/19 2:00 AM", "11/10/19 3:00 AM", "11/10/19 4:00 AM", "11/10/19 5:00 AM", "11/10/19 6:00 AM", "11/10/19 7:00 AM", "11/10/19 8:00 AM", "11/10/19 9:00 AM", "11/10/19 10:00 AM", "11/10/19 11:00 AM", "11/10/19 12:00 PM", "11/10/19 1:00 PM", "11/10/19 2:00 PM", "11/10/19 3:00 PM", "11/10/19 4:00 PM", "11/10/19 5:00 PM", "11/10/19 6:00 PM", "11/10/19 7:00 PM", "11/10/19 8:00 PM", "11/10/19 9:00 PM", "11/10/19 10:00 PM", "11/10/19 11:00 PM", "11/11/19 12:00 AM", "11/11/19 1:00 AM", "11/11/19 2:00 AM", "11/11/19 3:00 AM", "11/11/19 4:00 AM", "11/11/19 5:00 AM", "11/11/19 6:00 AM", "11/11/19 7:00 AM", "11/11/19 8:00 AM", "11/11/19 9:00 AM", "11/11/19 10:00 AM", "11/11/19 11:00 AM", "11/11/19 12:00 PM", "11/11/19 1:00 PM", "11/11/19 2:00 PM", "11/11/19 3:00 PM", "11/11/19 4:00 PM", "11/11/19 5:00 PM", "11/11/19 6:00 PM", "11/11/19 7:00 PM", "11/11/19 8:00 PM", "11/11/19 9:00 PM", "11/11/19 10:00 PM", "11/11/19 11:00 PM", "11/12/19 12:00 AM", "11/12/19 1:00 AM", "11/12/19 2:00 AM", "11/12/19 3:00 AM", "11/12/19 4:00 AM", "11/12/19 5:00 AM", "11/12/19 6:00 AM", "11/12/19 7:00 AM", "11/12/19 8:00 AM", "11/12/19 9:00 AM", "11/12/19 10:00 AM", "11/12/19 11:00 AM", "11/12/19 12:00 PM", "11/12/19 1:00 PM", "11/12/19 2:00 PM", "11/12/19 3:00 PM", "11/12/19 4:00 PM", "11/12/19 5:00 PM", "11/12/19 6:00 PM", "11/12/19 7:00 PM", "11/12/19 8:00 PM", "11/12/19 9:00 PM", "11/12/19 10:00 PM", "11/12/19 11:00 PM", "11/13/19 12:00 AM", "11/13/19 1:00 AM", "11/13/19 2:00 AM", "11/13/19 3:00 AM", "11/13/19 4:00 AM", "11/13/19 5:00 AM", "11/13/19 6:00 AM", "11/13/19 7:00 AM", "11/13/19 8:00 AM", "11/13/19 9:00 AM", "11/13/19 10:00 AM", "11/13/19 11:00 AM", "11/13/19 12:00 PM", "11/13/19 1:00 PM", "11/13/19 2:00 PM", "11/13/19 3:00 PM", "11/13/19 4:00 PM", "11/13/19 5:00 PM", "11/13/19 6:00 PM", "11/13/19 7:00 PM", "11/13/19 8:00 PM", "11/13/19 9:00 PM", "11/13/19 10:00 PM", "11/13/19 11:00 PM", "11/14/19 12:00 AM", "11/14/19 1:00 AM", "11/14/19 2:00 AM", "11/14/19 3:00 AM", "11/14/19 4:00 AM", "11/14/19 5:00 AM", "11/14/19 6:00 AM", "11/14/19 7:00 AM", "11/14/19 8:00 AM", "11/14/19 9:00 AM", "11/14/19 10:00 AM", "11/14/19 11:00 AM", "11/14/19 12:00 PM", "11/14/19 1:00 PM", "11/14/19 2:00 PM", "11/14/19 3:00 PM", "11/14/19 4:00 PM", "11/14/19 5:00 PM", "11/14/19 6:00 PM", "11/14/19 7:00 PM", "11/14/19 8:00 PM", "11/14/19 9:00 PM", "11/14/19 10:00 PM", "11/14/19 11:00 PM", "11/15/19 12:00 AM", "11/15/19 1:00 AM", "11/15/19 2:00 AM", "11/15/19 3:00 AM", "11/15/19 4:00 AM", "11/15/19 5:00 AM", "11/15/19 6:00 AM", "11/15/19 7:00 AM", "11/15/19 8:00 AM", "11/15/19 9:00 AM", "11/15/19 10:00 AM", "11/15/19 11:00 AM", "11/15/19 12:00 PM", "11/15/19 1:00 PM", "11/15/19 2:00 PM", "11/15/19 3:00 PM", "11/15/19 4:00 PM", "11/15/19 5:00 PM", "11/15/19 6:00 PM", "11/15/19 7:00 PM", "11/15/19 8:00 PM", "11/15/19 9:00 PM", "11/15/19 10:00 PM", "11/15/19 11:00 PM", "11/16/19 12:00 AM", "11/16/19 1:00 AM", "11/16/19 2:00 AM", "11/16/19 3:00 AM", "11/16/19 4:00 AM", "11/16/19 5:00 AM", "11/16/19 6:00 AM", "11/16/19 7:00 AM", "11/16/19 8:00 AM", "11/16/19 9:00 AM", "11/16/19 10:00 AM", "11/16/19 11:00 AM", "11/16/19 12:00 PM", "11/16/19 1:00 PM", "11/16/19 2:00 PM", "11/16/19 3:00 PM", "11/16/19 4:00 PM", "11/16/19 5:00 PM", "11/16/19 6:00 PM", "11/16/19 7:00 PM", "11/16/19 8:00 PM", "11/16/19 9:00 PM", "11/16/19 10:00 PM", "11/16/19 11:00 PM", "11/17/19 12:00 AM", "11/17/19 1:00 AM", "11/17/19 2:00 AM", "11/17/19 3:00 AM", "11/17/19 4:00 AM", "11/17/19 5:00 AM", "11/17/19 6:00 AM", "11/17/19 7:00 AM", "11/17/19 8:00 AM", "11/17/19 9:00 AM", "11/17/19 10:00 AM", "11/17/19 11:00 AM", "11/17/19 12:00 PM", "11/17/19 1:00 PM", "11/17/19 2:00 PM", "11/17/19 3:00 PM", "11/17/19 4:00 PM", "11/17/19 5:00 PM", "11/17/19 6:00 PM", "11/17/19 7:00 PM", "11/17/19 8:00 PM", "11/17/19 9:00 PM", "11/17/19 10:00 PM", "11/17/19 11:00 PM", "11/18/19 12:00 AM", "11/18/19 1:00 AM", "11/18/19 2:00 AM", "11/18/19 3:00 AM", "11/18/19 4:00 AM", "11/18/19 5:00 AM", "11/18/19 6:00 AM", "11/18/19 7:00 AM", "11/18/19 8:00 AM", "11/18/19 9:00 AM", "11/18/19 10:00 AM", "11/18/19 11:00 AM", "11/18/19 12:00 PM", "11/18/19 1:00 PM", "11/18/19 2:00 PM", "11/18/19 3:00 PM", "11/18/19 4:00 PM", "11/18/19 5:00 PM", "11/18/19 6:00 PM", "11/18/19 7:00 PM", "11/18/19 8:00 PM", "11/18/19 9:00 PM", "11/18/19 10:00 PM", "11/18/19 11:00 PM", "11/19/19 12:00 AM", "11/19/19 1:00 AM", "11/19/19 2:00 AM", "11/19/19 3:00 AM", "11/19/19 4:00 AM", "11/19/19 5:00 AM", "11/19/19 6:00 AM", "11/19/19 7:00 AM", "11/19/19 8:00 AM", "11/19/19 9:00 AM", "11/19/19 10:00 AM", "11/19/19 11:00 AM", "11/19/19 12:00 PM", "11/19/19 1:00 PM", "11/19/19 2:00 PM", "11/19/19 3:00 PM", "11/19/19 4:00 PM", "11/19/19 5:00 PM", "11/19/19 6:00 PM", "11/19/19 7:00 PM", "11/19/19 8:00 PM", "11/19/19 9:00 PM", "11/19/19 10:00 PM", "11/19/19 11:00 PM", "11/20/19 12:00 AM", "11/20/19 1:00 AM", "11/20/19 2:00 AM", "11/20/19 3:00 AM", "11/20/19 4:00 AM", "11/20/19 5:00 AM", "11/20/19 6:00 AM", "11/20/19 7:00 AM", "11/20/19 8:00 AM", "11/20/19 9:00 AM", "11/20/19 10:00 AM", "11/20/19 11:00 AM", "11/20/19 12:00 PM", "11/20/19 1:00 PM", "11/20/19 2:00 PM", "11/20/19 3:00 PM", "11/20/19 4:00 PM", "11/20/19 5:00 PM", "11/20/19 6:00 PM", "11/20/19 7:00 PM", "11/20/19 8:00 PM", "11/20/19 9:00 PM", "11/20/19 10:00 PM", "11/20/19 11:00 PM", "11/21/19 12:00 AM", "11/21/19 1:00 AM", "11/21/19 2:00 AM", "11/21/19 3:00 AM", "11/21/19 4:00 AM", "11/21/19 5:00 AM", "11/21/19 6:00 AM", "11/21/19 7:00 AM", "11/21/19 8:00 AM", "11/21/19 9:00 AM", "11/21/19 10:00 AM", "11/21/19 11:00 AM", "11/21/19 12:00 PM", "11/21/19 1:00 PM", "11/21/19 2:00 PM", "11/21/19 3:00 PM", "11/21/19 4:00 PM", "11/21/19 5:00 PM", "11/21/19 6:00 PM", "11/21/19 7:00 PM", "11/21/19 8:00 PM", "11/21/19 9:00 PM", "11/21/19 10:00 PM", "11/21/19 11:00 PM", "11/22/19 12:00 AM", "11/22/19 1:00 AM", "11/22/19 2:00 AM", "11/22/19 3:00 AM", "11/22/19 4:00 AM", "11/22/19 5:00 AM", "11/22/19 6:00 AM", "11/22/19 7:00 AM", "11/22/19 8:00 AM", "11/22/19 9:00 AM", "11/22/19 10:00 AM", "11/22/19 11:00 AM", "11/22/19 12:00 PM", "11/22/19 1:00 PM", "11/22/19 2:00 PM", "11/22/19 3:00 PM", "11/22/19 4:00 PM", "11/22/19 5:00 PM", "11/22/19 6:00 PM", "11/22/19 7:00 PM", "11/22/19 8:00 PM", "11/22/19 9:00 PM", "11/22/19 10:00 PM", "11/22/19 11:00 PM", "11/23/19 12:00 AM", "11/23/19 1:00 AM", "11/23/19 2:00 AM", "11/23/19 3:00 AM", "11/23/19 4:00 AM", "11/23/19 5:00 AM", "11/23/19 6:00 AM", "11/23/19 7:00 AM", "11/23/19 8:00 AM", "11/23/19 9:00 AM", "11/23/19 10:00 AM", "11/23/19 11:00 AM", "11/23/19 12:00 PM", "11/23/19 1:00 PM", "11/23/19 2:00 PM", "11/23/19 3:00 PM", "11/23/19 4:00 PM", "11/23/19 5:00 PM", "11/23/19 6:00 PM", "11/23/19 7:00 PM", "11/23/19 8:00 PM", "11/23/19 9:00 PM", "11/23/19 10:00 PM", "11/23/19 11:00 PM", "11/24/19 12:00 AM", "11/24/19 1:00 AM", "11/24/19 2:00 AM", "11/24/19 3:00 AM", "11/24/19 4:00 AM", "11/24/19 5:00 AM", "11/24/19 6:00 AM", "11/24/19 7:00 AM", "11/24/19 8:00 AM", "11/24/19 9:00 AM", "11/24/19 10:00 AM", "11/24/19 11:00 AM", "11/24/19 12:00 PM", "11/24/19 1:00 PM", "11/24/19 2:00 PM", "11/24/19 3:00 PM", "11/24/19 4:00 PM", "11/24/19 5:00 PM", "11/24/19 6:00 PM", "11/24/19 7:00 PM", "11/24/19 8:00 PM", "11/24/19 9:00 PM", "11/24/19 10:00 PM", "11/24/19 11:00 PM", "11/25/19 12:00 AM", "11/25/19 1:00 AM", "11/25/19 2:00 AM", "11/25/19 3:00 AM", "11/25/19 4:00 AM", "11/25/19 5:00 AM", "11/25/19 6:00 AM", "11/25/19 7:00 AM", "11/25/19 8:00 AM", "11/25/19 9:00 AM", "11/25/19 10:00 AM", "11/25/19 11:00 AM", "11/25/19 12:00 PM", "11/25/19 1:00 PM", "11/25/19 2:00 PM", "11/25/19 3:00 PM", "11/25/19 4:00 PM", "11/25/19 5:00 PM", "11/25/19 6:00 PM", "11/25/19 7:00 PM", "11/25/19 8:00 PM", "11/25/19 9:00 PM", "11/25/19 10:00 PM", "11/25/19 11:00 PM", "11/26/19 12:00 AM", "11/26/19 1:00 AM", "11/26/19 2:00 AM", "11/26/19 3:00 AM", "11/26/19 4:00 AM", "11/26/19 5:00 AM", "11/26/19 6:00 AM", "11/26/19 7:00 AM", "11/26/19 8:00 AM", "11/26/19 9:00 AM", "11/26/19 10:00 AM", "11/26/19 11:00 AM", "11/26/19 12:00 PM", "11/26/19 1:00 PM", "11/26/19 2:00 PM", "11/26/19 3:00 PM", "11/26/19 4:00 PM", "11/26/19 5:00 PM", "11/26/19 6:00 PM", "11/26/19 7:00 PM", "11/26/19 8:00 PM", "11/26/19 9:00 PM", "11/26/19 10:00 PM", "11/26/19 11:00 PM", "11/27/19 12:00 AM", "11/27/19 1:00 AM", "11/27/19 2:00 AM", "11/27/19 3:00 AM", "11/27/19 4:00 AM", "11/27/19 5:00 AM", "11/27/19 6:00 AM", "11/27/19 7:00 AM", "11/27/19 8:00 AM", "11/27/19 9:00 AM", "11/27/19 10:00 AM", "11/27/19 11:00 AM", "11/27/19 12:00 PM", "11/27/19 1:00 PM", "11/27/19 2:00 PM", "11/27/19 3:00 PM", "11/27/19 4:00 PM", "11/27/19 5:00 PM", "11/27/19 6:00 PM", "11/27/19 7:00 PM", "11/27/19 8:00 PM", "11/27/19 9:00 PM", "11/27/19 10:00 PM", "11/27/19 11:00 PM", "11/28/19 12:00 AM", "11/28/19 1:00 AM", "11/28/19 2:00 AM", "11/28/19 3:00 AM", "11/28/19 4:00 AM", "11/28/19 5:00 AM", "11/28/19 6:00 AM", "11/28/19 7:00 AM", "11/28/19 8:00 AM", "11/28/19 9:00 AM", "11/28/19 10:00 AM", "11/28/19 11:00 AM", "11/28/19 12:00 PM", "11/28/19 1:00 PM", "11/28/19 2:00 PM", "11/28/19 3:00 PM", "11/28/19 4:00 PM", "11/28/19 5:00 PM", "11/28/19 6:00 PM", "11/28/19 7:00 PM", "11/28/19 8:00 PM", "11/28/19 9:00 PM", "11/28/19 10:00 PM", "11/28/19 11:00 PM", "11/29/19 12:00 AM", "11/29/19 1:00 AM", "11/29/19 2:00 AM", "11/29/19 3:00 AM", "11/29/19 4:00 AM", "11/29/19 5:00 AM", "11/29/19 6:00 AM", "11/29/19 7:00 AM", "11/29/19 8:00 AM", "11/29/19 9:00 AM", "11/29/19 10:00 AM", "11/29/19 11:00 AM", "11/29/19 12:00 PM", "11/29/19 1:00 PM", "11/29/19 2:00 PM", "11/29/19 3:00 PM", "11/29/19 4:00 PM", "11/29/19 5:00 PM", "11/29/19 6:00 PM", "11/29/19 7:00 PM", "11/29/19 8:00 PM", "11/29/19 9:00 PM", "11/29/19 10:00 PM", "11/29/19 11:00 PM", "11/30/19 12:00 AM", "11/30/19 1:00 AM", "11/30/19 2:00 AM", "11/30/19 3:00 AM", "11/30/19 4:00 AM", "11/30/19 5:00 AM", "11/30/19 6:00 AM", "11/30/19 7:00 AM", "11/30/19 8:00 AM", "11/30/19 9:00 AM", "11/30/19 10:00 AM", "11/30/19 11:00 AM", "11/30/19 12:00 PM", "11/30/19 1:00 PM", "11/30/19 2:00 PM", "11/30/19 3:00 PM", "11/30/19 4:00 PM", "11/30/19 5:00 PM", "11/30/19 6:00 PM", "11/30/19 7:00 PM", "11/30/19 8:00 PM", "11/30/19 9:00 PM", "11/30/19 10:00 PM", "11/30/19 11:00 PM", "12/1/19 12:00 AM", "12/1/19 1:00 AM", "12/1/19 2:00 AM", "12/1/19 3:00 AM", "12/1/19 4:00 AM", "12/1/19 5:00 AM", "12/1/19 6:00 AM", "12/1/19 7:00 AM", "12/1/19 8:00 AM", "12/1/19 9:00 AM", "12/1/19 10:00 AM", "12/1/19 11:00 AM", "12/1/19 12:00 PM", "12/1/19 1:00 PM", "12/1/19 2:00 PM", "12/1/19 3:00 PM", "12/1/19 4:00 PM", "12/1/19 5:00 PM", "12/1/19 6:00 PM", "12/1/19 7:00 PM", "12/1/19 8:00 PM", "12/1/19 9:00 PM", "12/1/19 10:00 PM", "12/1/19 11:00 PM", "12/2/19 12:00 AM", "12/2/19 1:00 AM", "12/2/19 2:00 AM", "12/2/19 3:00 AM", "12/2/19 4:00 AM", "12/2/19 5:00 AM", "12/2/19 6:00 AM", "12/2/19 7:00 AM", "12/2/19 8:00 AM", "12/2/19 9:00 AM", "12/2/19 10:00 AM", "12/2/19 11:00 AM", "12/2/19 12:00 PM", "12/2/19 1:00 PM", "12/2/19 2:00 PM", "12/2/19 3:00 PM", "12/2/19 4:00 PM", "12/2/19 5:00 PM", "12/2/19 6:00 PM", "12/2/19 7:00 PM", "12/2/19 8:00 PM", "12/2/19 9:00 PM", "12/2/19 10:00 PM", "12/2/19 11:00 PM", "12/3/19 12:00 AM", "12/3/19 1:00 AM", "12/3/19 2:00 AM", "12/3/19 3:00 AM", "12/3/19 4:00 AM", "12/3/19 5:00 AM", "12/3/19 6:00 AM", "12/3/19 7:00 AM", "12/3/19 8:00 AM", "12/3/19 9:00 AM", "12/3/19 10:00 AM", "12/3/19 11:00 AM", "12/3/19 12:00 PM", "12/3/19 1:00 PM", "12/3/19 2:00 PM", "12/3/19 3:00 PM", "12/3/19 4:00 PM", "12/3/19 5:00 PM", "12/3/19 6:00 PM", "12/3/19 7:00 PM", "12/3/19 8:00 PM", "12/3/19 9:00 PM", "12/3/19 10:00 PM", "12/3/19 11:00 PM", "12/4/19 12:00 AM", "12/4/19 1:00 AM", "12/4/19 2:00 AM", "12/4/19 3:00 AM", "12/4/19 4:00 AM", "12/4/19 5:00 AM", "12/4/19 6:00 AM", "12/4/19 7:00 AM", "12/4/19 8:00 AM", "12/4/19 9:00 AM", "12/4/19 10:00 AM", "12/4/19 11:00 AM", "12/4/19 12:00 PM", "12/4/19 1:00 PM", "12/4/19 2:00 PM", "12/4/19 3:00 PM", "12/4/19 4:00 PM", "12/4/19 5:00 PM", "12/4/19 6:00 PM", "12/4/19 7:00 PM", "12/4/19 8:00 PM", "12/4/19 9:00 PM", "12/4/19 10:00 PM", "12/4/19 11:00 PM", "12/5/19 12:00 AM", "12/5/19 1:00 AM", "12/5/19 2:00 AM", "12/5/19 3:00 AM", "12/5/19 4:00 AM", "12/5/19 5:00 AM", "12/5/19 6:00 AM", "12/5/19 7:00 AM", "12/5/19 8:00 AM", "12/5/19 9:00 AM", "12/5/19 10:00 AM", "12/5/19 11:00 AM", "12/5/19 12:00 PM", "12/5/19 1:00 PM", "12/5/19 2:00 PM", "12/5/19 3:00 PM", "12/5/19 4:00 PM", "12/5/19 5:00 PM", "12/5/19 6:00 PM", "12/5/19 7:00 PM", "12/5/19 8:00 PM", "12/5/19 9:00 PM", "12/5/19 10:00 PM", "12/5/19 11:00 PM", "12/6/19 12:00 AM", "12/6/19 1:00 AM", "12/6/19 2:00 AM", "12/6/19 3:00 AM", "12/6/19 4:00 AM", "12/6/19 5:00 AM", "12/6/19 6:00 AM", "12/6/19 7:00 AM", "12/6/19 8:00 AM", "12/6/19 9:00 AM", "12/6/19 10:00 AM", "12/6/19 11:00 AM", "12/6/19 12:00 PM", "12/6/19 1:00 PM", "12/6/19 2:00 PM", "12/6/19 3:00 PM", "12/6/19 4:00 PM", "12/6/19 5:00 PM", "12/6/19 6:00 PM", "12/6/19 7:00 PM", "12/6/19 8:00 PM", "12/6/19 9:00 PM", "12/6/19 10:00 PM", "12/6/19 11:00 PM", "12/7/19 12:00 AM", "12/7/19 1:00 AM", "12/7/19 2:00 AM", "12/7/19 3:00 AM", "12/7/19 4:00 AM", "12/7/19 5:00 AM", "12/7/19 6:00 AM", "12/7/19 7:00 AM", "12/7/19 8:00 AM", "12/7/19 9:00 AM", "12/7/19 10:00 AM", "12/7/19 11:00 AM", "12/7/19 12:00 PM", "12/7/19 1:00 PM", "12/7/19 2:00 PM", "12/7/19 3:00 PM", "12/7/19 4:00 PM", "12/7/19 5:00 PM", "12/7/19 6:00 PM", "12/7/19 7:00 PM", "12/7/19 8:00 PM", "12/7/19 9:00 PM", "12/7/19 10:00 PM", "12/7/19 11:00 PM", "12/8/19 12:00 AM", "12/8/19 1:00 AM", "12/8/19 2:00 AM", "12/8/19 3:00 AM", "12/8/19 4:00 AM", "12/8/19 5:00 AM", "12/8/19 6:00 AM", "12/8/19 7:00 AM", "12/8/19 8:00 AM", "12/8/19 9:00 AM", "12/8/19 10:00 AM", "12/8/19 11:00 AM", "12/8/19 12:00 PM", "12/8/19 1:00 PM", "12/8/19 2:00 PM", "12/8/19 3:00 PM", "12/8/19 4:00 PM", "12/8/19 5:00 PM", "12/8/19 6:00 PM", "12/8/19 7:00 PM", "12/8/19 8:00 PM", "12/8/19 9:00 PM", "12/8/19 10:00 PM", "12/8/19 11:00 PM", "12/9/19 12:00 AM", "12/9/19 1:00 AM", "12/9/19 2:00 AM", "12/9/19 3:00 AM", "12/9/19 4:00 AM", "12/9/19 5:00 AM", "12/9/19 6:00 AM", "12/9/19 7:00 AM", "12/9/19 8:00 AM", "12/9/19 9:00 AM", "12/9/19 10:00 AM", "12/9/19 11:00 AM", "12/9/19 12:00 PM", "12/9/19 1:00 PM", "12/9/19 2:00 PM", "12/9/19 3:00 PM", "12/9/19 4:00 PM", "12/9/19 5:00 PM", "12/9/19 6:00 PM", "12/9/19 7:00 PM", "12/9/19 8:00 PM", "12/9/19 9:00 PM", "12/9/19 10:00 PM", "12/9/19 11:00 PM", "12/10/19 12:00 AM", "12/10/19 1:00 AM", "12/10/19 2:00 AM", "12/10/19 3:00 AM", "12/10/19 4:00 AM", "12/10/19 5:00 AM", "12/10/19 6:00 AM", "12/10/19 7:00 AM", "12/10/19 8:00 AM", "12/10/19 9:00 AM", "12/10/19 10:00 AM", "12/10/19 11:00 AM", "12/10/19 12:00 PM", "12/10/19 1:00 PM", "12/10/19 2:00 PM", "12/10/19 3:00 PM", "12/10/19 4:00 PM", "12/10/19 5:00 PM", "12/10/19 6:00 PM", "12/10/19 7:00 PM", "12/10/19 8:00 PM", "12/10/19 9:00 PM", "12/10/19 10:00 PM", "12/10/19 11:00 PM", "12/11/19 12:00 AM", "12/11/19 1:00 AM", "12/11/19 2:00 AM", "12/11/19 3:00 AM", "12/11/19 4:00 AM", "12/11/19 5:00 AM", "12/11/19 6:00 AM", "12/11/19 7:00 AM", "12/11/19 8:00 AM", "12/11/19 9:00 AM", "12/11/19 10:00 AM", "12/11/19 11:00 AM", "12/11/19 12:00 PM", "12/11/19 1:00 PM", "12/11/19 2:00 PM", "12/11/19 3:00 PM", "12/11/19 4:00 PM", "12/11/19 5:00 PM", "12/11/19 6:00 PM", "12/11/19 7:00 PM", "12/11/19 8:00 PM", "12/11/19 9:00 PM", "12/11/19 10:00 PM", "12/11/19 11:00 PM", "12/12/19 12:00 AM", "12/12/19 1:00 AM", "12/12/19 2:00 AM", "12/12/19 3:00 AM", "12/12/19 4:00 AM", "12/12/19 5:00 AM", "12/12/19 6:00 AM", "12/12/19 7:00 AM", "12/12/19 8:00 AM", "12/12/19 9:00 AM", "12/12/19 10:00 AM", "12/12/19 11:00 AM", "12/12/19 12:00 PM", "12/12/19 1:00 PM", "12/12/19 2:00 PM", "12/12/19 3:00 PM", "12/12/19 4:00 PM", "12/12/19 5:00 PM", "12/12/19 6:00 PM", "12/12/19 7:00 PM", "12/12/19 8:00 PM", "12/12/19 9:00 PM", "12/12/19 10:00 PM", "12/12/19 11:00 PM", "12/13/19 12:00 AM", "12/13/19 1:00 AM", "12/13/19 2:00 AM", "12/13/19 3:00 AM", "12/13/19 4:00 AM", "12/13/19 5:00 AM", "12/13/19 6:00 AM", "12/13/19 7:00 AM", "12/13/19 8:00 AM", "12/13/19 9:00 AM", "12/13/19 10:00 AM", "12/13/19 11:00 AM", "12/13/19 12:00 PM", "12/13/19 1:00 PM", "12/13/19 2:00 PM", "12/13/19 3:00 PM", "12/13/19 4:00 PM", "12/13/19 5:00 PM", "12/13/19 6:00 PM", "12/13/19 7:00 PM", "12/13/19 8:00 PM", "12/13/19 9:00 PM", "12/13/19 10:00 PM", "12/13/19 11:00 PM", "12/14/19 12:00 AM", "12/14/19 1:00 AM", "12/14/19 2:00 AM", "12/14/19 3:00 AM", "12/14/19 4:00 AM", "12/14/19 5:00 AM", "12/14/19 6:00 AM", "12/14/19 7:00 AM", "12/14/19 8:00 AM", "12/14/19 9:00 AM", "12/14/19 10:00 AM", "12/14/19 11:00 AM", "12/14/19 12:00 PM", "12/14/19 1:00 PM", "12/14/19 2:00 PM", "12/14/19 3:00 PM", "12/14/19 4:00 PM", "12/14/19 5:00 PM", "12/14/19 6:00 PM", "12/14/19 7:00 PM", "12/14/19 8:00 PM", "12/14/19 9:00 PM", "12/14/19 10:00 PM", "12/14/19 11:00 PM", "12/15/19 12:00 AM", "12/15/19 1:00 AM", "12/15/19 2:00 AM", "12/15/19 3:00 AM", "12/15/19 4:00 AM", "12/15/19 5:00 AM", "12/15/19 6:00 AM", "12/15/19 7:00 AM", "12/15/19 8:00 AM", "12/15/19 9:00 AM", "12/15/19 10:00 AM", "12/15/19 11:00 AM", "12/15/19 12:00 PM", "12/15/19 1:00 PM", "12/15/19 2:00 PM", "12/15/19 3:00 PM", "12/15/19 4:00 PM", "12/15/19 5:00 PM", "12/15/19 6:00 PM", "12/15/19 7:00 PM", "12/15/19 8:00 PM", "12/15/19 9:00 PM", "12/15/19 10:00 PM", "12/15/19 11:00 PM", "12/16/19 12:00 AM", "12/16/19 1:00 AM", "12/16/19 2:00 AM", "12/16/19 3:00 AM", "12/16/19 4:00 AM", "12/16/19 5:00 AM", "12/16/19 6:00 AM", "12/16/19 7:00 AM", "12/16/19 8:00 AM", "12/16/19 9:00 AM", "12/16/19 10:00 AM", "12/16/19 11:00 AM", "12/16/19 12:00 PM", "12/16/19 1:00 PM", "12/16/19 2:00 PM", "12/16/19 3:00 PM", "12/16/19 4:00 PM", "12/16/19 5:00 PM", "12/16/19 6:00 PM", "12/16/19 7:00 PM", "12/16/19 8:00 PM", "12/16/19 9:00 PM", "12/16/19 10:00 PM", "12/16/19 11:00 PM", "12/17/19 12:00 AM", "12/17/19 1:00 AM", "12/17/19 2:00 AM", "12/17/19 3:00 AM", "12/17/19 4:00 AM", "12/17/19 5:00 AM", "12/17/19 6:00 AM", "12/17/19 7:00 AM", "12/17/19 8:00 AM", "12/17/19 9:00 AM", "12/17/19 10:00 AM", "12/17/19 11:00 AM", "12/17/19 12:00 PM", "12/17/19 1:00 PM", "12/17/19 2:00 PM", "12/17/19 3:00 PM", "12/17/19 4:00 PM", "12/17/19 5:00 PM", "12/17/19 6:00 PM", "12/17/19 7:00 PM", "12/17/19 8:00 PM", "12/17/19 9:00 PM", "12/17/19 10:00 PM", "12/17/19 11:00 PM", "12/18/19 12:00 AM", "12/18/19 1:00 AM", "12/18/19 2:00 AM", "12/18/19 3:00 AM", "12/18/19 4:00 AM", "12/18/19 5:00 AM", "12/18/19 6:00 AM", "12/18/19 7:00 AM", "12/18/19 8:00 AM", "12/18/19 9:00 AM", "12/18/19 10:00 AM", "12/18/19 11:00 AM", "12/18/19 12:00 PM", "12/18/19 1:00 PM", "12/18/19 2:00 PM", "12/18/19 3:00 PM", "12/18/19 4:00 PM", "12/18/19 5:00 PM", "12/18/19 6:00 PM", "12/18/19 7:00 PM", "12/18/19 8:00 PM", "12/18/19 9:00 PM", "12/18/19 10:00 PM", "12/18/19 11:00 PM", "12/19/19 12:00 AM", "12/19/19 1:00 AM", "12/19/19 2:00 AM", "12/19/19 3:00 AM", "12/19/19 4:00 AM", "12/19/19 5:00 AM", "12/19/19 6:00 AM", "12/19/19 7:00 AM", "12/19/19 8:00 AM", "12/19/19 9:00 AM", "12/19/19 10:00 AM", "12/19/19 11:00 AM", "12/19/19 12:00 PM", "12/19/19 1:00 PM", "12/19/19 2:00 PM", "12/19/19 3:00 PM", "12/19/19 4:00 PM", "12/19/19 5:00 PM", "12/19/19 6:00 PM", "12/19/19 7:00 PM", "12/19/19 8:00 PM", "12/19/19 9:00 PM", "12/19/19 10:00 PM", "12/19/19 11:00 PM", "12/20/19 12:00 AM", "12/20/19 1:00 AM", "12/20/19 2:00 AM", "12/20/19 3:00 AM", "12/20/19 4:00 AM", "12/20/19 5:00 AM", "12/20/19 6:00 AM", "12/20/19 7:00 AM", "12/20/19 8:00 AM", "12/20/19 9:00 AM", "12/20/19 10:00 AM", "12/20/19 11:00 AM", "12/20/19 12:00 PM", "12/20/19 1:00 PM", "12/20/19 2:00 PM", "12/20/19 3:00 PM", "12/20/19 4:00 PM", "12/20/19 5:00 PM", "12/20/19 6:00 PM", "12/20/19 7:00 PM", "12/20/19 8:00 PM", "12/20/19 9:00 PM", "12/20/19 10:00 PM", "12/20/19 11:00 PM", "12/21/19 12:00 AM", "12/21/19 1:00 AM", "12/21/19 2:00 AM", "12/21/19 3:00 AM", "12/21/19 4:00 AM", "12/21/19 5:00 AM", "12/21/19 6:00 AM", "12/21/19 7:00 AM", "12/21/19 8:00 AM", "12/21/19 9:00 AM", "12/21/19 10:00 AM", "12/21/19 11:00 AM", "12/21/19 12:00 PM", "12/21/19 1:00 PM", "12/21/19 2:00 PM", "12/21/19 3:00 PM", "12/21/19 4:00 PM", "12/21/19 5:00 PM", "12/21/19 6:00 PM", "12/21/19 7:00 PM", "12/21/19 8:00 PM", "12/21/19 9:00 PM", "12/21/19 10:00 PM", "12/21/19 11:00 PM", "12/22/19 12:00 AM", "12/22/19 1:00 AM", "12/22/19 2:00 AM", "12/22/19 3:00 AM", "12/22/19 4:00 AM", "12/22/19 5:00 AM", "12/22/19 6:00 AM", "12/22/19 7:00 AM", "12/22/19 8:00 AM", "12/22/19 9:00 AM", "12/22/19 10:00 AM", "12/22/19 11:00 AM", "12/22/19 12:00 PM", "12/22/19 1:00 PM", "12/22/19 2:00 PM", "12/22/19 3:00 PM", "12/22/19 4:00 PM", "12/22/19 5:00 PM", "12/22/19 6:00 PM", "12/22/19 7:00 PM", "12/22/19 8:00 PM", "12/22/19 9:00 PM", "12/22/19 10:00 PM", "12/22/19 11:00 PM", "12/23/19 12:00 AM", "12/23/19 1:00 AM", "12/23/19 2:00 AM", "12/23/19 3:00 AM", "12/23/19 4:00 AM", "12/23/19 5:00 AM", "12/23/19 6:00 AM", "12/23/19 7:00 AM", "12/23/19 8:00 AM", "12/23/19 9:00 AM", "12/23/19 10:00 AM", "12/23/19 11:00 AM", "12/23/19 12:00 PM", "12/23/19 1:00 PM", "12/23/19 2:00 PM", "12/23/19 3:00 PM", "12/23/19 4:00 PM", "12/23/19 5:00 PM", "12/23/19 6:00 PM", "12/23/19 7:00 PM", "12/23/19 8:00 PM", "12/23/19 9:00 PM", "12/23/19 10:00 PM", "12/23/19 11:00 PM", "12/24/19 12:00 AM", "12/24/19 1:00 AM", "12/24/19 2:00 AM", "12/24/19 3:00 AM", "12/24/19 4:00 AM", "12/24/19 5:00 AM", "12/24/19 6:00 AM", "12/24/19 7:00 AM", "12/24/19 8:00 AM", "12/24/19 9:00 AM", "12/24/19 10:00 AM", "12/24/19 11:00 AM", "12/24/19 12:00 PM", "12/24/19 1:00 PM", "12/24/19 2:00 PM", "12/24/19 3:00 PM", "12/24/19 4:00 PM", "12/24/19 5:00 PM", "12/24/19 6:00 PM", "12/24/19 7:00 PM", "12/24/19 8:00 PM", "12/24/19 9:00 PM", "12/24/19 10:00 PM", "12/24/19 11:00 PM", "12/25/19 12:00 AM", "12/25/19 1:00 AM", "12/25/19 2:00 AM", "12/25/19 3:00 AM", "12/25/19 4:00 AM", "12/25/19 5:00 AM", "12/25/19 6:00 AM", "12/25/19 7:00 AM", "12/25/19 8:00 AM", "12/25/19 9:00 AM", "12/25/19 10:00 AM", "12/25/19 11:00 AM", "12/25/19 12:00 PM", "12/25/19 1:00 PM", "12/25/19 2:00 PM", "12/25/19 3:00 PM", "12/25/19 4:00 PM", "12/25/19 5:00 PM", "12/25/19 6:00 PM", "12/25/19 7:00 PM", "12/25/19 8:00 PM", "12/25/19 9:00 PM", "12/25/19 10:00 PM", "12/25/19 11:00 PM", "12/26/19 12:00 AM", "12/26/19 1:00 AM", "12/26/19 2:00 AM", "12/26/19 3:00 AM", "12/26/19 4:00 AM", "12/26/19 5:00 AM", "12/26/19 6:00 AM", "12/26/19 7:00 AM", "12/26/19 8:00 AM", "12/26/19 9:00 AM", "12/26/19 10:00 AM", "12/26/19 11:00 AM", "12/26/19 12:00 PM", "12/26/19 1:00 PM", "12/26/19 2:00 PM", "12/26/19 3:00 PM", "12/26/19 4:00 PM", "12/26/19 5:00 PM", "12/26/19 6:00 PM", "12/26/19 7:00 PM", "12/26/19 8:00 PM", "12/26/19 9:00 PM", "12/26/19 10:00 PM", "12/26/19 11:00 PM", "12/27/19 12:00 AM", "12/27/19 1:00 AM", "12/27/19 2:00 AM", "12/27/19 3:00 AM", "12/27/19 4:00 AM", "12/27/19 5:00 AM", "12/27/19 6:00 AM", "12/27/19 7:00 AM", "12/27/19 8:00 AM", "12/27/19 9:00 AM", "12/27/19 10:00 AM", "12/27/19 11:00 AM", "12/27/19 12:00 PM", "12/27/19 1:00 PM", "12/27/19 2:00 PM", "12/27/19 3:00 PM", "12/27/19 4:00 PM", "12/27/19 5:00 PM", "12/27/19 6:00 PM", "12/27/19 7:00 PM", "12/27/19 8:00 PM", "12/27/19 9:00 PM", "12/27/19 10:00 PM", "12/27/19 11:00 PM", "12/28/19 12:00 AM", "12/28/19 1:00 AM", "12/28/19 2:00 AM", "12/28/19 3:00 AM", "12/28/19 4:00 AM", "12/28/19 5:00 AM", "12/28/19 6:00 AM", "12/28/19 7:00 AM", "12/28/19 8:00 AM", "12/28/19 9:00 AM", "12/28/19 10:00 AM", "12/28/19 11:00 AM", "12/28/19 12:00 PM", "12/28/19 1:00 PM", "12/28/19 2:00 PM", "12/28/19 3:00 PM", "12/28/19 4:00 PM", "12/28/19 5:00 PM", "12/28/19 6:00 PM", "12/28/19 7:00 PM", "12/28/19 8:00 PM", "12/28/19 9:00 PM", "12/28/19 10:00 PM", "12/28/19 11:00 PM", "12/29/19 12:00 AM", "12/29/19 1:00 AM", "12/29/19 2:00 AM", "12/29/19 3:00 AM", "12/29/19 4:00 AM", "12/29/19 5:00 AM", "12/29/19 6:00 AM", "12/29/19 7:00 AM", "12/29/19 8:00 AM", "12/29/19 9:00 AM", "12/29/19 10:00 AM", "12/29/19 11:00 AM", "12/29/19 12:00 PM", "12/29/19 1:00 PM", "12/29/19 2:00 PM", "12/29/19 3:00 PM", "12/29/19 4:00 PM", "12/29/19 5:00 PM", "12/29/19 6:00 PM", "12/29/19 7:00 PM", "12/29/19 8:00 PM", "12/29/19 9:00 PM", "12/29/19 10:00 PM", "12/29/19 11:00 PM", "12/30/19 12:00 AM", "12/30/19 1:00 AM", "12/30/19 2:00 AM", "12/30/19 3:00 AM", "12/30/19 4:00 AM", "12/30/19 5:00 AM", "12/30/19 6:00 AM", "12/30/19 7:00 AM", "12/30/19 8:00 AM", "12/30/19 9:00 AM", "12/30/19 10:00 AM", "12/30/19 11:00 AM", "12/30/19 12:00 PM", "12/30/19 1:00 PM", "12/30/19 2:00 PM", "12/30/19 3:00 PM", "12/30/19 4:00 PM", "12/30/19 5:00 PM", "12/30/19 6:00 PM", "12/30/19 7:00 PM", "12/30/19 8:00 PM", "12/30/19 9:00 PM", "12/30/19 10:00 PM", "12/30/19 11:00 PM", "12/31/19 12:00 AM", "12/31/19 1:00 AM", "12/31/19 2:00 AM", "12/31/19 3:00 AM", "12/31/19 4:00 AM", "12/31/19 5:00 AM", "12/31/19 6:00 AM", "12/31/19 7:00 AM", "12/31/19 8:00 AM", "12/31/19 9:00 AM", "12/31/19 10:00 AM", "12/31/19 11:00 AM", "12/31/19 12:00 PM", "12/31/19 1:00 PM", "12/31/19 2:00 PM", "12/31/19 3:00 PM", "12/31/19 4:00 PM", "12/31/19 5:00 PM", "12/31/19 6:00 PM", "12/31/19 7:00 PM", "12/31/19 8:00 PM", "12/31/19 9:00 PM", "12/31/19 10:00 PM", "12/31/19 11:00 PM" ],
      yaxis: null,
      actualData: [0,0,0,0,0,0,0,0,0,0,0,0],
      calData: [0,0,0,0,0,0,0,0,0,0,0,0],
      capxData: [0,0,0,0,0,0,0,0,0,0,0,0],
      energystarGraphData: [0,0,0,0,0,0,0,0,0,0,0,0],
      energystarGraphAxis: [1,2,3,4,5,6,7,8,9,10,11,12],
      energystarAxis: [0,0,0,0,0,0,0,0,0,0,0,0],
      subData: [0,0,0,0,0,0,0,0,0,0],
      msg: null,
      energystarData: blank_estar,

      combineCalBool: false,
      calBool: false,
      combineCapxBool: false,
      capxBool: false,
    }

  },

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  created() {
    console.log('1')
    this.getMessage();
    this.getEnergystar();
  },

  watch: {
    calData() {
      this.sendMessage()

      this.drawChartCal()
      this.loading = false
      // var audio = new Audio(require('../assets/Turntables.mp3'))
      var audio = new Audio(require('../assets/ding-sound-effect_2.mp3'))
      audio.play()
    },

    actualData() {
      this.drawChartCal()
      this.drawChartCapx()
    },

    dataInterval() {
      this.drawChartCal()
      this.drawChartCapx()
    },

    subData() {
      this.drawPieEnergystar()
    },

    calParams() {
    },

    calSettings() {
    },

    GASettings(){
    },
    
    capxParameters(){
    },

    capxSettings() {
    },

    scheduleParams() {
    },

    heatParams() {
    },

    capxParams() {
    },

    capxData() {
        this.loading2 = false

        this.drawChartCapx()
        // var audio = new Audio(require('../assets/Turntables.mp3'))
        var audio = new Audio(require('../assets/ding-sound-effect_2.mp3'))
        audio.play()
    },

    loading() {
    },

    loading2(){
    },

    energystarGraphData() {
      this.drawChartEnergystar()
    },

    combineCalBool() {
      this.sendMessage()
      this.combineCalBool = false
    },

    combineCapxBool() {
      this.sendMessage()
      this.combineCapxBool = false
    },
  },

  methods: {

    getMessage() {
      const path = 'http://localhost:5000/Cal';
      axios.get(path)
        .then((res) => {
          this.calParams = res.data.calData.calibration_parameters
          this.scheduleParams = res.data.calData.schedule_parameters
          this.heatParams = res.data.calData.monthly_internal
          this.GASettings = res.data.calData.ga_settings
          this.calSettings = res.data.calData.calibration_settings
          this.type = res.data.calData.type
          this.capxParams = res.data.calData.capxParameters
          this.capxParameterValues = res.data.calData.capxParameterValues
          this.capxSettings = res.data.calData.capxSettings
          // this.combineCalibration()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    runCapx() {
      const path = 'http://localhost:5000/Capx';
      axios.get(path)
        .then((res) => {
          this.actualData = res.data.real
          this.capxData = res.data.modeled
          this.dataInteval = res.data.interval
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    getEnergystar() {
      const path = 'http://localhost:5000/energystar';
      axios.get(path)
        .then((res) => {
          this.energystarData = res.data.estarData;
          this.energystarGraphData = res.data.estarData.benchmark
          this.energystarGraphAxis = res.data.build_index
          this.runBEM()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    sendMessage() {
      const path = 'http://127.0.0.1:5000/Cal'
      axios.put(path, this.calCombine)
      .then(() => {
        this.getMessage();
      })
      .catch((error) => {
        console.error(error);
        this.getMessage();
      })
    },

    sendEnergystar() {
      const path = 'http://127.0.0.1:5000/energystar'
      let estarData = this.energystarData
      axios.put(path, estarData)
      .then(() => {
        this.getEnergystar();
      })
      .catch((error) => {
        console.error(error);
        this.getEnergystar();
      })
    },

    runCalibration() {
      const path = 'http://127.0.0.1:5000/Calibration'
      axios.get(path)
      .then((res) => {
        this.actualData = res.data.real
        this.calData = res.data.modeled
        this.dataInteval = res.data.interval
      })
      .catch((error) => {
        console.error(error);
      })
    },

    runBEM() {
      const path = 'http://127.0.0.1:5000/BEM'
      axios.get(path)
      .then((res) => {
        this.subData = res.data.subs
      })
      .catch((error) => {
        console.error(error);
      })
    },

    combineCalibration() {
      let calibration_parameters = this.calParams
      let calibration_settings = this.calSettings
      let schedule_parameters = this.scheduleParams
      let monthly_internal = this.heatParams
      let type = this.type
      let ga_settings = this.GASettings
      let capxParameters = this.capxParams
      let capxParameterValues = this.capxParameterValues
      let capxSettings = this.capxSettings

      let merged = {calibration_parameters, calibration_settings, schedule_parameters, monthly_internal, ga_settings, type, capxParameters, capxParameterValues, capxSettings}
      console.log(merged)

      this.calCombine = JSON.stringify(merged)
      this.combineCalBool = true
    },

    combineCapx() {
      let calibration_parameters = this.calParams
      let calibration_settings = this.calSettings
      let schedule_parameters = this.scheduleParams
      let monthly_internal = this.heatParams
      let type = this.type
      let ga_settings = this.GASettings
      let capxParameters = this.capxParams
      let capxParameterValues = this.capxParameterValues
      let capxSettings = this.capxSettings

      let merged = {calibration_parameters, calibration_settings, schedule_parameters, monthly_internal, ga_settings, type, capxParameters, capxParameterValues, capxSettings}
      console.log(merged)

      this.calCombine = JSON.stringify(merged)
      this.combineCapxBool = true
    },

    loadState() {
      this.loading = true
    },

    loadState2() {
      this.loading2 = true
    },

    editItem(item) {
      this.editedIndex = this.calParams.indexOf(item)
      this.editCalForm = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.calParams.indexOf(item)
      this.editCalForm = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.calParams.splice(this.editedIndex, 1)
      this.calCloseDelete()
    },

    calClose() {
      this.dialog = false

      this.$nextTick(() => {
        this.editCalForm = Object.assign({}, this.defaultCalForm)
        this.editedIndex = -1
      })
    },

    calCloseDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultCalForm)
        this.editedIndex = -1
      })
    }, 

    calSave() {
      if (this.editedIndex > -1) {
        Object.assign(this.calParams[this.editedIndex], this.editCalForm)
      } else {
        this.calParams.push(this.editCalForm)
      }
      this.calClose()
    },

    editItemCapx(item) {
      this.editedIndex2 = this.capxParams.indexOf(item)
      this.editCapxForm = Object.assign({}, item)
      this.dialogCapx = true
    },

    deleteItemCapx (item) {
      this.editedIndex2 = this.capxParams.indexOf(item)
      this.editCapxForm = Object.assign({}, item)
      this.dialogDeleteCapx = true
    },

    deleteItemConfirmCapx() {
      this.capxParams.splice(this.editedIndex2, 1)
      this.capxCloseDelete()
    },

    capxClose() {
      this.dialogCapx = false

      this.$nextTick(() => {
        this.editCapxForm = Object.assign({}, this.defaultCapxForm)
        this.editedIndex2 = -1
      })
    },

    capxCloseDelete() {
      this.dialogDeleteCapx = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultCapxForm)
        this.editedIndex2 = -1
      })
    }, 

    capxSave() {
      if (this.editedIndex2 > -1) {
        Object.assign(this.capxParams[this.editedIndex1], this.editCapxForm)
      } else {
        this.capxParams.push(this.editCapxForm)
      }
      this.capxClose()
    },

    editItemSchedule(item) {
      this.editedIndex3 = this.scheduleParams.indexOf(item)
      this.editScheduleForm = Object.assign({}, item)
      this.dialogSchedule = true
    },

    deleteItemSchedule (item) {
      this.editedIndex3 = this.scheduleParams.indexOf(item)
      this.editScheduleForm = Object.assign({}, item)
      this.dialogDeleteSchedule = true
    },

    deleteItemConfirmSchedule() {
      this.scheduleParams.splice(this.editedIndex3, 1)
      this.scheduleCloseDelete()
    },

    scheduleClose() {
      this.dialogSchedule = false

      this.$nextTick(() => {
        this.editScheduleForm = Object.assign({}, this.defaultScheduleForm)
        this.editedIndex3 = -1
      })
    },

    scheduleCloseDelete() {
      this.dialogDeleteSchedule = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultScheduleForm)
        this.editedIndex3 = -1
      })
    }, 

    scheduleSave() {
      if (this.editedIndex3 > -1) {
        Object.assign(this.scheduleParams[this.editedIndex3], this.editScheduleForm)
      } else {
        this.scheduleParams.push(this.editScheduleForm)
      }
      this.scheduleClose()
    },

    editItemHeat(item) {
      this.editedIndex4 = this.heatParams.indexOf(item)
      this.editHeatForm = Object.assign({}, item)
      this.dialogHeat = true
    },

    deleteItemHeat (item) {
      this.editedIndex4 = this.heatParams.indexOf(item)
      this.editHeatForm = Object.assign({}, item)
      this.dialogDeleteHeat = true
    },

    deleteItemConfirmHeat() {
      this.heatParams.splice(this.editedIndex4, 1)
      this.heatCloseDelete()
    },

    heatClose() {
      this.dialogHeat = false

      this.$nextTick(() => {
        this.editHeatForm = Object.assign({}, this.defaultHeatForm)
        this.editedIndex4 = -1
      })
    },

    heatCloseDelete() {
      this.dialogDeleteHeat = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultHeatForm)
        this.editedIndex4 = -1
      })
    }, 

    heatSave() {
      if (this.editedIndex4 > -1) {
        Object.assign(this.heatParams[this.editedIndex4], this.editHeatForm)
      } else {
        this.heatParams.push(this.editHeatForm)
      }
      this.heatClose()
    },

    drawChartCal() {
      if (this.dataInterval == "Monthly") {
        this.yaxis = this.monthlySchedule
      } else if (this.dataInterval == "Hourly") {
        this.yaxis = this.hourlySchedule  
      }
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("calchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Actual vs Calibrated Delivered Energy'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['Actual', 'Simulated'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          },
          {
            type: 'inside',
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          }
        ],
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.yaxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Actual Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.actualData
          },
          {
            name: 'Calibrated Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.calData
          },
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartCapx() {
      if (this.dataInterval == "Monthly") {
        this.yaxis = this.monthlySchedule
      } else if (this.dataInterval == "Hourly") {
        this.yaxis = this.hourlySchedule  
      }
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("capxchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Actual vs CapX Technology Infused Delivered Energy'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['Actual', 'CapX'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          },
          {
            type: 'inside',
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          }
        ],
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.yaxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Baseline Cost',
            type: 'line',
            stack: 'Total',
            data: this.actualData
          },
          {
            name: 'CapX Tech Implemented Cost',
            type: 'line',
            stack: 'Total',
            data: this.capxData
          },
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartEnergystar() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("energystarchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'EUI Benchmarking'
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: this.energystarGraphAxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'bar',
            data: this.energystarGraphData,
            markLine: {
              data: [{name: 'Source Building EUI', yAxis: this.energystarData.score.sourceEUI,
                lineStyle: {
                  color: 'red'
                }
              }],
            }
          },
        ],
      };
      option && myChart.setOption(option);
    },

    drawPieEnergystar() {
      
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("energystarpie"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Energy Use Break Down (kWh)',
          left: 'center'
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: this.subData[0][0], name: 'Heating' },
              { value: this.subData[1][0], name: 'Cooling' },
              { value: this.subData[2][0], name: 'Lighting' },
              { value: this.subData[3][0], name: 'Fans' },
              { value: this.subData[4][0], name: 'Pumps' },
              { value: this.subData[5][0], name: 'Plug Load' },
              { value: this.subData[6][0], name: 'DHW' },
              { value: this.subData[7][0], name: 'Electric Vehicle' },
              { value: this.subData[8][0], name: 'PV' },
              { value: this.subData[9][0], name: 'Wind' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      option && myChart.setOption(option);
    },

  },

  mounted() {
    console.log('2')
    this.getMessage()
    this.drawChartCal()
    this.drawChartCapx()
    this.drawChartEnergystar()
    this.drawPieEnergystar()
  },

}
</script>

<style>
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>

