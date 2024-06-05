thisset = {"apple", "banana", "cherry", "mango", "grape"}

thisset.remove("apple")
print(thisset)

"""shows error if we try to remove values which are not present in set"""
# thisset.remove("keep")
# print(thisset)

thisset.discard("cherry")
print(thisset)

"""discard wont show any errors if we try to remove the values which is not present in set"""
thisset.discard("keep")
print(thisset)

thisset.pop()
print(thisset)