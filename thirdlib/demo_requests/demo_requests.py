import requests
from requests import session
import yaml


def ttest_get():
    with open("get.yaml", "r") as f:
        d = yaml.safe_load(f)
        res = requests.request(d["method"], d["url"])
    return res


def ttest_post():
    method = "get"
    url = "http://httpbin.org/get"
    res = session().request(method, url)
    return res


if __name__ == '__main__':
    r = ttest_get()
    print(r, f"{r=}, {type(r)=}")
    print(r.json())

