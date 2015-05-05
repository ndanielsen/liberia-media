#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Scrape admin module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""

import os
import csv
import datetime
import time


from scrape import Collector 


class Scraper_Admin(object):
	"""
	Simple control for the scraper function

	Takes a list of media content providers and optimately scrapes each page by logging the second when it was scraped and comparing it to the scrape-time limit


	#### Consider adding check_log to this to prevent Collector class from inititating

	"""


	def __init__(self, media=None, lowrange=1, highrange=5000, message="default", debug=True):

		

		self.range = xrange(lowrange, highrange)

		self.message = message

		self.media = media

		self.debug = debug

		self.cache = {site:0 for site, base_url, sleep in self.media}

		self.process_list = [(site, sleep, base_url + str(num)) for num in self.range for site, base_url, sleep in self.media ]

		self.filename = "data/url_logger.csv"

		global DEBUG
		DEBUG = self.debug


	#### runs through the first url and adds the name, time to cache

	#### checks the time to see which 

	def processor(self):

		while len(self.process_list) > 0: ### while there are urls in the list to process 

			try:

				queue = self.process_list[:25]

				for order in range(len(queue)): ### list only processes ten at a time
					site, sleep, url = queue[order]
					

					try:
						self.check_log(url)

						 ### checks the log file to see if it's already been requested
						elapsed_seconds = time.time() - self.cache[site]    #### checks the time delta

						if 	elapsed_seconds > sleep: # if the timedelta is greater than the sleep time
							Collector(name=site, urlraw=url, message=self.message, debug=DEBUG)
							self.cache[site] = time.time()
							del self.process_list[order]

							if DEBUG:
								print 'scraped: ', url, "secs: ", elapsed_seconds
							
						else:
							pass

					except NameError:
						del self.process_list[order]
						pass

			except IndexError:
				pass

		if DEBUG:
			print self.process_list
					
	def check_log(self, url):

		"""
		Checks the log file to see if the URL Raw has already been process.

		If processed already, it will continue to the next order

		Otherwise it will process the URL
		"""

		if not os.path.exists("data/"):
			os.makedirs("data/")
	
			if DEBUG:
				print "*** %s created" % ("data dir")


		if not os.path.isfile(self.filename):
			with open(self.filename, "w+") as f:
				columns = ["url_request", "url_status_code", "header_len", "response_len", "name",  "time", "message"]
				csv_writer = csv.writer(f)
				csv_writer.writerow(columns)

		else:
			with open(self.filename, 'r') as f:
				reader = csv.reader(f)
				for row in reader:
					if row[0] == url:
						

						if DEBUG:
							print "Already scraped", url
						raise NameError("URL has already been scraped")


	def main(self):

		
		self.processor()





if __name__ == '__main__':


	print 'compiles correctly'
	pass