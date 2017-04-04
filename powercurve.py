import numpy as N
import pandas as pd
import scipy 

windvar = 'wind'
powervar = 'power'

class PowerCurve:

    def __init__(self, powerCurveDictionary, turbineType):
        """
        Initialized power curvve based on dictionary of {wind:[], power:[]} type input
        """
        self.data = pd.DataFrame(data=powerCurveDictionary)
        self.windvar = windvar
        self.powervar = powervar
        self.turbineType = turbineType

    def GeneratePolynomials(self, order):
        """
        Generates a polynomial of order ORDER for the partial load region of the power curve
        """
        #For each unique fitRegion, develop a ORDER polynomial fit
        fitRegions = pd.unique(self.data['fitRegion'])
        self.interpolatedDataFrames = []
        self.polynomials = []
        self.test = self.data.copy()
        self.maxWinds = []
        self.minWinds = []

        for n in fitRegions:
            points = self.data.fitRegion == n
            tempData = self.data[points]
            minidx = 0 if tempData.index.min() == 0 else tempData.index.min()-1
            maxidx = tempData.index.max()
            minWind = self.data[windvar][minidx]
            maxWind = self.data[windvar][maxidx]
            tempData = self.data[minidx:maxidx+1]
            interpWind = N.arange(minWind, maxWind, 0.1)
            coeffs = N.polyfit(tempData[windvar],tempData[powervar],order)
            polynomial = N.poly1d(coeffs)
            self.polynomials.append(polynomial)
            interpolatedData = {windvar:interpWind, powervar:polynomial(interpWind)}
            self.interpolatedDataFrames.append(pd.DataFrame(interpolatedData))
            self.maxWinds.append(maxWind)
            self.minWinds.append(minWind)

            #Generate interpolated values
            #self.test = pd.merge(self.test, tempData[tempData[windvar].isin(self.test[windvar])], how = 'left', on = windvar)
        self.interpolatedCurve = pd.concat(self.interpolatedDataFrames)
        #self.test = pd.merge(self.data, self.interpolatedCurve[self.interpolatedCurve[windvar].isin(self.data[windvar])], how = 'left', on = windvar)

    def Plot(self):
        """
        Plots powercurve.Data with label of the turbine type
        """
        ax = self.data.plot(kind='scatter', x = windvar, y = powervar, color = 'DarkBlue', label = 'Actual')
        for n in N.arange(0,len(self.interpolatedDataFrames)):
            self.interpolatedDataFrames[n].plot(kind='line', x = windvar, y = powervar, color = 'Red', label = 'Region %s'%n, ax = ax)
        

    def GenerateBazeTagFormula(self):
        """
        Generates string expression for power curve 
        """
        wdspdTag = 'TagTimeAvg([${Site}-${WTG}-WindSpeed])'
        strings = []
        strings.append("Expression=If(%s>%s||%s<%s,0.0"%(wdspdTag, max(self.data[windvar]), wdspdTag, min(self.data[windvar])))
        for i,n in enumerate(self.maxWinds):
            condition = "If(%s<%s,"%(wdspdTag,  n)
            polyLen = len(self.polynomials[i])
            formula = '+'.join(['%s*%s'%(xx,wdspdTag+'^'+str(polyLen-ii)) if (abs(xx) > 0.00000001 or ii == polyLen) else '' for ii,xx in enumerate(self.polynomials[i])])
            strings.append(condition + formula)

        #Replace needed polynomial coeffs
        bazeTagFormula = ','.join(strings) + ')|Interval=600|StartTime=00:00|PeriodInterval=600'
        
        bazeTagFormula2 = bazeTagFormula.replace('++','+')
        bazeTagFormula3 = bazeTagFormula2.replace('++','+')
        bazeTagFormula4 = bazeTagFormula3.replace('++','+')
        bazeTagFormula5 = bazeTagFormula4.replace('++','+')
        bazeTagFormula6 =bazeTagFormula5.replace(',+',',')
        bazeTagFormula7 = bazeTagFormula6.replace('*'+wdspdTag+'^0','')
        bazeTagFormula8 = bazeTagFormula7.replace('+-','-')
        self.bazeTagFormula = bazeTagFormula8.replace('^1','')
        
        return self.bazeTagFormula



