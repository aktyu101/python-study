## 집합 자료형 ##
s1 = set([1,2,3])
print(s1)
s2 = set("hello")
print(s2)

# 비어 있는 집합 자료형
s = set()
print(s)
# 중복을 허용하지 않음
# 순서가 없음(unordered) => 데이터의 중복을 제거하기 위한 필터로 사용
# 인덱싱을 통해 요솟값을 얻을 수 없음 > 딕셔너리 특징과 유사함
# set에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환 해야 함
l1 = list(s1)
t1 = tuple(s1)
print(l1) # [1, 2, 3]
print(l1[0]) # 1
print(t1) # (1, 2, 3)
print(t1[0]) # 1

# 교집합, 합집합, 차집합 구하기
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

# 교집합 &
print(s3 & s4)
# 교집합 intersection
print(s3.intersection(s4))

# 합집합 +
print(s3 | s4)
# 합집합 union
print(s3.union(s4))
# 차집합 -
print(s3 - s4)
print(s3.difference(s4))

# 집합 자료형 관련 함수
# 값 1개 추가하기 - add
s3.add(11)
print(s3)

# 값 여러개 추가하기 - update
s3.update([12,13])
print(s3)

# 특정 값 지우기 - remove
s3.remove(11)
print(s3)

a = [1, 2, 3, 4]
while a:
    print(a.pop())


