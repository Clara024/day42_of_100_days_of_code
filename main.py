import time,os
blue = '\033[34m'
red = '\033[31m'
green = '\033[32m'
default = '\033[0m'
yellow = '\033[33m'

print (f"{yellow}MokéBeast{default}")

myBeast = {"Beast Name" : None, "Type" : None, "Special move": None, "HP": None, "MP" : None}
print( )

for name, value in myBeast.items( ):
  myBeast[name] = input(f"{name}: ").strip( ).title( )
  print( )
time.sleep(1)
os.system("clear")

if myBeast ["Type"] =="Air":
     print(f"{blue}",end = " ")
elif myBeast["Type"]  == "Fire":
     print(f"{red}",end = " " )
elif myBeast ["Type"] == "Earth":
     print(f"{green}",end = " ")
elif myBeast ["Type"] == "Water":
     print(f"{default}",end = " ")
else:
     print(f"{yellow}",end = " ")
for name , value in myBeast.items( ):
      print (f"{name} : {value} ")
      print()