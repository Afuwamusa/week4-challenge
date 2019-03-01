import requests


class Sources():
    def __init__(self, user):
        self.user = user
    def get_source(self):
        api = "https://newsapi.org/v2/top-headlines?sources=entertainment-weekly&apiKey=3688862811be47739cdbeef14755154c" 
#creating the varriable that holds the information of API
        feedback = requests.get(api)
        json_feedback = feedback.json()
        article = json_feedback["articles"]
        headlines=0
        while headlines<10:
            tit = article[headlines]
            title = tit["title"]
            Description = tit["description"]
            url = tit["url"]
            item1 = tit["source"]
            source_id=item1["id"]
            print("Id:"+ source_id +"\n url: "+ url + "\ntitle:"+ title + "\ndescription:"+ Description)
            headlines += 1
    def get_s(self):
        api = "https://newsapi.org/v2/top-headlines?sources=entertainment-weekly&apiKey=3688862811be47739cdbeef14755154c" 
#creating the varriable that holds the information of API
        feedback = requests.get(api)
        json_feedback = feedback.json()
        article = json_feedback["articles"]
        headlines=0
        while headlines<10:
            tit = article[headlines]
            title = tit["title"]
            Description = tit["description"]
            url = tit["url"]
            item1 = tit["source"]
            source_id=item1["id"]
            print("Id:"+ source_id +"\n url: "+ url + "\ntitle:"+ title + "\ndescription:"+ Description)
            headlines += 1
    def get_sou(self):
        api = "https://newsapi.org/v2/top-headlines?sources=entertainment-weekly&apiKey=3688862811be47739cdbeef14755154c" 
#creating the varriable that holds the information of API
        feedback = requests.get(api)
        json_feedback = feedback.json()
        article = json_feedback["articles"]
        headlines=0
        while headlines<10:
            tit = article[headlines]
            title = tit["title"]
            Description = tit["description"]
            url = tit["url"]
            item1 = tit["source"]
            source_id=item1["id"]
            print("Id:"+ source_id +"\n url: "+ url + "\ntitle:"+ title + "\ndescription:"+ Description)
            headlines += 1
    def get_sourc(self):
        api = "https://newsapi.org/v2/top-headlines?sources=entertainment-weekly&apiKey=3688862811be47739cdbeef14755154c" 
#creating the varriable that holds the information of API
        feedback = requests.get(api)
        json_feedback = feedback.json()
        article = json_feedback["articles"]
        headlines=0
        while headlines<10:
            tit = article[headlines]
            title = tit["title"]
            Description = tit["description"]
            url = tit["url"]
            item1 = tit["source"]
            source_id=item1["id"]
            print("Id:"+ source_id +"\n url: "+ url + "\ntitle:"+ title + "\ndescription:"+ Description)
            headlines += 1
    
reader = Sources("Afua")
print(reader.get_source())
print(reader.get_s())
print(reader.get_sou())
print(reader.get_sourc())
    










