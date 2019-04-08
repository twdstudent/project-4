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
    
@app.route("/your_results", methods=["POST"])    
def your_results():
    print(request.form.to_dict())
    print('category is: {}'.format(request.form['category']))
    
    form_object = {
        'origin': request.form['origin'].lower(),
        'dietary_requirements': request.form['dietary_requirements'].lower(),
        'vegetarian_friendly': request.form['vegetarian_friendly'].lower(),
        'vegan_friendly': request.form['vegan_friendly'].lower(),
        'category': request.form['category'].lower()
    }
    
    recipes = mongo.db.recipePage.find(form_object)
    dumpedrecipes = dumps(recipes)
    recipes = json.loads(dumpedrecipes)
    
    for recipe in recipes:
        recipe['ingredients'] = recipe['ingredients'].split(', ')
        
    # for k, v in recipes[0].items():
    #     print('{} --> {}'.format(k, v))
        
    
    print(dumpedrecipes)
    
    for recipe in recipes:
        print('found a recipe!!! {} ------> {}'.format(recipe['title'], recipe['category']))
    
    return render_template('your-results.html', recipes=recipes)
    
  
@app.route('/share_recipe')
def share_recipe():
    return render_template('share-recipe.html')    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipePage
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('share_recipe'))    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipePage.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit-recipe.html', recipe=the_recipe,
                           categories=all_categories)    

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

'''    
@app.route("/your_results", methods=["GET"])    
def your_results():
    return render_template('share-recipe.html', recipePage=mongo.db.recipePage.find())
'''  
