#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Scraping module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""
import os
import json

import requests
# from bs4 import BeautifulSoup



class Collector(object):
	"""
	Downloads a unique page to a data folder and files the page header into a json object with 'link' being the key
	"""

	global DEBUG
	DEBUG = True


	def __init__(self, name, urlraw):
		self.name = name.lower().replace(" ", '')
		self.urlraw = url
		self.url = requests.get(url)
		self.status_code = self.url.status_code
		self.text = self.url.text # unicode
		self.headers = self.url.headers
		self.content = self.url.content # string
		
		self.date = self.headers['date'].replace(',','').replace(' ','_')
		
		self.dirname = 'data/' + self.name + "/"
		self.log_file = self.name + "_log.json"
		self.log_path = self.dirname + self.log_file

		self.filename = self.headers['content-length'] + "_" + self.date + ".txt"
		self.file_path = self.dirname + self.filename 

		self.cache = {}

	def	initialize(self):
		
		self.url = requests.get(url) 
		self.status_code = self.url.status_code
		self.text = self.url.text # unicode
		self.headers = self.url.headers
		self.content = self.url.content # string
		
		self.date = self.headers['date'].replace(',','').replace(' ','_')
		
		self.dirname = 'data/' + self.name + "/"
		self.log_file = self.name + "_log.json"
		self.log_path = self.dirname + self.log_file

		self.filename = self.headers['content-length'] + "_" + self.date + ".txt"
		self.file_path = self.dirname + self.filename 




	def setup_Dir(self):
		
		if not os.path.exists(self.dirname):
			os.makedirs(self.dirname)
			
			if DEBUG:
				print "*** %s created" % (self.dirname)


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

			key = self.headers['link']		#Link is an content specific headers, redirects do not have this
					
			if key not in self.cache:
				self.cache[key] = dict(self.headers)
				self.write_file()

			if DEBUG:
				print "Content added"


			else:
				if DEBUG:
					print "Content already present"

				pass

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

		# self.initialize()
		self.setup_Dir()
		self.load_log()
		self.updatecache()
		self.write_log()
		

		if DEBUG:
			print "All finished"






if __name__ == "__main__":

	print "Hello"

	base_url = "http://www.liberianobser3ver.com/node/"

	node = 99

	url = base_url + str(node)

	test = Collector("liberianobserver", url)

	test.main()

