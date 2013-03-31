# -*- coding: cp949 -*-
import httplib2
import BeautifulSoup

class opgg:
    def __init__(self, username):
        url = 'http://op.gg/summoner/userName=' + username
        print url
        r = self.getHttpContents(url)
        gis = r.findAll('div', attrs={'class':'gameInfo'})
        gss = r.findAll('div', attrs={'class':'gameSummary'})
        for i in range(0, len(gis)):
            self.champname = gis[i].find('div', attrs={'class':'championName'}).text
            self.game = gis[i].find('div', attrs={'class':'subType'}).text
            self.score = gss[i].findAll('li')[0].text
            break

    def getHttpContents(self, targeturl):
        try:
            http = httplib2.Http()
            res, c = http.request(targeturl);
            if 'err' in res['content-location'] or 'REDIRECT' in res['content-location']:
                print 'LR2IR Error: Error url loading'
                return None
            return BeautifulSoup.BeautifulSoup(c)
        except Exception, e:
            print ('LR2IR unexpected error: %s'%(e))
