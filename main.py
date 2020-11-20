import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='booktracker'
)

mycursor = mydb.cursor()

def add_book(Title, Author, Genre, StartDate, EndDate, Pages, Progress, Finished):
    formatted_date = StartDate.strftime('%Y-%m-%d')
    formatted_date = EndDate.strftime('%Y-%m-%d')
    sql = 'INSERT INTO books (title, author, genre, startdate, enddate, pages, progress, finished) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '
    new_book = (Title,  Author,  Genre,  StartDate,
                EndDate, Pages,  Progress,  Finished)

    mycursor.execute(sql, new_book)
    mydb.commit()

def show_books():
    mycursor.execute('SELECT * FROM books WHERE Genre="Crime"')
    myresult = mycursor.fetchall()

    for book in myresult: 
        print(book)

def show_finished(): 
    mycursor.execute('SELECT * FROM books WHERE finished=1')
    myresult = mycursor.fetchall()

    for book in myresult: 
        print(book)


def show_titles(): 
    mycursor.execute('SELECT title FROM books')
    myresult = mycursor.fetchall()

    for book in myresult: 
        print(book)

def show_genres(): 
    mycursor.execute('SELECT genre FROM books')
    myresult = mycursor.fetchall()

    for book in myresult: 
        print(book)

show_titles()