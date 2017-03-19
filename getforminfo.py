import requests
from bs4 import BeautifulSoup
import json
import ast

url = "https://htmlaccess.louisville.edu/classSchedule/setupSearchClassSchedule.cfm?error=1"

#setting up the webpage for scraping
result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,"html.parser")

#getting all the terms from the drop down list
term = soup.find(attrs={"name" : "term"})
childTerm = term.findChildren()
dataTerm = []

#creating a pseudo JSON object
for t in childTerm:
    temp = "{" + "'value' : {}, 'name' : '{}'".format(t['value'], t.text) + "}"
    dataTerm.append(ast.literal_eval(temp))

#getting all the subjects from the drop down list
subject = soup.find(attrs={"name" : "subject"})
childSubject = subject.findChildren()
dataSubject = []

#creating a pseudo JSON object
for s in childSubject:
    temp = "{" + '"value" : "{}", "name" : "{}"'.format(s['value'], s.text) + "}"
    dataSubject.append(ast.literal_eval(temp))
else:


with open('dataTerm.json', 'w') as outTerm:
    json.dump(dataTerm, outTerm)

with open('dataSubject.json', 'w') as outSubject:
    json.dump(dataSubject, outSubject)

print "All data processed into JSON files"
