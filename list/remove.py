leeeest = ["aaa", "jjj", "bbb", "vvv", "jjj"]
"""removes value"""
leeeest.remove("jjj")
print(leeeest)

"""removes index"""
lost = ["aaa", "jjj", "bbb", "vvv", "jjj", 7895, 62878]
lost.pop(3)
print(lost)


"""del """
del lost[0]
print(lost)

# del lost
lost.clear()
print(lost)