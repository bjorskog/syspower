# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
#import arctic
import pandas as pd
import datetime

def parse_date(date):
    try:
        return datetime.datetime.strptime(date, "%m/%d/%Y %H:%M %p")
    except:
        raise Exception("Error parsing datestring")

def read_config():
    """ reads the config-file """
    data = None
    with open('config.json') as f:
        data = json.loads(f.read())
    return data
    
class Client(object):
    """ a client for getting timeseries from syspower """

    _interval = None
    _user = None
    _pass = None

    _baseuri = "http://syspower.skm.no/webquery/webquery.aspx?series="

    def __init__(self, user, password):
        self._user = user
        self._pass = password
    
    def get_series(self, series, start, end="d", interval="day"):
        """ will retreve series """
        self._interval = interval
        periodstring = "&start=" + start + "&end=" + end
        
        uri = self._baseuri + series + periodstring + "&interval=" + self._interval + "&user=" \
              + self._user + "&pass=" + self._pass + "&headers=yes&updates=yes&emptydata=remove"
        print "Will get: %s" % uri
        data = pd.read_html(uri, index_col=0, header=0, parse_dates=True)[0]
        data["Timestamp"] = [parse_date(d) for d in data["Timestamp"]]
        return data

if __name__ == "__main__":
    config = read_config()
    print config
    client = Client(config["username"], config["password"])
    print client.get_series("SPOT", "d", "d", "hour")
