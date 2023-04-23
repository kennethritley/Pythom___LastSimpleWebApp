'''
This Python script is a "Hello World" using a very lightweight and popular
Python package called "Flask". Before you can use this application you must
"pip3 install Flask." Then when you start this application, what will happen
is that a "Hello World" will be sent out when you navigate to 
http://127.0.0.1:5000.

Ich möchte mich bei meinem KI-Freund und Kupferstecher herzlich bedanken.

Author: KEN
Date:   2023.04.23
'''

# For "hello_world" you need "Flask"
# For GET and PUT you need "request"
# For the HTML/JavaScript test you need "send_from_directory"
from flask import Flask, request, send_from_directory

# Flask is a class imported from the flask module. It is the main class
# that represents a Flask web application.  __name__ is a donder representing
# the name of the current module. It is essential to pass this to Flask so that it
# can determine the location of other resources, static files, etc.
app = Flask(__name__)

# We will demonstrate how to retrieve a cat's name (GET) and how to set the
# cat's name (PUT). Therefore, we need a global variable to store the name
cat_name = "Fluffy"

# This is a "decorator" that defines a route for the web app. This means that when a 
# user navigates to the root URL ("/") of the web app, the "hello_world()" function will be
# called.  In a more complicated app, this is where you would specify GET, PUT - but here
# it defaults to GET for this simple example.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Everything above was in SimpleWebApp.py. This new stsuff adds a new route
# "/cat" URL that accepts both GET and POST requests.  When a GET request
# is received, it returns the hard-coded cat's name. When a POST request
# is received, the 'cat' function gets the cat's name from the request.
# On a Mac you can test with
#    curl -X POST -F "name=Whiskers" http://127.0.0.1:5000/cat
# Not sure on Windows
@app.route('/cat', methods=['GET', 'POST'])
def cat():
    global cat_name
    # This next line shows how you can send log/debug messages to the terminal when
    # the Flask server is running
    print ("Scooby Doo")
    if request.method == 'GET':
        return cat_name
    elif request.method == 'POST':
        new_name = request.form.get('name')

        if new_name:
            cat_name = new_name
            return f"Successfully added cat with name {cat_name}."
        else:
            return "Please provide a cat name.", 400

# This route is how we handle http://localhost:5000/cat_page. 
# Because the Flask server app is located in /src and the HTML page is located
# in /static, we need "../static" to point to the file to be sent
@app.route('/cat_page',methods=['GET'])
def cat_page():
    # return render_template_string(open("cat_page.html").read())
    return send_from_directory('../static', 'cat_page.html')


# This route is how we handle the BUTTON PRESS "Set Cat Name" in http://localhost:5000/cat_page. 
# Because the Flask server app is located in /src and the HTML page is located
# in /static, we need "../static" to point to the file to be sent. When the button
# is pressed, the string in the text box is sent back as JSON.
@app.route('/cat', methods=['PUT'])
def set_cat_name():
    global cat_name
    new_name = request.json.get('name')
    if new_name:
        cat_name = new_name
        #Cat.set_name(new_name)
        return 'Cat name updated', 200
    else:
        return 'Invalid cat name', 400

# You might be wondering what this is. There is a CSS style sheet stored
# under LastSimpleWebApp/static/css/styles.css. This route is needed
# so that the Flask server can find the styles.css and send it to the
# browser for rendering. NOTE: If you want to include your own JavaScript
# code stored at LastSimpleWebApp/static/js/scripts.js, you'll need to 
# duplicate this code to create a route to handle that!  Pretty easy
# when you get the hang of it!
@app.route('/static/css/<path:filename>')
def serve_static(filename):
    return send_from_directory('../static/css', filename)

if __name__ == '__main__':
    app.run(debug=True)
