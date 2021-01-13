import requests
import logging
import logger

logger = logging.getLogger(__name__)


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
            logger.warning(f'GET request  (to {self.url}/cadeaus/{id}) not succesful')
            return r

    def post(self, id, payload):
        r = requests.post(f'{self.url}/cadeaus/{id}', data=payload)
        if r.ok:
            logger.info(f'POST request (for {self.name}) succesfully made')
            return r
        else:
            r.body('Bad response!')
            logger.warning(f'POST request  (to {self.url}/cadeaus/{id}) not succesful')
            return r