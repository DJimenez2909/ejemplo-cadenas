
#concatetation
text1="fundamentos con"
text2="Python"
result = text1+text2
print(result)


name = "duban"
lastName = "Jimenez"
fullName = name+""+lastName
print(fullName)

#formato estring
price=97
text3= f"the price is{price:.2f}dollaers"
print(text3)

#math operartion
text4=f"multiplicacion es {20*59}"
print(text4)
#string capitalice
text5="python es un lemjuage de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)


# string casefold()
title = "Cien Años de Soledad"
titleConvert =title.casefold()
print(titleConvert)

# string center()
fruit = "banana"
textCenter = fruit.center (20,"-")
print(textCenter)


#string count()
title1 ="I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

#string endswith
text6 = "Curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result2)


#string expandtabs

letter = "F\tU\tP"
delattrSpaces = letter.expandtabs(2)
print(letter)

#String find
text7 = "hola, bienvenio a colombia."
result4 = text7.find("bienvenidos")
print(result4)

#funcion title
text8 = "welome to my world"
result5 = text8.title()
print(result5)

# funcion isalnum
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)


#funcion isalpha
letters =" Space X"
result7 = letters.isalpha()
print(result7)

