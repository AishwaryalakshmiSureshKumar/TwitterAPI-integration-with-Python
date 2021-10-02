# TwitterAPI-integration-with-Python

**Prerequisites**
Twitter Developer account: if you don’t have one already, you can apply for one.
A Project and an App created in the dashboard.

**Using the code samples**
Clone the git repository to run in your local

In order to run the samples in this repository, need to set up some environment variables. Able to find your credentials in the App inside of your Project in the dashboard of the developer portal.

Be sure to replace <CONSUMER_KEY>, <CONSUMER_SECRET>, <ACCESS_TOKEN> and<ACCESS_TOKEN_SECRET> with your own credentials without the < >.

**Requirements**

Python with version 3.9.5 is required to run this code. Django version 3.2.4, djangorestframework version 3.12.4 and tweepy version 4.0.1 are also required.

Inorder to install all the above stated, please run below command:
cd twitterproject
pip install requirements.txt

**Documentation**

This Project is done in Python language on top of Django framework. For APIs, Django-restframework is used here. To connect to twitter API, tweepy module is used.

Created a project named 'twitterproject' and an app named 'tweetapp'. The endpoints and the required RESTful APIs can be found inside tweetapp. Included the tweetapp urls inside twitterproject.

The endpoints can be found inside tweetapp/urls.py
APIs can be found inside tweetapp/views.py

**Running the project**

Before running the curl command, make sure to run the project through below command:
python3 manage.py runserver


