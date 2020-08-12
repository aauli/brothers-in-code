import datetime
import mysql.connector as connector


class Note:

    def __init__(self, title, desc, date_exp):
        self.title = title
        self.desc = desc
        self.date_exp = date_exp

    def print_note(self):
        print("Name: {}".format(self.title))
        print("Description: {}".format(self.desc))
        print("Deadline: {}".format(self.date_exp.strftime("%x")))

    def change_title(self, new_title):
        self.title = new_title

    def change_desc(self, new_desc):
        self.desc = new_desc

    def chage_date(self, new_date):
        self.date_exp = new_date

#Creates a new note in the DB
def addNote(cursor):
    print("Let's create a new note!\n")
    print("Write a title for the note\n")
    title = input()
    print("Write a description\n")
    desc = input()
    print("When should it be finished?\n")
    day = int(input("Day-->"))
    month = int(input("Mont-->"))
    year = int(input("Year-->"))
    date_exp = datetime.datetime(year, month, day)
    note = Note(title, desc, date_exp)
    sql = "INSERT INTO notes (title, description, date_exp) VALUES (%s, %s, %s)"
    vals = (title, desc, str(year)+"-"+str(month)+"-"+str(day))
    cursor.execute(sql, vals)
    print("The note has been created succesfully!\n")
    note.print_note()

#Removes a DB from the DB
def remFromDB(cursor, id):
    sql = "DELETE FROM notes WHERE id = %s"

    cursor.execute(sql, (id,))

# Retrieves all notes in DB
def retAllNoteDB(cursor):
    cursor.execute("SELECT * FROM notes")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


# Retrieves n notes in DB
def retNNOteDB(cursor, n_notes):
    cursor.execute("SELECT * FROM notes")
    myresult = cursor.fetchmany(size=n_notes)

    for x in myresult:
        print(x)
#Retrieves an specific note from DB
def retXnoteDB(cursor, title_note):
    query = """ select * from notes where title = %s"""
    cursor.execute(query, (title_note,))
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

# TODO -> CREATE MAIN METHOD
def main():
    # Create connection to database

    mydb = connector.connect(
        host="localhost",
        user="ulysses",
        password="aaron1997",
        database="python_db"
    )

    # This make us able to execute MySQL statements
    mycursor = mydb.cursor()
    # Pseudo switch-case for choosing action
    print("What do you want to do?")
    option = input()
    if option == "Add":
        addNote(mycursor)
        mydb.commit()
    elif option == "Delete":
        print("Which note do you want to delete?")
        id = input()
        remFromDB(mycursor, id)
        mydb.commit()
    elif option == "Mod":
        print("Sorry that has not been implemented yet!")
    elif option == "View":
        n_option = input("How many notes do you want to see?")
        if n_option == 'All':
            retAllNoteDB(mycursor)
        elif int(n_option) > 0:
            retNNOteDB(mycursor, int(n_option))
    elif option == "Quit":
        print("See you soon!")


if __name__ == "__main__":
    main()
