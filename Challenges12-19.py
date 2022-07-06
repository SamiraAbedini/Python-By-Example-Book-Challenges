#===================================================================
#--------------------------------E5---------------------------------
#===================================================================


#--------------------------------12---------------------------------
Num1 = int(input('Enter the first number:'))
Num2 = int(input('Enter the second number:'))
if Num1>Num2:
    print(Num2)
    print(Num1)
else:
        print(Num1)
        print(Num2)


#--------------------------------13---------------------------------
Num3 = int(input('Enter a number that is under 20:'))
if Num3 >= 20 :
    print('Too high!')
else:
    print('Thank you')

    
#--------------------------------14---------------------------------        
Num4 = int(input('Enter a number between 10 and 20(inclusive):'))
if 10 <= Num4 <= 20 :
    print('Thank you')
else:
    print('Incorrect answer!')


#--------------------------------15---------------------------------
Colour = str(input("Enter your favourite colour:")).lower()
if Colour == 'red':
    print("I like red too :)")
else:
    print("I don't like", Colour, "I prefer red")


#--------------------------------16---------------------------------
weather = str(input('Is it raining? ')).lower()
if weather == 'yes':
    wind = str(input('Is it windy? ')).lower()
    if wind=='yes':
        print('It is too windy for an umbrella.')
    else:
            print('Take an umbrella.')
else:
    print('Enjoy your day :)')

    
#--------------------------------17---------------------------------
age = int(input('How old are you? '))
if age >= 18:
    print('You can vote.')
elif age==17:
    print('You can learn to drive.')
elif age==16:
    print('You can buy a lottery ticket.')
elif age<16:
    print('You can go Trick-or-Treating.')


#--------------------------------18---------------------------------
Num18= int(input('Enter a number: '))
if Num18 <10:
    print('Too low.')
elif 10 <= Num18 <= 20:
    print('Correct')
else:
    print('Too high')

    
#--------------------------------19---------------------------------
Num19 = int(input('Enter 1, 2 or 3 please: '))
if Num19 ==1:
    print('Thank you!')
elif Num19==2:
    print('Well done!')
elif Num19==3:
    print('Correct')
else:
    print('Error Message')
