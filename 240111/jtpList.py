## 리스트 자료형 ##
odd = [1, 3, 5, 7, 9]
# 리스트를 만들 때는 대괄호([])로로 감싸 주고 각 요솟값은 쉼표(,)로 구분
# 리스트명 = [요소1, 요소2, 요소3, ...]
# 리스트 안에는 숫자, 문자, 빈 리스트, 숫자와 문자, 리스트 자체를 요소값으로 가질 수 있음, 어떠한 자료형도 포함 가능
a = [] #a = list()와 같음 
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a) #[]

# 리스트의 인덱싱과 슬라이싱
a2 = [1, 2, 3]
print(a2[-1]) #3
print(a2[0] + a2[2]) #4

a3 = [1, 2, 3, ['a', 'b', 'c']]
print(a3[-1][0]) #a

a4 = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a4[2][-1][0]) #Life

# 리스트의 슬라이싱
a5 = [1, 2, 3, 4, 5]
print(a5[0:2]) #[1, 2]

# 중첩된 리스트에서 슬라이싱하기
a6 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a6[0:4]) # [1, 2, 3, ['a', 'b', 'c']]
print(a6[3][:2])
aList = [1, 2, 3]
bList = [4, 5, 6]
print(aList + bList) # 리스트 사이에서 +는 리스트를 합쳐줌
print(aList * 3) # *는 리스트 반복

# 리스트 길이 구하기
listLen = len(aList) # 튜플, 딕셔너리에서도 사용 가능
print(listLen)

# 숫자와 문자열은 더할 수 없음, 숫자에 문자를 더하고 싶을 경우 숫자를 문자로 바꿔줘야 함
a7 = [1, 2, 3]
print(str(a7[2]) + "hi")

# 리스트의 수정과 삭제 del
a7[2] = 4
del a7[1]
print(a7)
a8 = [1, 2, 3, 4, 5]
del a8[1:4]
print(a8)

# 리스트 요소 추가 append
a8.append(9) # 리스트는 어떤 자료형도 추가 가능
print(a8)

# 리스트 정렬 sort
a9 = [5, 2, 3, 4, 1]
b2 = ['ㄱ', 'ㅁ', 'ㄹ', 'ㄷ', 'ㄴ']
a9.sort()
print(a9)
b2.sort()
print(b2)

# 리스트 뒤집기 reverse
a10 = [1, 2, 3]
a10.reverse() # 값을 바꿈
print(a10)

# 인덱스 반환 index
print(a10.index(2))

# 리스트에 요소 삽입 insert
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
a10.insert(0,5)
print(a10)
a10.reverse()
print(a10)
# 리스트에 요소 삽입 insert

# 리스트 요소 제거 remove
# 리스트에서 첫번째로 나오는 x를 제거
a10.remove(2)
print(a10)

# 리스트 요소 끄집어 내기 pop
# 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제함
a10.pop()
print(a10)

# 리스트에 포함된 요소 x의 개수 세기 count
# 리스트안에 x가 몇개 있는지 조사하여 그 개수를 리턴
print(a10.count(1))

# 리스트 확장 extend
a11 = [1, 2, 3]
a11.extend([4, 5]) # a += [4, 5]
print(a11)
b = [6, 7, 1]
a11.extend(b)
print(a11)



