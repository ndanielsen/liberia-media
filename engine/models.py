import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class ScrapeLog(Base):

	__tablename__ = 'scrapelog'
	id = Column(Integer, primary_key=True)
	name = Column(String(250))
	url_request = Column(String(250))
	url_status_code = Column(String(250))
	header_len = Column(String(250))
	response_len = Column(String(250))
	time = Column(String(250))
	message = Column(String(50))


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
	author = Column(String(250))
	main_content = Column(String(2500)) #figure out better for this
	post_date = Column(String(250)) #change to time date object
	log_id = Column(Integer, ForeignKey('log.id'))
	log = relationship(Log)

class Image(Base):

	__tablename__ = "images"
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	imageurl = Column(String(250))
	log_id = Column(Integer, ForeignKey('log.id'))
	log = relationship(Log)




if __name__ == "__main__":
	engine = create_engine('sqlite:///sqlalchemy_example.db')
	Base.metadata.create_all(engine)

