## for문 ##
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [40, 50, 90, 80, 20]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('---')
        print('%d학생은 합격' % number)
    else: 
        print('%d학생은 불합격' % number)

# for문과 continue문 (for문을 수행하는 도중 continue문을 만나면 for문의 처음으로 돌아감)
marks2 = [40, 50, 90, 80, 20]
number2 = 0
for mark in marks2:
    number2 += 1
    if mark < 60:
        continue
    print(':::%d학생은 %d점으로 합격입니다.' % (number, mark))

# for문과 함께 자주 사용하는 range(숫자 리스트를 자동으로 만들어 줌)함수
b = range(10)
print(b)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

marks3 = [90, 25, 67, 45, 80]
for number in range(len(marks2)):
    # len(mark) = 5
    # range(len(marks)) = range(5)
    if marks3[number] < 60:
        continue
    print('%d학생 축하합니다. 합격입니다' % (number+1))
    
    
