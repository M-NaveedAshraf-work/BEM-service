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
    4) Input "python setup.py build_ext --inplace" into tyour command prompt (NOTE: may need to use python3 instead of python depending on your machine)
    
