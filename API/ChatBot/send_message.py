from flask import Flask, request
import requests
import json
import emoji
import ncclient
from ncclient import manager
import xml.dom.minidom

bot_name = "Joke.Bot@webex.bot"

token="NTVkODBiZjctMzg5YS00ZDI0LTlmODgtZWI5MzY4OTkyZTc5NTBjOThiMDUtOGQy_PF84_consumer"
header = {"content-type": "application/json; charset=utf-8", "authorization":"Bearer " + token}


node="192.168.1.67"

def connect(node):
    try:
        device_connection=ncclient.manager.connect(host=node,port=8181)
        return device_connection
    except:
        print("Unable to connect "+ node)
############## Flask Application ##############

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
        webhook = request.json
        url = 'https://api.ciscospark.com/v1/messages'
        msg = {"roomId": webhook["data"]["roomId"]}
        sender = webhook["data"]["personEmail"]
        message = getMessage()
        message = message.lower().capitalize()
       
        if (sender != bot_name):
            if (message=="Hello" or message=="Menu"or message=="Help"):
                msg["markdown"] = "**Welcome to Joke bot **!<br/><br/> If you want to laugh type **Start**!"  
            elif(message=="Start"):
                msg["markdown"] = "Choose the category of the Joke you want!(type the number)<br/>**1.Programming**<br/>**2.Miscellaneous**<br/>**3.Dark**<br/>**4.Any**" 
            elif(message=="1"):
                a=getJokes("programming")
                b=json.loads(a)
                if(b["type"]=="single"):
                    msg["markdown"]="**PROGRAMMING JOKE**" +"<br/><br/>" + str(b["joke"])+"<br/><br/>(For another joke type **Start** again 😁)"
                elif(b["type"]=="twopart"):
                    msg["markdown"]="**PROGRAMMING JOKE**"+ "<br/><br/>" + str(b["setup"]) + "<br/>" + str(b["delivery"])+"<br/><br/>(For another joke type **Start** again 😁)"
            elif(message=="2"):
                c=getJokes("Miscellaneous")
                d=json.loads(c)
                if(d["type"]=="single"):
                    msg["markdown"]="**MISCELLANEOUS JOKE**" +"<br/><br/>" + str(d["joke"])+"<br/><br/>(For another joke type **Start** again 😁)"
                elif(d["type"]=="twopart"):
                    msg["markdown"]="**MISCELLANEOUS JOKE**" +"<br/><br/>" +str(d["setup"]) + str(d["delivery"])+"<br/><br/>(For another joke type **Start** again 😁)"
            elif(message=="3"):
                c=getJokes("Dark")
                b=json.loads(c)
                if(b["type"]=="single"):
                    msg["markdown"]="**DARK JOKE**" +"<br/><br/>" + str(b["joke"])+"<br/><br/>(For another joke type **Start** again 😁)"
                elif(b["type"]=="twopart"):
                    msg["markdown"]="**DARK JOKE**" +"<br/><br/>" +str(b["setup"]) + "<br/>"+"-"+"<br/>"+"-"+"<br/>"+"-" + str(b["delivery"])+"<br/><br/>(For another joke type **Start** again 😁)"
            elif(message=="4"):
                a=getJokes("Any")
                b=json.loads(a)
                if(b["type"]=="single"):
                    msg["markdown"]="<br/>" + str(b["joke"])+"<br/><br/>(For another joke type **Start** again 😁)"
                elif(b["type"]=="twopart"):
                    msg["markdown"]=str(b["setup"]) + "<br/>" + str(b["delivery"])+"<br/><br/>(For another joke type **Start** again 😁)"
            else:
                msg["markdown"] = "Sorry! didn't recognize that command 😕 <br/><br/> To start again type **Help** or **Hello** 😃"
            requests.post(url,data=json.dumps(msg), headers=header, verify=True)

def getMessage():
        webhook = request.json
        url = 'https://api.ciscospark.com/v1/messages/' + webhook["data"]["id"]
        get_msgs = requests.get(url, headers=header, verify=True)
        message = get_msgs.json()['text']
        return message

def getJokes(cat):
    url = "https://jokeapi-v2.p.rapidapi.com/joke/"+cat
    headers = {
       'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
    'x-rapidapi-key': "45dff1e8d5mshe07caab195b7110p176d7ajsn7508329e9c9b"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


app.run(debug = True)
