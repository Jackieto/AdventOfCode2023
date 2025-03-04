
input = open("./inputs/day1")



def w2n(number):
    words = [ "zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten"]
    for i in words:
        number = number.replace(i, str(words.index(i)))
    return number


def computeNumber(tuples):
    
    #first number should be first min item sorted by index, second number max item 
    
    
    first_tuple = min(tuples,key=lambda x: x[1])
    first = w2n(first_tuple[0])
    
    
    second_tuple = max(tuples,key=lambda x: x[1])
    second = w2n(second_tuple[0])
    
    number = first + second
    #print("Numero: ",number)
    return int(number)    
    

numbers = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]

total = 0

for line in input:
    
    tuples = []
    
    for number in numbers:
        index = line.find(number)
        if(index != -1):
            number_index = (number, index)
            tuples.append(number_index)
        
    number = computeNumber(tuples)
    total += number
    
      
print(total)


"""PART ONE
for line in input:
    number = ""
    count = 0
    
    index = 0
    
    first = ""
    second = ""
    for char in line:
        #first digit
        if char.isdigit() and count == 0:
           #print(char)
            first = char
            number += first
            count += 1
            index += 1
            continue
            
        
        #second digit
        if char.isdigit() and count != 0:
          # print("Second: ",char)
            second = char
            index += 1
            continue
        index += 1         
        
    
    #If theres only 1 digit in line it repeats
    if second == "":
        number += first
        #rint("Last line: " + number)
    
           
    number += second
    numbers.append(int(number))
  


for n in numbers:
    total += n

    
print(total)
"""