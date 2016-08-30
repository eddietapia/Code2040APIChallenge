import requests
import json
import iso8601
from datetime import timedelta


def main():
    """
    This file will be used to complete the fifth challenge for the Code2040 API Challenge
    In this challenge, given a dictionary, we are given the value for an ISO 8601 'datestamp',
    and we will need to add the value 'interval' to that date, and return the resulting date
    to the API
    """
    try:
        # Initialize info to send post requests
        url = 'http://challenge.code2040.org/api/dating'
        post_url = 'http://challenge.code2040.org/api/dating/validate'
        my_token = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e'})
        headers = {'content-type': 'application/json'}

        # Get the dictionary that contain the prefix and array of strings
        dictionary = requests.post(url, data=my_token, headers=headers).json()
        date = dictionary['datestamp']
        interval = dictionary['interval']

        # Add the interval to the date and format it
        new_date = str((iso8601.parse_date(date) + timedelta(seconds=interval)).replace(tzinfo=None).isoformat()) + 'Z'

        # Post the new date back to the API
        answer = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e', 'datestamp': new_date})
        response = requests.post(post_url, data=answer, headers=headers)
        print response.content
    except Exception:
        # TODO: add logic to handle possible exception types
        raise

if __name__ == '__main__':
    main()
