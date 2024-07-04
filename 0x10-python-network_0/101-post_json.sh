#!/bin/bash
# Send a Json request to a known URL with a given file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
