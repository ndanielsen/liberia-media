from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from createDB import Log, Base, Content
 
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()
 
# Insert a Person in the person table
new_log = Log(name='new file 234', filename="somefile.txt")
session.add(new_log)
session.commit()
 
# Insert an Address in the address table
title = "New title"
sub_title = "sub_title"
author = "Mr Someone"
main_content = "hoahdsfkajfljadf;jad;lfkjsa;lfdja;ljfnwjlaslfdjalkjfa"
post_date =  "2015-0401"



new_content = Content(name=name, title=title, sub_title=sub_title, author=author, main_content= main_content, post_date=post_date )
session.add(new_content)
session.commit()


class Engine(object):
	"""
	Object for creating and inserting items into DB engine

	Tries to connect to DB. If not, creates a db and executes main instructions.
	"""


	def __init__(self):

		self.db = "name of db TBD"

		try:

			self.engine = create_engine('sqlite:///sqlalchemy_example.db')

			#excute main

		except Error:

			#create DB

			# execute main
			pass


	def main(self):

		new_content = Content(name=name, title=title, sub_title=sub_title, author=author, main_content= main_content, post_date=post_date )
		session.add(new_content)
		session.commit()

		pass

