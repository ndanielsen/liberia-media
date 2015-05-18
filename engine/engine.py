#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Database engine for content extraction 

Using SQLlite because it's easy

Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""


import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Base, Log, Content, Image, ScraperLog



class Engine(object):
	"""
	Object for creating and inserting items into DB engine

	Tries to connect to DB. If not, creates a db and executes main instructions.

	Flexible with the keyword arguments to allow for different DBs and types of datamodels to be entered

	"""


	def __init__(self, engine=None, log=None, content=None, image=None, scraperlog=None, debug=True):

		self.dbname = engine + '.db'
		self.debug = debug
		self.engine = create_engine('sqlite:///' + self.dbname )
		self.log = log
		self.content = content
		self.image = image
		self.scraperlog = scraperlog


		self.commitlist = []

		if not os.path.isfile(self.dbname) : # if DB doesn't exist, it will be created
			self.createDB()

		self.connectDB()

		
		if self.scraperlog: ### need to create method to check if any class attributes are positive and if they are, create the DB object like here
			self.ScraperLog()

		if self.log:
			self.Log()

		if self.content:
			self.Content()


		for entry in self.commitlist:
			
			try:
				self.session.add(entry)
				 
			
			except sqlalchemy.exc.IntegrityError as ex:
				print 'Exception'
				print type(self.commitlist)
				next(self.commitlist, None)


		self.session.commit()
		

		if self.debug:

			print "Ending DB connection"


		

	def ScraperLog(self): 
		
		log_len = len(self.scraperlog)
		

		if log_len > 1 and log_len != 7:
			for row in self.scraperlog:
				datetime, url_request, url_status_code,header_len,response_len,name,message = row
				row =  ScraperLog(datetime=datetime, name=name, url_request=url_request, url_status_code=url_status_code, 
										header_len=header_len, response_len=response_len, message=message )

				self.commitlist.append(row)

		else:

				datetime, url_request, url_status_code,header_len,response_len,name,message = self.scraperlog
				self.scraperlog =  ScraperLog(datetime=datetime, name=name, url_request=url_request, url_status_code=url_status_code, 
										header_len=header_len, response_len=response_len, message=message )

				self.commitlist.append(self.scraperlog)

		if self.debug:

			print "Scarper log added to commit list"

		

	def Log(self):

		
		log_len = len(self.log)
		

		if log_len > 1 and log_len != 7:
			for row in self.log:

				name, filename, category, title, datetime = row

				
				row =  Log(name=name, filename=filename, category=category, title=title, datetime=datetime)

				self.commitlist.append(row)

		else:

				name, filename, category, title, datetime = self.log
				self.log =  Log(name=name, filename=filename, category=category, title=title, datetime=datetime)

				self.commitlist.append(self.log)

		if self.debug:

			print "Log added to commit list"




	def Content(self):  
	
		content_len = len(self.content)
	
		if content_len  > 1 and content_len  != 7:
			for row in self.content:

				name, true_url, category, title, datetime, author, clean_content, image_url = row

				
				row =  Content(name=name, true_url=true_url, category=category, title=title, datetime=datetime, author=author, clean_contentclean_content, image_url=image_url)

				self.commitlist.append(row)

		else:

				name, true_url, category, title, datetime, author, clean_content, image_url = self.content
				self.content =  Content(name=name, true_url=true_url, category=category, title=title, datetime=datetime, author=author, clean_contentclean_content, image_url=image_url)

				self.commitlist.append(self.content)

		if self.debug:

			print "Content added to commit list"







	def erorcheck_db(self, check_table=None, column=None, value=None):
		"""
		Runs through DB and checks if there are identical entries such as url_request or etc.
		"""
		self.query = self.session.query(check_table).all()



	def connectDB(self):

		DBSession = sessionmaker(bind=self.engine)
		self.session = DBSession()
		if self.debug:
			print "DB initialized"

	def createDB(self):
		Base.metadata.create_all(self.engine)
		if self.debug:
			print "New DB %s created" % self.dbname


	def report(self):

		self.erorcheck_db(check_table=ScraperLog)

		for row in self.query:
			print row.url_request, row.datetime




if __name__ == '__main__':

	from dateutil import parser 
	import datetime 
	import time
	import sqlalchemy
	
	# try:

	
	# now2 = datetime.datetime.fromtimestamp(time.time())

	# row1 = [parser.parse("2015-05-03 12:33:16.688633"), u"http://news.analystliberia.com/index.php/news/1",404,12,874,u"theanalyst",u'production']

	now2 = datetime.datetime.fromtimestamp(time.time())

	row1 = [now2, u"http://news.analystliberia.com/index.php/news/1",404,12,874,u"theanalyst",u'production']


	
	# except sqlalchemy.exc.IntegrityError:

	now = datetime.datetime.fromtimestamp(time.time())

	row2 = [now, u"http://news.analystliberia.com/index.php/news/1",404,12,874,u"theanalyst",u'production']

	log = [row1, row2]


	Engine(engine='new_test', scraperlog=log)


	# 	Engine(engine='test', scraperlog=log).main()

	# 	print 'ok', now

	# except Exception as ex:

	# 	print ex.__class__


	# finally:

	# 	print 'done'