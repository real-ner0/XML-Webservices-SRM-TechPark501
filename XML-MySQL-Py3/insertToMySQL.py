#!/usr/bin/python3

import xml.etree.ElementTree as ET
import mysql.connector


tree = ET.parse("student.xml")
root = tree.getroot()

tags = []
elems = []

for elem in root:
	tags.append(elem.tag)
	elems.append(str(elem.text))

elems = tuple(elems)

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='security')
cur = mydb.cursor()

sql = "INSERT INTO xml (name,department,roll,venue,elective,year) VALUES (%s, %s, %s, %s, %s, %s)"

cur.execute(sql,elems)
mydb.commit()

print("ALL DONE...!")






