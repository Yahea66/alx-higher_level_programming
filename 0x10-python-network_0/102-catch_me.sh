#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -o /div/null -w "You got me!" 0.0.0.0:5000/catch_me
