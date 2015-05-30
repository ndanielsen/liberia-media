"""
Rules for scraping module for Liberia Media Collection

author: Nathan Danielsen
email: nathanjdanielsen@gmail.com
"""



class Rules(object):
	"""
	With the name of the media site, evaluates the header and other information to determine if the requested page is unique and should be stored.

	Returns True or False
	"""
	def __init__(name=name, url=urlresponse):

		self.name = name
		self.url = urlresponse
		self.status_code = self.url.status_code

		self.site_rules = 	{

								"theobserver": 	{	"header_len": None,
														"link": None,

																			},

								"theinquirer": 	{	"header_len": None,
														"link": None,

																			},
								"theanalyst": 	{	"header_len": None,
														"link": None,

																			},

								"frontpageafricaonline": 	{	"header_len": None,
														"link": None,

																			},
								"thenewdawn": 	{	"header_len": None,
														"link": None,

																			},
								"post1847": 	{	"header_len": None,
														"link": None,

																			},	
								"gnnliberia": 	{	"header_len": None,
														"link": None,

																			},	
								"dailyobserver": 	{	"header_len": None,
														"link": None,

																			},	
								"golministryofinformation": 	{	"header_len": None,
														"link": None,

																			},	

								"name_template": 	{	"header_len": None,
														"link": None,

																			},	
							}

	def test(self):

		# if status code != 200:
		#return False

		#if len of header is less than key value of name, return false








