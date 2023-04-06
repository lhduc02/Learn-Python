"""
You are given an integer N . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns N.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Function Description

Complete the rangoli function in the editor below.
rangoli has the following parameters:
+ int size: the size of the rangoli

Returns
+ string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format:
Only one line of input containing , the size of the rangoli.

Constraints:
0 < size < 27
"""
n = int(input())
length = 4*n-3
width = 2*n-1

arr = []
mt_a = []
for i in range(96+n, 96, -1):
    arr.append(chr(i))
for i in range(98, 97+n):
    arr.append(chr(i))
arr_bd = arr.copy()
arr_bd = "-".join(arr_bd)

for i in range(n-1):
    arr = arr[:n-i-1] + arr[n-i+1:]
    str = "-".join(arr)
    str = "-"*(i+1)*2 + str + "-"*(i+1)*2
    mt_a.append(str)
for i in range(n-2, -1, -1):
    print(mt_a[i])
print(arr_bd)
for i in range(n-1):
    print(mt_a[i])
