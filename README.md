![TestVagrant](https://user-images.githubusercontent.com/95631736/202631028-7d93378a-a38c-49c2-9812-3c5f7fc55f3a.jpg)


# TestVagrant Assesment

Root folder must be *TestVagrant*

## Technologies Used 
> Selenium, Python, Pytest

## Clone Framework into Your Machine
> git clone https://github.com/PriyankaHS/TestVagrant

## Navigate to Repo Folder in commend line
> cd TestVagrant

## Setup to run tests
Required -> Python(version >= 3.5.0)

## Steps to install from cmd line:
#### Pipenv 
> pip install pipenv || python3 -m pip install pipenv

## Set up venv and install packages
> pipenv install

> pip install -r requirements.txt

To execute scripts from command line
> pipenv run pytest -m marker_name

> pipenv run pytest module.py::ClassName::method_name


## To change grouping of scripts (change marker_name)
> Markers are used for grouping tests

## For reports option
> --html=report.html 

## For rerunning failed tests
> pipenv run pytest --lf

## For parallel execution 
> -n number_of_workers (input_type = integer)
