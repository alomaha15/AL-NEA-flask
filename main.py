from flask import Flask, render_template, request, redirect, url_for
from DatabaseCode import readSQL, newDatabase, populate
app = Flask('app')

@app.route('/', methods = ["GET"])
def mainPageGet():
  newDatabase()
  populate()
  return render_template("index.html")

@app.route('/', methods = ["POST"])
def mainPagePost():
  newDatabase()
  populate()
  return render_template("index.html")

@app.route('/loginpage', methods = ["GET"])
def loginPageGet():  
  return render_template("loginpage.html", error = "")

@app.route('/loginpage', methods = ["POST"])
def loginPagePost():
  username = request.form.get("username")
  print(username)
  results = readSQL("SELECT * FROM person WHERE username = '{}'".format(username)) 
  if results == []:
    return render_template("loginpage.html", error = "Username not valid")
  else:
    if results[0][0] == username:
      #return url_for("userLandingGet")
      return render_template("userlanding.html")

@app.route('/signuppage', methods =["Get"])
def signuppageGet():
  return render_template("signuppage.html")

@app.route('/signuppage', methods =["POST"])
def signuppagePost():
  username = request.form.get("username")
  print(username)
  results = readSQL("SELECT * FROM person WHERE username = '{}'".format(username)) 
  if results == []:
    return render_template("signuppage.html", error = "Username not unique")
  else:
    if results[0][0] == username:
      #return url_for("userLandingGet")
      return render_template("userlanding.html")
  firstname = writeSQL("INSERT INTO person (firstname) VALUES (")
#   return render_template("signuppage.html")
  

@app.route('/userlanding', methods =["Get"])
def userLandingGet():
  return render_template("userlanding.html")

@app.route('/userlanding', methods =["POST"])
def userLandingPost():
  return render_template("userlanding.html")






#@app.route('/signuppage', methods = ["GET"])
#def loginPageGet():  
  #return render_template("loginpage.html", error = "")

app.run(host='0.0.0.0', port=8080, debug=True)