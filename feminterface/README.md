# Create a python package using GIT,GIHUB and POETRY

## Procjet setup
### make a new project
`poetry new feminterface`

### project file structure
```plaintext
feminterface/
├── pyproject.toml
├── feminterface/
│   ├── __init__.py
│   ├── fem/
│   │   ├── __init__.py
│   │   ├── fem.py
│   │   ├── cards/
│   │   │   ├── __init__.py
│   │   │   └── gcoord.py
│   │   │── func/
│   │   │   ├── __init__.py
│   │   │   └── node_func.py
└── tests/
    ├── __init__.py
    └── test_beuslo.py
```


`cd feminterface`

### Activating the virtual environment

`poetry shell`


### Specifying dependencies

`poetry add numpy`

### pytest
Include test files.

`poetry run pytest`

### build  package 

`poetry build`

## setup Github
Create repostory on GITHUB named eg. feminterface. Don't add _

Create a new repostory on the command line, don't use "name_name"

`git init`
`git add .`
`git commit -m "first commit" ` <br>
`git branch -M main`<br>
`git remote add origin https://github.com/sveinomork/feminterface.git` <br>
`git push -u origin main`

# Clone the repostory
`git clone https://github.com/sveinomork/feminterface.git feminterfaceclone`

`cd feminterfaceclone`



### Activating the virtual environment

`poetry shell`

### install 
`poetry install`


# Install the package from github
## Install poetry
See, https://python-poetry.org/docs/#installing-with-the-official-installer

## Procjet setup
### make a new project
`poetry new feminterfacepackage`

`cd feminterfacepackage`

### Activating the virtual environment

`poetry shell`


### Add the pacage

`poetry add git+https://github.com/sveinomork/feminterface.git`
















