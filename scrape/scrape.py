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

	def __init__(self, name=None, urlraw=None, sleep=0, message="default", debug=False):
		self.name = name.lower().replace(" ", '')
		self.urlraw = urlraw
		self.sleep = float(sleep)
		self.message = message
		self.debug = debug
		self.cache = {}
		self.time = datetime.datetime.fromtimestamp(time.time())
		self.filename = "data/url_logger.csv"
		
		global DEBUG
		DEBUG = self.debug


		try:
			# self.check_log(self.urlraw)
			self.url = requests.get(urlraw) 
			self.status_code = self.url.status_code

			# print len(self.url.headers)

			if DEBUG:
				print "Waiting %s seconds after request" % self.sleep
				time.sleep(self.sleep) ### Added sleep timer here because easily place to control requests
			
		######################## Replace with Behavior Rules ######################

			### Load Scraping Rules
			### If  name === publication:

			### if length of header is less than something,
			### log it but don't save 

			if self.url.status_code != 200: # what about false positivies
				self.url_log()
				




			else:	
				self.main()

		#############################################################################3

		
		except requests.exceptions.ConnectionError:
			self.url = None
			self.status_code = None
			self.url_log()

			if DEBUG:
				print "ConnectionError Exception Caught"



	def url_log(self):
		"""    """
		
		
		data = [self.urlraw, str(self.status_code), len(self.url.headers), len(self.url.content) , self.name, str(self.time), self.message]

		with open(self.filename, 'a+') as f:
			csv_writer = csv.writer(f)
			csv_writer.writerow(data)

	def setUp(self):

		self.text = self.url.text # unicode
		self.headers = self.url.headers
		self.headers.update({"scrape_time": str(self.time)})
		self.content = self.url.content # string
		self.date = str(self.time)
		self.dirname = 'data/' + self.name + "/"
		self.log_file = self.name + "_log.json"
		self.log_path = self.dirname + self.log_file
		self.content_filename = self.date + ".txt"
		self.file_path = self.dirname + self.content_filename 

		if not os.path.exists(self.dirname):
			os.makedirs(self.dirname)
		
			if DEBUG:
				print "*** %s created" % (self.dirname)

		self.write_file()


	def load_log(self):
		"""
		Loads a serialized json file to a memory as the CACHE, otherwise creates the file.
		"""
		self.setUp()

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
		if DEBUG:
			print "Main executed at %s" % self.time
		
		self.url_log()
		self.setUp()
		self.load_log()
		self.updatecache()
		self.write_log()

		return self.content

		if DEBUG:
			print "All finished"



if __name__ == "__main__":

	Collector(name="liberianobserver", urlraw="http://www.liberianobserver.com/node/102", sleep=5)







