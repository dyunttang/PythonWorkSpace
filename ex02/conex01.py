
isChecked = False

# if Condition(조건) :
if True:
    print("안녕")
else:
    print("굿바이")

num = 10

if num > 10:
    print("만점")
elif num > 5:
    print("평균")
else:
    print("미만")


# or, and
if True or False:
    print("트루입니다")

if True and False:
    print("트루입니다")


# Python 에서는 Stack 에 아무것도 안 적고 싶으면 pass 를 쓴다
if True:
    pass


# 조건부 표현식
score = 80
message = "success" if score > 60 else "fail"
print(message)
