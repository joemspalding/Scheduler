import requests
from bs4 import BeautifulSoup
import json

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
    temp = '{' + "'value' : {}, 'name' : '{}'".format(t['value'],t.text) + '}'
    print temp
    dataTerm.append(temp)

#getting all the subjects from the drop down list
subject = soup.find(attrs={"name" : "subject"})
childSubject = subject.findChildren()
dataSubject = []

#creating a pseudo JSON object
for s in childSubject:
    temp = '{' + "'value' : '{}', 'name' : '{}'".format(s['value'],s.text) + '}'
    print temp
    dataSubject.append(temp)

print dataTerm
print dataSubject

with open('dataTerm.txt', 'w') as outTerm:
    json.dump(dataTerm, outTerm)

with open('dataSubject.txt', 'w') as outSubject:
    json.dump(dataSubject, outSubject)


