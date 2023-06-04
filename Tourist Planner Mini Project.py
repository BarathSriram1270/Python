import os
def clr():
    os.system("cls")
def tour(place,days,native,dir=1):
    amount=0
    #morning
    dosa,idly,pongal,vada,chapatti,poori,ravakesari,baji,bhakri=20,10,50,5,20,50,50,5,20
    #afternoon
    rice,vegbriyani,chickenbriyani,muttonbriyani,friedrice,egg,boiledegg,tamarindrice,pudinarice=110,110,150,200,70,10,10,70,70
    #snacks and juice
    cake,puff,fruitjuice,milkshake=20,20,50,80
    #dinner
    parotta,chilliparotta,milk,noodles=50,90,10,50
    if place==1: #Tamilnadu
        if native==1 or native==4 or native==3 or native==5 or native==8:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(20000)\n2.Helicopter(40000)\n3.Ship(10000)")
                if trs1=='1':
                    amount=amount+20000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+10000
                clr()
                print("Your budget is",amount)
        elif native==2 or native==6 or native==7 or native==9 or native==10:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(15000)\n2.Helicopter(40000)\n3.Bus(2500)\n4.Car(5700)")
                if trs1=='1':
                    amount=amount+15000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+2500
                elif trs1=='4':
                    amount=amount+5700
                clr()
                print("Your budget is",amount)
        print("WELCOME TO TAMILNADU")
        o=input("Are you going to stay at \nnormal hotel(per day 1000) press 1\n5 star hotel(per day 2400) press 2\nIf not needed press number other than 1,2")
        if o=='1':
            amount=amount+1000*days
            clr()
            o=input("do you want a/c room(+500 per day) or not\npress 1 for a/c \nn for non a/c")
            if o=="1":
                amount=amount+500*days
        elif o=='2':
            amount=amount+2400*days
            clr()
            o=input("do you want a/c room(+700 per day) or not\npress 1 for a/c \nn for non a/c")
            if o=="1":
                amount=amount+700*days
        clr()
        print("amount you need to pay for room",amount)
        day1=days #Tourist place selection TN
        i=1
        xy='y'
        while days>0 and xy=='y':
            print("TOURIST PLACES IN TAMILNADU...\nChoose for your day ",i,"\n1.Meenakshi Amman Temple(rs.100)\n2.Srivilliputhur Andal Temple(500)\n3.Queens land(1000)\n4.VGP(1000)\n5.ooty(500)\n6.kodaikanal(500)\n7.Anna University(100)\n8.Marina Beech(500)\npress the number according to the place\nIf none press any number except the following")
            w=input()
            if w=='1' or w=='7':
                amount=amount+100
                print("Good choice you can go at day",i," Morning")
            elif w=='2' or w=='5' or w=='6' or w=='8':
                amount=amount+500
                print("Good choice you can go at day",i," Morning to evening")
            if w=='4' or w=='3':
                amount=amount+1000
                print("Good choice you can go at day ",i," morning to evening fullday")
            days=days-1
            if days!=0:
                print("enter choice for next day")
                i=i+1
            if i>2:
                clr()
                xy=input("If you are confused to pick for next day\nYou can select lated by pressing n\nOr just press y to continue")
            clr()
        print("now your budget is",amount)
        days=day1 #Purchasig special foods TN
        j='y'
        while j=='y': 
            fo=input("Special foods in Tamil nadu\n1.vala elai parotta(150)\n2.kalaki(50)\n3.thalapakathi briyani(150)\n4.mix juice(50)\n press the number according to the foods\n if not press any number to exit this")
            clr()
            if fo=='1' or fo=='3':
                e=int(input("how many do you want"))
                clr()
                amount=amount+50*e
            elif fo=='2' or fo=='4':
                e=int(input("how many do you want"))
                clr()
                amount=amount+150*e
            j=input("do you want to order anything that you need extra from the list \npress y to purchace extra or else press any")
            clr()
        print("Your budget is",amount)
        print("Do you want to purchase food for Morning,Aternoon,Evening,Dinner For ALL DAYS\nIf so press y\n[even you can purchase later by pressing no]")
    elif place==2: #Mumbai
        if native==1 or native==4 or native==3 or native==5 or native==8:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(20000)\n2.Helicopter(40000)\n3.Ship(10000)")
                if trs1=='1':
                    amount=amount+20000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+10000
                clr()
                print("Your budget is",amount)
        elif native==2 or native==6 or native==7 or native==9 or native==10:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(15000)\n2.Helicopter(40000)\n3.Bus(2500)\n4.Car(5700)")
                if trs1=='1':
                    amount=amount+15000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+2500
                elif trs1=='4':
                    amount=amount+5700
                clr()
                print("Your budget is",amount)
        print("WELCOME TO MUMBAI")
        o=input("Are you going to stay at \nnormal hotel(per day 1000) press 1\n5 star hotel(per day 2400) press 2\nIf not needed press any number to exit other than 1,2")
        if o=='1':
            amount=amount+1000*days
            clr()
            o=input("do you want a/c room(+500 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+500*days
        elif o=='2':
            amount=amount+2400*days
            clr()
            o=input("do you want a/c room(+700 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+700*days
        clr()
        print("amount you need to pay for room",amount)
        day1=days #Tourist place selection Mumbai
        i=1
        xy='y'
        while days>0 and xy=='y':
            print("TOURIST PLACES IN MUMBAI...\nChoose for your day ",i,"\n1.Gateway of India(rs.100)\n2.Essal world(1000)\n3.Kenhari Caves(500)\n4.Sanjay Gandhi National park(500)\n5.Elephant Caves(500)\n6.Shree Mahalakshmi Temple(500)\n7.Chhatrapati Shivaji Maharaj terminus(100)\n8.Marine Drive(1000)\npress the number according to the place\nIf none press any number except the following")
            w=input()
            if w=='1' or w=='7':
                amount=amount+100
                print("Good choice you can go at day",i," Morning")
            elif w=='3' or w=='5' or w=='6' or w=='4':
                amount=amount+500
                print("Good choice you can go at day",i," Morning to evening")
            if w=='2' or w=='8':
                amount=amount+1000
                print("Good choice you can go at day ",i," morning to evening fullday")
            days=days-1
            if days!=0:
                print("enter choice for next day")
                i=i+1
            if i>2:
                clr()
                xy=input("If you are confused to pick for next day\nYou can select lated by pressing n\nOr just press y to continue")
            clr()
        print("now your budget is",amount)
        days=day1 #special food Munbai
        j='1'
        while j=='1':
            fo=input("Special foods in Mumbai\n1.Veg pav(150)\n2.Pel poori(50)\n3.Pani poori(150)\n4.bombay sandwich(50)\n press the number according to the foods\n if not press any number to exit this")
            clr()
            if fo=='1' or fo=='3':
                e=int(input("how many do you want"))
                clr()
                amount=amount+50*e
            elif fo=='2' or fo=='4':
                e=int(input("how many do you want"))
                clr()
                amount=amount+150*e
            j=input("do you want to order anything that you need extra from the list \npress 1 to purchace extra or else press any")
            clr()
        print("Your budget is",amount)
        print("Do you want to purchase food for Morning,Aternoon,Evening,Dinner For ALL DAYS\nIf so press y\n[even you can purchase later by pressing no]")
    elif place==3: #Goa
        if native==1 or native==4 or native==3 or native==5 or native==8:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(20000)\n2.Helicopter(40000)\n3.Ship(10000)")
                if trs1=='1':
                    amount=amount+20000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+10000
                clr()
                print("Your budget is",amount)
        elif native==2 or native==6 or native==7 or native==9 or native==10:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(15000)\n2.Helicopter(40000)\n3.Bus(2500)\n4.Car(5700)")
                if trs1=='1':
                    amount=amount+15000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+2500
                elif trs1=='4':
                    amount=amount+5700
                clr()
                print("Your budget is",amount)
        print("WELCOME TO GOA")
        o=input("Are you going to stay at \nnormal hotel(per day 1000) press 1\n5 star hotel(per day 2400) press 2\nIf not needed press any number to exit other than 1,2")
        if o=='1':
            amount=amount+1000*days
            clr()
            o=input("do you want a/c room(+500 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+500*days
        elif o=='2':
            amount=amount+2400*days
            clr()
            o=input("do you want a/c room(+700 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+700*days
        clr()
        print("amount you need to pay for room",amount)
        day1=days #Tourist place in GOA
        i=1
        xy='y'
        while days>0 and xy=='y':
            print("TOURIST PLACES IN GOA...\nChoose for your day ",i,"\n1.Dudhsagar Falls(rs.100)\n2.Arjuna beach(1000)\n3.Harvelam Waterfalls(500)\n4.Reis Magos Fort(500)\n5.Palolem beach(500)\n6.Shree Mangesh Temple(500)\n7.Basilisa of Bom Jesus(100)\n8.Candolim Beach(1000)\npress the number according to the place\nIf none press any number except the following")
            w=input()
            if w=='1' or w=='7':
                amount=amount+100
                print("Good choice you can go at day",i," Morning")
            elif w=='3' or w=='5' or w=='6' or w=='4':
                amount=amount+500
                print("Good choice you can go at day",i," Morning to evening")
            if w=='2' or w=='8':
                amount=amount+1000
                print("Good choice you can go at day ",i," morning to evening fullday")
            days=days-1
            if days!=0:
                print("enter choice for next day")
                i=i+1
            if i>2:
                clr()
                xy=input("If you are confused to pick for next day\nYou can select lated by pressing n\nOr just press y to continue")
            clr()
        print("now your budget is",amount)
        days=day1 #Special foods Goa
        j='1'
        while j=='1':
            fo=input("Special foods in Goa\n1.Kingfish(150)\n2.Ripe Jackfruit Cake (50)\n3.Neuri [A Tasty Sweet](150)\n4.Malabar Spinach Stir Fry (50)\n press the number according to the foods\n if not press any number to exit this")
            clr()
            if fo=='1' or fo=='3':
                e=int(input("how many do you want"))
                clr()
                amount=amount+50*e
            elif fo=='2' or fo=='4':
                e=int(input("how many do you want"))
                clr()
                amount=amount+150*e
            j=input("do you want to order anything that you need extra from the list \npress 1 to purchace extra or else press any")
            clr()
        print("Your budget is",amount)
        print("Do you want to purchase food for Morning,Aternoon,Evening,Dinner For ALL DAYS\nIf so press y\n[even you can purchase later by pressing no]")
    elif place==4: #Banglore
        if native==1 or native==4 or native==3 or native==5 or native==8:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(20000)\n2.Helicopter(40000)\n3.Ship(10000)")
                if trs1=='1':
                    amount=amount+20000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+10000
                clr()
                print("Your budget is",amount)
        elif native==2 or native==6 or native==7 or native==9 or native==10:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(15000)\n2.Helicopter(40000)\n3.Bus(2500)\n4.Car(5700)")
                if trs1=='1':
                    amount=amount+15000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+2500
                elif trs1=='4':
                    amount=amount+5700
                clr()
                print("Your budget is",amount)
        print("WELCOME TO BANGLORE")
        o=input("Are you going to stay at \nnormal hotel(per day 1000) press 1\n5 star hotel(per day 2400) press 2\nIf not needed press any number to exit other than 1,2")
        if o=='1':
            amount=amount+1000*days
            clr()
            o=input("do you want a/c room(+500 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+500*days
        elif o=='2':
            amount=amount+2400*days
            clr()
            o=input("do you want a/c room(+700 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+700*days
        clr()
        print("amount you need to pay for room",amount)
        day1=days #Tourist place in Banglore
        i=1
        xy='y'
        while days>0 and xy=='y':
            print("TOURIST PLACES IN BANGLORE...\nChoose for your day ",i,"\n1.Bengaluru Palace(rs.100)\n2.Cubbon Park(1000)\n3.UV City(500)\n4.National Gallary of Mordern art(500)\n5.Tipu sultan's Summer Palace(500)\n6.Sri Someshwara Swami Temple(500)\n7.Bannarghatta National Park(100)\n8.Wounderla(1000)\npress the number according to the place\nIf none press any number except the following")
            w=input()
            if w=='1' or w=='7':
                amount=amount+100
                print("Good choice you can go at day",i," Morning")
            elif w=='3' or w=='5' or w=='6' or w=='4':
                amount=amount+500
                print("Good choice you can go at day",i," Morning to evening")
            if w=='2' or w=='8':
                amount=amount+1000
                print("Good choice you can go at day ",i," morning to evening fullday")
            days=days-1
            if days!=0:
                print("enter choice for next day")
                i=i+1
            if i>2:
                clr()
                xy=input("If you are confused to pick for next day\nYou can select lated by pressing n\nOr just press y to continue")
            clr()
        print("now your budget is",amount)
        days=day1 #Special foods Banglore
        j='1'
        while j=='1':
            fo=input("Special foods in Goa\n1.Rava Idli(150)\n2.Holige(50)\n3.kova(150)\n4.badam Cake(50)\n press the number according to the foods\n if not press any number to exit this")
            clr()
            if fo=='1' or fo=='3':
                e=int(input("how many do you want"))
                clr()
                amount=amount+50*e
            elif fo=='2' or fo=='4':
                e=int(input("how many do you want"))
                clr()
                amount=amount+150*e
            j=input("do you want to order anything that you need extra from the list \npress 1 to purchace extra or else press any")
            clr()
        print("Your budget is",amount)
        print("Do you want to purchase food for Morning,Aternoon,Evening,Dinner For ALL DAYS\nIf so press y\n[even you can purchase later by pressing no]")
    elif place==5: #Rajasthan
        if native==1 or native==4 or native==3 or native==5 or native==8:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(20000)\n2.Helicopter(40000)\n3.Ship(10000)")
                if trs1=='1':
                    amount=amount+20000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+10000
                clr()
                print("Your budget is",amount)
        elif native==2 or native==6 or native==7 or native==9 or native==10:
            trs=input("Do you want any transport?\nIf yes press y\nIf you have own transport press n")
            clr()
            if trs=='y':
                trs1=input("1.Flight(15000)\n2.Helicopter(40000)\n3.Bus(2500)\n4.Car(5700)")
                if trs1=='1':
                    amount=amount+15000
                elif trs1=='2':
                    amount=amount+40000
                elif trs1=='3':
                    amount=amount+2500
                elif trs1=='4':
                    amount=amount+5700
                clr()
                print("Your budget is",amount)
        print("WELCOME TO RAJASTHAN")
        o=input("Are you going to stay at \nnormal hotel(per day 1000) press 1\n5 star hotel(per day 2400) press 2\nIf not needed press any number to exit other than 1,2")
        if o=='1':
            amount=amount+1000*days
            clr()
            o=input("do you want a/c room(+500 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+500*days
        elif o=='2':
            amount=amount+2400*days
            clr()
            o=input("do you want a/c room(+700 per day)?\npress 1 for a/c \n2 for non a/c")
            if o=="1":
                amount=amount+700*days
        clr()
        print("amount you need to pay for room",amount)
        day1=days #Tourist place in Rajasthan
        i=1
        xy='y'
        while days>0 and xy=='y':
            print("TOURIST PLACES IN RAJASTHAN...\nChoose for your day ",i,"\n1.Amber Palace(rs.100)\n2.City Palace(1000)\n3.Magic Land(500)\n4.Ranthamboor National Park(500)\n5.Udaipur(500)\n6.Ranakapur JaniTemple(500)\n7.Junagarh Fort(100)\n8.Hawa Mahal(1000)\npress the number according to the place\nIf none press any number except the following")
            w=input()
            if w=='1' or w=='7':
                amount=amount+100
                print("Good choice you can go at day",i," Morning")
            elif w=='3' or w=='5' or w=='6' or w=='4':
                amount=amount+500
                print("Good choice you can go at day",i," Morning to evening")
            if w=='2' or w=='8':
                amount=amount+1000
                print("Good choice you can go at day ",i," morning to evening fullday")
            days=days-1
            if days!=0:
                print("enter choice for next day")
                i=i+1
            if i>2:
                clr()
                xy=input("If you are confused to pick for next day\nYou can select lated by pressing n\nOr just press y to continue")
            clr()
        print("now your budget is",amount)
        days=day1 #Special foods Rajasthan
        j='1'
        while j=='1':
            fo=input("Special foods in Rajasthan\n1.SAFED MAAS(150)\n2.MIRCHI BADA(50)\n3.Rajasthani cuisine(150)\n4.Melon Big Ice(50)\n press the number according to the foods\n if not press any number to exit this")
            clr()
            if fo=='1' or fo=='3':
                e=int(input("how many do you want"))
                clr()
                amount=amount+50*e
            elif fo=='2' or fo=='4':
                e=int(input("how many do you want"))
                clr()
                amount=amount+150*e
            j=input("do you want to order anything that you need extra from the list \npress 1 to purchace extra or else press any")
            clr()
        print("Your budget is",amount)
        print("Do you want to purchase food for Morning,Aternoon,Evening,Dinner For ALL DAYS\nIf so press y\n[even you can purchase later by pressing no]")
    i=1
    bm=input()
    clr()
    while bm=="y" and days>0:        
            j='y'
            while j=='y':
                print("Order for day",i," morning\n1.dosa(20)\n2.idly(10)\n3.pongal(50)\n4.vada(5)\n5.chapatti(20)\n6.poori(50)\n7.ravakesari(50)\n8.baji(10)\n9.bhakri(20)\npress number according to the foods\nif not press any number except the following")
                fo1=int(input())
                if fo1==1 or fo1==5 or fo1==9:
                    ee=int(input("how many do you need"))
                    amount=amount+20*ee
                elif fo1==2 or fo1==8:
                    ee=int(input("how many do you need"))
                    amount=amount+10*ee
                elif fo1==3 or fo1==6 or fo1==7:
                    ee=int(input("how many do you need"))
                    amount=amount+50*ee
                elif fo1==4:
                    ee=int(input("how many do you need"))
                    amount=amount+5*ee
                j=input("do you want to order anything that you need extra from the list \npress y to purchace extra")
                clr()
            print("your budget is",amount)
            j='y'
            while j=='y':
                print("Order for day ",i," aftenoon\n1.rice with 6 vegetables(110)\n2.vegbriyani(110)\n3.chickenbriyani(150)\n4.muttonbriyani(200)\n5.friedrice(70)\n6.egg x2(10)\n7.boiledegg(10)\n8.tamarindrice(70)\n9.pudinarice(70)\nIF YOU DON'T WANT ANYTHING JUST PRESS ANY NUMBER EXCEPT THAT FOLLOWING TO EXIT" )
                fo1=int(input())
                if fo1==1 or fo1==2:
                    ee=int(input("how many do you need"))
                    amount=amount+110*ee
                elif fo1==3:
                    ee=int(input("how many do you need"))
                    amount=amount+150*ee
                elif fo1==8 or fo1==5 or fo1==9:
                    ee=int(input("how many do you need"))
                    amount=amount+70*ee
                elif fo1==6 or fo1==7:
                    ee=int(input("how many do you need"))
                    amount=amount+10*ee
                j=input("do you want to order anything that you need extra from the list \npress y to purchace extra")
                clr()
            print("your budget is",amount)
            j='y'
            while j=='y':
                print("Order for day", i ,"evening snacks\n1.cake(20)\n2.puff(20)\n3.fruitjuice(50)\n4.milkshake(80)\nIF YOU DON'T WANT ANYTHING JUST PRESS ANY NUMBER EXCEPT THAT FOLLOWING TO EXIT")
                fo1=int(input())
                if fo1==1 or fo1==2:
                    ee=int(input("how many do yo want"))
                    amount=amount+20*ee
                elif fo1==3:
                    ee=int(input("how many do you need"))
                    amount=amount+50*ee
                elif fo1==4:
                    ee=int(input("how many do you need"))
                    amount=amount+80*ee
                j=input("do you want to order anything that you need extra from the list \npress y to purchace extra")
                clr()
            print("your budget",amount)
            j='y'
            while j=='y':
                print("Order for day ",i," dinner\n1.parotta(50)\n2.chilliparotta(90)\n3.milk 250ml(10)\n4.noodles50\nIF YOU DON'T WANT ANYTHING JUST PRESS ANY NUMBER EXCEPT THAT FOLLOWING TO EXIT")
                fo1=int(input())
                if fo1==1 or fo1==4:
                    ee=int(input("enter how many do you want"))
                    amount=amount+ee*50
                elif fo1==2:
                    ee=int(input("how many do you need"))
                    amount=amount+90*ee
                elif fo1==3:
                    ee=int(input("how many do you need"))
                    amount=amount+10*ee
                j=input("do you want to order anything that you need extra from the list \npress y to purchace extra")
                clr()
            print("your budget",amount)
            days=days-1
            i=i+1
            if i<=day1:
                print("Do you want to purchase for day",i,"also press y to purchase now itself\nor you can purchase later by pressing n")
                bm=input()
    days=day1
f=int(input("*****************************Welcome to tourist planner site*****************************\nyour tourist places are given below\npress the number according to the place you want\n1.Tamil nadu\n2.mumbai\n3.goa\n4.banglore\n5.rajasthan\nif not press any number except that following"))
for i in range(1,6):
    if i==f:
        clr()
        s=int(input("Ok,fine how many days are you planned"))
        clr()
        ma=int(input("where are you from?\n1.America\n2.Europe\n3.Australia\n4.Africa\n5.Japan\n6.china\n7.Russia\n8.Ireland\n9.pakisthan\n10.India[If you are from India,say that you are in which direction]\npress the number"))
        clr()
        ma1=1
        if ma==10:
            ma1=int(input("1.north\n2.south\n3.east\n4.west\n5.north-east\n6.north-west\n7.south-east\n8.south-west"))
        clr()
        tour(f,s,ma,ma1)
clr()
print("****************************************WELCOME SEE YOU AGAIN***************************************")