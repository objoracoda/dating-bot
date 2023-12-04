import sqlite3


class Database:
    
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?",(user_id,)).fetchall()
            return bool(len(result))


    def add_user(self,user_id,user_name,user_age,user_gender,user_photo,user_content,user_find_gender,user_city,signup):
        with self.connection:
            if self.user_exists(user_id):
                return self.cursor.execute("UPDATE `users` SET `name`=?, `age`=?,`content`=?,`photo`=?,`city`=? WHERE `user_id` = ?", (user_name,user_age,user_content, user_photo, user_city,user_id,))
            else:
                return self.cursor.execute("INSERT INTO `users` (`user_id`,`name`,`age`,`content`,`photo`,`city`,`signup`) VALUES (?,?,?,?,?,?,?)", (user_id,user_name,user_age,user_content, user_photo, user_city,signup,))

    
    def get_user_data(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return result[0]

    
    def get_users_recommend(self,user_age):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `age` < ?",(user_age,)).fetchall()
            print(result)
            return result
