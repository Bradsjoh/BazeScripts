import numpy as N
import requests as r
import json
import pandas
from datetime import datetime

class pyBaze:

    def __init__(self, serverName, apiKey, rootApiUrl='/Bazefield.Services/api'):
        """
        Initialize a connection to baze demo server, and return a pyBaze server object
        """
        self.baseUrl = serverName + rootApiUrl
        self.apiKey = apiKey
        self.bearer = 'Bearer ' + apiKey
        self.header = {'mediaType':'application/json','Authorization':self.bearer}

    def getRawMeasurementsJson(self, tag, start, end):
        apiQuery = '/measurements/' + tag + '/from/' + start + '/to/' + end + '?format=json'
        dataresponse = r.get(self.baseUrl+apiQuery, headers=self.header)
        data = json.loads(dataresponse.text)
        return data
		
    def getRawMeasurementsPandas(self, tag, start, end):
        """
        Return raw data in the form of a pandas array from a query and authenticated session
        """
        pd = pandas.DataFrame()
        data = self.getRawMeasurementsJson(tag,start,end)
        tempPd = pandas.DataFrame(data['timeSeriesList'][0]['timeSeries'])
        name = data['timeSeriesList'][0]['measurementName']
        pd['TimeUtc'] = [datetime.fromtimestamp(i/1000) for i in tempPd['t']]
        pd[name] = tempPd['v']
        return pd
		
    def getAggregatesJson(self, tag, start, end, aggregate, intervalSec):
        """
		Return tag(s) in json
        """
        interval = str(intervalSec*1000)
        apiQuery = '/measurements/' + tag + '/aggregates/' + aggregate + '/from/' + start + '/to/' + end + '/interval/' + interval + '?format=json'
        dataresponse = r.get(self.baseUrl+apiQuery, headers=self.header)
        data = json.loads(dataresponse.text)
        return data
		
    def getAggregatesPandas(self, tags, start, end, aggregate, intervalSec):
        """
        Return tag(s) in a pandas dataFrame
        """
        pd = pandas.DataFrame()
        if type(tags) == str:
            tags = [tags]
        for tag in tags:
            tempJson = self.getAggregatesJson(tag,start,end,aggregate,intervalSec)
            tempPd = pandas.DataFrame(tempJson['timeSeriesList'][0]['timeSeries'])
            name = tempJson['timeSeriesList'][0]['measurementName']
            pd['TimeUtc'] = [datetime.fromtimestamp(i/1000) for i in tempPd['t']]
            pd[name] = tempPd['v']
        return pd

    def getAllocationsJson(self, allocationType, assets, start, end):
        """
        Return raw allocations to Json
		"""
        apiQuery = '/allocations/' + allocationType + '/from/' + start + '/to/' + end + '?turbineids=' + assets + '&format=json'
        dataresponse = r.get(self.baseUrl+apiQuery, headers=self.header)
        data = json.loads(dataresponse.text)
        return data

    def getAllocationStats(self, allocationType, assets, start, end, includeAvailable = 1, includeExcluded = 1, groupBy='categories'):
        """
        Return allocation stats to json
		"""
        apiQuery = '/turbines/allocations/' + allocationType + '/statistics/from/' + start + '/to/' + end + '?turbineids=' + assets + '&includeAvailable=' + str(includeAvailable) + '&includeExcluded=' + str(includeExcluded) + '&chartGroup=' + groupBy + '&format=json'
        dataresponse = r.get(self.baseUrl+apiQuery, headers=self.header)
        self.baseUrl+apiQuery
        data = json.loads(dataresponse.text)
        return data


	
			
			
	








   


