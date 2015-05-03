from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from createDB import Log, Base, Content
 
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
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



new_content = Content(title=title, sub_title=sub_title, author=author, main_content= main_content, post_date=post_date )
session.add(new_content)
session.commit()