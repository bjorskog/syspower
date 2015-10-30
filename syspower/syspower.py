# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import json
import pandas as pd
import datetime

def parse_date(date):
    """ util for parsing timestamps """
    try:
        return datetime.datetime.strptime(date, "%m/%d/%Y %H:%M %p")
    except:
        raise Exception("Error parsing datestring")

def read_config():
    """ reads the config-file """
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, './config.json')
    with open(filename) as configfile:
        data = json.loads(configfile.read())
    return data

config = read_config()

class Client(object):
    """ a client for getting timeseries from syspower """

    _user = None
    _pass = None

    _baseuri = "http://syspower.skm.no/webquery/webquery.aspx?series="

    def __init__(self, user=None, password=None):
        """ constructor """
        if user is None:
            self._user = config["username"]
        if password is None:
            self._pass = config["password"]

    def get_series(self, series, start, end="d", interval="day", timestamps=True):
        """ will retreve series """
        periodstring = "&start=" + start + "&end=" + end
        uri = self._baseuri + series + periodstring + "&interval=" + interval + "&user="\
              + self._user + "&pass=" + self._pass + "&headers=yes&emptydata=remove"
        if timestamps:
            uri = uri + "&updates=yes"
            print "Will get: %s" % uri
        data = pd.read_html(uri, index_col=0, header=0, parse_dates=True)[0]
        if timestamps:
            data["Timestamp"] = [parse_date(d) for d in data["Timestamp"]]
        return data

if __name__ == "__main__":
    client = Client()
    data = client.get_series("SPOT", "d", "d", "hour")
