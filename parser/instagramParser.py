import requests #http[s] requests
import re       #regular expression lib
import json     #json parsing

class InstagramParser:
    INSTAGRAM_URL="https://www.instagram.com/"
    PATH_TO_CONSUMER = "static/bundles/es6/Consumer.js/"   
    HEADERS={
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "cache-control": "max-age=0"
    }
    GRAPHQL_QUERY="graphql/query/?"
    QUERY_HASH="query_hash="

    def __init__(self,account_name):
        self.account_name = account_name
        self.session = requests.Session()
        self.session.headers = self.HEADERS

        html = self.__get_accountPage(account_name)
        consumer_js_filename = self.__find_consumer_name(html)
        consumer_js = self.__get_consumer_file(consumer_js_filename)
        
        #self.accountId = self.__get_accountID()
        self.queryHash = self.__find_queryHash(consumer_js)
        

    
    def __get_accountPage(self,account_name):
        response=self.session.get(self.INSTAGRAM_URL+account_name)
        html=response.text
        return html

    def __find_consumer_name(self,html):
        regex = r"Consumer\.js/(.+\.js)"
        js_file_name = re.findall(regex,html)[0]
        return js_file_name

    def __get_consumer_file(self,js_file_name):
        responce = self.session.get(self.INSTAGRAM_URL+self.PATH_TO_CONSUMER+js_file_name)
        js_file = responce.text
        return js_file

    def __find_queryHash(self,js_file):
        regex = r"queryId:\"(.+?)\","
        queryHashes = re.findall(regex,js_file)
        #https://www.instagram.com/graphql/query/?query_hash=003056d32c2554def87228bc3fd9668a&variables={"id":"4709813291","first":12}
        prerequest=self.INSTAGRAM_URL+self.GRAPHQL_QUERY+self.QUERY_HASH
        for i in queryHashes:
            #find valid query hash
            request=prerequest+i+'&variables={"id":"4709813291","first":12}'
            responce=self.session.get(request)
            print(request)
            print(responce)
            file=open(f"{i}.txt","w")
            file.write(responce.text)
            file.close()
        return queryHashes

    def __get_accountID(self):
        request = self.INSTAGRAM_URL+self.account_name+"/?__a=1"
        responce = self.session.get(request)
        json_dict = json.loads(responce.text)
        regex = r"(\d+)"
        return re.findall(regex,json_dict['logging_page_id'])[0]
        
    def get_item():
        pass
    

account_name="c.h.o.i.c.e.store"

instPaser=InstagramParser(account_name)
