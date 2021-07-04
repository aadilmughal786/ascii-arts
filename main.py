from  ascii_magic  import from_image_file,to_terminal,Modes
from art import tprint

tprint("ASCI","alpha")
tprint("    by : Aadil","red_phoenix")

print("\t\t+-------------------------------------------+")
print("\t\t| WAELCOME TO  ASCII MAGIC ∎∎∎∎∎∎∎∎∎        |")
print("\t\t|       ∎∎∎∎∎∎∎∎∎ made by Aadil Mugal       |")
print("\t\t|       ∎∎∎∎∎∎∎∎∎ version V1.0-1            |")
print("\t\t+-------------------------------------------+")

print("\t\t1. Convert text to ASCII/")
print("\t\t2. Convert photo to ASCII/")

while True:
    try:
        flag1 = int(input("\t\tchoose a option : "))
        if flag1 in [1,2]:
            break
        else:
            print("\t\t\aERROR not a valid choice")
    except:
        print("\t\t\aERROR not a valid choice")


if flag1==1:
    text = input("\t\tEnter your text : ")
    tprint(text,font='random')
    while 1:
        try:
            flag2 = input("\t\tDo you want to more styles(Y/N) : ")
            if flag2 in ['Y',"n","N","y"]:
                if flag2 in ["y","Y"]:
                    tprint(text,font='random')
                else:
                    print("\n\n\t\tHave a nice day\n\t\tthanks for try my program\n\n")
                    break
                        
            else:
                print("\t\t\aERROR not a valid choice")
        except:
            print("\t\t\aERROR not a valid choice")



if flag1==2:
    pathh = input("\t\tEnter the path to photo : ")
    output = from_image_file(pathh,columns = 400,width_ratio=2,char = "#")
    to_terminal(output)
    
    



