#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Extracts content and cleans data from media content html page using beautiful soup, 

and 

Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""

import os
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import arrow
import bs4




class DailyObserverExtractor(object):
	"""
	Takes in a directory of HTML pages for Liberian Daily Obeserver articles

	Goes through various extraction and cleaning procedures

	Returns in unicode: true_url, category, title, date(datetime object), author, clean_content, image_url

	"""



	def __init__(self, name=None, num=None, debug=True):

		self.name = name

		self.num = num

		self.data_dir = "data/" + self.name + "/"

		self.docs_dir = os.listdir(self.data_dir)

		self.extractlist = []

		self.hello = 'hello'

	def whitespaceremover(self, field):
		field = field.replace(u'\xa0', u'')
		
		return field

	def emailremover(self, field):
		cleaned = u''
		field = field.split()
		for word in field:
			if word.find('@') > 0:
				pass
			else:
				cleaned += word + u' '

		return cleaned




	def contents_cleaner(self, soup):
		# body = soup.findAll(name='div', attrs={'class':"field-items"})#     title = str(title)
		
		try:
			head = soup.find(name='head')
			link = head.find(name='link', attrs={'rel':"canonical"})
			true_url = 'http://liberianobserver.com' + link['href']
			

		except Exception:

			true_url = None
			


		try:
			category = link['href'].split('/')[1]

		except Exception:	

			category = None


		try:

			image_content = soup.find(name='div', attrs={'class':'block block-system'})

			image = image_content.find(name='img')

			image_url = image['src']

			loc = image_url.index('?itok')

			image_url = image_url[:loc]

		except Exception:

			image_url = None



		main_body = soup.find(name='div', attrs={'class':"node-content-wrapper"})

		try:
			title = main_body.find(name="h1",  attrs={'class':"title"}).text
			title = title.replace(u'\xa0', u' ')

			if 'edition' in title.split(): 
				raise Exception

		except Exception:
			title = None


		try:
			author = main_body.find(name="div",  attrs={'class':"field field-name-field-by field-type-text field-label-inline clearfix"}).text 
			author = author.replace('By:', '').replace('By', '')
			author = self.emailremover(author)
			author = self.whitespaceremover(author)
			author = author.strip()
		
		except AttributeError:
		 	author = None

		try:
			content_body = main_body.find(name='div', attrs={'class':"field field-name-body field-type-text-with-summary field-label-hidden"})
			pset = content_body.findAll('p')

			clean_content = ''
			for p in pset:
				p = p.text
				p = p.replace(u'\xa0', u'')
				clean_content += p + unicode("\n ")

		except Exception:
			clean_content = None

		try:
			date = main_body.find(name="span",  attrs={'class':"date"}).text
			date = date[5:]
			date = arrow.get(date, 'MM/DD/YYYY - HH:mm')
			date = date.naive

		except Exception:
			date = None

		return true_url, category, title, date, author, clean_content, image_url
		# return date

	
	def comments(self):
		pass

	def image_lead(self):
		pass

	def image_caption(self):
		image_caption = soup.findAll(name='div', attrs={'id':"capption"})


		return image_caption[0]
		


	def cleaner(self, num):

		doc = self.docs_dir[num]

		# try: 

		with open(self.data_dir + doc, 'r') as f:
			self.soup = bs4.BeautifulSoup(f)
			content = self.contents_cleaner(self.soup)

		return doc, self.name, content



if __name__ == '__main__':

	e = DailyObserverExtractor(name='dailyobserver')
	
	for num in xrange(1,20):
		print e.cleaner(num=num)
		print '--' * 100