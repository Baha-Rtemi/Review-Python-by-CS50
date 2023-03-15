thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))
print(thisdict["brand"])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
print("model" in thisdict)
thisdict.pop("model")
print(thisdict)