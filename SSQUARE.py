"""
Cho hai hình vuông có độ dài cạnh lần lượt là a và b.
In ra bằng các dấu * một hình vuông cạnh a bị cắt ở góc dưới cùng bên phải một vùng bằng với hình vuông cạnh b

      Input: Gồm một dòng duy nhất chứa hai số tự nhiên a,b.
      Constraints: b<a≤100
      Output: In ra hình vuông bị cắt theo đề bài.

Sample Test
Input: 5 3

Output
* * * * * 
* * * * * 
* * 
* * 
* * 

"""

a, b = [int(i) for i in input().split()]
 
mt = []
for i in range(a-b):
    lst = ['*' for i in range(a)]
    mt.append(lst)
 
for i in range(b):
    lst = ['*' for i in range(a-b)]
    mt.append(lst)
 
for i in mt:
    for j in i:
        print(j, end = " ")
    print()
