#def search(x,y):
x=list(input('put in a list of numbers:'))
y= int(input('put in a number to search for:'))
for i in x:
    if i==y:
        print('The number exists')
    elif i!= y:
        print('Please try again')
    else:
        break



