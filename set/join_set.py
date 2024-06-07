#Union -> can join other iterable object also

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}
po = [111, 222, 333, 444]
op = (555, 666, 222, 7777, 444)



set3 = set1.union(set2, op, po)
# print(set3)

set4 = set1 | set2
# print(set4)

# Intersection => takes only values which are present in both variables
"""intersection() -> returns only new set of duplicate values present in both set"""
s1 = {"hlo", "loo", "oy"}
s2 = {"oy", "bloom", "loo" }

s3 = s1.intersection(s2)
# print(s3)

s1.intersection_update(s2)
# print(s1)


"""difference => returns new set of 1st set which the values are not present in 2nd set"""
ll = {'sbc', 'avc', 'poi', 'hgh'}
pp = {'pop', 'poi', 'hgh', 'lsl'}

io = ll.difference(pp)
# print(io)

ll.difference_update(pp)
print(ll)

"""symmetric_difference"""
kj = {'sbc', 'avc', 'poi', 'hgh'}
jk = {'pop', 'poi', 'hgh', 'lsl'}
tt = kj.symmetric_difference(jk)
print(tt)

kj.symmetric_difference_update(jk)
print(kj)