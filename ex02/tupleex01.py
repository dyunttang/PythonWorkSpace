tuple1 = (1, 2, 3, 4)

print(tuple1)
print(tuple1[0])

# tuple 은 변경불가능한 Data 이다. 이런 Data Type 이 왜 필요할까? Java에서 final 은 왜 필요할까?
# 한 번 정해지면 변경불가능한 Data 를 왜 만들까?
# 이전 Data 가 없으면 변경된 것을 감지할 수 없기 때문이다. 기존 Data 를 건드리지 않으면 변경을 감지할 수 있다. Opserver
# tuple 은 list 와 똑같이 생겼지만 변경이 되지 않는다

print(type(tuple1))
