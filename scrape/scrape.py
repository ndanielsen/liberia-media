#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Scraping module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""

import csv
import datetime 
import json
import os
import time

import requests
# from bs4 import BeautifulSoup



class Collector(object):
	"""
	Downloads a unique page to a data folder and files the page header into a json object with 'link' being the key
	"""

	global DEBUG
	DEBUG = True


	def __init__(self, name=None, urlraw=None, sleep=None):
		self.name = name.lower().replace(" ", '')
		self.urlraw = urlraw
		self.sleep = float(sleep)

		self.cache = {}
		self.time = datetime.datetime.fromtimestamp(time.time())

		try:

			# Check log for url			
			self.check_log()

			self.url = requests.get(urlraw) 
			self.status_code = self.url.status_code

			if DEBUG:
				print "Waiting ten seconds after request"

			time.sleep(self.sleep) ### Added sleep timer here because easily place to control requests
			
			if self.url.status_code != 200:
				self.url_log()
	
			else:	

				self.main()

			if DEBUG:

				print "Main executed at %s" % self.time
		
		except requests.exceptions.ConnectionError:
			self.url = None
			self.status_code = None
			self.url_log()


			if DEBUG:

				print "ConnectionError Exception Caught"

		except NameError: # if URL already in logger

			pass

	def check_log(self):
		"""
		Checks the log file to see if the URL Raw has already been process.

		If processed already, it will continue to the next order

		Otherwise it will process the URL
		"""



		filename = "url_logger.csv"

		if not os.path.isfile(filename):
			with open(filename, "w+") as f:
				columns = ["url_request", "url_status_code", "name",  "time"]
				csv_writer = csv.writer(f)
				csv_writer.writerow(columns)
				


		else:
			with open(filename, 'r') as f:

				reader = csv.reader(f)

				for row in reader:
	


					if row[0] == self.urlraw:
						if DEBUG:
							print "Already scraped"
						raise NameError("URL has already been scraped")
					
				

			# self.urlraw, str(self.status_code)


	def url_log(self):
		"""    """
		filename = "url_logger.csv"
		columns = ["url_request", "url_status_code", "name",  "time"]
		data = [self.urlraw, str(self.status_code), self.name, str(self.time)]



		with open(filename, 'a+') as f:
			csv_writer = csv.writer(f)
			csv_writer.writerow(data)
				

	#### NEED to write unique HEADER identification class for each site being scrapped			




	def setUp(self):

		self.text = self.url.text # unicode
		self.headers = self.url.headers
		self.headers.update({"scrape_time": str(self.time)})

		self.content = self.url.content # string
		
		# self.date = self.headers['date'].replace(',','').replace(' ','_') ### update to the time scrapped

		self.date = str(self.time)
		
		self.dirname = 'data/' + self.name + "/"
		self.log_file = self.name + "_log.json"
		self.log_path = self.dirname + self.log_file

		# self.filename = self.headers['content-length'] + "_" + self.date + ".txt" ### removed to generalize to other media sitess

		self.filename = self.date + ".txt"

		self.file_path = self.dirname + self.filename 


		if not os.path.exists(self.dirname):
			os.makedirs(self.dirname)
			
			if DEBUG:

				print "*** %s created" % (self.dirname)

		self.write_file()


	def load_log(self):
		"""
		Loads a serialized json file to a memory as the CACHE, otherwise creates the file.
		"""
		if os.path.isfile(self.log_path):
			with open(self.log_path, 'r+') as outfile:
			 	data = json.load(outfile)
			 	self.cache.update(data)
		else:
			
			if DEBUG:
				print "*** %s created" % (self.log_file)

			pass

	def write_log(self):
		"""Writes the CACHE to JSON serialized file	"""		

		with open(self.log_path, 'w+') as outfile:
			json.dump(self.cache, outfile, sort_keys=True, indent=4)
			
			if DEBUG:
				print "Log loaded"



	def updatecache(self):
		""" 
		Checks to see if the publication and story has been collected. If false, it will add the publication and story to CACHE.  
		"""
		try:
			key = self.urlraw	#Link is an content specific headers, redirects do not have this
			if key not in self.cache:
				self.cache[key] = dict(self.headers)
				self.write_file()

				if DEBUG:
					print "Content added"
			else:
				if DEBUG:
					print "Content already present"
				
		except KeyError:
			key = self.urlraw
			self.cache[key] = None
			if DEBUG:
				print "Content does not exist"




			

	def write_file(self):
		"Writes response to file with unique identifer"

		with file(self.file_path, 'w+') as outfile:
			outfile.write(self.content)
		
			if DEBUG:
				print "%s written" % (self.file_path)

		pass


	def main(self):


		self.url_log()
		self.setUp()
		self.load_log()
		self.updatecache()
		self.write_log()
		



		if DEBUG:
			print "All finished"



if __name__ == "__main__":

	Collector(name="liberianobserver", urlraw="http://www.liberianobserver.com/node/102", sleep=5)






