"""
Module Name:   SavedItems.py
Coded by:      Daniel Austin
Date coded:    July 16, 2020.
Date approved: July 27, 2020
Approved by:   Daniel Austin

Desctiption:   This module handles the backend of the 'saved items' portion of PriceAid. 
               That is, when a user wants to save an item for later, this module is 
               used to store the information about that item in a database.

Arguments:
    arg connection: A connection object to the relational database
    arg cursor: The cursor within the database object.

Files accesed:
    saveditems - A relational database.

Testing File:  savedItems_tests.docx

"""
import os
import mysql.connector

#Connect to database
print("Connecting...")
connection = mysql.connector.connect(host='localhost',
                                         database='saveditems',
                                         user='root',
                                         password='')
cursor = connection.cursor()
print("Connected")


def addNewItem(item, url, imageUrl, price): 
    #Adds a saved item
    sql = 'INSERT INTO saved_table (Name, URL, ImageUrl, Price) VALUES (%s, %s, %s, %s)'
    val = (item, url, imageUrl, price)
    try:
        cursor.execute(sql, val)
    except mysql.connector.errors.IntegrityError:
        return "Item already saved"
    connection.commit()
    return "Item inserted"

def removeItem(item):
    #Removes a saved item
    cursor.execute("DELETE FROM saved_table WHERE Name = '{}'".format(item))
    count = cursor.rowcount
    if (count == 0):
        return "Item does not exist"
    connection.commit()
    return "Item deleted successfully"


def cleanCart():
    #Emptys all saved items
    cursor.execute("DELETE FROM saved_table")
    connection.commit()
    return "Saved items cleaned"

def displayData():
    #Displays all data in the saved items table, used for debugging.
    cursor.execute("SELECT * FROM saved_table")
    for x in cursor:
        print(x)
