
class User:
    # f_name = "", l_name = "", email = ""
    def __init__(self, first, last, email):
        self.fname = first
        self.lname = last
        self.email = email
        print(f"my name is {self.fname} {self.lname} and my email is {self.email}")

    # print(f"my name is {f_name} {l_name} and my email is {email}")


akash = User()
akash_1 = User()
# akash.user_details("akash deep", "singh", "akasky9835@gmail.com")

akash.fname = "akash"
# anurag = User()
#
# print(akash.f_name)
# print(anurag.f_name)
#
# print(akash.l_name)
print(id(akash))
print(id(akash_1))