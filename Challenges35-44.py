#===================================================================
#--------------------------------E6---------------------------------
#===================================================================


#--------------------------------35---------------------------------
name = str(input('Enter your name please: '))
print((name+' ')*3)


#--------------------------------36---------------------------------
name = str(input('Enter your name please: '))
Num36 = int(input('Enter a number please: '))
print((name+' ')*Num36)


#--------------------------------37---------------------------------
name = str(input('Enter your name please: '))
l1 = list(name)
print(*l1, sep='\n')


#--------------------------------38---------------------------------
name = str(input('Enter your name please: '))
Num38 = int(input('Enter a number please: '))
l1 = list(name)
print(*l1*Num38, sep='\n')


#--------------------------------39---------------------------------
Num39 = int(input('Enter a number between 1 and 12: '))
print ("The Times Table of: ", Num39)    
for count in range(1, 11):      
   print (Num39, 'x', count, '=', Num39 * count)    


#--------------------------------40---------------------------------
Num40 = int(input('Enter a number below 50: '))
for i in reversed( range(Num40 , 51)):
    print(i)

#--------------------------------41---------------------------------
name = str(input('Enter your name please: '))
Num41 = int(input('Enter a number please: '))
if Num41<10:
    print((name+' ')*Num41)
else:
    print('Too high  '*3)
#--------------------------------42---------------------------------
total=0
for i in range(5):
    Num42 = int(input('Enter a number please: '))
    include= str(input('Do you want this number included? ')).lower()
    if include=='yes':
        total+=Num42

print('Total = ', total)


#--------------------------------43---------------------------------
direction = str(input('which direction do you want to count?(up or down) ')).lower()
if direction== 'up':
    Num43 = int(input('Enter the top number please: '))
    for i in range(1,Num43+1):
        print (i)
elif direction=='down':
    Num43 = int(input('Enter below 20 please: '))
    for i in reversed(range(Num43,20+1)):
        print (i)
else:
    print("I don't understand!")


#--------------------------------44---------------------------------
Num44 = int(input('How many people do you want to invite to the party? '))
if Num44<10:
    for i in range(1, Num44+1):
        Name = str(input('Enter the name: '))
        print(Name,'has been invited.')
else:
    print('Too many people!')
    





















