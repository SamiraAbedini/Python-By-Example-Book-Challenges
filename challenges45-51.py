#===================================================================
#--------------------------------E7---------------------------------
#===================================================================


#--------------------------------45---------------------------------
total = 0
while total<=50:
    Num45 = int(input('Enter a number please: '))
    total+= Num45
    print('The total is: ',total)

    
#--------------------------------46---------------------------------
Num46=0
while Num46<=5:
    Num46 = int(input('Enter a number please: '))
    
print('The last number you entered was a ',Num46)


#--------------------------------47---------------------------------
Num47 = int(input('Enter a number please: '))
num47 = int(input('Enter another number please: '))
total= Num47+num47
ask= input('Do you want to add another number? ')
while ask== 'y':
    num = int(input('Enter another number please: '))
    ask= input('Do you want to add another number? ')
    total+=num
print('Total = ',total)


#--------------------------------48---------------------------------
name = str(input('Who do you want to invite to the party?(Enter the name please): '))
print(name,'has now been invited')
ask= str(input('Do you want to invite another one to the party? ')).lower()
count=1
while ask=='yes':
    name = str(input('Who do you want to invite to the party?(Enter the name please: '))
    print(name,'has now been invited')
    count+=1
    ask= str(input('Do you want to invite another one to the party? ')).lower()
    
print(count,'people are comming to the party')


#--------------------------------49---------------------------------
compnum=50
Num49 = int(input('Enter a number please: '))
count=1
while Num49!=compnum:
    if Num49> compnum:
        print('Your guess is too high!')
        Num49 = int(input('Enter a number please: '))
        count+=1
    elif Num49<compnum:
        print('Your guess is too low!')
        Num49 = int(input('Enter a number please: '))
        count+=1

print("well done, You took ",count ,'attempts')


#--------------------------------50---------------------------------
Num50 = int(input('Enter a number between 10 and 20: '))
while Num50>21 or Num50<10:
    if Num50<10:
        print('Too low!')
        Num50 = int(input('Try again: '))
    elif Num50>21:
        print('Too high!')
        Num50 = int(input('Try again: '))
print('Thank you :)')


#--------------------------------51---------------------------------
Num51 = int(input('Enter a number please: '))
print('There are',Num51, 'green bottles hanging on the wall,',
      Num51, 'green bottles hanging on the wall.'," If 1 green bottle sould accidentally fall,")
Num5 =int(input('How many green bottles will be hanging on the wall? '))
while Num5!=Num51-1:
    Num5 =int(input('No, try again! How many green bottles will be hanging on the wall? '))
    
print('There will be ',Num5,'green bottles hanging on the wall!')

