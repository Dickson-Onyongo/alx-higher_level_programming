#!/usr/bin/python
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)

"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.arg[2]}).encode('ascii')
    req = urllib.request.Reqest(sys.argv[1], data
)
    with urllib.request.urlopen(req) as response:
        response = response.read()
        print('Your email is: {}'.format(response.decode('utf-8')))
