import requests
import json


def main():
    """
    This file will be used to complete the fourth challenge for the Code2040 API Challenge
    This challenge is asking me to return an array containing only the strings that do not start
    with a prefix. We are given a prefix(string) and array of strings
    """
    try:
        # Initialize info to send post requests
        url = 'http://challenge.code2040.org/api/prefix'
        post_url = 'http://challenge.code2040.org/api/prefix/validate'
        my_token = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e'})
        headers = {'content-type': 'application/json'}
        my_list = []

        # Get the dictionary that contain the prefix and array of strings
        dictionary = requests.post(url, data=my_token, headers=headers).json()
        prefix = dictionary['prefix']
        array = dictionary['array']

        # Search for words that do not start with the prefix, case insensitive
        for index in range(0, len(array)):
            if not array[index].lower().startswith(prefix.lower()):
                my_list.append(array[index])

        # Post the list back to the API
        answer = json.dumps({'token': '3de4e34b13ebc2912ab209a77aec363e', 'array': my_list})
        response = requests.post(post_url, data=answer, headers=headers)
        print response.content
    except Exception:
        # TODO: add logic to handle possible exception types
        raise

if __name__ == '__main__':
    main()
