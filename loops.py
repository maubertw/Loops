

# a = 1

# while (a < 21):
#     if a == 13:
#         print "hello!",
#     else:
#         print a ,
#     a = a + 1

# fruits = ["apples", "oranges", "bananas"]
# index = 0
# while index<len(fruits):
#     print fruits[index]
#     index += 1
#   


def sum_nums(num):
    count = 0
    # print range(num)
    for n in range(0, num, 1):
        print n
        # print count
        count = count + n
    return count    

print sum_nums(10)
