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




if __name__ == '__main__':
	
	test = exEngine(name="test123")

	test.createDB()