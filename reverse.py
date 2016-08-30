import requests
import json


def main():
    """
    This file will be used to complete the first challenge for the Code2040 API Challenge
    This challenge is asking me to reverse a string
    """
    try:
        # Initialize info to send post requests
        url = 'http://challenge.code2040.org/api/reverse'
        post_url = 'http://challenge.code2040.org/api/reverse/validate'
        my_token = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e'})
        headers = {'content-type': 'application/json'}

        # Get the string that we will reverse
        word = requests.post(url, data=my_token, headers=headers).content

        # Reverse the string that we got from the API
        reverse = word[::-1]

        # Post the reversed string back to the API
        answer = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e', 'string': reverse})
        response = requests.post(post_url, data=answer, headers=headers)
        print response.content

    except Exception:
        # TODO: add logic to handle possible exception types
        raise

if __name__ == '__main__':
    main()
