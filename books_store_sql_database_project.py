
import mysql.connector

# class about Author: 
class Author:

    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??'
    )
    # creating the cursor object:
    my_cursor = myDb.cursor() 

    # function to create the author table :
    def create (self) :

        super().create() 
        
        try:             
            my_cursor = self.my_cursor 
            # using the database : 
            query_2 = ('''use books_store ''') 
            # creating :
            query_3 = ('''create table if not exists author_info (
                            a_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL UNIQUE 
                            )''') 
            
    
            my_cursor.execute(query_2) 
            my_cursor.execute(query_3) 
            
        except Exception as e :
            print(e)

    # function for adding the new records of authors :
    def add(self) :

        try:
            my_cursor = self.my_cursor

            # using the database:
            my_cursor.execute("use books_store;")

            # loop for continuing :
            while True :
                
                print("To save record just type 'enter' ")
                a_name = input("Enter the author name :  ")
                
                # conditions for breaking the loop :
                if a_name.lower() == 'enter' :
                    break
                else:
                    pass
                
                # inserting is here :
                query_4 = (f'''insert into author_info (name)
                                values 
                                ("{a_name}")''')
 
                my_cursor.execute(query_4)   
                self.myDb.commit() 

        except Exception as e:
            print(e)
 
    # function for reading the all the records :
    def read (self) :

        u_input = input("Are you sure to check all records. \n--> Type 'yes'/'no'    : ")

        if u_input.lower() == 'yes' :

            try:
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute("select * from author_info ") 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)     
        
        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass
    
    # function  for searching the record about Publisher :
    def filter (self) : 
        # confirmation :
        u_input = input("Are you sure to check author's records. \n--> Type 'yes'/'no'    : ")

        # conditions:
        if u_input.lower() == 'yes' :

            try:
                a_name = input("> Please enter the name of author of which you want to check the record : ")
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute(f'''select * from author_info where  name like "%{a_name}%"''') 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass
    
    # function about the updation of author table :
    def update (self) : 
        # confirmation :
        u_input = input("Are you sure to update author's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                a_name = input('''> ok, Now enter the name of author of which you want to update : ''') 
                u_name = input('''> ok, Now enter the updated name of author : ''') 

                my_cursor.execute("use books_store; ")
                my_cursor.execute(f'''update author_info set name = "{u_name}" where name = "{a_name}" ''') 

                # saving the changes :
                self.myDb.commit() 

            except Exception as e :
                print(e) 
            
            else:
                print("_____Process successful_____")

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

            
    # function to delete any record from author table :
    def delete (self) :
        # confirmation :
        u_input = input("Are you sure to delete author's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                a_name = input('''> ok, Now enter the name of author of which you want to update : ''')  

                my_cursor.execute("use books_store; ")
                my_cursor.execute(f'''delete from author_info where name = "{a_name}" ''') 

                # saving the changes :
                self.myDb.commit() 

            except Exception as e :
                print(e) 
            else:
                print("_____Process successful_____")

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

# class about Publisher:        
class Publisher: 
    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??'
    )
    # creating the cursor object:
    my_cursor = myDb.cursor() 

    # function to create the publisher's table :
    def create (self) :
        
        super().create()  

        try:             
            my_cursor = self.my_cursor 
            # using the database :
            query_2 = ('''use books_store ''') 
            # creating :
            query_3 = ('''create table if not exists publisher_info (
                            p_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL UNIQUE 
                            )''') 
            
    
            my_cursor.execute(query_2) 
            my_cursor.execute(query_3) 
            
        except Exception as e :
            print(e)
        
    
    # function for adding the new records of publishers :
    def add(self) :

        try:
            my_cursor = self.my_cursor

            # using the database :
            my_cursor.execute("use books_store;")
            # loop for continuing :
            while True :
                
                print("To save record just type 'enter' ")
                a_name = input("Enter the publisher name :  ")
                
                # conditions for breaking the loop :
                if a_name.lower() == 'enter' :
                    break
                else:
                    pass
                
                # inserting is here :
                query_4 = (f'''insert into publisher_info (name)
                                values 
                                ("{a_name}")''')
 
                my_cursor.execute(query_4)   
                self.myDb.commit() 

        except Exception as e:
            print(e)
        
    # function for reading the all the records :
    def read (self) :

        u_input = input("Are you sure to check all records. \n--> Type 'yes'/'no'    : ")

        if u_input.lower() == 'yes' :

            try:
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute("select * from publisher_info ") 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)     
        
        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

    # function for searching the record about the publisher using where clause :
    def filter (self) : 
        # confirmation :
        u_input = input("Are you sure to check publisher's records. \n--> Type 'yes'/'no'    : ")

        # conditions:
        if u_input.lower() == 'yes' :

            try:
                a_name = input("> Please enter the name of publisher of which you want to check the record : ")
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute(f'''select * from publisher_info where  name like "%{a_name}%"''') 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass
        
    
    # function about the updation of author table :
    def update (self) : 
        # confirmation :
        u_input = input("Are you sure to update publisher's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                a_name = input('''> ok, Now enter the name of publisher of which you want to update : ''') 
                u_name = input('''> ok, Now enter the updated name of publisher : ''') 

                my_cursor.execute("use books_store; ")
                my_cursor.execute(f'''update publisher_info set name = "{u_name}" where name = "{a_name}" ''') 

                # saving the changes :
                self.myDb.commit() 

            except Exception as e :
                print(e) 

            else:
                print("_____Process successful_____")

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass
        
    
    # function to delete any record from author table :
    def delete (self) :
        # confirmation :
        u_input = input("Are you sure to delete publisher's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                a_name = input('''> ok, Now enter the name of publisher of which you want to delete : ''')  

                my_cursor.execute("use books_store; ")
                my_cursor.execute(f'''delete from publisher_info where name = "{a_name}" ''') 

                # saving the changes :
                self.myDb.commit() 

            except Exception as e :
                print(e)

            else:
                print("_____Process successful_____") 

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

# class for making a relationship between the author and Publisher:
class AuthorPublisherRelatiion : 
    
    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??'
    )
    # creating the cursor object:
    my_cursor = myDb.cursor() 

    # function to create the author table :
    def create (self) :
        
        try:             
            my_cursor = self.my_cursor 
            # using the database : 
            query_7 = ('''use books_store; ''') 
            my_cursor.execute(query_7)
            # creating :
            query_8 = ('''create table if not exists join_ap (
                            aut_id INT NOT NULL,
                            pub_id INT NOT NULL         
                        ); ''') 
            
     
            my_cursor.execute(query_8) 
            
        except Exception as e :
            print(e) 
    
    def add(self):
        
        my_cursor = self.my_cursor

        # using the database :
        my_cursor.execute("use books_store;")


        # getting all info from the user :
        while True:
            try:
                print("_____Just type 'enter' to save the record_____")
                print("_____For enter new records_|just press enter|_____")
                cont_loop = input()
                if cont_loop.lower() == 'enter':
                    break
                # table columns inputs :
                at_id = input("Enter the id of author : ")
                pb_id = input("Enter the id of publisher : ")
                                          
                # inserting the data in tables :
                query_4 = ('''INSERT INTO join_ap (
                                    aut_id,
                                    pub_id )
                                    VALUES (%s,%s)
                ''')
                query_5 = at_id, pb_id
                my_cursor.execute(query_4, query_5) 

                self.myDb.commit()
            
            except Exception as f :
                print(f) 
        

    # function for reading the all the records :
    def read (self) :

        u_input = input("Are you sure to check all records. \n--> Type 'yes'/'no'    : ")

        if u_input.lower() == 'yes' :

            try:
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute("select * from join_ap ") 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)     
        
        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

    # this function is for creating a relationship between author and publisher :
    def filter(self) :
        # confirmation :
        u_input = input("Are you sure to check the Author and publisher relationship . \n--> Type 'yes'/'no'    : ")

        # conditions:
        if u_input.lower() == 'yes' :

            try:
                my_cursor = self.my_cursor
                # using the database :
                my_cursor.execute("use books_store") 

                    # creating the relationship between the tables :

                user_Input = int(input('''Pres 1 to the check the relationship of publishers with authors :   
Press 2 to the check relationship of authors with publishers :  \n''')) 

                if user_Input == 1 :
                    name = input("Enter the name of author :  ") 

                    query_11 = (f'''select a.name, pb.name
                                from author_info a join join_ap j 
                                on aut_id = a.a_id 
                                join publisher_info pb
                                on pub_id = pb.p_id 
                                where a.name like "%{name}%"  ''')

                    my_cursor.execute(query_11) 

                    results = my_cursor.fetchall() 

                    for data in results:
                        print(data) 

                elif user_Input == 2 :
                    name = input("Enter the name of publisher : ")

                    query_12 = (f'''select pb.name, a.name
                                from author_info a join join_ap j 
                                on aut_id = a.a_id 
                                join publisher_info pb
                                on pub_id = pb.p_id 
                                where pb.name like "%{name}%"  ''')

                    my_cursor.execute(query_12) 

                    results = my_cursor.fetchall() 

                    for data in results:
                        print(data)

            except Exception as e :
                print(e)

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

