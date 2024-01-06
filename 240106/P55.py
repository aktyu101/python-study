# Tuple : 소괄호로 데이터를 묶음, 데이터를 변경할 수 없음
a_tuple = (1,2,3,4,5)
'''
a_tuple[0] = 5
-> throw arror
'''

#Dictionary : key value 형태로 구성, 중괄호로 데이터를 묶음
'''
{key1:value,key2:value,key3:value}
'''
a_dic = {'a':1, 'b':[1,2,3], 'c':3}
print(a_dic)
print(a_dic['a'])
print(a_dic['b'])
a_dic['4'] = 2
print(a_dic)

#Set : 집합, 자료형 -> 중복이 없는 자료형 
a_set = set([1,2,3,4])
print(a_set)
b_set = set([1,1,2])
print(b_set)
c_set = set(["p","y","t","h","o","n"])
print(c_set) #set은 순서가 없음, 데이터를 순서대로 정렬해야 하는 경우 사용x



