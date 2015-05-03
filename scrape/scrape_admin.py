#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Scrape admin module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""

from scrape import Collector 


class Scraper_Admin(object):
	"""
	Simple control for the scraper function
	"""


	def __init__(self, name=None, urlraw=None, sleep=10, irange=None, message="default" ):

		self.name = name

		self.urlraw = urlraw

		self.sleep = sleep

		self.range = irange

		self.message = message




	def main(self):

		print self.name

		print self.urlraw

		print self.sleep

		print self.range

		print self.message



if __name__ == '__main__':

	test = Scraper_Admin(name="site", urlraw="url", sleep="sleep", message="test_extactor")

	test.main()
	

# if __name__ == "__main__":

# 	numbers = [num for num in range(1, 5000)]

# 	for num in numbers:
# 		# print num

# 		for site, base_url, sleep in media:

# 			url = base_url + str(num)

# 			print url, site, sleep
			
# 			Collector(name=site, urlraw=url, sleep=sleep, message="test_extactor")
# 		