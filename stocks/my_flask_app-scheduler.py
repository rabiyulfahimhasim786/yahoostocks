activate_this = '/var/www/stocksdess/t/venv/bin/activate_this.py'

#with open(activate_this) as file_:
with open(activate_this) as file:
   exec(file.read(), dict(__file__=activate_this))
import time
import atexit
from flask import Flask, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import requests
#from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') 
def hello_world():
   return 'Hello world from Flask!' 


@app.route("/ssl", methods =["GET", "POST"])
def sslchecker():
  #if request.method == "GET":
    #if True:
  requests.get("https://desss.com/")
  print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))#time.strftime convert a time string to tuple 
  return "Welcome Home :) !"

@app.route("/statuscode", methods =["GET", "POST"])
def statuscodechecker():
  #if request.method == "GET":
    #if True:
  requests.get("http://ssl.zunamelt.com/status/")
  print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))#time.strftime convert a time string to tuple 
  return "Welcome Home :) !"


@app.route("/gainers", methods=["GET", "POST"])
def print_date_time():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/gainersfile")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/mostactive", methods=["GET", "POST"])
def mostactive():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/mostactivefile")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/trending", methods=["GET", "POST"])
def trending():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/trendingfile")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/losers", methods=["GET", "POST"])
def losers():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/losersfile")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaq", methods=["GET", "POST"])
def nasdaq():
    #if request.method == "GET":
    #if True:
    requests.get("https://testing.mobilteam.repl.co/nasdaqefile")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/php", methods=["GET", "POST"])
def php():
    #if request.method == "GET":
    #if True:
    requests.get(
        "https://stocks.desss-portfolio.com/yahoo/yahoo_master_null_update")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaqc", methods=["GET", "POST"])
def nasdaqc():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/nasdaqc")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaqfuture", methods=["GET", "POST"])
def nasdaqfuture():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/nasdaqfuture")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaqcsv", methods=["GET", "POST"])
def nasdaqcsv():
    #if request.method == "GET":
    #if True:
    #requests.get("https://testing.mobilteam.repl.co/nasdaqcsvfiles")
    requests.get("https://ystocks.mobilteam.repl.co/nasdaqcsvfiles")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaq301", methods=["GET", "POST"])
def nasdaq301():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/ystocks301")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaq601", methods=["GET", "POST"])
def nasdaq601():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/ystocks601")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/nasdaq1001", methods=["GET", "POST"])
def nasdaq1001():
    #if request.method == "GET":
    #if True:
    requests.get("https://ystocks.mobilteam.repl.co/ystocks1001")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


@app.route("/php24", methods=["GET", "POST"])
def php24():
    #if request.method == "GET":
    #if True:
    requests.get(
        "https://stocks.desss-portfolio.com/yahoo/master_daytrading_truncate")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p")
          )  #time.strftime convert a time string to tuple
    return "Welcome Home :) !"


scheduler = BackgroundScheduler()
#scheduler.add_job(func=sslchecker, trigger="interval", seconds=5)#seconds=60)#minutes=13# hours=11
#scheduler.add_job(func=statuscodechecker, trigger="interval", hours=12)
#scheduler.add_job(func=sslchecker, trigger="cron", day='last sun')
scheduler.add_job(func=print_date_time, trigger="interval",
                  minutes=13)  #seconds=60)
scheduler.add_job(func=losers, trigger="interval", minutes=17)
scheduler.add_job(func=mostactive, trigger="interval", minutes=11)
scheduler.add_job(func=trending, trigger="interval", minutes=19)
#scheduler.add_job(func=nasdaq, trigger="interval", minutes=58)
#scheduler.add_job(func=nasdaqc, trigger="interval", minutes=10)
scheduler.add_job(func=nasdaqc, trigger="interval", minutes=8)
scheduler.add_job(func=nasdaqfuture, trigger="interval", minutes=30)
scheduler.add_job(func=php, trigger="interval", hours=11)
scheduler.add_job(func=nasdaqcsv, trigger="interval", hours=12)
scheduler.add_job(func=nasdaq301, trigger="interval", hours=12)
scheduler.add_job(func=nasdaq601, trigger="interval", hours=13)
scheduler.add_job(func=nasdaq1001, trigger="interval", hours=14)
scheduler.add_job(func=php24, trigger="interval", hours=24)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

# app.run(host='0.0.0.0', port=5000)