def main():
    
    import pickle
    import os
    import sys

    os.system("clear")

    
    

    print("What would you like to do?\n\n0:Exit\n1:Enter new workout\n2:View Previous Workouts\n")
    userSelect = input()
    
    if(userSelect == 0):
        sys.exit

    elif(userSelect == "1"):
        date = input("Date: ")
        e = input("Exercise: ")
        d = input("Information about the exercise: ")

        a = "data"
        data = []
        file = open(".dat", "wb")
        data.append((date))
        data.append((e))
        data.append((d))

        pickle.dump(data, file)

        print(data)

    #elif(userSelect == "2"):


main()