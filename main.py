from flask import Flask, request
import json 
from services.quickSort import quickSort
from services.palindrom import is_palindrom
from database.database import DatabaseConnection 
app = Flask(__name__)
DATABASE_HOST='localhost';
DATABASE_USER='postgres';
DATABASE_PASSWORD='passwd123';
DATABASE_NAME='test_database';
database = DatabaseConnection(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME)

@app.get("/sort-my-list")
def sortListFunction():

    args = request.args
    print(args)
    reqList = json.loads(args.get('reqList'))
    resList = quickSort(reqList)
    print(resList)
    return {"sortedList":json.dumps(resList)}

@app.get("/check-if-palindrom")
def chekfIfPalindrom():

    args = request.args
    print(args)
    reqWord = args.get('reqWord')
    resWord = is_palindrom(reqWord)
    return {"isPalindrom":resWord}

@app.get("/users")
def getAllUsers():

    res = database.getAllUsers()
    return {"users":res}

@app.get("/user")
def getUser():
    args = request.args
    print(args)
    reqData = {"name": args.get('name'), "last_name": args.get('last_name')}
    res = database.getByName(reqData)
    return res

@app.post("/user")
def addNewUser():
    
    res = database.addUser(request.get_json())
    print(request.get_json())
    print("request.form")

    if(res == True):
        return ""
    else:
        return res

@app.post("/user/relation")
def addNewRelation():
    
    res = database.addRelation(request.get_json())
    print(request.get_json())
    print("request.form")

    if(res == True):
        return ""
    else:
        return res

@app.get("/user/relation")
def getUserRelation():
    args = request.args
    print(args)
    reqData = {"name": args.get('name'), "last_name": args.get('last_name')}
    res = database.getRelationsByName(reqData)
    
    return res

@app.get("/user/relation/camera")
def findCamera():
    args = request.args
    print(args)
    
    
    reqData = {"name": args.get('name'), "last_name": args.get('last_name')}
    checked = [reqData]
    checkList = []
    res = database.getRelationsByName(reqData)
    checkList.extend(res)
    while(True):
        checkListAfter = []
        if len(checkList) == 0:
            return {"errorMessage": "no connection found"}
        for i in checkList:
            print("checkNow:")
            print(i[0])
            print(i[1])
            if {"name": i[0], "last_name": i[1]} in checked:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue
            currentUser = database.getByName({"name": i[0], "last_name": i[1]})
            print(currentUser[0][4])
            print(currentUser[0][4])

            if currentUser[0][4] == "CAMERA":
                print("FOUND")
                return {"name": i[0], "last_name": i[1]}
            checked.append({"name": i[0], "last_name": i[1]})
            addF = database.getRelationsByName({"name":i[0], "last_name": i[1]})
            checkListAfter.extend(addF)
        checkList = checkListAfter
        print("new List is:")
        print(checkList)

app.run()