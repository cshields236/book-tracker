from firebase import firebase
import datetime

firebase = firebase.FirebaseApplication(
    'https://book-tracker-696b0.firebaseio.com', None)


def show_books():
    result = firebase.get('/books', None)
    print(result)


def add_book(Title, Author, Genre, StartDate, EndDate, Pages, Progress, Finished):
    new_book = {
        'Title': Title, 'Author': Author, 'Genre': Genre, 'Start Date': StartDate, 'End Date': EndDate, 'Pages': Pages, 'Progress': Progress, 'Finished': Finished
    }
    result = firebase.post('/books', new_book)
    print(result == None)


# add_book('Champagne Football', 'Mark Tighe', 'Sport', datetime.datetime(
#     2020, 5, 17), datetime.datetime(2020, 5, 19), 350, 350, True)

show_books()