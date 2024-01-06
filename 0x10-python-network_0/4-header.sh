#!/bin/bash
# Send a GET request to a given URL with a header variable.
#curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
curl -sLX PUT -H "Origin: HolbertonSchool" -d "User_Id=98" 0.0.0.0:5000/catch_me```
