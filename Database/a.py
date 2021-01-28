import string
l= string.ascii_lowercase


lst = [[1, 'Code', 'a'], [2, 'Code', 'b'], [3, 'Code', 'zz'], [4, 'Code', 'py'], [5, 'Code', 'bit']]

lst = [[i[0],i[1],i[2].lower()] for i in lst]

lst=sorted(lst, key=lambda x: l.find(x[2][0]))
print(lst)
