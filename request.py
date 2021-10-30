import  requests
import json
import os
if os.path.isfile("courses.json"):
    with open("courses.json","r") as a:
        y=json.load(a)
else:

  r=requests.get('http://saral.navgurukul.org/api/courses')    #print(dir(r)) getting all the directoties
  y=r.json()                                                    #print(help(r))# getting the help from the server of the link
                                                             #print(r.text) prints the text from the particular link in the requested data
with open("courses.json","w") as response:
      json.dump(y,response,indent=4)
j=0
for i in y["availableCourses"]:#getting available courses
    print(j+1,".",i["name"],"_",i["id"],i["type"]) #working on the loop to print the name and id of the course
    j+=1   
#y=json.dump(y)
course=int(input("Enter the course number:"))#getting the course number and printing its details such as name
print(y["availableCourses"][course-1]["name"])
if os.path.isfile("serial.json"):
    with open("serial.json","r") as b:
        t=json.load(b)
else:
    s=requests.get('http://saral.navgurukul.org/api/courses/'+str(y["availableCourses"][course-1]["id"])+'/exercises')
    t=s.json() #get the data from the saral and dump as json file and getting the values of the courses id 
    with open("serial.json","w") as new_file:
        json.dump(t,new_file,indent=4) 
    n=0
    s=0 #intialized to get the serial number
    for i in t.values():#loop to get the values of the data stored in the json file 
        for k in  i:#running another loop for the values of the data 
            print(n+1,".",k[ "name"]) #printing the name withe the serial number as n
            n=n+1 
            print(s+1,t["data"]["availableCourses"][i]["name"])
            s+=1
 #intialized to get the serial number
user3=int(input("Enter parent number:"))#getting the user input to print data in the parent 
if t["data"][user3-1]["childExercises"]!=[]:
    d=0
    for j in range(len(t["data"][user3-1]["childExercises"])): #getting the other fields from the child exercise
      print(d+1,t["data"][user3-1]["childExercises"][j]["name"]) #data printing from childExercise
      d=d+1 #checking for the childexercise
    #print(t["data"][user3-1]["slug"])  
else:
    print(t["data"][user3-1]["slug"])
child=int(input("Enter child number:")) #child number input to fetch its data 
print(t["data"][user3-1]["childExercises"][child-1]["name"]) 
if os.path.isfile("slug.json"):
       with open("slug.json","r") as c:
        tr=json.load(c)
else:
    slug_url=requests.get('http://saral.navgurukul.org/api/courses/'+str(t["data"][user3-1]["childExercises"][child-1]["id"])+'/exercise/getBySlug?slug='+(t["data"][user3-1]["childExercises"][child-1]["slug"]))
    tr=slug_url.json()
    with open("slug.json","w") as content_file:
        json.dump(tr,content_file,indent=4)
        print(tr["content"])

 