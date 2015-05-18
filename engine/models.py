#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Models for the Database engine for content extraction and access

Using SQLlite because it's easy

Author:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Unicode, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

### TO DO: Should the primary key be the datetime object?








Base = declarative_base()

class ScraperLog(Base):

	__tablename__ = 'scraperlog'
	id = Column(Integer, primary_key=True)	
	name = Column(Unicode(250))
	url_request = Column(Unicode(250))
	url_status_code = Column(Integer)
	header_len = Column(Integer)
	response_len = Column(Integer)
	datetime = Column(DateTime)	
	message = Column(Unicode(50))
	error = Column(Boolean, default=False)


class Log(Base):
	"""
	name, filename, category, title, datetime # to unpack
	Log(name=name, filename=filename, category=category, title=title, datetime=datetime)

	"""
	__tablename__ = 'log'
	id = Column(Integer, primary_key=True)
	name = Column(Unicode)
	filename = Column(Unicode, nullable=False)
	category = Column(Unicode)
	title = Column(Unicode)
	datetime = Column(DateTime)

class Content(Base):
	"""
	name, true_url, category, title, datetime, author, clean_content, image_url #to unpack
	
	Content(name=name, true_url=true_url, category=category, title=title, datetime=datetime, author=author, clean_contentclean_content, image_url=image_url)
	"""
	__tablename__ = "content"

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	true_url = Column(Unicode)
	category = Column(Unicode)
	title = Column(Unicode)
	datetime = Column(DateTime)	
	author = Column(Unicode)
	clean_content = Column(Unicode)
	image_url = Column(Unicode)

	log_id = Column(Integer, ForeignKey('log.id'))
	log = relationship(Log)
	


class Image(Base):

	__tablename__ = "images"
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	image_url = Column(String(250))
	log_id = Column(Integer, ForeignKey('log.id'))
	log = relationship(Log)




if __name__ == "__main__":
	engine = create_engine('sqlite:///sqlalchemy_example.db')
	Base.metadata.create_all(engine)

