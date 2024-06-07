thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

"""changing key name is not possible but if want to change this the method"""
thisdict["name"] = thisdict["model"]
print(thisdict)

del thisdict["model"]
print(thisdict)

"""accessing values"""
brand_name = thisdict["brand"]
print(brand_name)

x = thisdict.get("year")
print(x)

"""creating a new key value pairs"""
thisdict["color"] = "black"
print(thisdict)

