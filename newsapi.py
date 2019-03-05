import click
import requests
class Sources():
    def __init__(self, user):
        self.user = user
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
            print(click.secho(click.style("Id:", fg ="white")+ click.style(source_id, fg="yellow") + click.style("\n url: ", fg="white")+ click.style( url, fg="yellow") + click.style("\ntitle:", fg="white")+ click.style(title, fg="yellow") + click.style("\ndescription:", fg="white")+click.wrap_text(click.style(Description,fg="yellow")) ))
            headlines += 1
            click.echo('\n')
    def get_sou(self):
        api = "https://newsapi.org/v2/top-headlines?sources=argaam&apiKey=3688862811be47739cdbeef14755154c" 
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
            print(click.secho(click.style("Id:", fg ="white")+ click.style(source_id, fg="yellow") + click.style("\n url: ", fg="white")+ click.style( url, fg="yellow") + click.style("\ntitle:", fg="white")+ click.style(title, fg="yellow") + click.style("\ndescription:", fg="white")+click.wrap_text(click.style(Description,fg="yellow")) ))
            headlines += 1
            click.echo('\n')
    def get_sourc(self):
        api = "https://newsapi.org/v2/top-headlines?sources=ansa&apiKey=3688862811be47739cdbeef14755154c" 
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
            print(click.secho(click.style("Id:", fg ="white")+ click.style(source_id, fg="yellow") + click.style("\n url: ", fg="white")+ click.style( url, fg="yellow") + click.style("\ntitle:", fg="white")+ click.style(title, fg="yellow") + click.style("\ndescription:", fg="white")+click.wrap_text(click.style(Description,fg="yellow")) ))
            headlines += 1
            click.echo('\n')
    def get_so(self):
        api = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3688862811be47739cdbeef14755154c" 
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
            print(click.secho(click.style("Id:", fg ="white")+ click.style(source_id, fg="yellow") + click.style("\n url: ", fg="white")+ click.style( url, fg="yellow") + click.style("\ntitle:", fg="white")+ click.style(title, fg="yellow") + click.style("\ndescription:", fg="white")+click.wrap_text(click.style(Description,fg="yellow")) ))
            headlines += 1
            click.echo('\n')
    
reader = Sources("Afua")
#click.secho(click.style('TITLE: ' + h['title'], fg='green'))
print(click.secho(reader.user +"!" + "," + "welcome to our News Page.", fg="green"))
print(click.secho(click.style("1.Entertainment Weekly  ", fg="blue")))
print(click.secho("2. Argaam ", fg = "blue"))
print(click.secho("3. ANSA.it ", fg="blue"))
print(click.secho("4.BBC News  ", fg="blue"))
inputi = input("enter number of source:")
entry = int(inputi)
if entry == 1:
        reader.get_s()
elif entry == 2:
        reader.get_sou()
elif entry == 3:
        reader.get_sourc()
elif entry == 4:
        reader.get_so()
else:
        print("wrong entry")






    










