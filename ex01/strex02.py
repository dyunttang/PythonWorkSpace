test = "가나-다-라"

print(test[0:2])

print(test.find("-"))
print(test.find("-", 3))
print(test.rfind("-"))

# Q1) 끝 번호 4자리 찾기
phone1 = "050-222-3333"
phone2 = "02-7777-9999"

# MyAnswer
print(phone1[phone1.rfind("-")+1:])
print(phone2[phone2.rfind("-")+1:])


# Q2) 가운데 번호 찾아내기

# MyAnswer
print(phone1[phone1.find("-")+1:phone1.rfind("-")])
print(phone2[phone2.find("-")+1:phone2.rfind("-")])


# Teacher's Answer
si1 = phone1.rfind("-")+1
si2 = phone2.rfind("-")+1

print(phone1[si1:])  # : 는 slice operator
print(phone2[si2:])

fi1 = phone1.find("-")+1
li1 = phone1.rfind("-")
x
fi2 = phone2.find("-")+1
li2 = phone2.rfind("-")

print(phone1[fi1:li1])
print(phone2[fi2:li2])
