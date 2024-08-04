import turtle
import random
def carloan():

    window.resetscreen()
    window1=turtle.Screen()
    cursor.penup()
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-250,200)
    cursor.write("INTEREST CALCULATOR",font=("Arial",35,"bold"))
    cursor.setpos(0,0)

    principal=turtle.numinput("total cost","enter car  price")
    downpayment=turtle.numinput("down payment","enter downpayment")
    interest=turtle.textinput("interest","enter the interest rate")
    loanterm=turtle.numinput("loan term","enter the terme of the loan in years")
    interest=float(interest)
    netpayment=principal-downpayment
    monthterm=loanterm*12
   

    monthly_interest_rate = interest / 100 / 12
  
    numerator = netpayment * monthly_interest_rate * (1 + monthly_interest_rate) ** monthterm
    denominator = (1 + monthly_interest_rate) ** monthterm - 1
    monthlypayment = numerator / denominator
    monthlyloan=netpayment/12
    monthlyinterest=netpayment*monthly_interest_rate
    monthlypayment = str(round(monthlypayment,2))
    temp = "Monthly payment = " + monthlypayment
    monthlypayment= str(monthlypayment)
    temp="monthly payment = "+monthlypayment
    cursor.write(temp,font=("Arial",20,"normal"))
    cursor.setheading(270)
    cursor.forward(40)
    totalinterest=monthlyinterest*monthterm
    monthlyinterest=str(round(monthlyinterest,2))
    temp1="monthly interest = "+monthlyinterest
    cursor.write(temp1,font=("Arial",20,"normal"))
    cursor.forward(40)
    totalinterest=str(totalinterest)
    temp2="total interest = " + totalinterest
    cursor.write(temp2,font=("Arial",20,"normal"))
    window1.onkey(res,"q")
    window1.listen()
 

  
def game():
    window.resetscreen()
    cursor.penup()
    number= 100*random.random()
    number=int(number)
    guess=-1
    
    while(number!=guess):
        cursor.penup()
        guess=turtle.numinput("guess","guess the number")
        guess=int(guess)
        if(number<guess):
            window.resetscreen()
            cursor.penup()
            cursor.setpos(-50,160)
            cursor.write("lower⬇️",font=("Arial",50,"normal"))
        
        elif(number>guess):
            window.resetscreen()
            cursor.penup()
            cursor.setpos(-50,160)
            cursor.write("higher⬆️",font=("Arial",50,"normal"))
    window.resetscreen()
    cursor.backward(200)
    cursor.write(number,font=("Arial",50,"normal"))
    cursor.forward(80)
    cursor.write("is the number",font=("Arial",50,"normal"))
    
def calculator():
    window.resetscreen()
    number1= turtle.numinput("number1","enter the first number")
    sign = turtle.textinput("sign","enter the operation + - / *")
    number2=turtle.numinput("number2","enter the second number")
    if(sign=="+"):
        cursor.write(number1+number2,font=("Arial",50,"normal"))
    elif(sign=="-"):
        cursor.write(number1-number2,font=("Arial",50,"normal"))
    elif(sign=="*"):
        cursor.write(number1*number2,font=("Arial",50,"normal"))
    elif(sign=="/"):
        cursor.write(number1/number2,font=("Arial",50,"normal"))

  
def settings():
    window=turtle.Screen()
    colour=turtle.textinput("coulour","type the colour you want to change into")
    window.bgcolor(colour)
    window.onkey(res,"q")
    window.listen()
def weather():
    window.resetscreen()
    cursor.penup()
    
    window.bgcolor("grey")
    cursor.color("gold")
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-150,200)
    cursor.color("black")
    cursor.write("WEATHER",font=("Arial",50,"bold"))
    cursor.color("gold")
    cursor.setpos(0,0)

    file=open("weather_info.txt","r")
    content=file.readlines()
    l=len(content)

    cursor.backward(100)
    for i in range(l):
        if(i!="\n"):
            
            cursor.write(content[i],font=("Arial",25,"normal"))
            cursor.setheading(270)
            cursor.forward(40)
    file.close()
def schedule():
    window.resetscreen()
    cursor.penup()
    window.bgcolor("white")
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-250,200)
    cursor.write("CLASS SCHEDULE",font=("Arial",40,"bold"))
    cursor.setpos(0,0)

    file=open("UFV_schedule.txt","r")
    content=file.readlines()
    l=len(content)

    cursor.backward(100)
    for i in range(l):
        if(i!="\n"):
            cursor.write(content[i],font=("Arial",25,"normal"))
            cursor.setheading(270)
            cursor.forward(40)
    file.close()
def bus():
    window.resetscreen()
    cursor.penup()
    window.bgcolor("white")
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-250,200)
    cursor.write("BUS SCHEDULE",font=("Arial",40,"bold"))
    cursor.setpos(0,0)

    file=open("bus_schedule.txt","r")
    content=file.readlines()
    l=len(content)
    cursor.backward(100)
    for i in range(l):
        if(i!="\n"):
            cursor.write(content[i],font=("Arial",18,"normal"))
            cursor.setheading(270)
            cursor.forward(40)

    file.close()

        
      

     
   
   
      
