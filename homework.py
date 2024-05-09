# def get_first_value(lst):
#     return lst[0]
# print(get_first_value([1,2,3]))
# print(get_first_value([80, 5, 100]))
# print(get_first_value([-500, 0, 50]))
#
#
#

#
# def concat(lst1,lst2):
#     concatt = lst1 + lst2
#     return concatt
# print(concat([1, 3, 5], [2, 6, 8]))
# print(concat([7, 8], [10, 9, 1, 1, 2]))
# print(concat([4, 5, 1], [3, 3, 3, 3]))



#
# def get_last_item(lst4):
#     return lst4[-1]
# print(get_last_item([1, 2, 3]))
# print(get_last_item(['cat', 'dog', 'duck']))
# print(get_last_item([True, False, True]))
# print(get_last_item([7, 'Stringg', False]))
#
#
#
# def first(lis):
#     return lis[0]
# ruseult = first([1,1,1,1])
# print(ruseult)


# def test(teww):
#     return teww[0]
# print(test([1,2,3,45,6]))
#

# def test1(tes):
#     return [tes]
# print(test(12))




# def test2(hhh):
#     return hhh[-1]
# print(test([1,3,334,5,6]))


#1 sposob
# def test(lst, num):
#     return num in lst
# print(test([1,2,3,4,5,6,7], 2))
# print(test([12,2,3,2,4,4,1], 33))
#2 sposob
# while True:
#     son = int(input('son: '))
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
#     def test(list):
#         if son in list:
#             return True
#         else:
#             return False
#
#
#     print(test(list))

# def test2(lst2):
#     sonlar = 0
#     for numbers in lst2:
#         sonlar += numbers
#         if sonlar >= 100:
#             return False
#     return True
# print(test2([50, 49]))
# print(test2([50, 51]))
# print(test2([50, 50]))


def number_split(num):
    nums = num // 2
    if num % 2 != 0:
        return [nums, nums + 1]
    else:
        return [nums, nums]

print(number_split(1260))


def numbers(lst):
    a = sum(lst)
    if a > 1:
        return f'{a} ohms'
    elif a == 1:
        return f'{a} ohm'

print(numbers([1,4,5,6,4]))
print(numbers([0.5, 0.5]))



def nums(lst,s):
    if s == "Asc":
        return sorted(lst)
    elif s == "Des":
        return sorted(lst,reverse=True)
    elif s == "None":
        return lst


print(nums([4,3,2,1], "Asc"))
print(nums([7,8,11,66],"Des"))
print(nums([1,2,3,4],"None"))
        
