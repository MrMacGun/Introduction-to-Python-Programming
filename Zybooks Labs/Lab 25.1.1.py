#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/25/section/1
#Lab removes all , . and spaces then counts the number of characters

userin = input()
inp1 = userin.replace(" ","")
inp2 = inp1.replace("," ,"")
inp3 = inp2.replace(".", "")
inp4 = inp3.replace("!", "")
print(len(inp4))
