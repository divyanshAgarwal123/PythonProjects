#a1={}
#print(type(a1))
a2={"divyansh":"coding",
    "papa":"bhagwat",
    "mama":"accupresure",
    "games":{"fav":"assain creed",
             "downloading":"lego ninjago",
             "played":"memories of mars"}}
a2["sheryl"]="padhai"
a2["divyansh1"]="games"
del a2["divyansh1"]
print(a2["games"]["downloading"])
a3=a2.copy()
del a3["games"]
print(a2.get("divyansh"))     #one more option to get the value
a2.update({"sheryl": "instagram"})
print(a2)
print(a3)
#print(a2.keys())
#print(a2.items())