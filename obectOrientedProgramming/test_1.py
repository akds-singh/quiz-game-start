class Test:

    def __int__(self, x, a):
        self.name = x
        self.value = a
        print(self.name, self.value)

    def __getitem__(self, i):
        print("hello World")


i = "akash"
x = Test()
# x.__getitem__
print(x)
# x.__new__(i[1])
# print(x.__init__("as", "sljsdfla"))
y = Test()
# print(y("lafj", "sdfjls"))
