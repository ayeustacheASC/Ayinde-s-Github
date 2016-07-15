from random import*
list1 = ["return","big","small","sharp","fast","super","man","attack","appocalypse","scary"]
list2 = ["the","bang","of","amazing","2","boy","girl","fly","speed","furious"]
list3 = ["plane","fall","jump","hard","fire","tornado","disaster","natural","tssunami","rise"]
i = 0
while i <= 10:
    x = list1[randrange(10)]
    y = list2[randrange(10)]
    z = list3[randrange(10)]
    title = x + " " + y + " " + z
    print (title)
    i  = i + 1
    