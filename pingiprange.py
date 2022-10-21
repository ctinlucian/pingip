import os

address = input("Enter Ip address:") 
range1 = input("Enter your start range:")
range2 = input("Enter your end range:")

for ip in range(int(range1),int(range2)+1):
        Hosts = address + str(ip)
        response = os.system("ping -c 1 -w 1" + Hosts + ">/dev/null")
        if response == 0:
                with open("foundIps.txt" , "a") as myFile:
                        myFile.write(Hosts + "is alive\n")
                
        
