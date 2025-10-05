a = int(24)
b = int(9)
string = str("")

for i in range(a-2):
    string += "▓"

string = "█"+string+"█"



if b > 1:
    print("█"*a)
if b > 1:
    for i in range(b-2):
        print(string)
else:
    print("█"*a)        
if b > 1:
    print("█"*a)
