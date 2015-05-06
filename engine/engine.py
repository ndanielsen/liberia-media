import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Base, Log, Content, Image, ScrapeLog

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
# Base.metadata.bind = engine
 
# DBSession = sessionmaker(bind=engine)

# session = DBSession()
 
# # Insert a Person in the person table
# new_log = Log(name='new file 234', filename="somefile.txt")
# session.add(new_log)
# session.commit()
 
# # Insert an Address in the address table
# title = "New title"
# sub_title = "sub_title"
# author = "Mr Someone"
# main_content = "hoahdsfkajfljadf;jad;lfkjsa;lfdja;ljfnwjlaslfdjalkjfa"
# post_date =  "2015-0401"


class Engine(object):
	"""
	Object for creating and inserting items into DB engine

	Tries to connect to DB. If not, creates a db and executes main instructions.
	"""


	def __init__(self, engine=None, log=None, content=None, image=None, scrapelog=None, debug=True):

		self.dbname = engine + '.db'
		self.debug = debug
		self.engine = create_engine('sqlite:///' + self.dbname )
		self.log = log
		self.content = content
		self.image = image
		self.scrapelog = scrapelog


		if not os.path.isfile(self.dbname) :
			self.createDB()


		self.commitlist = []

		if self.scrapelog: ### need to create method to check if any class attributes are positive and if they are, create the DB object like here
			self.ScrapeLog()

		self.connectDB()


		self.session.add(self.scrapelog)
		# (self.session.add(entry) for entry in self.commitlist)
		# print self.commitlist
		self.session.commit()

		first = self.session.query(ScrapeLog).first()
		
		print first.name, first.time


	def ScrapeLog(self):
		# name, filename, url_request, url_status_code, header_len, response_len, time, message 
		url_request, url_status_code,header_len,response_len,name,time,message = self.scrapelog
		self.scrapelog = ScrapeLog(	name=name, url_request=url_request, url_status_code=url_status_code, 
									header_len=header_len, response_len=response_len, time=time, message=message )



	def connectDB(self):

		DBSession = sessionmaker(bind=self.engine)
		self.session = DBSession()
		if self.debug:
			print "DB initialized"

	def createDB(self):
		Base.metadata.create_all(self.engine)
		if self.debug:
			print "New DB %s created" % self.dbname




if __name__ == '__main__':

	log = ["http://news.analystliberia.com/index.php/news/1",404,12,874,"theanalyst","2015-05-03 12:33:16.688633","production"]
	
	Engine(engine='test', scrapelog=log)