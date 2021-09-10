list1 = [1, 2, 3, 4]

print(list1[-1])  # - 는 list 제일 끝에서부터 세느 것

list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)


# 방향이 있는 Data 를 Vector 라고 하며 Vector 는 1 Demension Array 이다

list4 = [list1] + [list2]

print(list4)


# 2 Demsion Array == Matrix  행렬이 있으면 Matrix

list2.append(9)
list2 = list2 + [9]
print(list2)


# 요소 제거
print("="*50)
arr = [5, 6, 7, 8]
arr.remove(8)
print(arr)  # [5,6,7]

del arr[0]
print(arr)  # [6,7]


# 끝에 추가
print("="*50)
arr2 = [5, 6, 7, 8]
arr2.append(9)
print(arr2)


# 원하는 위치에 추가
print("="*50)
arr3 = [5, 6, 7, 8]
arr3.insert(2, 500)
print(arr3)


# 정렬  sort
print("="*50)
arr4 = [8, 5, 1, 3]
arr4.sort()
print(arr4)
arr4.reverse()
print(arr4)

# for statement 반복문
print("="*50)
arr5 = [1, 3, 5, 7]

for i in arr5:
    print(i)

print("="*50)

for i in range(0, 6):  # range(x,y) 는 y의 바로 앞에 값까지
    print(i)   # for 문에서 : Enter 하면 space 4칸 꼭 지켜야됨. Python 의 문법임
    # : 엔터 이렇게만 하면 됨  : 이하는 모두 다 Stack 이다
