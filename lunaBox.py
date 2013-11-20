import sqlite3

# Define and initialize global variables
STATEMENT_PRINT_ALL_TITLES = 'SELECT * FROM sailorMoon ORDER BY episode'
STATEMENT_PAGINATE = 'SELECT * FROM sailorMoon ORDER BY episode LIMIT 6'

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

# Count the number of records in the database
def count(statement):
  rows = c.execute(statement)


# Connect to the database
conn = sqlite3.connect('sailorMoon.sqlite')
c = conn.cursor()

# Query the database and print titles
# query(STATEMENT, 1)

# Query the database and print six entries
query(STATEMENT_PAGINATE, 1)