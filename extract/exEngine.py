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
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class exEngine(object):

	def __init__(self, name=None):

		self.name = name


	def map_data(self):
		"""
		Maps all stories in the data folder for the content provider
		"""
		data_dir = "data/" + self.name

		return os.listdir(data_dir)

		
	def connectDB(self):

		try:
			
			#connect to DB

			pass
		except Exception, e:
			
			# DB does not exist

			# Create DB

			# Create taable for log

			# Create able for cleaned data

			pass

		except Exception, e:

			# Table does not exist

			# Create table for log 

			# Create table for cleaned_data

			pass


		else:
			pass
		finally:
			pass


	def createDB(self):

		Base = declarative_base()
 
		class Log(Base):
			__tablename__ = 'log'
			id = Column(Integer, primary_key=True)
			name = Column(String(250), nullable=False)
			filename = Column(String(250), nullable=False)

 
		class Content(Base):

			media_content = self.name + "_" + "content"

			__tablename__ = media_content


			id = Column(Integer, primary_key=True)
			title = Column(String(250))
			sub_title = Column(String(250))
			author = Column(String(250))
			
			main_content = Column(String(2500)) #figure out better for this

			post_date = Column(String(250)) #change to time date object

			log_id = Column(Integer, ForeignKey('log.id'))
			log = relationship(Log)

		# class Images(Base):

		# 	media_content = self.name + "_" + "image"

		# 	__tablename__ = media_content


		# 	log_id = Column(Integer, ForeignKey('Log.id'))
		# 	log = relationship(Log)



		engine = create_engine('sqlite:///sqlalchemy_example.db')
		Base.metadata.create_all(engine)


if __name__ == '__main__':
	
	test = exEngine(name="test123")

	test.createDB()