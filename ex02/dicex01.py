# Dictionary  사전 Data

# { "key" : value }     Python Dictionary
# {  key  : value }     JavaScript Object
# { "key" : value }     JSON

dic1 = {"username": "ssar", "password": "1234", "age": 19}

print(dic1)
print(type(dic1))

print(dic1["password"])

print("="*50)

users = [
    {"username": "ssar", "password": "1234", "age": 19},
    {"username": "cos", "password": "1234", "age": 30}
]

print(users[1]["age"])

for user in users:
    print(user["username"])

# 나중에 DB 에서 SELECT 를 하면  위의 [ ] 안에 있는 형식으로 Data 를 준다. dictionary 로만 준다.
# 그런데 SELECT 를 하면 기본적으로 Dictionary type 으로 주는 것이 아니라 Tuple 으로 준다. 변경을 방지하기 위함
# Tuple type 으로 줄 때는 아래의 ( ) 안에 있는 형식으로 Data 를 준다. DBS SELECT 하면 Tuple type 으로 data 를 준다.


# This is Tuple type
users = (
    {"username": "ssar", "password": "1234", "age": 19},
    {"username": "cos", "password": "1234", "age": 30}
)


# Java 에서는 ResultSet 을 준다.
