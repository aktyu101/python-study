#if조건문
'''
if조건문 뒤에 :(콜론)을 붙여준다
조건문을 만족하면 동작하는 코드는 조건문에 들여쓰기를 사용한다
'''
a = 1
b = 2
if a == b:
    print("값 일치")
else:
    print("갑 불일치")
# if a != b: 
#     print("값 불일치")

if a > b:
    print('a값이 더 큽니다')
elif a < b:
    print('b값이 더 큽니다')
else:
    print('두 개의 값은 같습니다')

#문자열 비교
a_str = 'hello python'
if a_str == 'hello python':
    print('문자열이 같습니다.')

if a_str == 'Hello python':
    print('문자열이 같습니다.')
else:
    print('문자열이 같지 않습니다.')

if 'hello' in a_str:
    print('"hello"가 포함되어 있습니다')
if 'dd' not in a_str:
    print('"dd"가 포함되어 있지 않습니다')

a_list = ['안녕',1,2,"파이썬"]
if '안녕' in a_list:
    print('a_list에 안녕이 포함되어 있습니다.')
if 2 in a_list:
    print('a_list에 2가 포함되어 있습니다.')

#반복문 while문
'''
while문 : 참과 거짓을 기준으로 조건이 거짓이 되기 전까지 무한 반복적으로 실행
for문 : 반복되는 부분이나 범위를 구체적으로 지정하여 실행
'''

#for문
for i in range(7): #0부터 7-1 까지 반복
    print(i)
for ii in range(5, 10): #5부터 10-1까지 출력
    print("ii:",ii)
for ii in range(10, 5, -1): #10부터 역순으로 5+1까지 출력
    print(ii)

#list에서 for문을 활용하여 값 가져오는 법
a_list2 = ['안녕','하세요',1,2,3,4,5]
for j in a_list2:
    print(j)

a_str2 = 'hello python'
for jj in a_str2:
    print(jj)

#enumerate: 리스트에서 위치값 가져올 때 사용
name_list = ['지수','철수','영희']
age_list = [500,5,12]
for ij,kj in enumerate(name_list):
    print(ij,end='') 
    '''end=''빈 값이 들어갔기 때문에 종료문자를 넣지 않겠다는 뜻
    end=''을 넣어주지 않으면 기본적으로 종료문자는 줄바꿈이 들어감'''
    print(kj,end='')
    #ij는 리스트의 위치, kj는 값

#하나의 for문을 이용해 데이터 출력
for ij,kj in enumerate(name_list):
    print(kj,end='')
    print(age_list[ij])



