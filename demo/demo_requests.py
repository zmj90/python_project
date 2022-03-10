import json

import requests


class DemoRequests:
    def __init__(self):
        self.url = "http://httpbin.org"

    def url(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get(self.url + "/get", params=payload)
        print(r.url)

    def text(self):
        r = requests.get(self.url + "/get")
        print(r)
        print("----------")
        print(r.text)
        print("----------")
        print(type(r.text))
        return r.text

    def content(self):
        ...


if __name__ == '__main__':
    demo1 = DemoRequests()


    # demo1.text()
    # demo1.content()


