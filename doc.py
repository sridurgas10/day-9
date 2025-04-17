

class Library:
    def __init__(self):
        self.books = []
        self.users = []

class Books(Library):
    def __init__(self):
        super().__init__()

    def addbook(self, *booklist):
        for book in booklist:
            self.books.append(book)
        return f"{booklist} added to the library."

    def rembook(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"'{book}' removed from the library."
        else:
            return "No book matches."

    def updbook(self, book):
        if book in self.books:
            index = self.books.index(book)
            newbook = input("Enter new book name: ")
            self.books[index] = newbook
            return f"Book '{book}' updated to '{newbook}'."
        else:
            return "No book matches."

    def searchbook(self, book):
        if book in self.books:
            return f"Book '{book}' is available in the library."
        else:
            return "No book matches."


booklist = Books()
print(booklist.addbook("krishna", "ramayana", "lord"))
print("Removed book:", booklist.rembook("lord"))
print("Updated book:", booklist.updbook("ramayana"))
print("Searched book:", booklist.searchbook("krishna"))


class Users(Library):
    def __init__(self):
        super().__init__()


    def adduser(self,*userlist):
        for user in userlist:
            self.users.append(user)
        return f"{userlist} user added in the library"
    def remuser(self,user):
        if user in self.users:
            self.users.remove(user)
            return f" {user} removed user successfully"
        else :
            return f"no matches found"
    def seauser(self,user):
        if user in self.users:
            return f" {user} is present in users"
        else:
            return f"no matches found"
    def upduser(self,user):
        if user in self.users:
            index=self.users.index(user)
            newuser=input("enter a new user")
            self.users[index]=newuser   
            return f" {user} updated successfullly"
        else:
            return f" no match found in this libarary"
userlist=Users()

print(userlist.adduser("sri","durga","lithiksha","naresh"))
print("remove user successfully: ",userlist.remuser("durga"))
print("search user successfully: ",userlist.seauser("sri"))
print("updated user successfully: ",userlist.upduser("lithiksha"))
