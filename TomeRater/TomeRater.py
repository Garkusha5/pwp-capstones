"""
================================================================================
Section: Create a User
================================================================================
"""
class User(object):
    def __init__(self, name, email):
        """
        A constructor which takes self, name and email. It should set instance
        variables self.name, self.email, and self.books.
        """
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        """
        A method that returns the email associated with a given user
        """
        return self.email

    def change_email(self, email):
        """
        A method that takes in a new email and changes the email associated with this user. 
        Should also print message saying the user's email has been updated.
        """
        if email.find('@') == -1 or (email.find('.com') == -1 and email.find('.edu') == -1 and email.find('org') == -1):
            print('\'{email}\' is not a valid e-mail. A valid e-mail must include \'@\' and the domain name\nAccepted domains are:\n> .com\n> .edu\n> .org\nTry again.'.format(email=email))
        elif email == self.email:
            print('{email} is already associated with this user.'.format(email=email))
        else:
            old_email = self.email
            self.email = email
            print('You have successfully updated the user email associated with {user} from:\n{old_email}\nto\n{email}.'.format(user=self.name, old_email = old_email, email=self.email))

    def __repr__(self):
        """
        A string representation method that returns a string to print the user info in a human readable format.
        """
        count_books = 0
        for book in self.books.keys():
            count_books += 1
        return 'User {user}:\n> E-mail address: {email}\n> Books Read: {count_books}'.format(user=self.name, email=self.email, count_books=count_books)

    def __eq__(self, other_user):
        """
        A method to define comparison between User objects.
        A User object should be equal to another User object if they both have the same name and email.
        Adding a validation step to make sure that the two objects being compared are instances of the User class
        """
        if isinstance(other_user, User):
            return self.name == other_user.name and self.email == other_user.email
        else:
            print('Invalid comparison. Comparison must be between two instances of User. Current comparison references a {type} object'.format(type=type(other_user)))

    def read_book(self, book, rating=None):
        """
        Method which takes in book and an optional parameter rating , which defaults to None. 
        It should add a key:value pair to self.books where the key is book and the value is rating.
        Adding a validation step to make sure that the key being passed through is a Book object.
        """
        if isinstance(book, Book):
            self.books[book] = rating
        else:
            print('Invalid entry. {book} is not an instance of the class, Book.\nBe sure to create a book object by calling the Book class'.format(book=book))

    def get_average_rating(self):
        """
        Method which *iterates* through all of the values in self.books and calculates + returns the average rating
        Adding some validation to make sure we skip None values (default rating in None) and that the dictionary actually has values
        """
        sum_values = 0
        num_values = 0
        if len(self.books) > 0:
            for book_rating in self.books.values():
                if book_rating is not None:
                    sum_values += book_rating
                    num_values += 1
                else:
                    continue
            return sum_values / num_values
        else:
            print('{name} has not logged any ratings for their books.\nTo log a book, simply call the \'Read Book\' method'.format(name=self.name))


