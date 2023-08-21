name = " JOHn ."
name=(name.strip().replace(".","").replace(" ","").capitalize())
print(name)
#slice"The Dog Breed is German Shepherd"  to Breed is German
sentense_one = "The Dog Breed is German Shepherd"
sentense= slice(7,-9)
print(sentense_one[sentense])
#"Defeats for the clinton forces, this was her moment of triumph" to 
sentense_two = "Defeats for the clinton forces, this was her moment of triumph"
sentense_three= slice(15,-32)
print(sentense_two[sentense_three])
#split "The lazy; ran so fast; it hit the wall" with semicolon and display the length
sentence_one = "The lazy; ran so fast; it hit the wall"
sentence_two= sentence_one.split(";")
print(sentence_one,len(sentence_one))