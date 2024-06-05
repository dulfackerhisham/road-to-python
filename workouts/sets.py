sset = {'hi', 99, 'looo', 78, 'hi'}
wow = {3,7,4,1}
print(sset)

"""sets are immutable but we can add and remove items"""

sset.add('dulfu')
print(sset)
sset.update(wow)
print(sset)

sset.remove('hi')
print(sset)

wow.discard(4)
print(wow)

