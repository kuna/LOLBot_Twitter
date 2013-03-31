# -*- coding: cp949 -*-
from tweepy import *
import opggParser
import settings


username = u'��¹��'

# start parsing site
g = opggParser.opgg(username)

# consumer login
consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
 
# access_token login
ACCESS_KEY = settings.ACCESS_KEY
ACCESS_SECRET = settings.ACCESS_SECRET
 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = API(auth)
 
# send test-DM
api.update_status(username + u'�� ���� ����: ' + g.champname + u'(��)�� ' + g.game + u'���� ' + g.score)
