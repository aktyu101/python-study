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

# 정렬과 공백
f = "%10s" % "hi"
print(f)
g = "%-10sjane." % 'hi'
print(g)

# 소수점 표현
h = "%0.4f" % 3.42134234
print(h)