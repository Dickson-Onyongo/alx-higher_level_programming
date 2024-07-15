#!/bin/bash
# Script to Display all HTTP methods the server will accept using curl.
curl -sI "$1" | grep Allow | cut -f2- -d' '

