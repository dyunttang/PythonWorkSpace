# Exception is occured always when runtime

try:
    print(2/0)
except Exception as e:
    print(e)
finally:
    print("끝")
