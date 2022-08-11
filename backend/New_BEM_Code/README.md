# Building-Energy-Model-Code

You will first want to create a local Cythonized version of BEMP.py before starting the backend server

## Starting the Backend Server

1) Open command prompt anc change directory to the New_BEM_Code Folder
2) Run:
```
python app.py
```

## Creating a cythonized version of BEMP.py

    1) Ensure that you are running Python 3.8 or greater 
    2) Open command prompt and change directory to the "Cython" folder
    3) Delete the files except "setup.py", "BEMP.py" and "BEMP.pyx"
    4) Input "python setup.py build_ext --inplace" into your command prompt (NOTE: may need to use python3 instead of python depending on your machine)
    5) This should then create a file that starts with "BEMP.cp" 
    6) The file then needs to be moved over to the parent directory "New_BEM_Code"
    
## Docs

### Service Endpoints

    1) /input               methods=['GET 'PUT'])
    2) /BEM                 methods=['GET'])
    3) /Calibration         methods=['GET'])
    4) /auto_calibration    methods=['GET'])
    5) /Cal                 methods = ['GET 'PUT'])
    6) /UQ                  methods = ['GET 'PUT'])
    7) /runUQ               methods = ['GET'])
    8) /Capx                methods = ['GET'])
    9) /energystar          methods = ['GET 'PUT'])
    10) /graph              methods = ['GET 'PUT'])
    11) /loadProject        methods=['GET 'PUT'])
    12) /runZero            methods = ['GET 'PUT'])
    
[Detailed Breakdown of Endpoints](https://github.com/Joulea-com/BEM_Dashboard/blob/master/backend/New_BEM_Code/API_Response_Doc.md)
