
class User:

    # Constructor 의 self 는 Object Create 시 Automatically Injected 된다.
    # __init__  This Function is Constructor  이 함수가 생성자
    def __init__(self, username, password="1234"):
        self.username = username
        self.password = password

    def hello(self):  # Function 만들 때 Default 로 (self) 를 적어준다
        print("Hello")


u = User("ssar", "1234")
u1 = User("cos")

print(u.username)

u.hello()

print(u.username)

# Constructor 가 있어야 가능! (class 를 dictionary 로 convert 해줌)
print(u.__dict__)