def contact():
    def addcontact():
        window=turtle.Screen()
        file=open("contacts.txt","a")

        cursor.setheading(270)
        cursor.forward(60)
        numbe =turtle.textinput("name","enter the number you want to add")
        content=file.write(numbe)
     
        cursor.write(numbe,font=("Arial",25,"normal"))
        file.close()
        window.onkey(res,"q")
        window.listen()
       
      
    window.resetscreen()
    cursor.penup()

    window.bgcolor("black")
    cursor.color("white")
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-150,200)
    cursor.write("CONTACTS",font=("Arial",50,"bold"))
    cursor.setpos(0,0)

    file=open("contacts.txt","r")
    content=file.readlines()
    l=len(content)

    cursor.backward(100)
    for i in range(l):
       
            cursor.write(content[i],font=("Arial",25,"normal"))
            cursor.setheading(270)
            cursor.forward(40)
    cursor.forward(120)
    file.close()
    cursor.write('press a to add / save a number',font=("Arial",20,"normal"))
    cursor.forward(30)
    cursor.right(90)
    cursor.forward(250)

    cursor.setpos(-100,0)
    cursor.setheading(270)
    cursor.forward(20)
    window.onkey(addcontact,"a")
    window.listen()
def ranwords():
    window.resetscreen()
    cursor.penup()
    window.bgcolor("white")
    cursor.setpos(-340,300)
    cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)
    cursor.setpos(-150,200)
    cursor.write("RANDOMIZER",font=("Arial",40,"bold"))
    cursor.setpos(0,0)

    cursor.setpos(-280,0)
    def inranwords():


       
        file = open("random_words.txt","r")
        window.resetscreen()
     
        cursor.penup()
        cursor.speed(10)
        cursor.setpos(-340,300)
        cursor.write("press x to move for main menu",font=("Arial",13,"normal"))
        cursor.setpos(0,0)
        cursor.setpos(-150,200)
        cursor.write("RANDOMIZER",font=("Arial",40,"bold"))
        cursor.setpos(0,0)

        cursor.penup()
        content = file.readlines()
        file.close()
        content_size=len(content)
        random_value=content_size*random.random()
        random_value=int(random_value)
        cursor.setpos(-50,-30)
        cursor.write(content[random_value-1],font=("Arial",40,"normal"))

    cursor.penup()
    cursor.write("keep pressing t to see a random word \n from a list",font=("Arial",25,"normal"))
    window.onkey(inranwords,"t")
    window.listen()
    
  
    
def call():
    window.resetscreen()
    def endcall():
        window.resetscreen()
      
      
        window.bgcolor("white")
        
        cursor.penup()
        cursor.setpos(-150,0)
        cursor.write("the call has been ended \n press x to go back to main menu",font=("Arial",25,"normal"))
        cursor.hideturtle()
    window.bgcolor("black")
    cursor.penup()
   

    cursor.color("white")
    cursor.setpos(-340,300)
    cursor.write("press x to move to main menu",font=("Arial",13,"normal"))
    cursor.setpos(0,0)

    name= turtle.textinput("num","please enter the number you wanna dial")
    cursor.setpos(-100,0)
    if(len(name)==7):
        name = "calling... "+name
        cursor.write(name,font=("Arial",25,"normal"))
        cursor.setpos(-50,-200)
        cursor.color("red")
        cursor.write("✆",font=("Arial",75,"normal"))
        cursor.backward(50)
        cursor.setheading(270)
        cursor.forward(20)
        cursor.write("Press E to end call",font=("Arial",25,"normal"))
    else:
        cursor.write("invalid number\nPlease try again by pressing C",font=("Arial",25,"normal"))
   
    window.onkey(endcall,"e")
    window.listen()
