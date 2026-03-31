# 파일이름 :4주차 미션: 도장깨기 나만의 맛집 버킷리스트
# 작 성 자 : 60232179 강성재
#1. 맛집 빈 리스트 만들기
bucket_list = []

#2. 맛집 입력하고 리스트에 추가하기
restaurant = input(f'맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant = input(f'맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant = input(f'맛집 리스트 입력: ')
bucket_list.append(restaurant)


#3. 맛집 리스트 출력
print(f'리스트: {bucket_list}')
#4. 첫번째로 가려는 맛집을 입력받아 맛집 리스트에 추가
vip_restaurant = input(f'맛집 리스트 추가: ')
bucket_list.insert(0, vip_restaurant)
#5. 맛집 리스트 출력
print(f'리스트: {bucket_list}')
#6 도장깨기 후 맛집 리스트에서 제거
visited = input('도장 깨기: ')
bucket_list.remove(visited)
#7 맛집 리스트 출력
print(f'리스트: {bucket_list}')


