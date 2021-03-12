import requests #http[s] requests
import re       #regular expression lib
import json     #json parsing

class InstagramParser:
    INSTAGRAM_URL="https://www.instagram.com/"
    PATH_TO_CONSUMERLIBCOMMONS = "static/bundles/es6/ConsumerLibCommons.js/"
    PATH_TO_CONSUMER = "static/bundles/es6/Consumer.js/"   
    HEADERS={
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107",
        "accept": "text/html",
        "accept-encoding": "gzip, deflate, br",
        "cache-control": "max-age=0"
    }
    
    def __init__(self,account_name):
        self.account_name = account_name
        self.session = requests.Session()
        self.session.headers = self.HEADERS
        html = self.__get_accountPage(account_name)
        js_file_name = self.__find_consumer_name(html)
        js_file = self.__get_consumer_file(js_file_name)
        self.queryHash = self.__find_queryHash(js_file)

    
    def __get_accountPage(self,account_name):
        response=self.session.get(self.INSTAGRAM_URL+account_name)
        html=response.text
        return html

    #output example: '9a71d389f82c.js'
    def __find_consumerLibCommons_name(self,html):
        regex = r"ConsumerLibCommons\.js/(.+\.js)"
        js_file_name = re.findall(regex,html)[0]
        return js_file_name

    #output is json formatted text
    def __get_consumerLibCommons_file(self,js_file_name):
        responce = self.session.get(self.INSTAGRAM_URL+self.PATH_TO_CONSUMERLIBCOMMONS+js_file_name)
        js_file = responce.text
        my_file = open("otus2.txt", "w")
        my_file.write(js_file)
        my_file.close()
        return js_file

    def __find_consumer_name(self,html):
        regex = r"Consumer\.js/(.+\.js)"
        js_file_name = re.findall(regex,html)[0]
        return js_file_name

    def __get_consumer_file(self,js_file_name):
        responce = self.session.get(self.INSTAGRAM_URL+self.PATH_TO_CONSUMER+js_file_name)
        js_file = responce.text
        my_file = open("otus.txt", "w")
        my_file.write(js_file)
        my_file.close()
        return js_file

    def __find_queryHash(self,js_file):
        regex = r"queryId:\"(.+?)\","
        queryHash = re.findall(regex,js_file)
        for i in queryHash:
            #find valid query hash
        return queryHash

    def get_item():
        pass
    

account_name="c.h.o.i.c.e.store"

instPaser=InstagramParser(account_name)
