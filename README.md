# Monitor

project was created to learn the python language.

it aims to check if any of the domains reported are offline, if any of them are offline, a notification will be sent via telegram.
   
# Configuration

In line 8 of the app.py file, you must enter the domains you want to monitor, in the example below are google and amazon, you can add as many more as you want
        
    DOMAINS = ['https://google.com.br','https://www.amazon.com/']

In the docker-compose.yml file you must insert the token and telegram group id
     
    TOKEN_TELEGRAM: ''
    CHAT_ID_TELEGRAM: ''

# How to run

To execute this code just run these two commands:

    docker-compose build
    docker-compose up -d

With these steps the server will already be running on port 5000 on your machine.

# Dependencies

    Flask [https://palletsprojects.com/p/flask/]
    Schedule [https://pypi.org/project/schedule/]
