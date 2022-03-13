from flask import Flask, render_template, request, redirect, url_for
from DatabaseCode import readSQL, newDatabase, populate, writeSQL, populateHabit, printSQL
import datetime
app = Flask('app')

# newDatabase()
# populate()


@app.route('/', methods = ["GET"])
def mainPageGet():
  newDatabase()
  # populate()
  return render_template("index.html")

@app.route('/', methods = ["POST"])
def mainPagePost():
  newDatabase()
  # populate()
  return render_template("index.html")


@app.route('/loginpage', methods = ["GET"])
def loginPageGet():  
  return render_template("loginpage.html", error = "")

@app.route('/loginpage', methods = ["POST"])
def loginPagePost():
  username = request.form.get("username") #getting username from html form
  results = readSQL("SELECT * FROM person WHERE username = '{}'".format(username)) 
  if results == []:
    return render_template("loginpage.html", error = "Username not valid")
  else:
    if results[0][0] == username:
      
      #return render_template("userlanding.html") #return url_for("userLandingGet")
      return redirect(url_for('userLandingGet', username=username, firstname= results[0][1]))
      # return userLandingGet(results[0][1],username)


@app.route('/signuppage', methods =["Get"])
def signupPageGet():
  return render_template("signuppage.html", error="")

@app.route('/signuppage', methods =["POST"])
def signupPagePost():
  username = request.form.get("username") #return username and firstname from HTML form and assign to respective variables
  firstname = request.form.get("firstname")
  print("firstname: ", firstname)
  results = readSQL("SELECT * FROM person WHERE username = '{}'".format(username))
  print("YES")
  if results == []:
    #return url_for("userLandingGet")
    print("I worked")
    writeSQL("INSERT INTO person VALUES('{}','{}')".format(username,firstname))
    print("This SQL worked")
    #return render_template("userlanding.html",firstname=firstname)
    return redirect(url_for('userLandingGet', firstname=firstname, username=username))
  elif results[0][0] == username:
    print('i didint work')
    return render_template("signuppage.html", error = "Username not unique")
  else:
    return render_template("signuppage.html", error = "Error")
  
# First name not displayed when accessing through login

# @app.route('/userlanding', methods =["GET"])
# def userLandingGet():
#   return render_template("userlanding.html",firstname="")

@app.route('/userlanding', methods =["GET"])
# def userLandingGet(firstname,username):
def userLandingGet():
  print("request arg:", request.args)
  username = request.args.get("username")
  firstname = request.args.get("firstname")
  #if in here to test if there are habit, description,frequency
  if request.args.get("habitName"):
    habitName = request.args.get("habitName")#
    frequency = request.args.get("frequency")#
    description = request.args.get("description")#
    if habitName != "" and frequency != "" and description != "":
      writeSQL("INSERT INTO habit(username, habitName, description, frequency) VALUES('{}','{}', '{}','{}')".format(username, habitName, description, frequency))
    #  
   #if request.args.get("")     
    #addcode to validate they are not empty and add to database
  
  habitstreakslist = []  
  totalcompletelist = [] 
  habitbuttons = []
  print("hello")
  habits = readSQL("SELECT * FROM habit WHERE username = '{}'".format(username))
  #print("habits", habits)
  print("Length of habits:",len(habits))
  #TO DO run a subroutine in database code to populate habit streak
  if len(habits)> 0 :
    for i in range(len(habits)):
      habitstreaks = readSQL("SELECT * FROM habitstreak WHERE habitID = {}".format(habits[i][0]))
      print("Habitstreaks", habitstreaks )
      print("Length of habit streaks", len(habitstreaks))
      totalcomplete = 0 #total number of records where a habit has been complted regardless of streak
      entryDay = 0
      for n in range(len(habitstreaks)):
        if habitstreaks[3] == 1:
          totalcomplete += 1 
          entryDay = habitstreaks[2]
      print("Total Complete",totalcomplete)
      if totalcomplete == 0:
        completionrate = 0
      else:
        completionrate = round((totalcomplete/len(habitstreaks)*100)) #convert to % for the progress bar
      habitstreakslist.append(completionrate)
      totalcompletelist.append(totalcomplete) #do we need to save the amount of records?
      
      if habits[i][4] == "D":
        currentDate = str(datetime.date.today().strftime("%d/%m/%y")) #current date (day)
        if currentDate == entryDay: #make code for entryDay and entryWeek
          deactivate = True
        else:
          deactivate = False
      elif habits[i][4] == "W":
        currentWeek = str(datetime.date.today().strftime("%U")) 
        #current week of year
        #convert entryDay to week of year and save as entryWeek
        entryDay = entryDay.split("/")
        day = int(entryDay[0])
        month = int(entryDay[1])
        year = int(entryDay[2])
        entryWeek = datetime.date(year, month, day).strftime("%U")
        if currentWeek == entryWeek:
          deactivate = True
        else:
          deactivate = False
    # if deactivate == True:
    #   return render_template("userlanding.html")#how do I load this with the button deactivated?
        habitbuttons.append(deactivate)
  else:
    habits = []
    habitstreaklist = 0
    totalcompletelist = 0
    length = 0 
    habitbuttons = [False] ###
      
        #if today's date and the date of the last entry in habitstreak table is the same deactivate otherwise activiate. Then you need another condition if the button is checked to regenterate the page with deactive button
  #name, frequency, streak, totalcomplete, 
  return render_template("userlanding.html",username=username,firstname=firstname, habits=habits, habitstreaklist=habitstreakslist, totalcompletelist=totalcompletelist, length = len(habits),deactiveButton=habitbuttons,counter=0)#where to indent this? within the if otherwise you'll need to return an error
  #search database for persons habit and return all habits (query) 
  #change html of habit to run in for loop for each habit with their own data  

@app.route('/createHabit', methods = ["GET"])
def createHabitGet():
  
  return render_template("createHabit.html",firstname="")

@app.route('/createHabit', methods = ["POST"])
def createHabitPost():
  return render_template("createHabit.html",firstname="")

@app.route('/edithabitpage', methods = ["GET"])
def editHabitGet():
  return render_template("edithabitpage.html")

@app.route('/edithabitpage', methods = ["POST"])
def editHabitPost():
  return render_template("edithabitpage.html")

app.run(host='0.0.0.0', port=8080, debug=True)


# print("person table: \n")
# print(readSQL("SELECT * FROM person"))
# print("habit table: \n")
# print(readSQL("SELECT * FROM habit"))
# print("habitStreak table: \n")
# # print(readSQL("SELECT * FROM habitStreak"))
