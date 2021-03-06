# Technical Assessment (From Offerzen)

## I am tasked to create a function to do a bubble sort and eventually dockerize and automate everything

# My Thinking:

* Initialize git repo!
    * This is necessary for backing up my code but also integration and automation

* Write Unit Test
    * TDD is important - Write a test first. Then write the code that makes it work!

* Write code to do a bubble sort
    * It took some iterations to get it working correctly

* Test
    * I like to test everything as far as I go

* Configure a server for the API
    * A simple flask app with very basic config is good for this assignment

* Dockerize
    * Maked the solution shippable and easily deployable

* Automate
    * Automate all the things

* Python modules to install
    * flask 

- - - -

# Important Notes

* **curlsort.sh** is a script to do 3 curl commands pointing to the local application "server" which will return the sorted list
* **setup-python-environment.sh** is a cool little script which works excellent for big python projects with many dependencies (Ideally combine it with venv)
* **run-api.sh** is the script which runs the unit tests and upon success will start the application server

- - - -
## Questions

# How is the application limited by available resources?

The application is fortunately very lightweight and should consume very few resources.  
It can run on any server/cloud service which provides the option of running docker containers.
If it was a real world project, I would implement some for of monitoring of resources regarding the cloud service/server to ensure any limited resources are picked up and scaled before it becomes an issue.
I was also able to run the image on a corporate server and hit the api from my machine while connected to the vpn.

# How would I host the service?

As everything regarding running the application is already automated and dockerized, I now have a very compact, shippable solution to simply deploy on any UNIX server/system.  I would prefer to have it deployed on a scalable cloud platform which can also autoscale if configured correctly.  Thus I can then host my application without worrying about the amount of requests versus resources. A scalable AWS EC2 instance might be a simple and easy solution.

# How long did this assignment take and what did I spend my time on?

The total working hours was around 6 hours.  Challenges and rough time spent:
* Corporate VPN and Proxies
    * I wasted about 2-2.5 hours configuring my local machine to be able to bypass proxies to github and python libraries etc.
* Docker image not running on the corporate server
    * 1 hour - I eventually figured that the issue was because of a chmod command which is not supported on the alpine image I used
* Unit test failing due to output from unit test being different than output recieved by manually calling the method with exact same parameters
    * 1.5 hour

# What I like to have done differently in my solutions?

* I would have liked to have it hosted on a web service and have more free time to do assignments like this one
* I would have made my file structures better and to have a better test environment for personal projects
