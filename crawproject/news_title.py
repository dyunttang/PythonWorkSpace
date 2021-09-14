import requests  # 통신하기 위해 제일 먼제 해야할 것!

# Crawling 하기 위해 해야할 것: 1.주소분석, 2.알고리즘(for문 돌면서 다운받는 것), 3.text/html 이기 때문에 parsing 하는 게 힘듦

# https://newsstand.naver.com/?list=&pcode=001 주소를 보니 url 이 아니라 uri 이다.
# 주소를 보니 source 를 request 하는 것이 아니라 identifier 이다
# 신문사 이름을 crawling
# 목적 : oid 수집
start_oid = 1
#oid_list = []
oid_names = []

for num in range(0, 2):
    start_oid_str = str(start_oid).zfill(3)
    uri = f"https://newsstand.naver.com/?list=&pcode={start_oid_str}"

    # requsets 해서 uri 를 받아준다
    response = requests.get(uri)

    # http status message
    # print(response.status_code)

    if(response.status_code == 200):
        # pcode 를 담아야 하는데, 이것을 담으려면 variable 로 만들어야 한다 -> start_oid = "001"
        # oid_list.append(start_oid_str)
        print(response.text)

    start_oid = start_oid + 1

    # print(f"oid 총 개수 : {len(oid_list)}")
    # print(oid_list)

# 001, 002, 003 ... 이것은 숫자가 아니라 문자인데 어떻게 하면 +1씩 증가할 수 있을까? oid_test.py 만들어서 test
