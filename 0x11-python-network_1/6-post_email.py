#!/usr/bin/python3
"""
Sends a POST request to a URL with an email...
"""

if __name__ == "__main__":
    import sys
    import requests

    responses = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(responses.text)
