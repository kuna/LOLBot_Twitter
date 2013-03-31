# -*- coding: cp949 -*-
from tweepy import *
import opggParser
import settings


username = u'쿠나쨔응'

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
api.update_status(username + u'의 게임 전적: ' + g.champname + u'(으)로 ' + g.game + u'에서 ' + g.score)
