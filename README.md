# Scrapyd-Django
Setup to run ScrapyD + Django and save it in Django Models. You can be up and running in just a few minutes. This template includes

* Basic structure of a Django project.
* Basic structure of a DRF
* Basic structure for scrapy.
* Configuration of scrapy in order to access Django models objects.
* Basic scrapy pipeline to save crawled objets to Django models.
* Basic spider definition



## Setup
1 - Install requirements
````
$ pip install -r requirements.txt
````
2 - Configure the database
````
$ python manage.py migrate
````

## Start the project
In order to start this project you will need to have running Django and Scrapyd at the same time.

In order to run Django
````
$ python manage.py runserver
````
In order to run Scrapyd
````
$ cd scrapy_app
$ scrapyd
````


Django is running on: http://localhost:8000
Scrapyd is running on: http://localhost:6800


At this point you will be able to send job request to Scrapyd. This project is setup with a demo spider from the oficial tutorial of scrapy. To run it you must send a http request to Scrapyd with the job info
````
curl http://localhost:6800/schedule.json -d project=default -d spider=repo_scrapy
````

The crawled data will be automatically be saved in the Django models


