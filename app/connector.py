import requests


class Connector:
    
    def __init__(self, name):
        self.name = name 
        self.url = f'https://{self.name}.com' 
    
    def get(self, id):
        r = requests.get(f'{self.url}/cadeaus/{id}')
        if r.ok:
            return r
        else:
            r.body('Bad response!')
            return r

    def post(self, id, payload):
        r = requests.post(f'{self.url}/cadeaus/{id}', data=payload)
        if r.ok:
            return r
        else:
            r.body('Bad response!')
            return r