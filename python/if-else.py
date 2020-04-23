#link of the problem here
# https://share.getcloudapp.com/YEu11kXn





# def if_else(n):
#     if n in range(2, 5):
#         print("Not Weird")
#     elif n in range(6, 20):
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")
#     else:
#         print("Weird")
#
#
# print(if_else(1))

n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
