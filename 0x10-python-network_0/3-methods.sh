#!/bin/bash
# all HTTP methods through the  server of a given URL will accept is displayed
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
