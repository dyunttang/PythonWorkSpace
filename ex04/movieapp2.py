# 20개의 영화 데이터의 제목, 평점, 러닝시간, 미디엄-커버-이미지
# for 문 돌려서 Console 에 출력
# 구분 (==========================================================================)

# 제목: 쇼생크 탈출
# 평점: 9.5
# 러닝시간: 77분
# 사진: "https://yts.mx/assets/images/movies/doctor_who_the_day_of_the_doctor_2013/medium-cover.jpg"
# 구분 (==========================================================================)


import requests

url = '''
https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
'''

response = requests.get(url)
responseDict = response.json()

movies = responseDict["data"]["movies"]

for movie in movies:

    print("제목:" + movie["title"])
    print("평점:" + str(movie["rating"]) + "점")
    print("러닝시간:" + str(movie["runtime"]) + "분")
    print("사진:" + movie["medium_cover_image"])
    print("="*50)
