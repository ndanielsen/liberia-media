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

### TO DO: Should the primary key be the timedate object?








Base = declarative_base()

class ScraperLog(Base):

	__tablename__ = 'scraperlog'
	id = Column(Integer, primary_key=True)	
	name = Column(Unicode(250))
	url_request = Column(Unicode(250))
	url_status_code = Column(Integer)
	header_len = Column(Integer)
	response_len = Column(Integer)
	timedate = Column(DateTime)	
	message = Column(Unicode(50))
	error = Column(Boolean, default=False)


class Log(Base):

	__tablename__ = 'log'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	filename = Column(String(250), nullable=False)

class Content(Base):

	__tablename__ = "content"

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	title = Column(String(250))
	sub_title = Column(String(250))
	author = Column(String(250), index=True)
	main_content = Column(String(2500)) #figure out better for this
	post_date = Column(String(250)) #change to time date object
	log_id = Column(Integer, ForeignKey('log.id'))
	log = relationship(Log)
	true_url = Column(Unicode)

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

