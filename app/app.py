#flask app
#serve up a jumbotron with a button in it
#first class activity on scraping {{  }}
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#start mongodb compass and establish a connection
#set up a mongo db connection using flask pymongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#create home route
@app.route("/")
def index():
    #identify the name of the db collection mars
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    #create mars collection in mongodb mars db
    mars = mongo.db.mars

    #call the function scrape all and assign to mars data
    mars_data = scrape_mars.scrape_all_content()
    mars.update({}, mars_data, upsert=True)

    return "Scraping Complete - Please return to homepage and refresh to view scraped Mars news, facts and images, thank you"
    








if __name__ == "__main__":
    app.run()