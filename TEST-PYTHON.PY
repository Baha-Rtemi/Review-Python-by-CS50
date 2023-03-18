people = [
    {"name" : "Baha",
     "live" : "Italy"},
    {"name" : "Ali",
     "live" : "Libya"},
    {"name" : "Same",
     "live" : "Irland"}]
def f(person):
    return person["name"]
    
print(people.sort(key = f))