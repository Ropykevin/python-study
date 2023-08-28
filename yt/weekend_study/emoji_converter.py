# emoji converter with dictionaries
message = input(">")
words = message.split(" ")
emojis ={
    ":)":"happy emoji",
    ":(":"sad emoji"
}
output = ""
for word in words :
    output += emojis.get(word,word)+" "
print(output)
