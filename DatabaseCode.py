import sqlite3, cgi, os  #importing libraries that may be of use to me. Libraries contain pretested code and modules so using these will save me time whilst programming

# form = cgi.FieldStorage()
#username = str(form.getvalue("username"))
#firstname = str(form.getvalue("firstname"))
#print(username)

def newDatabase():
    with sqlite3.connect("userDatabase.db")as db:
        cursor = db.cursor()

        sql  = """CREATE Table IF NOT EXISTS person(
                username text PRIMARY KEY,
                firstname text);"""
        cursor.execute(sql)

        sql  = """CREATE Table IF NOT EXISTS habit(
                habitID integer PRIMARY KEY AUTOINCREMENT,
                username text,
                habitName text,
                description text,
                frequency text,
                streak integer,
                FOREIGN KEY (username) REFERENCES person(username));"""
        cursor.execute(sql)

        sql  = """CREATE Table IF NOT EXISTS habitStreak(
                habitStreakID integer PRIMARY KEY AUTOINCREMENT,
                habitID integer,
                date integer,
                completed integer,
                FOREIGN KEY (habitID) REFERENCES habit(habitID));"""
        cursor.execute(sql)

# def populate():
#   writeSQL("INSERT INTO person VALUES ('guru1','Adam')")
  
#   writeSQL("INSERT INTO habit (username, habitName, description, frequency, streak) VALUES ('guru1', 'workout', 'workout for 20 minutes', 'D', 3)")
  
#   writeSQL("INSERT INTO habitStreak (habitID, date, completed) VALUES (0, 21, 'F')")

#   writeSQL("INSERT INTO person VALUES ('guru2','Bob')")
  
#   writeSQL("INSERT INTO habit (username, habitName, description, frequency, streak) VALUES ('guru2', 'read', 'readbook', 'M', 5)")

      
  #print(readSQL("SELECT * FROM person"))
  #writeSQL("INSERT INTO person (username) VALUES ('alomaha14') ")

def realPopulate(sql):
  with sqlite3.connect("userDatabase.db")as db:
    cursor = db.cursor()  
    writeSQL("INSERT INTO person VALUES ('guru1','Adam')")
    
    writeSQL("INSERT INTO habit (username, habitName, description, frequency, streak) VALUES ('guru1', 'workout', 'workout for 20 minutes', 'D', 3)")
    
    writeSQL("INSERT INTO habitStreak (habitID, date, completed) VALUES (0, 21, 'F')")
  
    writeSQL("INSERT INTO person VALUES ('guru2','Bob')")
    
    writeSQL("INSERT INTO habit (username, habitName, description, frequency, streak) VALUES ('guru2', 'read', 'readbook', 'M', 5)")
    
    writeSQL("INSERT INTO habitStreak (habitID, date, completed) VALUES (1, 29, 'T')")
    db.execute(sql)
  
    
    #print(readSQL("SELECT * FROM person"))


    
def populateHabit():
  #writeSQL("INSERT INTO person VALUES ('guru1','Bob')")
  writeSQL("INSERT INTO habit VALUES (null,'guru1', 'run', 'run 3km a day', 'daily',0)")
  #writeSQL("INSERT INTO habitStreak VALUES (13, 0)")

  writeSQL("INSERT INTO person VALUES ('guru2','Adam')")
  writeSQL("INSERT INTO habit VALUES (null, 'guru2', 'meditate', 'meditate 3 times a week', 'weekly',0)")
 # writeSQL("INSERT INTO habitStreak VALUES (10, 1)")
        
  #add 2 people
  #give them a habbit




#here I have established my database with the three tables that i will use throughout my program HABIT NAME IN PERSON TABLE

def checkDatabase():
    pass

def readSQL(sql):
  with sqlite3.connect("userDatabase.db")as db:
    cursor = db.cursor()