"""
================================================================================
Section: Create a Book
================================================================================
"""
class Book(object):
    def __init__(self, title, isbn):
        """
        Constructor (see 'dunder') method which takes self, title, and isbn. Set instance variables self.title, and self.isbn.
        Also set self.ratings as an empty list
        Adding a string method .title() to make sure that the book title is formatted correctly.
        """
        self.title = title.title()
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        """
        Method that returns the title of the book
        """
        return self.title

    def get_isbn(self):
        """
        Method that returns the isbn of the book
        """
        return self.isbn

    def set_isbn(self, isbn):
        """
        A method set_isbn that takes in a new ISBN and sets the book's ISBN to be this number.
        It should also print a message indicating that this book's ISBN has been updated
        """
        if isbn == self.isbn:
            return '{isbn} is already associated with this book.'.format(isbn=isbn)
        else:
            self.isbn = isbn
            return 'You have successfully updated the ISBN associated with {book}. The new ISBN is: {isbn}.'.format(book=self.title, isbn=self.isbn)

    def add_rating(self, rating):
        """
        A method called add_rating that takes in a rating and adds it to self.ratings.
        It should only accept ratings between 0 and 4, otherwise print 'Invalid Rating'
        """
        if rating is None or rating < 0 or rating > 4:
            print('Invalid Rating.')
        else:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        """
        A method to define comparison between Book objects.
        A Book object should be equal to another Book object if they both have the same title and isbn.
        Adding a validation step to make sure that the two objects being compared are instances of the Book class
        """
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            print('Invalid comparison. Comparison must be between two instances of Book. Current comparison references a {type} object'.format(type=type(other_book)))

    def get_average_rating(self):
        """
        Method which *iterates* through all of the values in self.ratings and calculates
        and returns the average.
        Repurposing code from User class.
        """
        sum_values = 0
        num_values = 0
        if len(self.ratings) > 0:
            for book_rating in self.ratings:
                sum_values += book_rating
                num_values += 1
            return sum_values / num_values
        else:
            print('{name} has not logged any ratings for their books.\nTo log a rating, simply call the \'Add Rating\' method'.format(name=self.name))

    def __hash__(self):
        """
        A __hash__ method to make sure we can make a dictionary in User that has Book objects as keys
        """
        return hash((self.title, self.isbn))

    def __repr__(self):
        """
        Adding a string representation method to return a human readable string when printing the object 
        """
        return '{title} by {author}, with an average rating: {average_rating}'.format(title=self.title, author=self.title, average_rating=self.get_average_rating())

"""
================================================================================
Section: Make a Fiction Subclass of Book
================================================================================
"""
class Fiction(Book):
    """
    Subclass, Fiction (i.e. a type of Book) which inherits from the parent class, Book.
    """
    def __init__(self, title, author, isbn):
        """
        A constructor which takes self, title, author, and isbn.
        It should call the __init__ of its parent class, with title and isbn.
        Then it should set the instance variable self.author
        Adding string formatting to make sure the author's name is formatted correctly.
        """
        super().__init__(title, isbn)
        self.author = author.title()

    def get_author(self):
        """
        A method which returns the author
        """
        return self.author

    def __repr__(self):
        """
        String representation to return a string outlining attributes of the Fiction object in a human readable format.
        """
        return '{title} by {author}'.format(title=self.title, author=self.author)

"""
================================================================================
Section: Make a Non-Fiction Subclass of Book
================================================================================
"""
class Non_Fiction(Book):
    """
    Subclass, Non-Fiction (i.e. a type of Book) which also inherits from the parent class, Book.
    """
    def __init__(self, title, subject, level, isbn):
        """
        A constructor which takes in self, title, subject, level and isbn.
        It should first call the __init__ of its parent class with title and isbn.
        Then, it should set instance variables self.subject and self.level
        """
        super().__init__(title, isbn)
        self.subject = subject.title() # Setting instance variable for subject. Adding a string formatting method to match formatting from instructions
        self.level = level.lower() # Setting instance variable for the book level. Adding a string formatting method to match formatting from instructions

    def get_subject(self):
        """
        A method which returns the subject
        """
        return self.subject

    def get_level(self):
        """
        A method which returns the level
        """
        return self.level

    def __repr__(self):
        """
        String representation which will return a string outlining attributes of the Non-fiction object in a human readable format
        """
        return '{title}, a {level} manual on {subject}.'.format(title=self.title, level=self.level, subject=self.subject)

"""
================================================================================
Section: Give Books and Users Methods
Now that we multiple classes, we can create more methods (that potentially reference other classes)
For User Class - add following methods:
> read_book which takes book and an optional parameter rating (default=None),
and adds them as a key value pair to self.books where book is the key and the value is rating.
> get_average_rating, which iterates through all the values in self.books (ratings),
and calculates + returns the average

For the Book class - add following methods:
> get_average_rating which iterates through the values in self.ratings, 
and calculates + returns the average
> __hash__ to make sure we can make a dictionary in User that has Book objects as keys

^ see relevant methods above.
================================================================================
"""

