import requests 


def comunicar(url: str, method='GET', data=None, headers=None):

    def post(url, data):
        return requests.post(url, json=data)
    
    def get(url, data):
        return requests.get(url, data=data)
    
    if method == 'GET':
        return get(url, data)
    
    return post(url, data)