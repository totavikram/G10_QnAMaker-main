# Instructions

## Tools 

1. PyCharm : https://www.jetbrains.com/pycharm/download/#section=mac
1. Anaconda : https://www.anaconda.com/products/individual

## Create Virtual Environment
```
Virtual Environment in Pycharm
Reference link : https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

```

```
Create virtual environment using command line

python -m venv FOLDER_NAME
```

## Install the below using the below
> Go to the application root director

```
Install the packages using requirements.txt

pip install -r requirements.txt

python -m spacy download en_core_web_md

python -m spacy download en-core-web-sm

```

## Use this command to add the project source to resolve internal modules
> syntax : export PYTHONPATH="${PYTHON_PATH}:${SOURCE_PATH}"
```

## Run the APP
```
python project/api/main.py       
```

#### Note : you should be able to access the Swagger UI using http://127.0.0.1:8000/docs

## Access application logs

Application logs are available under root directory as app.log

## DOCS


## Notebooks 


## Data

[Raw Data Directory](resources/data/raw): contains raw web scrapped job links and job descriptions.
[Cleaned Data Directory](resources/data/cleaned): contains cleaned, consolidated, and labelled job descriptions.
[Raw Q&A Directory](resources/data/Q&ABank/raw): contains raw question answers.
[Cleaned Q&A Directory](resources/data/Q&ABank/cleaned): contains cleaned, consolidated, and labelled question answers.

## Build Models


## Modules:

