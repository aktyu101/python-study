#method =클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음

#문자열 메소드 : python 내장형
'''
count
str.count(x)
str.count(x, start)
str.count(x, start, end)
'''
count_test = 'apple'
print(count_test.count('p'))
print(count_test.count('p', 3))
'''
find, rfind : find는 검색된 문자가 여러개일 경우 첫번째 인덱스를, rfind는 마지막 인덱스를 반환
str.find(x)
str.find(x, start)
str.find(x, start, end)
'''
home = '집보내줘 집보내줘 집 보내줘'
print(home.find('집'))
print(home.find('집', 3))
print(home.find('집', 3, 12))
print(home.find('', 3, 12))

'''
upper, lower, swapcase
str.upper() : 모든 문자를 대문자로 반환
str.lower() : 모든 문자를 소문자로 반환
str.swapcase() : 대문자는 소문자로, 소문자는 대문자로 반환
'''

'''
capitalize, title
str.capitalize() : 맨 처음 문자만 대문자로 변경 나머지 문자열은 소문자로 반환
str.title() : 각 단어의 첫 문자만 대문자로 변경
'''

'''
stript, lstrip, rstrip, strip
str.stript() : 앞뒤로 불필요한 문자 제거, 괄호에 아무것도 안넣으면 공백 제거
str.lstrip() : 문자열의 왼쪽 공백 제거
str.rstrip() : 문자열의 오른쪽 공백 제거
str.strip() : 양쪽 공백 제거
'''

'''
replace
str.replace(old, new) : 문자 대체
str.replace(old, new, count) : 원하는 개수만큼 문자 대체
'''

'''
split
str.split() : 문자열을 리스트 형태로 반환
'''

'''
startwith, endswith
str.startswith() : 결과값을 불리언 형태로 반환
str.endswith() : 결과값을 불리언 형태로 반환
'''

'''
cneter
str.center(10, '-') : 다른 문자들 사이에 가운데로
'''
