import requests
from core.config import Config

class APIClient:
    #Generic rapper for requests
    #handles Base url and session management and timeouts.
    def __init__(self):
        self.base_url=Config.BASE_URL_API
        self.session=requests.Session()
        self.session.headers.update({"Content-Type":"application/json","Accept":"application/json"})

    def get(self,endpoint:str,params:dict=None)->requests.response:
        # generic get request
        url=f"{self.base_url}/{endpoint}"
        print(f"INFO:API:GET {url} with params {params}")
        response=self.session.get(url,params=params,timeout=Config.TIMEOUT/1000)
        return response

    def post(self,endpoint:str,payload:dict)->requests.response:
        #generic post request 
        url=f"{self.base_url}/{endpoint}"
        print(f"INFO:API:POST {url} with payload {payload}")
        response=self.session.post(url,json=payload,timeout=Config.TIMEOUT/1000)
        return response