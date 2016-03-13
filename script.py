import requests
import re

class Generator:

	def __init__(self):
		self.session=requests.Session()
		self.proxy=''
		self.firstname=''
		self.lastname=''
		self.email=''
		self.password=''

	def register(self):
		try:
			html1=self.session.get('http://reg.ebay.it/reg/PartialReg?siteid=101&UsingSSL=0&co_partnerId=2&ru=http%3A%2F%2Fwww.ebay.it%2F&pos=1&rv4=1', proxies={'http':self.proxy}).text
		except:
			return 0
		try:
			mid=re.search('mid":"(.*?)"',html1).group(1)
			tmxSessionId=re.search('tmxSessionId":"(.*?)"',html1).group(1)
		except:
			return 0
		payload = {
			'isSug':'false',
			'countryId':'101',
			'userid':'',
			'ru':'http%3A%2F%2Fwww.ebay.it%2F',
			'email':self.email,
			'remail':self.email,
			'PASSWORD':self.password,
			'firstname':self.firstname,
			'lastname':self.lastname,
			'promotion':'true',
			'mode':'1',
			'frmaction':'submit',
			'tagInfo':'ht5%253D'+mid+'%257Cht5new%253Dtrue%2526usid%253D'+tmxSessionId,
			'isGuest':'0',
			'pos':'1',
			'idlstate':'',
			'profilePicture':'',
			'agreement':'Termini+e+condizioni',
			'personalFlag':'true'
		}
		try:
			html2=self.session.post('http://reg.ebay.it/reg/PartialReg',data=payload,proxies={'http':self.proxy}).text
		except:
			return 0
		try:
			username=re.search("nome utente univoco per te: <b>(.*?)</b>",html2).group(1)
			return username
		except:
			return 0
