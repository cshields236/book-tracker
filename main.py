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


add_book('Champagne Football', 'Mark Tighe', 'Sport', datetime.datetime(
    2020, 5, 17), datetime.datetime(2020, 5, 19), 350, 350, True)
