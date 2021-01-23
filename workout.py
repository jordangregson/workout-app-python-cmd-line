import sqlite3
import sys
import os
os.system("clear")

class WorkoutData:
    def __init__(self, date, title, info):
        self.date = date
        self.title = title
        self.info = info

conn = sqlite3.connect('workout_data.db')
c = conn.cursor()

# c.execute("""CREATE TABLE workouts (
#             date text,
#             workouttype text,
#             workoutinfo text
#             )""")

def insert_data():
    with conn:
        c.execute("INSERT INTO workouts VALUES ('{}', '{}', '{}')".format(date, workoutTitle, workoutInfo))

def get_workouts_by_date(date):
    
    c.execute("SELECT * FROM workouts WHERE date= :date", {'date': date})
    return c.fetchall()

def show_all_workouts():
    with conn:
        c.execute("SELECT * FROM workouts")
        print(c.fetchall())



addOrClose = input("What would you like to do:\n(0) Exit\n(1) Enter a new workout\n(2) Show all workouts\n(3) Search workouts by date\n\n")



if(addOrClose == '0'):
    sys.exit(0)  

elif(addOrClose == '1'):
    date = input("What is today's date (MM/DD/YYYY: ")
    workoutTitle = input("What was the workout: ")
    workoutInfo = input("What did you do during the workout: ")   
    insert_data()

elif(addOrClose == '2'):
    show_all_workouts()


elif(addOrClose =='3'):
    search = input("Search date: ")
    searchDate = get_workouts_by_date(search)
    print(searchDate)
    pass

    



c.close()
