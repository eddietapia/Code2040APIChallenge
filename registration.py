import requests
import json


def main():
    """
    This file will be used to register my account for the API challenge
    """
    try:
        # Initialize info to send the post request
        url = 'http://challenge.code2040.org/api/register'
        my_info = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e',
                   'github':'https://github.com/etapiahe/Code2040APIChallenge.git'})
        headers = {'content-type': 'application/json'}

        # Send the post request
        response = requests.post(url, data=my_info, headers=headers)
        print response.content
    except Exception:
        # TODO: add logic to handle possible exception types
        raise

if __name__ == '__main__':
    main()
