# what's sets?
# list can use append, sets can use add
# s
# {1, 2, 3}
# s.add(4)
# s
# set 可以使用的命令有很多
s1 = set()
s2 = set()


s1 = {1,2,3,4,5}
# s1.union(s)
s2.add("one")
s2.add(2)
s2.add(3)

print(s1)
print(s2)
# print(s1.union(s2))
print(s2.intersection(s1))
print('Print the difference: ',s1.difference(s2))