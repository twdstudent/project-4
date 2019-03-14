import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipePage'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/') 
def index():
    return render_template("index.html")
    
@app.route('/find_recipe')
def find_recipe():
    return render_template('find-recipe.html', recipePage=mongo.db.recipePage.find())
'''    
@app.route("/your_results", methods=["GET"])    
def your_results():
    return render_template('share-recipe.html', recipePage=mongo.db.recipePage.find())
'''    
@app.route('/share_recipe')
def share_recipe():
    return render_template('share-recipe.html')    
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipePage
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('share_recipe'))    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 


#'/' refers to the default route.

'''
MongoDB stores its data in a JSON like format called BSON.
so import something from the BSON library as well
'''

'''
setting it to true allows the changes to be picked up automatically in the browser.

MongoDB stores its data in a JSON like format called BSON.
so import something from the BSON library 
'''

