import numpy as np
import pandas as pd
import scipy
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.pylab as pylab

windFarm = {}
windFarm['Demo1'] = {'windWeibull':1.8, 
                     'windMean': 8.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 75 ,
                     'startingAvail': 73 ,
                     'ratedPower': 1.8,
                     'maxUnavail':8,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo2'] = {'windWeibull':1.7, 
                     'windMean': 7.1, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 40 ,
                     'startingAvail': 39 ,
                     'ratedPower': 3.0,
                     'maxUnavail':5,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo3'] = {'windWeibull':1.8, 
                     'windMean': 7.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 120 ,
                     'startingAvail': 115 ,
                     'ratedPower': 1.5,
                     'maxUnavail':10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo4'] = {'windWeibull':2.0, 
                     'windMean': 6.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines':102 ,
                     'startingAvail': 91 ,
                     'ratedPower': 1.5,
                     'maxUnavail':30,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo5'] = {'windWeibull':1.8, 
                     'windMean': 8.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 60 ,
                     'startingAvail': 60 ,
                     'ratedPower': 2.5,
                     'maxUnavail':5,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo6'] = {'windWeibull':1.8, 
                     'windMean': 10.0, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 18 ,
                     'startingAvail': 16 ,
                     'ratedPower': 2.3,
                     'maxUnavail':10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo7'] = {'windWeibull':1.8, 
                     'windMean': 6.9, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 72 ,
                     'startingAvail': 69 ,
                     'ratedPower': 1.65,
                     'maxUnavail': 10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo8'] = {'windWeibull':1.8, 
                     'windMean': 12.1, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 54 ,
                     'startingAvail': 10 ,
                     'ratedPower': 2.3,
                     'maxUnavail':10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Demo9'] = {'windWeibull':1.8, 
                     'windMean': 8.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 48 ,
                     'startingAvail': 47 ,
                     'ratedPower': 2.0,
                     'maxUnavail':5,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }


windFarm['Dem10'] = {'windWeibull':1.8, 
                     'windMean': 8.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 108 ,
                     'startingAvail': 107 ,
                     'ratedPower': 2.0,
                     'maxUnavail':10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Dem11'] = {'windWeibull':1.5, 
                     'windMean': 13.0, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 24 ,
                     'startingAvail': 23 ,
                     'ratedPower': 6.0,
                     'maxUnavail':4,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Dem12'] = {'windWeibull':1.5, 
                     'windMean': 10.0, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 30 ,
                     'startingAvail': 30 ,
                     'ratedPower': 3.2,
                     'maxUnavail':1,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Dem13'] = {'windWeibull':1.8, 
                     'windMean': 8.5, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 84 ,
                     'startingAvail': 83 ,
                     'ratedPower': 2.3,
                     'maxUnavail':3,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Dem14'] = {'windWeibull':1.8, 
                     'windMean': 9.3, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 90 ,
                     'startingAvail': 87 ,
                     'ratedPower': 2.1,
                     'maxUnavail':10,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }

windFarm['Dem15'] = {'windWeibull':1.8, 
                     'windMean': 6.0, 
                     'timeIncrement':  10, 
                     'availIncrement': 60, 
                     'numberTurbines': 102 ,
                     'startingAvail': 100 ,
                     'ratedPower': 2.0,
                     'maxUnavail':20,
                     'startTime': '2017-01-01',
                     'endTime': '2017-03-08'
                     }






