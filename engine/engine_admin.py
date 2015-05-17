#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Database engine controller for content extraction 

Using SQLlite because it's easy

Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""

import csv
from dateutil import parser 
import datetime 
import time

from engine import Engine

class Engine_Admin(object):
    """Control for Database Operations"""

    def __init__(self, engine=None, log=None, content=None, image=None, scraperlog=None, debug=True):


        pass


    def main():

        pass


class Engine_URL_Logger(object):

    def __init__(self, engine=None, inputfile=None, debug=True):

        self.urlengine = engine
        self.inputfile = inputfile
        self.debug = debug

        self.main()

    def main(self):

        self.loglist = []
        with open(self.inputfile, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                url_request = unicode(row[0])  
                url_status_code = row[1]
                header_len = row[2]
                response_len = row[3]
                name = unicode(row[4]) 
                timedate = parser.parse(row[5])
                message = unicode(row[6])
                scraperlog = timedate, url_request, url_status_code, header_len, response_len, name, message
                self.loglist.append(scraperlog)

        Engine(engine=self.urlengine, scraperlog=self.loglist, debug=self.debug)


if __name__ == "__main__":

    print 'hello'

    Engine_URL_Logger(engine='liberia_main', inputfile="data/url_logger.csv" )
