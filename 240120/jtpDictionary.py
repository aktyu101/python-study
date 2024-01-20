## 딕셔너리 자료형 (associative array, hash) ##
# key, value를 한쌍으로 가지는 자료형
# key를 통해 value를 얻음
dic = {'key1' : 'value1','key2': 'value2', 'key3' : 'value3' }
a = {1:[1, 2, 3]} # value에 리스트를 넣을 수 있음
print(a[1])

# 딕셔너리 쌍 추가하기
a[2] = 3
print(a)
a['name'] = 'ayeon' # {1: [1, 2, 3], 2: 3, 'name': 'ayeon'}
print(a)

# 딕셔너리 요소 삭제하기
del a['name']
print(a)

# key를 활용해 value얻기 => 리스트 튜플과 같이 인덱싱, 슬라이싱 기법으로 요솟값을 얻을 수 없음

# 딕셔너리 생성시 주의사항
# 1. 중복값을 무시함
a2 = { 1: 'a', 1: 'b' } # 첫번째 1 요솟값 무시
print(a2[1])
# 2. key로 리스트(값이 변할 수 있어서)를 넣을 수 없음, 튜플은 key로 쓸 수 있음
# => 변하는 값을 키로 쓸 수 없음

# 딕셔너리 관련 함수
# key 리스트 만들기 - keys
a3 = {'name': 'ayeon', 'birth': '0903', 'number': '5238'}
print("keys:", a3.keys())
# values
print("values:", a3.values())
# 3.0 이후 버전에서 리턴값으로 리스트가 필요한 경우
print("list 반환:", list(a3.keys()))
# dict_keys

# 리스트를 사용하는 것과는 별 차이가 앖지만
# 리스트 고유의 append, sort, insert, pop, remove 함수 수행 불가
for k in a3.keys():
    print(k)

# key, value 쌍 얻기 - items
print(a3.items())
# 리턴값으로 key, value 한 쌍의 리스트가 필요한 경우
print(list(a3.items()))

# key, value 쌍 모두 지우기 - clear
a4 = {'name': 'tt', 'birth': 980903}
a4.clear()
print(a4)
# 빈 리스트[] 빈 튜플() 빈 딕셔너리{}

# key로 value 얻기 - get
print(a3.get('name'))
# 존재하지 않는 값을 키로 가져올 경우 None을 리턴
# a3['nokey'] => 오류 발생시킴

# 찾으려는 키가 없을 경우 미리 정해둔 디폴트 값을 반환
# get(x, 디폴트 값)
print(a3.get('n', 'nokey'))

# 해당 키가 딕셔너리 안에 있는지 조사하기 - in
print('name' in a3)
print('nokey' in a3)




