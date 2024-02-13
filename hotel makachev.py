print("WELCOME TO HOTEL MAKACHEW")
print("MENU ITEMS")
print("1.BIRIYANIS")
print("2.STARTERS")
print("3.KEBABS")
print("4.DESSERTS")
print("Go one by one")

chicken_biriyani = 120
mutton_biriyani = 220
egg_biriyani = 75
veg_biriyani = 60
n=0
x=0
z=0
total1=0
total2=0
total3=0
total4=0
total5=0
total6=0
total7=0
total8=0
total9=0
total10=0
total11=0
total12=0
total13=0
total14=0

user=int(input("Enter your choice:"))

t=0
if user==1:

    print("1.Chicken biriyani = ₹.120")
    print("2.Mutton biriyani = ₹.220") 
    print("3.Egg biriyani = ₹.75")
    print("4.Veg biriyani = ₹.60")
    
    A=int(input("Enter your choice:"))
    if A==1:
        n=int(input("Enter quantity;"))
        b=input("Do you want it more spicy Y/N:")
        if b=='y':
            print("preparing you dish")
        total1=chicken_biriyani*n
        
    elif A==2:
        n=int(input("Enter quantity:"))
        b=input("Do you want it more spicy Y/N:")
        if b=='y':
            print("preparing you dish")
        total2=mutton_biriyani*n

    elif A==3:
        n=int(input("Enter quantity:"))
        b=input("Do you want it more spicy Y/N:")
        if b=='y':
            print("preparing you dish")
        total3=egg_biriyani*n

    
    elif A==4:
        n=int(input("Enter quantity:"))
        b=input("Do you want it more spicy Y/N:")
        if b=='y':
            print("preparing you dish")
        total4=veg_biriyani*n
     

c=input("Do you want to take a look on next items Y/N:")
t=total1+total2+total3+total4
    
if c=='n' or 'N':
    print("Total amount",T)

else:
    print("1.STARTERS")
    print("2.KEBABS")   
    print("3.DESSERTS")
    user=int(input("Enter your choice:"))

    if user==1:           

        print("1.Paneer Tikka = ₹.128")
        tikka = 120

        print("2.crispy potato wedges = ₹.175")
        potato_wedges = 220
            
        print("3.Dahi puri = ₹.160")
        dahi_puri = 160

        print("4.spring roll = ₹.60")
        veg_biriyani = 60

        d=int(input("Enter your choice:"))

        if d==1:
            n=int(input("Enter quantity:"))
            print("preparing...")
            total5=tikka*n

        elif d==2:
            n=int(input("Enter quantity:"))
            print("preparing...")
            total6=potato_wedges*n

        elif d==3:
            n=int(input("Enter quantity:"))
            print("preparing...")
            total7=dahi_puri*n

        elif d==4:
            n=int(input("Enter quantity:"))
            print("preparing...")
            total8=veg_biriyani*n

c=input("Do you want to take a look on next items Y/N:")
r=t+total5+total6+total7+total8

if c=='n' or 'N':
    print("Total amount",r)

else:
    print("1.KEBABS")
    print("2.DESSERTS")
    
user=int(input("Enter your choice:"))

if user==1:           

    print("1.Galouti kebab = ₹.245")
    Galouti = 120

    print("2.seekh kebab = ₹.190")
    seekh = 220
            
    print("3.reshmi kebab = ₹.260")
    reshmi = 160

    e=int(input("Enter your choice:"))

    if d==1:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total9=Galouti*n

    elif d==2:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total10=seekh*n

    elif d==3:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total11=reshmi*n

c=input("Do you want to take a look on next items Y/N:")
x=r+total9+total10+total11

if c=='n' or 'N':
    print("Total amount",x)

else:
    print("1.DESSERTS")

user=int(input("Enter your choice:"))

if user==1:           

    print("1.Gulab jamun = ₹.245")
    Gulab = 120

    print("2.Gajar alwa = ₹.190")
    Gajar = 220
            
    print("3.Kaju katli = ₹.260")
    Kaju = 160

    e=int(input("Enter your choice:"))

    if d==1:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total12=Gulab*n

    elif d==2:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total13=Gajar*n

    elif d==3:
        n=int(input("Enter quantity:"))
        print("preparing...")
        total14=kaju*n
z=x+total12+total13+total14
print("Bill amount=",z)
print("Thankyou for visiting")
