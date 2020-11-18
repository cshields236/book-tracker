from firebase import  firebase

def connect():
    firebase = firebase.FirebaseApplication('https://book-tracker-696b0.firebaseio.com', None)

# result = firebase.get('/Test', None)
# print(result)

def add_book(Title, Author, Genre, StartDate, EndDate, Pages, Progress, Finished):
    new_book = [Title, Author, Genre, StartDate, EndDate, Pages, Progress, Finished]
    result = firebase.post('/books', new_book)
    print(result)