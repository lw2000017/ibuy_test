# -*- coding:utf-8 -*-          
# @Time     :2019/5/15 11:28    
# @Author   :LW                 
# @File     :test_1_水仙花.py         


def narcissistic_number_1(num):
    length = len(str(num))

    count = length

    num_sum = 0

    while count:

        num_sum += ((num // 10 ** (count - 1)) % 10) ** length

        count -= 1

    else:

        if num_sum == num:

            print("%d is %d bit narcissistic_number" % (num, length))
        else:
            print("%d is not a narcissistic_number" % num)


narcissistic_number_1(153)


str1 = '100'
if str1.endswith('00'):
    str1 = f'{str1[:-2]}.{str1[-2:]}'
    print(str1)
elif str1.endswith('0'):
    str1 = f'{str1[:-2]}.{str1[-2:-1]}'
    print(str1)
else:
    str1 = f'{str1[:-2]}.{str1[-2:]}'
    print(str1)



name = 'jackfrued'
fruits = ['apple', 'orange', 'grape']
owners = {'1001': '骆昊', '1002': '王大锤'}
if name and fruits and owners:
    print('I love fruits!')


fruits = ['orange', 'grape', 'pitaya', 'blueberry']
for index, fruit in enumerate(fruits):
    print(index, ':', fruit)