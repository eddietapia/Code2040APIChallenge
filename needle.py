import requests
import json


def main():
    """
    This file will be used to complete the third challenge for the Code2040 API Challenge
    This challenge is asking me to find the index of a particular string in an array of strings
    """
    try:
        # Initialize info to send post requests
        url = 'http://challenge.code2040.org/api/haystack'
        post_url = 'http://challenge.code2040.org/api/haystack/validate'
        my_token = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e'})
        headers = {'content-type': 'application/json'}

        # Get the dictionary that contain the string and array of strings
        dictionary = requests.post(url, data=my_token, headers=headers).json()
        needle = dictionary['needle']
        haystack = dictionary['haystack']

        # Search for the needle in the haystack
        for index in range(0, len(haystack)):
            if needle == haystack[index]:
                # Post the index back to the API
                answer = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e', 'needle': index})
                response = requests.post(post_url, data=answer, headers=headers)
                print response.content
    except Exception:
        # TODO: add logic to handle possible exception types
        raise

if __name__ == '__main__':
    main()
