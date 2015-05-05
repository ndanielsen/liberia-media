#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Control module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""

from scrape.scrape_admin import Scraper_Admin 



media = [

		("theanalyst", "http://news.analystliberia.com/index.php/news/", 10), ### JOOMLA unique story ids for all categories 

		("frontpageafricaonline", "http://www.frontpageafricaonline.com/index.php/news/", 5), ### unique numbers for each story, go back and pick out category later

		("thenewdawn", "http://www.thenewdawnliberia.com/general/", 7),  # Joomla

		("post1847", "http://www.1847post.com/?q=node/", 10 ), # node based iternation would work

		("gnnliberia", "http://www.gnnliberia.com/node/", 10), #Drupal

		('dailyobserver', "http://www.liberianobserver.com/node/", 10), #drupal nodebased

		('golministryofinformation', 'http://www.micatliberia.com/index.php/blog/', 7) #JOOMLA nodebase

		]

shitty_media = [

		("theinquirer", "http://www.theinquirer.com.lr/content1.php?main=news&news_id=", 5),

		("liberianewsagency", "http://www.liberianewsagency.org/pagesnews.php?nid=", 5), # custom built but look like page iternation would work
		
		]






### Scrape site and deposit raw HTML into organized data folders

### Process HTML and load to database

### Analyze database


if __name__ == "__main__":

	test = Scraper_Admin(media, lowrange=1, highrange=15000, message="production1", debug=True)
	
	test.main()


