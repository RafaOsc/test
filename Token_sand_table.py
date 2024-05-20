#import numpy as np
dir = input(" Enter the dir of file :")
try:
    file = open(dir, "r")
    list_command = []
    for line in file:
        position = ""    
        if(line[0]=='G'):
            for n in range(4,len(line)):
                if(line[n].isdigit() or line[n]=='.'):
                    position+=line[n]
                else:
                    if(len(position)>0):
                       list_command.append(float(position))
                    position=""

    print("{",end="")
    count = 1
    for element in  list_command:
        print(int(element),end="")
        if(count != len(list_command)):
            if(count%2==0):
                print(",")
            else:
                print(",",end="")
        else:
            print("};")
        count+=1       
except:
    print("Directory not valid")
