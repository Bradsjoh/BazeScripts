import numpy as N
import requests as r
import json
import pandas 

serverName = 'https://demo.bazefield.com/Bazefield.Services/api'
user = 'Administrator'
password = 'B@ze!2015'
query = 'measurements/[WFU-T09-WindSpeed,WFU-T09-ActivePower,WFU-T11-WindSpeed,WFU-T11-ActivePower]/aggregates/[3,3,3,3]/from/*-7d/to/*/interval/600000?format=json'

class pyBaze:

    def __init__(self, serverName = serverName, username = user, password = password):
        """
        Initialize a connection to baze demo server, and return a pyBaze server object
        """
        self.serverName = serverName
        self.userName = username
        self.password = password 
        response = self.authenticate()
        jsondata = json.loads(response.text)
        self.sessionId = jsondata['sessionId']

    def authenticate(self, mediaType="application/json"):
        """
        Authenticate a session based on username and password
        """
        urlstr = "/auth/baze?format=json"
        payload = {"UserName": self.userName, "Password": self.password, "mediaType":mediaType}
        response = r.post(serverName+urlstr, data = payload)
        return response

    def getJsonData(self, query):
        """
        Return data in the form of a pandas DataFrame from a query and authenticated session
        """
        dataresponse = r.get(self.serverName+query, headers={'MediaType':'application/json','x-ss-id':self.sessionId})
        data = json.loads(dataresponse.text)['timeSeriesList'][0]['timeSeries']
        pd = pandas.DataFrame(data)
        return pd








   


