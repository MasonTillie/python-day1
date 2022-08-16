num = int(input('1000'))
for i in range(1, num+1):
    print('Number is :' ,i, 'Cube is :' ,(i**3) )


        
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
            if(count==2):
                print(i,end=' ')