#!/usr/bin/python3
"""
Script that takes a URL and sends a request to it,
and displays value of the X-Request-Id variable
"""
from sys import argv
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        print(res.getheader("X-Request-Id"))
