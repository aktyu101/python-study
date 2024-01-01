lang = 'python'
print(lang[0])#p
print(lang[-1])#n
print(lang[1:5])#1부터 5직전까지 ytho
print(lang[1:])#1부터 끝까지 ython
print(lang[:4])#맨처음부터 4직전까지 pyth

#문자열 처리
snack = '과자'
two = '두개'
juseyo = snack + two
#juseyo = juseyo += '주세요'
juseyo += '주세요'
print(juseyo)

num = 10
num1 = num + 2 
num += 5
print(num)
print(num1)

test = '''
여러줄의문장
작성 할 때
'''
print(len(test))