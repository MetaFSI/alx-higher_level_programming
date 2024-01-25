#!/bin/bash
#Script sending request to a URL and displays the size of the body
curl -s "$1" | wc -c
