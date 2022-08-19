import requests
import json


def main(words):
    url = "http://127.0.0.1:5000/info/translate"

    data = {
        "words": words
    }

    resp = requests.post(url, data=json.dumps(data))
    translate = resp.text
    return translate


if __name__ == '__main__':
    words = "I love China"
    ret = main(words)
    print(ret)
