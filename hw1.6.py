#1

def shorter(phrase):
    phrase_dict = phrase.split()
    for i in range(len(phrase_dict)):
        print(phrase_dict[i][0], end = "")

shorter("Кыргызская Республика")  

shorter("Ruby On Rails")

shorter("for Your Interest")


#2

b = {}

def return_amount(phrase):
    a = phrase.lower().split(" ")
    for word in a:
        b[word] = a.count(word)



return_amount("Money, money, money, it's always sunny, in the richmen's world")
print(b)

#3

for char in word:
    if word.count(char) > 1:
        return (word, False)
return (word, True)




#4
n1 = int(input("Введите целое число: "))
 

digit = n1 % 10
n2 = digit
 
n1 = n1 // 10
 
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit
 
print('"Обратное" ему число:', n2)


#5

