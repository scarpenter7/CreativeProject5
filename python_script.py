from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Wassupp homiesssssss<br> this is the request method: {}".format(request.method)
    
@app.route("/wassup")
def wassup():
    return "<h1>Whaddup gangasta</h1>"

@app.route("/profile/<username>") # this is how you pass in a string
def profile(username): 
    return "Wassup {}".format(username)

@app.route("/post/<int:post_id>") # this is how you pass in an int or any other data type
def show_int(post_id): 
    return "This is my favorite number: {}".format(post_id)

@app.route("/addmethods", methods=["GET", "POST"]) # this is how you add the POST method
def addmethod():
    if request.method == "GET":
        return"The request method is GET!!!"
    elif request.method == "POST":
        return"The request method is POST!!!"
    else:
        return"Bad request method"

@app.route("/template/<name>")
def template(name):
    return render_template("index.html", name=name)
    
@app.route("/bangbang")
@app.route("/bangbang/<dumbdumb>") # multiple urls to a single function
def double_url(dumbdumb=None):
    return render_template("demo_template.html", dummy = dumbdumb) # note the html uses jinja syntax

@app.route("/mylist") # using list objects
def coollist():
    food = ["Fruit", "Chicken", "Burritos", "Ice Cream", "Rice"]
    return render_template("shopping.html", mylist = food)

host = 'localhost' # '0.0.0.0' #"127.0.0.1" # I tried all of these ip's

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8080)) # I also tried port was 5000
    app.run(host='0.0.0.0', port=8080, debug=True)