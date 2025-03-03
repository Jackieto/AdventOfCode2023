
input = open("./inputs/day1")

#Assuming theres only 2 digits per line
total = 0
numbers = []

for line in input:
    number = ""
    count = 0
    
    first = ""
    second = ""
    for char in line:
        #first digit
        if char.isdigit() and count == 0:
           #print(char)
            first = char
            number += first
            count += 1
            continue
            
        
        #second digit
        if char.isdigit() and count != 0:
          # print("Second: ",char)
            second = char         
        
    
    #If theres only 1 digit in line it repeats
    if second == "":
        number += first
        #rint("Last line: " + number)
    
           
    number += second
    numbers.append(int(number))
  


for n in numbers:
    total += n

    
print(total)