# BaseClass :
class BaseClass(Publisher, Author, AuthorPublisherRelatiion):
    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??'
    )
    # creating the cursor object:
    my_cursor = myDb.cursor() 

    def create(self):

        try:

            my_cursor = self.my_cursor

            #query for creating database :
            query_4 = ("create database if not exists books_store") 

            # query for using the database :
            query_5 = ("create database if not exists books_store") 
    
            my_cursor.execute(query_4) 
            my_cursor.execute(query_5)

            # the under super method is for the execution for the table of author and publisher :
            super().create() 

            #query for creating books table :
            query_6 = ('''create table if not exists books_info(
                        id INT NOT NULL,
                        book_name VARCHAR(100) NOT NULL,
                        author_id INT NOT NULL,
                        publisher_id INT NOT NULL,
                        price VARCHAR(20) NOT NULL DEFAULT "0$",
                        published_at YEAR NOT NULL,
                        PRIMARY KEY (id),
                        FOREIGN KEY (author_id) REFERENCES author_info (a_id), 
                        FOREIGN KEY (publisher_id) REFERENCES publisher_info (p_id) 
                        ) ''')  


            my_cursor.execute(query_6) 

        except Exception as e :
            print(e) 
        
    # function for adding the new records of publishers :
    def add(self) :

            my_cursor = self.my_cursor 
        
            # getting all info from the user :
            while True:
                try:
                    print("_____Just type 'enter' to save the record_____")
                    print("_____For enter new records_|just press enter|_____")

                    cont_loop = input()
                    if cont_loop.lower() == 'enter':
                        break

                    # table columns inputs :
                    id = input("Enter the id of book : ")
                    bookName = input('Enter the name of book :  ')
                    
                
                    # printing the id's of authors
                    print("Here the authors names with their id's are follows:-")
                    my_cursor.execute("use books_store")
                    my_cursor.execute("select * from author_info")
                    res = my_cursor.fetchall() 
                    for row in res :
                        print(row)
                    
                    authorName = input(f'''Now enter the id of author : ''')
                    
                    # printing the id's of authors
                    print("Here the publishers names with their id's are follows:-")
                    my_cursor.execute("use books_store")
                    my_cursor.execute("select * from publisher_info") 
                    rs = my_cursor.fetchall() 
                    for row in rs :
                        print(row)
                    
                    publisherName = input("Enter the id of book's publisher : ") 
                    price = input("Enter the price of book with doller sign($) : ")
                    year = input("Enter the year of publish (like '1985') : ")
                                              
                    # inserting the data in tables :
                    query_4 = ('''INSERT INTO books_info(
                                        id,
                                        book_name,
                                        author_id,
                                        publisher_id,
                                        price,
                                        published_at)
                                        VALUES (%s,%s,%s,%s,%s,%s)
                    ''')

                    query_5 = id, bookName, authorName, publisherName, price, year

                    my_cursor.execute(query_4, query_5) 

                    self.myDb.commit()

                except Exception as f :
                    print(f) 


    # function for reading the all the records :
    def read (self) :

        u_input = input("Are you sure to check all records. \n--> Type 'yes'/'no'    : ")

        if u_input.lower() == 'yes' :

            try:
                my_cursor = self.my_cursor
                
                my_cursor.execute("use books_store") 
                my_cursor.execute("select * from books_info ") 
                
                result = my_cursor.fetchall() 

                # loop for displaying :
                for data in result:
                    print(data)
            except Exception as e :
                print(e)     
        
        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass

    def filter(self):
        try:

            u_input = input("Are you sure to check the books records of author and publisher records. \n--> Type 'yes'/'no'    : ")

            if u_input.lower() == 'yes' :
                
                my_cursor = self.my_cursor

                # using the database :
                my_cursor.execute("use books_store") 

                U_input = input('''PRESS '1' TO CHECK THE BOOKS RECORD OF AUTHOR'S : \nPRESS '2' TO CHECK THE BOOKS RECORD OF PUBLISHER'S : \n''') 

                if U_input == '1' :
                    r_name = input("Kindly enter the author name of which you want to check book's record :  \n")


                    query = (f'''select b.book_name, b.price, b.published_at, a.name, pb.name  
                                       from books_info b join author_info a 
                                       on b.author_id = a.a_id 
                                       join publisher_info pb 
                                       on b.publisher_id = pb.p_id 
                                       where a.name like "%{r_name}%" ; ''')  

                    my_cursor.execute(query) 
                    results = my_cursor.fetchall() 

                    # loop for printing the searched record :

                    for row in results :
                        print(row) 

                elif U_input == '2' :
                    p_name = input("Kindly enter the publisher name of which you want to check book's record :  ")

                    query = (f'''select b.book_name, b.price, b.published_at, a.name, pb.name  
                                       from books_info b join author_info a 
                                       on b.author_id = a.a_id 
                                       join publisher_info pb 
                                       on b.publisher_id = pb.p_id 
                                       where pb.name like "%{p_name}%" ; ''')  

                    my_cursor.execute(query) 
                    results = my_cursor.fetchall() 

                    # loop for printing the searched record :

                    for row in results :
                        print(row)  

            elif u_input == 'no':
                print("*****THANK YOU*****")

            else :
                pass
        
        except Exception as e  :
            print(e)


    # function about the updation of author table :
    def update (self) : 
        # confirmation :
        u_input = input("Are you sure to update publisher's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # using the database :
        my_cursor.execute("use books_store") 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                
                book_name = input('Hello! dear please enter the name of book of which you want to update : ') 

                att = input('''Now Type 
                                        '1' for update book's name :
                                        '2' for update author's name :
                                        '3' for update price of book : 
                                        '4' for update published date of book :
                                        '5' for update author id for book : 
                                        '6' for update publisher id for book:  ''')

                if att == '1' :
                    name = input('Enter the updated name : ') 

                    my_cursor.execute(f'''update books_info set book_name = "{name}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit() 

                elif att == '2' :
                    Name = input('Enter the updated name : ') 

                    my_cursor.execute(f'''update books_info set author_name = "{Name}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit()

                elif att == '3' :
                    price = input('Enter the updated price : ') 

                    my_cursor.execute(f'''update books_info set price = "{price}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit()

                elif att == '4' :
                    year = input(f'Enter the updated year of publishing {book_name}  like (1985) : ') 

                    my_cursor.execute(f'''update books_info set published_at = "{year}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit()

                elif att == '5' :
                    id = input(f'Enter the updated author id : ') 

                    my_cursor.execute(f'''update books_info set author_id = "{id}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit()

                elif att == '6' :
                    pId = input(f'Enter the updated publisher id : ') 

                    my_cursor.execute(f'''update books_info set publisher_id = "{pId}" 
                    where book_name = "{book_name}" ''') 

                    self.myDb.commit()

            except Exception as e:
                print(e)


        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass    


    # function to delete any record from author table :
    def delete (self) :
        # confirmation :
        u_input = input("Are you sure to delete book's records. \n--> Type 'yes'/'no'    : ")

        my_cursor = self.my_cursor 

        # conditions :
        if u_input.lower() == 'yes' :

            try:
                b_name = input('''> ok, Now enter the name of book of which you want to delete : ''')  

                my_cursor.execute("use books_store; ")
                my_cursor.execute(f'''delete from books_info where book_name = "{b_name}" ''') 

                # saving the changes :
                self.myDb.commit() 

            except Exception as e :
                print(e)

            else:
                print("_____Process successful_____") 

        elif u_input == 'no':
            print("*****THANK YOU*****")

        else :
            pass


# creating object for baseclass:
books_instance = BaseClass()

# calling the create function :
books_instance.create() 

# other object instansiations:
author_instance = Author() 
publisher_instance = Publisher() 
author_publisher_instance = AuthorPublisherRelatiion()  

try:

    # getting the name of user :
    name = input("Hello! Buddy \nI hope you will be alright \nPlease enter your name : \n")

    # printing the name of user also getting the input about what he\she want to do :
    while True :
        user_input = input(f'''Well {name}, 
                  Type 'a' for enter a new records : 
                  Type 'r' for read all records : 
                  Type 's' for search any record from saved records :   
                  Type 'u' for update any record :    
                  Type 'd' for update any record :    
                  Type 'exit' for exit this session : \n''')
        # conditions for continuety of program :
        if user_input.lower() == 'exit':
            u_in = input("Do you want to exit? \n yes / no ")
            if u_in.lower() == 'yes' :
                break 
            else :
                pass 

        elif user_input.lower() == 'a' :
            print("_oK_")
            U_input = input('''Now 
                  Press '1' to add a record of book's author :
                  Press '2' to add a record of book's publisher :
                  Press '3' to add a relationship between Author and Publisher :
                  Press '4' to add a record of books : 
                    ''') 

            # conditions for adding record :
            if U_input == '1' : 
                author_instance.add() 

            if U_input == '2' : 
                publisher_instance.add() 

            if U_input == '3' : 
                author_publisher_instance.add() 

            if U_input == '4' : 
                books_instance.add()  

        elif user_input.lower() == 'r' :
            print("_oK_")
            U_input = input('''Now 
                  Press '1' to read a record of book's author :
                  Press '2' to read a record of book's publisher :
                  Press '3' to read a relationship between Author and Publisher :
                  Press '4' to read a record of books : 
                    ''') 

            # conditions for adding record :
            if U_input == '1' : 
                author_instance.read() 

            if U_input == '2' : 
                publisher_instance.read() 

            if U_input == '3' : 
                author_publisher_instance.read() 

            if U_input == '4' : 
                books_instance.read()


        elif user_input.lower() == 's' :
            print("_oK_")
            U_input = input('''Now 
                  Press '1' to search any record of book's author :
                  Press '2' to search any record of book's publisher :
                  Press '3' to search any relationship between Author and Publisher :
                  Press '4' to search any record of books :  
                    ''') 

            # conditions for searching record :
            if U_input == '1' : 
                author_instance.filter() 

            if U_input == '2' : 
                publisher_instance.filter() 

            if U_input == '3' : 
                author_publisher_instance.filter() 

            if U_input == '4' : 
                books_instance.filter()

        elif user_input.lower() == 'u' :
            print("_oK_")
            U_input = input('''Now 
                  Press '1' to update any record of book's author : 
                  Press '2' to update any record of book's publisher :  
                  Press '3' to update any record of books :  
                    ''') 

            # conditions for updating record :
            if U_input == '1' : 
                author_instance.update() 

            if U_input == '2' : 
                publisher_instance.update() 

            if U_input == '3' : 
                books_instance.filter()

        elif user_input.lower() == 'd' :
            print("_oK_")
            U_input = input('''Now 
                  Press '1' to delete any record of book's author : 
                  Press '2' to delete any record of book's publisher :  
                  Press '3' to delete any record of books :  
                    ''') 

            # conditions for deleting record :
            if U_input == '1' : 
                author_instance.delete() 

            if U_input == '2' : 
                publisher_instance.delete() 

            if U_input == '3' : 
                books_instance.delete() 



except Exception as e :
    print(e) 

else:
    print("_____Process successful_____")