def generateTimeSeriesData(startTime, endTime,  numberTurbines, ratedPower, startingAvail, timeIncrement = 5, availIncrement = 60, windWeibull = 1.8, windMean = 10.0, maxUnavail = 10):

    dstart          = datetime.datetime.strptime(startTime, '%Y-%m-%d')
    dend            = datetime.datetime.strptime(endTime, '%Y-%m-%d')
    drepeat         = dstart + datetime.timedelta(days=1)
    data = {}
    data['time']    = np.array(pd.date_range(start=dstart, end=dend,    freq='%is'%timeIncrement))
    dataLen         = len(data['time'])
    rand = np.random.uniform(-1,1)
    randseed = 1 if rand > 0 else -1

    #develop wind signal
    data['wind'] = np.array([])
    data['time'] = np.array([])
    while dstart < dend:  
        todaytime    = dstart + np.arange(86400/timeIncrement) * datetime.timedelta(seconds=timeIncrement)
        dataLen      = len(todaytime)
        x            = np.arange(0,2*np.pi,2*np.pi/len(todaytime)) 
        mean         = windMean*(1+randseed*np.cos(x)*np.random.uniform(0,0.5))
        turb         = np.random.normal(0,0.1,dataLen)*windMean
        windmin      = np.random.uniform(0.5,1.5,dataLen)
        wind         = np.maximum(np.maximum(mean,windmin) + turb,windmin)
        data['wind'] = np.append(data['wind'], wind)
        data['time'] = np.append(data['time'],todaytime)
        dstart       += datetime.timedelta(days=1)
        
    #generate step function type for available turbines (changes every 'availIncrement' period)
    availdata = {}
    dstart          = datetime.datetime.strptime(startTime, '%Y-%m-%d')
    timerange = np.array(pd.date_range(start=dstart, end=dend, freq='%is'%availIncrement))
    availdata['time']    = dstart + np.arange(len(timerange)) * datetime.timedelta(seconds=availIncrement)
    availdata['available'] = np.random.randint(startingAvail-maxUnavail, startingAvail, len(availdata['time']))
    availdata['unavailable'] = numberTurbines - availdata['available']

    df_avail = pd.DataFrame(availdata)
    df = pd.DataFrame(data)

    #fill in missing available timestamps to make data square and non-null
    df = pd.merge(df,df_avail,how='left',on='time')
    df = df.fillna(method='ffill')

    #calculate power with simple model
    df['power'] = df['available']*ratedPower*np.minimum(df['wind']/18.0,1.0)
    return df


tagDict = {'time':'TIMEUTC','wind':'Calc-AverageWindSpeed', 'power': 'Calc-ActivePowerMW', 'available':'CALC-AvailableWTGs', 'unavailable':'CALC-UnavailableWTGs'}
def writeBazeData(windFarm, dataFrame, tagMapping = tagDict, dataType = 'RAW'):

    #header/column information
    startTime   = datetime.datetime.strftime(dataFrame['time'].min(),'%d.%m.%Y') + ' 00:00:00'
    endTime     = datetime.datetime.strftime(dataFrame['time'].max(),'%d.%m.%Y') + ' 00:00:00'
    bazeTimes   = [datetime.datetime.strftime(t, '%d.%m.%Y %H:%M:%S') for t in dataFrame['time']]
    header      = "%s Data\nStart Time: %s\nEnd Time: %s\n"%(dataType, startTime, endTime)
    keyOrder = ['time'] + [k for k in tagDict.keys() if k!='time']
    tagOrder = ['TIMEUTC'] + ['%s-'%windFarm + tagDict[k] for k in keyOrder if k!='time']
    colheader = "\t".join(['%s'%tag for tag in tagOrder])
    totalheader = header + colheader + "\n"

    #write data
    dataFrame['bazeTimes'] = bazeTimes

    with open('DataImport/%s.txt'%windFarm, 'w') as file:
        file.write(totalheader)
        dataFrame.to_csv(file, columns = keyOrder, sep = '\t', index=False, header=False) 

def generateBatchData(windFarm):
    for k in windFarm.keys():
        print(k)
        df = generateTimeSeriesData(startTime = windFarm[k]['startTime'],
                                    endTime   = windFarm[k]['endTime'],
                                    numberTurbines = windFarm[k]['numberTurbines'],
                                    ratedPower = windFarm[k]['ratedPower'],
                                    startingAvail = windFarm[k]['startingAvail'],
                                    timeIncrement = windFarm[k]['timeIncrement'],
                                    availIncrement = windFarm[k]['availIncrement'],
                                    windWeibull = windFarm[k]['windWeibull'],
                                    windMean = windFarm[k]['windMean'],
                                    maxUnavail = windFarm[k]['maxUnavail'])
        
        try:
            ax = df.plot('time','wind')
            fig = ax.get_figure()
            fig.savefig('DataImport/%s_Wind.png'%k)
            pyplot.close(fig)

            ax = df.plot('time','power')
            fig = ax.get_figure()
            fig.savefig('DataImport/%s_power.png'%k)
            pyplot.close(fig)

            ax = df.plot('time','available')
            fig = ax.get_figure()
            fig.savefig('DataImport/%s_available.png'%k)
            pyplot.close(fig)
        except:
            pass

        
        writeBazeData(k, df, tagMapping = tagDict, dataType = 'RAW')