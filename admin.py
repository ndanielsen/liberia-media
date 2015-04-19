#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
Control module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""

from scrape.scrape import Collector 



media = [("theobserver","http://www.liberianobserver.com/node/", 10),

		("theinquirer", "http://www.theinquirer.com.lr/content1.php?main=news&news_id=", 5),

		#("theinquirer", "http://www.theinquirer.com.lr/content1.php?main=editorial&ed_id=", 5), ### a few of these have defaulted to home page

		#("theinquirer", "http://www.theinquirer.com.lr/content1.php?main=sports&sports_id=", 5), ### if not cookie in header, then index page

		("theanalyst", "http://news.analystliberia.com/index.php/news/", 10), ### JOOMLA unique story ids for all categories 

		("frontpageafricaonline", "http://www.frontpageafricaonline.com/index.php/news/", 5), ### unique numbers for each story, go back and pick out category later

		("thenewdawn", "http://www.thenewdawnliberia.com/general/", 5),  # Joomla

		("liberianewagency", "http://www.liberianewsagency.org/pagesnews.php?nid=", 5), # custom built but look like page iternation would work

		("post1847", "http://www.1847post.com/?q=node/", 10 ), # node based iternation would work

		("gnnliberia", "http://www.gnnliberia.com/node/", 10), #Drupal

		('dailyobserver', "http://www.liberianobserver.com/node/", 10), #drupal nodebased

		('golministryofinformation', 'http://www.micatliberia.com/index.php/blog/', 5) #JOOMLA nodebased



		]

	




### Scrape site and deposit raw HTML into organized data folders

### Process HTML and load to database

### Analyze database


if __name__ == "__main__":

	numbers = [num for num in range(350, 400)]

	# for num in numbers:
	# 	print num

	for site, base_url, sleep in media:

		url = base_url + str(1500)

		Collector(name=site, urlraw=url, sleep=sleep)
		


	# print "Hello"

	# scraper = Collector(name="theanalyst", urlraw="http://news.analystliberia.com/index.php/memo/401", sleep=0)