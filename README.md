# Project 4, Recipe Site.
#### Using Flask.

- <a href="https://github.com/twdstudent/project-4">Link to GitHub Repository.</a>
- <a href="https://dashboard.heroku.com/apps/project-4-recipe-site">Link to Heroku Repository.</a>
- <a href="https://project-4-recipe-site.herokuapp.com/">Live site on Heroku</a>

A simple cook book website where people can view update and add recipes for others to see.
Taken this site down to its bare CRUD coponents.

*UX*
Wire frames located in the wireframes directory of this project.
Site was kept simple as possible, the navbar is responsive to allow for better navigation on smaller devices such as mobiles etc.
CSS styling is kept to a minimum, bootstrap was used for styling of buttons and forms.

I ran into some heavy problems in this project which forced me to abandoned a part of it, originally I planned to to have a form where a user
could filter there options and view the results that are filtered out that match the selection (is vegetarian friendly etc).
But after weeks of head scratching and crying I decided to leave this out as it was taking up too much time with no results and time was running
out.
So as a result, I decided to just stick with a basic CRUD application where you can view a recipe, add a recipe, edit a recipe and delete a recipe.
I added in printing functionality where a user is able to open a recipe in full screen and, if wanted, go on to print it.

*Printing*:
Users can print each recipe, when you click on the print button at the bottom of each recipe it redirects you to a new page
so you can see the selected recipe in full screen and then print. Nav bar available to take you back to main site.

*Inputting a recipe*:
Simple and responsive form was used for a user to input a recipe, dropdown selections were used to ensure users could only enter pre-determined
options like the allergen section-this would make life easier when searching the DB.

*The Recipes*:
On the find recipe page, all recipes that are in the DB are displayed here, I decided to keep each recipe within a div with overflow set to auto
and with use of media queries made said divs responsive so that large recipes didn't take up to much retail space and make the page seem 
cluttered.

### Future plans!
Despite what my parents say, I do have plans, but back this project!
I would like to add (mentioned earlier) a search filter where a user can use the same form they used to input a recipe to seatch for a spceific
recipe that matches there desired criteria ie vegan freindly, gluten free etc.
A log in feature is something I'd want to add, this would help with only allowing users to edit/delete reipes they have entered.
Abiltility to add images so a user can show/see what the final result will look like.
And finally a thumbs up/down, like facebook users would be able to like or even dislike a recipe allowing me to show users most popular dush etc.

### Technologies Used
This is a Flask application. HTML used within the templates and CSS used for styling, JS used to wirte functionality for printing recipes.
Bootstrap was used for styling buttons and forms.
MongoDB was used for storing and retrieving recipes.
Google fonts was also used, 'Dosis' was used for the titles.

### Testing 
testing of this site has primarly been done using chrome tools to test responsiveness also by adding and editing recipes through the site it self
see if CRUD functionality is working and connected to MongoDB, this was done through C9 and the lainched app through Heroku.

### Deployment
This site is backed up to both GitHub and Heroku (links at the top of this file).
Initially the site was first backed to GitHub and then I linked to it through Heroku so that every time I did a push to GitHub it would also back up
Heroku.

Config Var for Heroku as follows:<br>
*IP 0.0.0.0*<br>
*MONGO_URI mongodb+srv://twdstudent:<password>recipepage-pd1w8.mongodb.net/recipePage?retryWrites=true*<br>
*PORT 5000*<br>

### Deployment on GitHub (not including final commit for submission);
- intial commit.
- build and succesfully connected to mongodb database.
- linking database to find recipe page to site.
- fixed bug in app.py file.
- backing to share.
- fixed connection issues with find recipe template.
- adde form for find recipe page.
- successfully link submission form to mongodb.
- updated req.txt file.
- fixing bug with req.txt file.
- added printing functionality.
- getting ready for mentor session.
- removed contact template as not relevent.
- updating for mnetoring.
- fixed printing functionality & edit button wired up succesfully.
- removed form search page along with backend code for it.
- more styling o buttons, delete functionality added & working.
- updated readme.md file, fixed edit button bug.
- fixed post method on edit button.
- updated read me file and tweeked some styling.
- tidy up of comments in HTML code, removed unneeded CDN links and tweeked styling.

#### Credits
Would like to thank my mentor Chris Zielinski for his help and guidence with this proejct.
#### Content
recipes on this site were gathered from *https://www.bbcgoodfood.com/recipes*
#### Media
The photo used in this site are of my own *Thomas Dodson*
#### Acknowledgements
I received inspiration for this project from my love of food! 
