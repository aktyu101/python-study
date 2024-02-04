## if문 ##
money = True
if money:
    print('택시')
else :
    print('도보')

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# elif
pocket2 = ['cellphone', 'paper']
card = True
if money in pocket:
    print('택시2')
elif card: #이전 조건문이 거짓일 때 실행 됨, 개수에 제한 없음
    print('택시2')
else:
    print('걸어가')

# 수행할 문장이 한 줄일 경우
'''
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket: pass
... else: print("카드를 꺼내라")
'''

# 조건부 표현식
score = 50
if score >= 60:
    message = "success"
else:
    message = 'failure'
print(message)
# message = "success" if score >= 60 else "failure" (정규식)
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값



