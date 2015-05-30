#!/usr/local/bin/python

import unittest
from scrape import scrape

class TestScrape(unittest.TestCase):

	def setUp(self):
		self.collector = scrape.Collector('Httpbin', 'http://httpbin.org/')
		self.text = self.collector.text
		self.headers = self.collector.headers
		self.content = self.collector.content
		self.name = self.collector.name

	
	def test_the_world_is_sane(self):
		self.assertEquals(1+1, 2)

	def test_Confirm_Connection(self):
		self.assertEquals(self.collector.status_code, 200)
		


	