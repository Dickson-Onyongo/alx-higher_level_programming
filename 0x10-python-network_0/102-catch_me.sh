#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT -H "Origin: ALXSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
