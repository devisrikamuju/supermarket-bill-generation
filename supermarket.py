from datetime import datetime
name=input("enter your name:")
#lits of items
lists ='''
suger      rs 30
rice       rs 28
oil        rs 130
dairy milk rs 100
cococola   rs 75
termaric   rs 44
colgate    rs 80
palli      rs 116
rin        rs 110
vim        rs 10
'''
#declarations
ilist=[]
qlist=[]
plist=[]
price=0
totalprice=0
finalprice=0
pricelist=[]
product=[]
items={'rice':28,'suger':30, 'oil':135,'dairy milk':100,
       'cococola':75,'termaric':44,'colgate':80, 'palli':116,'rin':110,
       'vim':10}
try:
    option = int(input("list of items press 1 :"))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

if option==1:
  print(lists)
for i in range(len(items)):
    try:
      inb= int(input("if you want to buy press 1 or 2 for exist:"))
    except ValueError:
       print("invalide input")
    if inb==2:
     break
    if inb==1:
        item=input("enter your items:")
        
        quantity=input("enter your quantity")
        if item in items.keys():
            print(items[item])
            price= int(quantity)*(items[item])
            pricelist.append((item, quantity,items,price))
            
            
   
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            totalprice =sum(plist)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
           print("sorry you entered item is not available")
    else:
       print("you entered wrong item")
inp=input("can i bill the items yes or no")
if inp =='yes':
        pass
        if finalprice!=0:
           print(25*"=","KST Supermarket",25*"=")
           print(25*" "," Ramachandrapuram",25*" ")
           print("Name:",name,30*" ","Date:",datetime.now())
           print(70*"-")
           print("sno", 8*" ", "items", 7*" ", "quantity", 5*" ","price")
           for i in range(len(pricelist)):
              print(i,8*" ",ilist[i],8*" ",qlist[i],10*" ",plist[i])
              product.append(pricelist)
           print(75*"-")
           print(40*" ", "totalprice:" "Rs", totalprice)
           print(40*" ", "gst ammount:" "Rs", gst)
           print(70*"-")
           print(50*" ", "finalprice:","Rs", finalprice)
           print(75*"-")
           print(40*"-", "thank you for visiting", 40*"-")