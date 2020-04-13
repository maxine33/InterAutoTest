# requesrs类的封装
"""
封装
1、先定义方法a.b（小功能）
2、定义类A（理解成一个房间）
3、将所有功能的相同点定义成一个公共方法A_1
4、然后再重新定义方法ab并调用公共方法
"""

import requests


# 创建封装get方法
def requests_get(url, header):
    r = requests.get(url, header=header)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res['code'] = code
    res['body'] = body
    return res


def requests_post(url, json=None, headers=None):
    r = requests.post(url, json=json, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res['code'] = code
    res['body'] = body
    return res


class Requests:
    def __init__(self):
        pass

    def requests_api(self, url, json=None, data=None, headers=None, method=None):
        if method == "get":
            r = requests.get(url, data=data, json=json)
        elif method == "post":
            r = requests.post(url, data=data, json=json, headers=headers)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res['code'] = code
        res['body'] = body
        return res

    def get(self, url, **kwargs):
        return self.requests_api(url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.requests_api(url, method='post', **kwargs)
