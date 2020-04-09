message=input(">")
wors=message.split(' ') # bu split mehod kiritgan  belgilarimizni alohida listga olib beradi
emojies={
    ":)":":)",
    ":(":":("
}
output=""
for word in wors:
    output+= emojies.get(word,word)+" "
print(output)