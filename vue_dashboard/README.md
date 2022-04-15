# vue_dashboard

## Required
node js
Vue
(Other Plug-ins / Dependencies can be downloaded in the Vue GUI. See "Easy Setup" Section)

## Overview

The BEM Dashboard is a GUI environment to run a building through the Joulea energy modeling process. The modules within include: input, Uncertainty Quantification, Calibration/Capx, and Outputs.

*** WARNING: THE BACKEND MUST BE RUNNING FOR THE BEM DASHBOARD TO FUNCTION. SEE THE BACKEND README IN THE NEW_BEM_CODE FOLDER FOR INSTRUCTIONS TO ACTIVATE THE BACKEND ***

# Input
The input section is where the parameters of the building are input by the user. All fields must have an input for the BEM to run effectivly. The fields that designate building parameters auto populate with standard values that can either be left or modified by the user. 

*** Prep Work Required to Run *** 
1) A Generated Weather EPW file placed in the weather folder
2) A Data File that contains at least a full year of building load data in an hourly, monthly, or both time interval placed in the Inputs Folder

*** Steps to Run Input ***

*** New Building ***
1) Make sure the top left input box reads "New Building Input Files". If it does not, select the new building button at the bottom of the input box.
2) Select at minimum the designated weather (.epw) and data file (.xls). You may also select a building file (.json) from a past building that is similar to save time with the amount of inputs that need to be modified. Click "Read Files" to populate the form.
3) Enter the building information into the top right input box.
4) Fill out the Building Systems, Building Operation, and Envelope Input fields completely
5) Select the desired output period in the Run BEM input box and click the RUN BEM button

*** Existing Building Project ***
1) Make sure the top left input box reads "Existing Building Project Input Files". If it does not, select the Past Building Project button at the bottom of the input box.
2) Select the Input, UQ, Cal, and Estar files (.json) that were generated on the Output Graphs Page from a previous project. Click the "Read Files" button to populate the Dashboard. 
5) Select the desired output period in the Run BEM input box and click the RUN BEM button

# Uncertainty Quantification
The Uncertainty Quantification (UQ) section is where you can run Uncertainty Analysis and Sensitivity Analysis. Uncertainty Analysis and Sensitivity Analysis must be run one at a time. 

*** Steps to Run UQ ***
1) Fill in the top input box with desired parameters for your experiment
2) Click either Uncertainty Analysis or Sensitivity Analysis to run the desired analysis. Note: Must be run one at a time

# CapX and Calibration
This section contains Calibration, Energystar Calculation, and CapX. Each section is housed within its own section and are designed to be completeed in the order they are displayed. 

NOTE: If trying to skip to CapX before running calibration, make sure the Genetic Algorithm Inputs are filled in on the first input box

*** Steps to Run Calibration ***
1) Make sure the Genetic Algorithm section is filled in to the correct specifications
2) Fill in the Calibration Settings Inputs
3) Select Schedule, Monthly Internal Heat Gain, and Calibration Parameters
4) Run Calibration

*** Steps to Run Energy Star ***
1) Fill in Energy Star Inputs and click the "Run EnergyStar Calculation Button.

*** Steps to Run CapX ***
1) Make sure the Genetic Algorithm section is filled in to the correct specifications
2) Fill in the CapX Settings Inputs
3) If you want to modify any of the CapX parameter values, do so before running.
4) Select CapX Parameters
5) Run CapX

# Output Graphs
Output Graphs displays all the outputs from the modules in one easy to view section. All the graphs can be downloaded by clicking the top right of the images. You can also download the input files to save the inputs for all the runs completed for the building project. 

*** Steps to Run Output Graphs ***
1) Show up and enjoy the view
2) Download the building project files to save the project inputs. (It is recommended you place these in a folder together and upload to Teams/Sharepoint)

## Easy Setup

Open terminal and type: 
```
vue ui
```

This opens the GUI that makes it easy to set up and serve the BEM Dashboard

1) Select Project Folder in the VUE Project Manager Section
2) Update/Download Plugins and Dependencies in the Plugins and Dependencies Tabs
3) Go to Tasks -> Serve -> Serve Task Button -> Open App

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
