class User:
    def __init__(self, first_name, last_name, email, password):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.password = password
        # return 12

    def change_password(self, new_password):
        self.password = new_password

    def get_info(self):
        print(f"This user Name is {self.fname} {self.lname} and email is {self.email} ")

    def get_private_info(self):
        print(f"This user Name is {self.fname} {self.lname} and email is {self.email}  and password is {self.password}")


user1 = User("akash", "singh", "akasky@gmail.com", "12345")
print(id(user1))
user1.get_info()
user1.get_private_info()

user2 = User("avinash kumar", "singh", "avinash@gmail.com", "1234")
print(id(user2))
user2.get_info()
user2.get_private_info()

# change password of user1 and user2
user1.change_password("akadh123")
user1.get_info()
user1.get_private_info()