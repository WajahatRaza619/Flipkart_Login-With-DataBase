import mysql.connector

class DBhelper:

    def __init__(self):
        try:
           self.conn = mysql.connector.connect(host = "localhost",user="root",password="",database="Flipkart_db")
           self.mycursor=self.conn.cursor()
        except:
           print("Connection Failed")
        else:
           print("Connection Successful")

    def register(self,name,email,password):
        try:
           self.mycursor.execute("""INSERT INTO `users` (`user_id`, `email`, `name`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(email,name,password))
           self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

        data = self.mycursor.fetchall()
        return data