thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"model": "figo"})
thisdict.update({"color": "white"}) #if we try to update non existing keyvalue pairs then it will be added to dict
print(thisdict)

"""adding new keyvalue pair"""
thisdict["modified"] = "20/05/2024"
print(thisdict)