# Project 4, Recipe Site.
#### Using Flask.

- <a href="https://github.com/twdstudent/project-4">Link to GitHub Repository.</a>
- <a href="https://dashboard.heroku.com/apps/project-4-recipe-site">Link to Heroku Repository.</a>


use sudo pip install flask.
And that sets us up with our Flask functionality ready to be imported.


To get Flask talking to Mongo, we're going to install a third party library called flask-pymongo.
This is just slightly different from the pymongo that you would have used in our earlier lessons in the sense that it's optimized to work with Flask.
So we've installed that.
We also need to install a package called dnsython to use the new style connection string for MongoDB Atlas.

command line used to un-install out dated mongodb library and use more updated version:
wget -q https://git.io/fh7vV -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh

https://youtu.be/jfan7PwYWwg