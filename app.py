import os
import env #will import the entire file, and therefore, allow us access to our environmental variables.
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

'''
MongoDB stores its data in a JSON like format called BSON.
so import something from the BSON library as well
'''

app = Flask(__name__)
#app.config["MONGO_DBNAME"] = 'recipe_page'
#app.config["MONGO_URI"] = os.environ.get('SRV_CONNECTION_STRING')

#mongo = PyMongo(app)

@app.route('/') #'/' refers to the default route.
def index():
    return render_template("index.html")
    
@app.route('/find')
def find():
    return render_template('find-recipe.html')   
    
@app.route('/share')
def share():
    return render_template('share-recipe.html')    
    
@app.route('/contact')
def contact():
    return render_template('contact.html')    

#@app.route('/get_recipe')

#def get_recipe():
#    return render_template("find-recipe.html", tasks=mongo.db.recipe.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
'''
setting it to true allows the changes to be picked up automatically in the browser.
'''