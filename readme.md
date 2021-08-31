# WebCrawler #
You'll need to have Python 3.6 or higher

[Download latest version of Python (3.9.6)](https://www.python.org/downloads/release/python-396/)

***
### Virtual Environment (PIPENV) ###
**Installation**

You can install the pipenv package by running the following command.

`pip install pipenv` 

Once the package is installed navigate into the webcrawler folder

`cd path/to/webcrawler` 

---

**Setting up the virtual environment**

Once you're into the webcrawler folder you can run the command. 

`pipenv install` 

It will generate the virtual environment and install all the dependencies packages. 

---

**Starting virtual environment and running the webcrawler**

You can start the virtual environment by running this command :

`pipenv shell` 

After the virtual environment is launch, you can start the webcrawler application by running the command : 

`python app.py`

---

You can stop the webcrawler by typing **CTRL-D** 

You can close the virtual environment by typing **exit**

---

## File and Folder ##

**website.txt**

- Contain the list of all the website used by crawler. *(The url don't have to contain the http:// or https://, the app manage this automatically)*


**subject.txt**

- Contain the list of all the subject used by crawler. *(It can be a word or phrase, it can't be multiline, one subject must be one line long)*

**article_list.txt**

- The file is create automatically if it not exist, it store all the url return by the webcrawler to prevent resaving it each time the webcrawler run. *(Can be remove if you want a search to start with an empty list)*

**result**

- This folder is generate automatically, it contain all the result save by the webcrawler.
*(Once create, every new session will be increment in this folder. You can delete it for a fresh new search, or rename it to keep a specific research out of the result folder )*

