import mysql.connector
import sys
class DBhelper:
    
        def __init__(self):
            try:
                self.conn = mysql.connector.connect(host = "localhost",user = 'root',password = '',database = 'computerscience_class')
                self.mycursor = self.conn.cursor()
            except:
                print("Connection Failed,Error Occurred ")
                sys.exit(0)
            else:
                print("Connected to Database")

        def register(self,name,email,password):
            try:
                self.mycursor.execute(""" INSERT INTO `students` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')
    """.format(name,email,password))
                self.conn.commit()
            except:
                return -1
            else:
                return 1
        def search(self,email,password):
            self.mycursor.execute(""" select * from students where email like '{}' and password like '{}' """.format(email,password))
            data = self.mycursor.fetchall()
            print("Hello",data[0][1])
            if len(data)==0:
                print("Incorrect email/password")
            else:
                sys.exit(0)

                              

