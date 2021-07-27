cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

for i in cro:
    string = string.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(string))