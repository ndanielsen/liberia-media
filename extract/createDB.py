import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

###################### REVISE THIS
global name
name = "outlet"
#######################

Base = declarative_base()

class Log(Base):
	__tablename__ = 'log'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	filename = Column(String(250), nullable=False)


class Content(Base):

	media_content = name + "_" + "content"

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
