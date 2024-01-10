## 문자열 자료형 ##
# 이스케이프 코드 /n
multiline = "Life is too short\nYou need python"
print(multiline)

# 연속된 따옴표 3개
multiline2='''
Life is too short
You need python
'''
print(multiline2)

# 이스케이프 코드
'''
\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	\를 그대로 표현할 때 사용
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용
\r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b	백 스페이스
\000	널 문자
활용 빈도가 높은 것은 \n, \t, \\, \', \"
'''

# 문자열에서 단어 슬라이싱
a = "Life is too short, You need Python"
print(a[0:4])
print(a[:])
'Life'

# 문자열 바꾸기
a2 = "Pithon"
print(a2[:1])
print(a2[2:])
print(a2[:1] + 'y' + a2[2:])

# 문자열 포매팅
# 숫자 바로 대입
'''
: %d => 문자열 포맷 코드
"I eat %d apples." %3
'I eat 3 apples.'
'''
b = "I eat %d apples." %3
print(b)
# 문자 바로 대입
c = "I eat %s apples." %"three"
print(c)
# 변수대입
d = 4
c2 = "I eat %d apples." % d
print(c2)

number = 10
day = "three"
e = "I ate %d apples. so I was sick for %s days." % (number, day)
print(e)

# 문자열 포맷 코드
'''
%s	문자열(String) => 어떤 형태의 값이든 변환해 대입 가능
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체) => %와 %d를 같이 쓸 때 
'''

# %와 %d를 같이 쓸 때 %% => 규칙
'''
"Error is %d%." % 98 => error
ㄴ"Error is %d%%." % 98
'Error is 98%.'
'''

# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백
f = "%10s" % "hi"
print(f)
g = "%-10sjane." % 'hi'
print(g)

# 소수점 표현
h = "%0.4f" % 3.42134234
print(h)

# 포맷 함수를 사용한 포매팅
# 숫자 바로 대입하기
i = "I eat {0} apples".format(3)
print(i)
# 문자열 바로 대입하기
i2 = "I eat {0} apples".format("five")
print(i2)
# 숫자 값을 가진 변수로 대입하기
i3 = "I eat {0} apples".format(number)
print(i3)
# 2개 이상의 값 넣기
number2 = 5
day = "three"
i4 = "I ate {0} apples. so I was sick for {1} days.".format(number2, day)
print(i4)
# 이름으로 넣기 
i5 = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(i5)
# 인덱스와 이름 혼용해서 넣기
i6 = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(i6)
# 왼쪽 정렬
i7 = "{0:<10}".format('hi')
print(i7+"*")
# 오른쪽 정렬
i8 = "{0:>10}".format('hi')
print(i8)
# 가운데 정렬
i9 = "{0:^10}".format('hi')
print(i9)
# 공백 채우기
i10 = "{0:=^10}".format('hi')
print(i10)
# 소수점 표현하기
y = 3.42134234
print("{0:=^10.4f}".format(y))
# { 또는 } 문자 표현하기
i11 = "{{and}}".format()
print(i11)
# f 문자열 포매팅 : 3.6버전부터 사용 가능
name = "홍길동"
age = 20
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# 딕셔너리(key, value를 한쌍으로 가지는 자료형) f 문자열 포매팅
i12 = {"name":'홍길동', "age":30}
print(f'나의 이름은 {i12["name"]:=<10}입니다. 나이는 {i12["age"]}입니다.')

# 문자열 관련 함수들

# 문자 개수 세기 count
hobby = "hobby"
print(hobby.count('b'))
# 위치 알려 주기 1 - find
str = "Python is the best choice"
print(str.find('i')) #처음으로 검색된 문자열의 인덱스를 봔환, 찾는 문자나 문자열이 존재하지 않는다면 -1 반환
# 위치 알려 주기 2 - index
print(str.index('t')) #처음으로 검색된 문자열의 인덱스를 봔환, 찾는 문자나 문자열이 존재하지 않는다면 오류 발생
# 문자열 삽입 join (리스트, 튜플에서도 사용 가능)
strA = "abcd"
print(",".join(strA))
# 리스트에서 join 사용
listA = ",".join(['a','b','c','d'])
print(listA)

# 소문자를 대문자로 바꾸기 - upper
# 대문자를 소문자로 바꾸기 - lower
text1 = 'hi'
text2 = "HI"
print(text1.upper())
print(text2.lower())

# 공백 지우기
texta = "  text  "
print(texta.lstrip())
print(texta.rstrip())
print(texta.strip())

# 문자열 바꾸기 replace
textb = "life is too short"
print(textb.replace("life","your leg"))

# 문자열 나누기 split
print(textb.split())
print(textb.split("o"))
# 괄호안에 아무것도 입력하지 않으면 space, enter, tab을 기준으로 나눠줌
# 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 줌