def res():
    window.resetscreen()
    
    cursor.penup()
    window.bgcolor("white")
    cursor.speed(10)
    cursor.setpos(-340,300)

    cursor.write("page1/2,press z to move to next page",font=("Arial",13,"normal"))
    cursor.setpos( -320,150)
    cursor.color("green")
    cursor.write('📞',font=("Arial",100,"normal"))

    cursor.left(-90)
    cursor.forward(30)
    cursor.color("black")
    cursor.write('Call\npress c to open ',font=("Arial",20,"bold"))
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("orange")
    cursor.write('☀️',font=("Arial",100,"normal"))
    cursor.left(-90)
    cursor.forward(40)
    cursor.color("black")
    cursor.write('  Weather\npress w to open ',font=("Arial",19,"bold"))
    cursor.backward(20)
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("blue")
    cursor.write('📒',font=("Arial",100,"normal"))
    cursor.left(-90)
    cursor.forward(50)
    cursor.color("black")
    cursor.write('Contact list \npress p to open ',font=("Arial",18,"bold"))

    cursor.setpos(-325,-50)
    cursor.color("lime")
    cursor.write('📅',font=("Arial",100,"normal"))
    cursor.setheading(270)

    cursor.forward(50)
    cursor.color("black")
    cursor.write('Class schedule \npress u to open ',font=("Arial",19,"bold"))
    cursor.backward(30)
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("red")
    cursor.write('🚌',font=("Arial",100,"normal"))
    cursor.left(-90)
    cursor.forward(50)
    cursor.color("black")
    cursor.write('Bus schedule\npress b to open ',font=("Arial",19,"bold"))
    cursor.backward(20)
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("grey")
    cursor.write('⚙️',font=("Arial",100,"normal"))
    cursor.left(-90)
    cursor.forward(50)
    cursor.color("black")
    cursor.write('     Settings\npress s to open ',font=("Arial",19,"bold"))

    cursor.setpos(-325,-250)
    cursor.color("blue")
    cursor.write('🔠',font=("Arial",100,"normal"))
    cursor.setheading(270)
    cursor.forward(50)
    cursor.color("black")
    cursor.write('Word randomizer\npress r to open ',font=("Arial",19,"bold"))
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("black")
    cursor.write('🖩',font=("Arial",150,"normal"))
    cursor.left(-90)
    cursor.forward(20)
    cursor.write('Calculator\npress v to open ',font=("Arial",20,"bold"))
    cursor.backward(40)
    cursor.left(180)
    cursor.forward(20)
    cursor.left(-90)
    cursor.forward(250)
    cursor.color("dodgerblue")
    cursor.write('⬆⬇',font=("Arial",75,"normal"))
    cursor.left(-90)
    cursor.forward(60)
    cursor.color("black")
    cursor.write('Higher or Lower\npress g to open ',font=("Arial",18,"bold"))

def page2():
    window.resetscreen()
    cursor.penup()
    cursor.setpos(-340,300)
    cursor.write("page2/2,press x to move to prev page",font=("Arial",13,"normal"))

    cursor.setpos( -320,150)
    cursor.color("maroon")
    cursor.write('🚗',font=("Arial",100,"normal"))

    cursor.left(-90)
    cursor.forward(65
                   )
    cursor.color("black")
    cursor.write(' Auto interest \n  calculator\npress i to open ',font=("Arial",18,"bold"))






window=turtle.Screen()
cursor = turtle.Turtle()
cursor.penup()
cursor.speed(10)

cursor.setpos(-340,300)
cursor.write("page1/2,press z to move to next page",font=("Arial",13,"normal"))
cursor.setpos( -320,150)
cursor.color("green")
cursor.write('📞',font=("Arial",100,"normal"))

cursor.left(-90)
cursor.forward(30)
cursor.color("black")
cursor.write('Call\npress c to open ',font=("Arial",20,"bold"))
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("orange")
cursor.write('☀️',font=("Arial",100,"normal"))
cursor.left(-90)
cursor.forward(40)
cursor.color("black")
cursor.write('  Weather\npress w to open ',font=("Arial",19,"bold"))
cursor.backward(20)
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("blue")
cursor.write('📒',font=("Arial",100,"normal"))
cursor.left(-90)
cursor.forward(50)
cursor.color("black")
cursor.write('Contact list \npress p to open ',font=("Arial",18,"bold"))

cursor.setpos(-325,-50)
cursor.color("lime")
cursor.write('📅',font=("Arial",100,"normal"))
cursor.setheading(270)

cursor.forward(50)
cursor.color("black")
cursor.write('Class schedule \npress u to open ',font=("Arial",19,"bold"))
cursor.backward(30)
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("red")
cursor.write('🚌',font=("Arial",100,"normal"))
cursor.left(-90)
cursor.forward(50)
cursor.color("black")
cursor.write('Bus schedule\npress b to open ',font=("Arial",19,"bold"))
cursor.backward(20)
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("grey")
cursor.write('⚙️',font=("Arial",100,"normal"))
cursor.left(-90)
cursor.forward(50)
cursor.color("black")
cursor.write('     Settings\npress s to open ',font=("Arial",19,"bold"))

cursor.setpos(-325,-250)
cursor.color("blue")
cursor.write('🔠',font=("Arial",100,"normal"))
cursor.setheading(270)
cursor.forward(50)
cursor.color("black")
cursor.write('Word randomizer\npress r to open ',font=("Arial",19,"bold"))
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("black")
cursor.write('🖩',font=("Arial",150,"normal"))
cursor.left(-90)
cursor.forward(20)
cursor.write('Calculator\npress v to open ',font=("Arial",20,"bold"))
cursor.backward(40)
cursor.left(180)
cursor.forward(20)
cursor.left(-90)
cursor.forward(250)
cursor.color("dodgerblue")
cursor.write('⬆⬇',font=("Arial",75,"normal"))
cursor.left(-90)
cursor.forward(60)
cursor.color("black")
cursor.write('Higher or Lower\npress g to open ',font=("Arial",18,"bold"))




window.onkey(res,"x")
window.onkey(call,"c")
window.onkey(weather,"w")
window.onkey(contact,"p")
window.onkey(schedule,"u")
window.onkey(bus,"b")
window.onkey(settings,"s")
window.onkey(ranwords,"r")
window.onkey(calculator,"v")
window.onkey(game,"g")
window.onkey(carloan,"i")
window.onkey(page2,"z")
window.listen()

window.mainloop()