#this function enables me to perform some process on the database where I read data from the table(s)

    #cursor.execute("SELECT * FROM nonExistantTable")
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return results
    # cursor.execute("SELECT * FROM person")
    # results = cursor.fetchall()
    # print(results)

    # cursor.execute("SELECT * FROM habit")
    # results = cursor.fetchall()
    # print(results)


        
def writeSQL(sql):
  with sqlite3.connect("userDatabase.db")as db:
    cursor = db.cursor()    
#This function enables me to perform some process on the database where I write data to the table(s)
    db.execute(sql)
    #db.execute("INSERT INTO habitStreak (date, completed) VALUES (21, 'F')")
    
    #db.execute("INSERT INTO habit (username, description, frequency, streak) VALUES ('guru1', 'workout', 'D', 3)")

    #db.execute("INSERT INTO habit (username, description, frequency, streak) VALUES ('guru2, 'readbook', 'M', 5)")

    #db.execute("INSERT INTO habitStreak (habitID, date, completed) VALUES (1, 29, 'T')")

def deleteSQL():
    with sqlite3.connect("userDatabase.db")as db:
        cursor = db.cursor() 
        db.execute("DELETE FROM person WHERE username = 'guru1' ")
#I will use this function when I need to delete data from the table(s)

newDatabase()
# realPopulate()
# populateHabit()
# print("readSQL: ", readSQL())








# import sqlite3 

# def newDatabase():
#     with sqlite3.connect("userDatabase.db")as db:
#         cursor = db.cursor()

#         sql  = """CREATE Table IF NOT EXISTS person(
#                 username text PRIMARY KEY,
#                 firstname text);"""
#         cursor.execute(sql)

#         sql  = """CREATE Table IF NOT EXISTS habit(
#                 habitID integer PRIMARY KEY AUTOINCREMENT,
#                 username text,
#                 description text,
#                 frequency text,
#                 streak integer,
#                 FOREIGN KEY (username) REFERENCES person(username));"""
#         cursor.execute(sql)

#         sql  = """CREATE Table IF NOT EXISTS habitStreak(
#                 habitStreakID integer PRIMARY KEY AUTOINCREMENT,
#                 habitID integer,
#                 date integer,
#                 completed integer,
#                 FOREIGN KEY (habitID) REFERENCES habit(habitID));"""
#         cursor.execute(sql)

# def checkDatabase():
#     pass

# def readSQL():
#     with sqlite3.connect("userDatabase.db")as db:
#         cursor = db.cursor()
#         cursor.execute("SELECT * FROM person")
#         results = cursor.fetchall()
#         print(results)

#         cursor.execute("SELECT * FROM habit")
#         results = cursor.fetchall()
#         print(results)

#         cursor.execute("SELECT * FROM habitStreak")
#         results = cursor.fetchall()
#         print(results)

# def writeSQL():
#     with sqlite3.connect("userDatabase.db")as db:
#         cursor = db.cursor()    
#         db.execute("INSERT INTO person (username, firstName) VALUES ('guru1', 'Alex')")

#         #db.execute("INSERT INTO person (username, firstName) VALUES ('guru2', 'Alan')")

#         db.execute("INSERT INTO habit (username, description, frequency, streak) VALUES ('guru1', 'workout', 'D', 3)")

#         #db.execute("INSERT INTO habit (username, description, frequency, streak) VALUES ('guru2, 'readbook', 'M', 5)")

#         db.execute("INSERT INTO habitStreak (habitID, date, completed) VALUES (1, 29, 'T')")

#         cursor.execute("SELECT * FROM person")

#         results = cursor.fetchall()
#         print(results)

#         cursor.execute("SELECT * FROM habit")

#         results = cursor.fetchall()
#         print(results)

#         cursor.execute("SELECT * FROM habitStreak")

#         results = cursor.fetchall()
#         print(results)

#         cursor.execute("DELETE FROM person WHERE username = 'guru1'")

#         cursor.execute("SELECT * FROM person")

#         results = cursor.fetchall()
#         print(results)



