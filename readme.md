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

By default, the webcrawler will run in strict search mode, meaning it will search for the exact sentence found in the subject.txt file

You can also run the webcrawler in nostrict mode, this mode will let you search by sending the request sentence as separeted words.

To run the application in nostrict mode you need to pass the argument -ns or --nostrict when starting the application.

`python app.py -ns` or `python app.py --nostrict`

It's also possible to perform a search ignoring the websites list with the argument -as or --allsite.

`python app.py -as` or `python app.py --allsite`

If you want to run the webcrawler without saving files to the computer, you can use argument -d or --debug

`python app.py -d` or `python app.py --debug`


The arguments can be combined together, if you want to run a none strict search, on any website, without saving the data, it will look like this 

`python app.py -ns -as -d` or `python app.py --nostrict --allsite --debug`
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

