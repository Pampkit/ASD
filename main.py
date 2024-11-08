# ----------------------------3.1 1----------------------------
# n = int(input())
#
# def rec(n):
#     if n > 1:
#         return n * rec(n-1)
#     else:
#         return 1
#
#
# print(rec(n))


# ----------------------------3.1 2----------------------------
# arr = input().split()
# n = int(arr[0])
# k = int(arr[1])
#
# def rec(n):
#     if n > 1:
#         return n * rec(n-1)
#     else:
#         return 1
#
#
# print(int(rec(n) / (rec(n-k) * rec(k))))


# ----------------------------3.1 3----------------------------
# arr = input().split()
# n = int(arr[0]) + int(arr[1]) - 1
# k = int(arr[1])
#
# def rec(n):
#     if n > 1:
#         return n * rec(n-1)
#     else:
#         return 1
#
#
# print(int(rec(n) / (rec(n-k) * rec(k))))


# ----------------------------3.5 1----------------------------
# n = int(input())
# arr = list(map(int, input().split()))
# out_arr = []
# for i in range(len(arr)):
#     min_item = min(arr)
#     out_arr.append(str(min_item))
#     arr.pop(arr.index(min_item))
# print(' '.join(out_arr))


# ----------------------------3.5 2----------------------------
# n = int(input())
# gen_arr = []
# out_arr = []
# for i in range(n):
#     count_items = int(input())
#     arr = list(map(int, input().split()))
#     gen_arr.append(arr)
#
# indexes = [0] * n
#
# while True:
#     inner_arr = []
#     for i in range(len(gen_arr)):
#         if indexes[i] < len(gen_arr[i]):
#             inner_arr.append((gen_arr[i][indexes[i]], i))
#     if not inner_arr:
#         break
#
#     min_item, min_index = min(inner_arr, key=lambda x: x[0])
#     out_arr.append(str(min_item))
#     indexes[min_index] += 1
# print(" ".join(out_arr))


# ----------------------------3.5 3----------------------------
# def merge(arr, left, mid, right):
#     left_arr = arr[left:mid]
#     right_arr = arr[mid:right]
#     i = j = 0
#     k = left
#
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] <= right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k] = right_arr[j]
#             j += 1
#         k += 1
#
#     while i < len(left_arr):
#         arr[k] = left_arr[i]
#         i += 1
#         k += 1
#
#     while j < len(right_arr):
#         arr[k] = right_arr[j]
#         j += 1
#         k += 1
#
# def merge_sort(arr, left, right):
#     if right - left > 1:
#         mid = (left + right) // 2
#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid, right)
#         merge(arr, left, mid, right)
#
# n = int(input())
# arr = list(map(int, input().split()))
# merge_sort(arr, 0, len(arr))
# print(" ".join(map(str, arr)))


# ----------------------------3.6 1----------------------------
# def sorted_lomuto(arr):
#     main_point = arr[0]
#     index = 0
#     for i in range(1, len(arr)):
#         if arr[i] <= main_point:
#             index+=1
#             if index != i:
#                 mid = arr[index]
#                 arr[index] = arr[i]
#                 arr[i] = mid
#     temp = arr[index]
#     arr[index] = arr[0]
#     arr[0] = temp
#     return " ".join(arr)
#
# n = int(input())
# print(sorted_lomuto(list(map(int, input().split()))))


# ----------------------------3.6 2----------------------------
# from random import randint, random
#
#
# def random_quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     random_item = arr[randint(0, len(arr)-1)]
#     print(random_item)
#     small_arr = list(filter(lambda x: (x < random_item) , arr))
#     equal_arr = list(filter(lambda x: (x == random_item), arr))
#     large_arr = list(filter(lambda x: (x > random_item), arr))
#     arr = random_quick_sort(small_arr) + equal_arr + random_quick_sort(large_arr)
#     return arr
#
# print(random_quick_sort([13, 17, 37, 73, 31, 19, 23]))


# ----------------------------5.1 1----------------------------
# table_fib = {}
# def fib(n):
#     if not n in table_fib.keys():
#         if n <= 1:
#             table_fib[n] = n
#         else:
#             table_fib[n] = fib(n - 2) + fib(n - 1)
#     return table_fib[n]
# print(fib(3))


# ----------------------------5.1 2----------------------------
# def fib_last_digit(n):
#     if n <= 1:
#         return n
#     f = [0, 1]
#     for i in range(2, n+1):
#         f.append((f[i-1] + f[i-2]) % 10)
#     return f[n]
#
# print(fib_last_digit(int(input())))

# def pisano_period(m):
#     cache = [0, 1]
#     current_n = 0
#     next_n = 1
#     period = 0
#     while True:
#         old_next = next_n
#         next_n = (current_n + next_n) % m
#         current_n = old_next
#         cache.append(next_n)
#         period = period + 1
#         if current_n == 0 and next_n == 1:
#             return cache, period
#
# def fib(n, m):
#     if n <= 1:
#         return n
#     table, p_pis = pisano_period(m)
#     return table[n % p_pis]
#
# n, m = map(int, input().split())
# print(fib(n, m))


