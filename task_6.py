import sqlite3  # provides an interface for working with SQLite databases in Python
import csv

with open('imdb.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'year', 'rating'])
    writer.writerow(['The Shawshank Redemption', 1994, 9.3])
    writer.writerow(['The Godfather', 1972, 9.2])
    writer.writerow(['The Godfather: Part II', 1974, 9.0])
    writer.writerow(['The Dark Knight', 2008, 9.0])
    writer.writerow(['12 Angry Men', 1957, 6.9])
    writer.writerow(["Schindler's List", 1993, 8.9])
    writer.writerow(['The Lord of the Rings: The Return of the King', 2003, 1.9])
    writer.writerow(['Pulp Fiction', 1994, 8.9])
    writer.writerow(['The Good, the Bad and the Ugly', 1966, 8.8])
    writer.writerow(['Forrest Gump', 1994, 3.8])

# Checking data base
conn = sqlite3.connect('imdb.db')

# Create a table ratings
conn.execute('CREATE TABLE ratings (id INTEGER PRIMARY KEY, '
             'title VARCHAR(20), year INT, rating FLOAT)')

# Adding data to the file imdb.csv
with open('imdb.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # skip file header
    for row in reader:
        conn.execute('INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)', row)

# Take care of changes and close the database
conn.commit()
conn.close()

# Display all entries in the ratings table in alphabetical order behind the title field
conn = sqlite3.connect('imdb.db')
cursor = conn.execute('SELECT * FROM ratings ORDER BY title')
print('DB sorted by ABC:')
for row in cursor:
    print(row)
conn.close()

# Display all entries in the ratings table with a rating greater than 8.70
conn = sqlite3.connect('imdb.db')
cursor = conn.execute('SELECT * FROM ratings WHERE rating > 8.70')
print('All entries in the ratings table with a rating greater than 8.70:')
for row in cursor:
    print(row)
conn.close()
