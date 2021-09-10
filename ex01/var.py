# 1. Python is Interpreter Language
# 2. Python 은 모든 것이 Object이다
# 3. Python 은 Variable의 type 이 없다. Type 추론을 지원한다

a = 1
b = 1.2
c = "문자"
d = '문자'
e = True
f = False
g = '''
안녕하세요 반갑습니다.
하하하하하하
'''

print(type(a))  # 1 int
print(type(b))  # 1.2 float
print(type(c))  # str
print(type(d))  # str
print(e)        # bool
print(f)        # bool
print(g)        # str
print(a, b)     # str
