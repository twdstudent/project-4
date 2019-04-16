import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import json
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
  
@app.route('/share_recipe')
def share_recipe():
    return render_template('share-recipe.html')    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipePage
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('share_recipe'))    
    
@app.route('/edit_recipe/<recipePage_id>')
def edit_recipe(recipePage_id):
    the_recipe =  mongo.db.recipePage.find_one({"_id": ObjectId(recipePage_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit-recipe.html', recipe=the_recipe,
                           categories=all_categories)
                           
@app.route('/update_recipe/<recipePage_id>')
def update_recipe(recipePage_id):
    recipe = mongo.db.recipePage
    recipe.update( {'_id': ObjectId(recipePage_id)},
    {
        'title':request.form.get('title'),
        'origin':request.form.get('origin'),
        'dietary_requirements': request.form.get('dietary_requirements'),
        'vegetarian_friendly': request.form.get('vegetarian_friendly'),
        'vegan_friendly':request.form.get('vegan_friendly'),
        'category':request.form.get('category'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
    })
    return redirect(url_for('find_recipe'))
    
@app.route('/delete_recipe/<recipePage_id>')
def delete_recipe(recipe_id):
    mongo.db.recipePage.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('find_recipe'))    

@app.route('/print_recipe/<recipePage_id>')
def print_recipe(recipePage_id):
    the_recipe =  mongo.db.recipePage.find_one({"_id": ObjectId(recipePage_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('print-recipe.html', recipe=the_recipe,
                           categories=all_categories) 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 

