#!/usr/local/bin/python
 # -*- coding: utf-8 -*-
"""
NLP analysis functions


noAuthor:
Nathan Danielsen
nathan.danielsen [at] gmail.com
"""
import string


import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tag.stanford import NERTagger



class NLP(object):
	"""
	Using some basic NLP methods to analyze text


	Inspiration found here:
	https://github.com/ndanielsen/A-Smattering-of-NLP-in-Python

	"""
	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.tokens = [word for sent in nltk.sent_tokenize(self.text) for word in nltk.word_tokenize(sent)]
		self.sentences = nltk.sent_tokenize(self.text)
		self.json = {}
	
	# @staticmethod
	# def from_txt(txt, title="", text=""):
	# 	"""Constructs a NLP class object from a text file with line[0] as title and following as text """	
	# 	text = []
	# 	with open(txt, 'r') as f:
	# 		for line in f.readlines():
	# 			text.append(line)
	# 	title, body = text[0], text[1:]
		
	# 	return NLP(title, body)



	def count(self):
		token_dict = {}
		for token in sorted(set(self.tokens))[:30]:
    		 token_dict[token] = str(self.tokens.count(token))
		return token_dict


	def stemmer(self):
		""" 
		Takes a list tokens and stems them into a list.
		Stemming is the process of reducing a word to its base/stem/root form. 
		"""

		stemmer = SnowballStemmer("english")
		stemmed_tokens = [stemmer.stem(t) for t in self.tokens]
		
		for token in sorted(stemmed_tokens):
			print token + ' [' + str(stemmed_tokens.count(token)) + ']'


	def lemmatizer(self):
		lemmatizer = nltk.WordNetLemmatizer()
		temp_sent = "Several women told me I have lying eyes."
		stemmer = SnowballStemmer("english")
		stemmed_tokens = [stemmer.stem(t) for t in self.tokens]

		#print [stemmer.stem(t) for t in nltk.word_tokenize(temp_sent)]
		#print [lemmatizer.lemmatize(t) for t in nltk.word_tokenize(temp_sent)]

		# fdist = nltk.FreqDist(stemmed_tokens)

		# for item in fdist.items()[:25]:
		# 	print item

		stemmed_tokens_no_stop = [stemmer.stem(t) for t in stemmed_tokens if t not in nltk.corpus.stopwords.words('english') ]

		fdist2 = nltk.FreqDist(stemmed_tokens_no_stop)

		for item in fdist2.items()[:25]:
			print item



	def entities(self):
		"""Need to fix loop with hasattr  """
		pass

		# def extract_entities(text):
		# 	entities = []
		# 	for sentence in nltk.sent_tokenize(text):
		# 		chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
		# 		#print chunks
		# 		print [chunk for chunk in chunks if hasattr(chunk, 'node')]
		# 	return entities

		# for entity in extract_entities(self.text):
		# 	print '[' + entity.node + '] ' + ' '.join(c[0] for c in entity.leaves())	


	def NER(self):
		"""
		Stanford NER in action, returns a dict of Named Entities by type
		

		I need to clean up the dictionary output and organize by type
		"""
		# NER = {"LOCATION":{}, "PERSON":{}, "ORGANIZATION":{}  }
		NER = {}
				
		st = NERTagger('/home/nathan/nltk_data/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
			'/home/nathan/nltk_data/stanford-ner/stanford-ner.jar', 'utf-8')

		body = self.text.strip('\n')
		body = body.split()
		entityName = ""
		entityType = ""

		for sentence in self.sentences:	
			print "Processing"
			
			for word in st.tag(sentence.split()): #loop through text
			# 
			# for entityName, entityType in st.tag(sentence.split()): #loop through text
			# 	NER[entityType] = {}
			# 	print entityName, entityType
			
			# 	NER[entityType][entityName] += 1 
				# entityMultiname = None
				# print entityName, entityType
	

				# if entityType == "O":
				# 	continue
				# elif entityName[:-1] != ",":
				# 	entityMultiname = entityName + " "

				# else:
				# 	if entityMultiname:
				# 		NER[entityType] = entityMultiname # += 1
				# 		entityMultiname = None
				# 	else:
				# 		NER[entityType] = entityName #+= 1
						


				if word[1] != "O":

					if word[:-1] == ",": #prevents lists of NER from being clumped together
						continue
					else:	
						entityName += word[0] +" "
						entityType = word[1]

				else: 
					NER[entityName] = entityType
					# NER[entityType] = entityName
					entityName = ""
				

		del NER['']

		return NER





if __name__ == '__main__':
	# title = "This is a title"

	# text = "facilisis lorem tristique aliquet. Phasellus fermentum convallis"

	# mrtesty = NLP(title, text)
	
	# assert len(mrtesty.sentences) == 2

	# assert mrtesty.count() == {'tristique': '1', 'Phasellus': '1', 'lorem': '1', 'convallis': '1', '.': '1', 'facilisis': '1', 'aliquet': '1', 'fermentum': '1'}


	mytitle = "Nathan Danielsen"

	mytext = "My name is Charlie, Charlie and I work for Altamira in Tysons Corner."

	mytest = NLP(mytitle, mytext)

	print mytest.title
	print mytest.NER()
	print mytest.json

	"""
	Classmethod Constructor for importing text files needs work
	"""

	# ftester = NLP.from_txt('nytimes.txt')

	# print (ftester.title)

	# print (ftester.text)