# Building-Energy-Model-Code

## Starting the Backend

1) Set up a virtual environment on your machine to the New_BEM_Code Folder
2) Run:
```
python app.py
```

## Creating a cythonized version of BEMP.py

    1) open command prompt and change directory to the "Cython" folder
    2) delete the files except "setup.py", "EPCP.py" and "EPCP.pyx"
    3) input "python setup.py build_ext --inplace" 
