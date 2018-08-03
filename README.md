PROJECT DJANGO-BLOG

A simple application in which people can post blogs.It has applications in which people can add post,edit there post and delete their post.
It has application where users can have a small chat facility also.


REQUIREMENTS

Here is a list of requirements you need to run this project

1)adium-theme-ubuntu==0.3.4
2)Django==1.11.15
3)pytz==2018.5
4)unity-lens-photos==1.0
5)virtualenv==16.0.0
6)redis 2.8
7)channel 1.1


start project with
sudo-apt install python3 dev
To start a Redis server on port 6379, run the following command:
docker run -p 6379:6379 -d redis:2.8
To run redis use this command
pip3 install channels_redis

**note Make sure that you have python 3 installed and install channels for chat activation


RUNNING THE PROJECT 

While starting the server you will start with login page where you can login or if not you can register by clicking on the link button for registeringand this will lead to a page where you can register your name and confirm your password.Next page is about creating a post with text and title in it.
You can edit,delete and chat by clicking on it.