# ----------------------------5.1 3----------------------------
# def pisano_period(m):
#     cache = [0, 1]
#     current_n = 0
#     next_n = 1
#     period = 0
#     while True:
#         old_next = next_n
#         next_n = (current_n + next_n) % m
#         current_n = old_next
#         cache.append(next_n)
#         period = period + 1
#         if current_n == 0 and next_n == 1:
#             return cache, period
#
# def fib(n, m):
#     if n <= 1:
#         return n
#     table, p_pis = pisano_period(m)
#     return table[n % p_pis]
#
# n, m = map(int, input().split())
# print(fib(n, m))


# ----------------------------5.1 4----------------------------
# def pisano_period(m):
#     cache = [0, 1]
#     current_n = 0
#     next_n = 1
#     period = 0
#     while True:
#         old_next = next_n
#         next_n = (current_n + next_n) % m
#         current_n = old_next
#         cache.append(next_n)
#         period = period + 1
#         if current_n == 0 and next_n == 1:
#             return cache, period
#
# def fib(n, m):
#     if n <= 1:
#         return n
#     table, p_pis = pisano_period(m)
#     res = table[n % p_pis]
#     return (res if res > 0 else 10) - 1
#
# n = int(input())
# print(fib(n+2, 10))


# ----------------------------5.1 5----------------------------
# def pisano_period(m):
#     cache = [0, 1]
#     current_n = 0
#     next_n = 1
#     period = 0
#     current_n_100 = 0
#     next_n_100 = 1
#     while True:
#         current_n, next_n = next_n, (current_n + next_n) % m
#         current_n_100, next_n_100 = next_n_100, (current_n_100 + next_n_100) % 100
#         cache.append(next_n_100)
#         period = period + 1
#         if current_n == 0 and next_n == 1:
#             return cache, period
#
# def fib(n, m):
#     if n <= 1:
#         return (n if n == 0 else n - 1)
#
#     table, p_pis = pisano_period(m)
#     res = table[n % p_pis]
#     return (res if res > 0 else 10) - 1
#
# m, n = map(int, input().split())
# print((fib(n+2, 10) - fib(m+1, 10)) % 10)


# ----------------------------9.1 1----------------------------
# class LinkedNode:
#     def __init__(self, value, next):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     def add(self, value):
#         self.head = LinkedNode(value, self.head)
#         self.length += 1
#
#     def get_index(self, index):
#         current = self.head
#         while index > 1:
#             current = current.next
#             index -= 1
#         return current.value
#
#     def insert(self, index, value):
#         if self.head is None or index == 0:
#             self.add(value)
#
#         else:
#             current = self.head
#             while current.next is not None and index > 1:
#                 current = current.next
#                 index -= 1
#             current.next = LinkedNode(value, current.next)
#         self.length += 1
#
#     def remove(self, index=1):
#         if index == 1 or self.head.next is None:
#             self.head = self.head.next
#
#         else:
#             current = self.head
#             while current.next.next is not None and index > 2:
#                 current = current.next
#                 index -= 1
#             current.next = current.next.next
#         self.length -= 1
#
#
# link_list = LinkedList()
# q = int(input())
# for i in range(q):
#     arr_q = list(map(int, input().split()))
#     if arr_q[0] == 1:
#         x, y = arr_q[1], arr_q[2]
#         link_list.insert(x, y)
#     elif arr_q[0] == 2:
#         print(link_list.get_index(arr_q[1]))
#     elif arr_q[0] == 3:
#         link_list.remove(arr_q[1])


# ----------------------------9.2 1----------------------------
# set_num = set()
# n = int(input())
#
# for i in range(n):
#     type_operation, num = list(map(int, input().split()))
#     if type_operation == 1:
#         set_num.add(num)
#     elif type_operation == 2:
#         print(int(num in set_num))


# ----------------------------9.3 1----------------------------
# map_num = {}
# n = int(input())
# for i in range(n):
#     settings = list(map(int, input().split()))
#     if settings[0] == 1:
#         map_num[settings[1]] = settings[2]
#     elif settings[0] == 2:
#         if settings[1] in map_num.keys():
#             print(map_num[settings[1]])
#         else:
#             print(-1)


# ----------------------------9.4 1----------------------------
# from collections import deque
#
# myStack = deque()
#
# n = int(input())
# for i in range(n):
#     settings = list(map(int, input().split()))
#     if settings[0] == 1:
#         myStack.append(settings[1])
#     elif settings[0] == 2:
#         myStack.pop()
#     if len(myStack) > 0:
#         print(myStack[-1])
#     else:
#         print(-1)


# ----------------------------9.4 2----------------------------
# from collections import deque
#
# myStack = deque()
#
# n = int(input())
# arr_n = list(map(int, input().split()))
# out_arr = [0] * n
#
# for i in range(n):
#     while myStack and arr_n[i] > arr_n[myStack[-1]]:
#         num = myStack.pop()
#         out_arr[i] += out_arr[num] + 1
#
#     myStack.append(i)
#
# print(*out_arr)


# ----------------------------9.6----------------------------
# from collections import deque
#
# myStack = deque()
#
# n = int(input())
# for i in range(n):
#     settings = list(map(int, input().split()))
#     if settings[0] == 1:
#         myStack.append(settings[1])
#     elif settings[0] == 2:
#         myStack.popleft()
#     if len(myStack) > 0:
#         print(myStack[0])
#     else:
#         print(-1)




