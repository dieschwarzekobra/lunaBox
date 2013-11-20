import sqlite3

# Define and initialize global variables
STATEMENT = 'SELECT * FROM sailorMoon ORDER BY episode'

# Define a querying function that prints to the console
def query(statement, i):
  rows = c.execute(statement)

  for row in rows:
    # Print entire row or print selected column
    if i >= 0:
      print row[i]
    else:
      print row
  return

# Connect to the database
conn = sqlite3.connect('sailorMoon.sqlite')
c = conn.cursor()

# Query the database and print titles
query(STATEMENT, 1)

