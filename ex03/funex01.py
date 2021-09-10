
# type 이 없으니까 Abstract 가 필요없다. 모든 type 을 다 받을 수 있는 것이다
# return type 도 필요없다. return 하고 싶으면 하고 싫으면 print만 해도 된다
def add(n1, n2):
    print(n1+n2)


def add(n1, n2):
    return n1+n2


print(add(1, 3))


# 선택적 매개변수  ex) n2=5  Default Value Setting 가능
def minus(n1, n2=5):
    return n1-n2

# Python 은 Overloading 가능할까?  안 된다. Python 은 Interpreter Language 로 앞에 함수를 읽고 지워버리기 때문이다.


# def minus(n1):
#     return n1


print(minus(10))
print(minus(10, 9))

# 1급 Object Function 안에 있는 것도 아니고, 꼭 어디 안에 포함되지 않아도 되는 객체들. Java 에서 1급 Object는 class 밖에 없다.
# 1급 객체는 가장 바깥에, 최상위에 존재할 수 있어야 한다. Python 에서는 모든 Object 가 1급객체이다
sum = 20


def vartest():
    global sum
    sum = sum + 1


vartest()

print(sum)

# 함수 오버로딩 없음
# 선택적 매개변수 (디폴트로 초기화 가능)
# 전역변수를 함수 내부에서 사용하려면 global
