#Tuple
student_record = ("Seth",20,"Java")
print(student_record)
(name,age,favorite_progamming_lang )= student_record
print(f"{name} \n {age} \n {favorite_progamming_lang} \n")

#set 
hobbies ={"skating","basketball","drawing","basketball"}
print(hobbies)

#Duplicates disappeared because sets cannot have items with the same value.

hobbies.add("swimming")
print(hobbies)

hobbies.remove("skating")
print(hobbies)

#print a final sentence
print(f"My name is {name}. I am {age} years old and I love {favorite_progamming_lang}.")
