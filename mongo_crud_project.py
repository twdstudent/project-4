import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "recipePage"
COLLECTION_NAME = "recipePage"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
def show_menu():
    print("")
    print("1. Add a recipe")
    print("2. Find a recipe")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option  
    
def get_record():
    print("")
    category = input("Enter category name: starter, main, side-dish, dessert or snack > ")
    origin = input("Enter country dish is from > ")
    dietary_requirements = input("Enter any dietry requirements ie nuts, gluten, dairy etc")
    vegetarian_friendly = input("looking for vegatarian dish? yes/no")
    vegan_friendly = input("looking for a vegan freindly dish? yes/no")

    try:
        doc = coll.find_one({'category': category.lower(), 'origin': origin.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc    
    
def add_record():
    print("")
    title = input("Enter Recipe Title > ")
    category = input("Enter category name, 'starter', 'main', 'side-order', 'dessert' or 'snack' > ")
    origin = input("Enter country of dish > ")
    ingredients = input("List the ingredients > ")
    instructions = input("List cooking instructions > ")
    dietary_requirements = input("Is it free from? ie nuts, if no allergy requirements in this dish then enter 'none' > ")
    vegetarian_friendly = input("Is your dish vegetarian freindly? yes/no > ")
    vegan_friendly = input("Is your dish Vegan freindly? yes/no > ")
    
    new_doc = {'title': title.lower(), 'category': category.lower(), 'origin': origin.lower(),
               'ingredients': ingredients, 'instructions': instructions, 'dietary_requirements': dietary_requirements,'vegetarian_friendly': vegetarian_friendly, 'vegan_friendly': vegan_friendly}
#calling the lower() method on title, category and origin. So that they are stored in the database in lowercase, thus making it easy for me to find later.               
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")
        
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
            
def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")            
    
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()    