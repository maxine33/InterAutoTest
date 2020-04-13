from utils.RequestsUtil import Requests


def login():
    url = "http://211.103.136.242:8064/authorizations/"
    data = {
        "username": "python",
        "password": "12345678"
    }
    # r = requests.post(url, json=data)
    request = Requests()
    r = request.post(url, json=data)
    print(r)


def infor():
    url = "http://211.103.136.242:8064/user"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODU3ODk5MTIsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.niRQazRzXu98V7gVJgfvmjNd9bgiIYBHJHZWLfQ_RVk"
    headers = {
        "Authorization": "JWT" + token
    }
    request = Requests()
    r = request.get(url, headers=headers)
    print(r)


if __name__ == '__main__':
    login()
    infor()