"""
================================================================================
Section: Create TomeRater

================================================================================
"""
class TomeRater(object):
    """
    Application to store users, their books, and applicable attributes for both
    """
    def __init__(self):
        """
        Constructor that only takes self, but will create two empty dictionaries:
        > one dictionary that will map users' emails to the corresponding User objects
        > one dictionary that will map Book objects to the number of Users that have read it
        """
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        """
        A method which creates + returns a new Book with the title and isbn provided
        Adding an isbn validation to make sure all books have unique ISBN's
        """
        existing_isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in existing_isbns:
            print('{isbn} already exists in the list of books.\nCheck the ISBN provided and try again.'.format(isbn=isbn))
        else:
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """
        A method which creates + returns a new Fiction with the title, author, and isbn provided.
        """
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """
        A method which creates + returns a new Non_Fiction object with the title, subject, level, and isbn provided.
        """
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        """
        Method which takes a book, email, and optional rating (defaults to None), and gets the user
        in self.users with the key 'email'. 
        If the user doesn't exist, it should print a string
        indicating that the user doesn't exist. If the user exists:
        > call the read_book method on the user, with book and rating
        > call add_rating on book, with rating
        > check if the book is in TomeRaters self.books dictionary:
        > If it's not - add the key book to self.books with a value of 1
        > If it is, increase the value associated with that book by 1
        """
        if self.users.get(email) is not None:
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print('No user with email {email}.'.format(email=email))

    def add_user(self, name, email, user_books=None):
        """
        Method which creates a new User object from name and email.
        Also, if user_books is provided (i.e. not None) then it should ook through the list
        and add each Book to the user (using the method add_book_to_user)
        Adding same validation from User class to validate user email
        """
        if email.find('@') == -1 or (email.find('.com') == -1 and email.find('.edu') == -1 and email.find('org') == -1):
            print('\'{email}\' is not a valid e-mail. A valid e-mail must include \'@\' and the domain name\nAccepted domains are:\n> .com\n> .edu\n> .org\nTry again.'.format(email=email))
        if email in self.users.keys():
            print('The user already exists with the email \'{email}\'.'.format(email=email))
        else:
            self.users[email] = User(name, email)
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        """
        method which iterates through all of the keys in the self.books (these are Book objects) and prints them
        """
        for key in self.books.keys():
            print(key) # this will print the object though? May need to add a __repr__ to Book

    def print_users(self):
        """ 
        method which iterates through all of the values in self.users (which are User objects) and prints them
        """
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        """
        Method which iterates through all books in self.books,
        and return the book that has been read the most.
        self.books (keys = Books, values = number of times read)
        """
        most_read = 0
        most_read_book = ''
        for book, reads in self.books.items():
            if reads > most_read:
                most_read = reads
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        """
        Method which iterates through all of the books in self.books,
        and returns the book that has the highest average rating
        The keys in self.books are Book objects, meaning we utilize
        the Book method .get_average_rating().
        """
        average_rating = 0
        best_rated_book = ''
        for book in self.books.keys():
            if book.get_average_rating() > average_rating:
                average_rating = book.get_average_rating()
                best_rated_book = book
        return best_rated_book

    def most_positive_user(self):
        """
        Method which iterates through all of the users in self.users,
        and returns the user with the highest average rating.
        The values in self.users are User objects, meaning we utilize
        the User method .get_average_rating().
        """
        average_rating = 0
        highest_rating_user = ''
        for user in self.users.values():
            if user.get_average_rating() > average_rating:
                average_rating = user.get_average_rating()
                highest_rating_user = user
        return highest_rating_user

"""
================================================================================
Section: Create Some Analysis Methods
See above - methods are going in to the TomeRater class
================================================================================
"""

"""
================================================================================
Section: Get Creative!
See above - added methods to:
> Check if someone add an existing user to TomeRater and print out a message telling them that this user already exists
> Make sure that books all have unique ISBNs
> Make sure that an email address is valid by checking if it has an @ character and either .com , .edu , .org
================================================================================
"""
