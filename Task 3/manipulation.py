# request input in form of a sentence from the user
# save the response in variable str_manip
# calculate and display the length of str_manip
# find the last letter in str_manip sentence
# replace every occurence of the last letter in str_manip with '@'
# print the last three characters backwards
# create a five-letter word that is made up of the first three characters and the last two characters in str_manip

# CODE
# accept input from user
str_manip = input("Please provide a sample sentence: ")

# display the length of str_manip
length_of_sentence = print(len(str_manip))

# get the last letter of the sentence
last_letter = str_manip[-1]
print(last_letter)

# replace all the occurence of the last last letter with "@"
new_sentence = str_manip.replace(last_letter, "@")
print(new_sentence)

# printing the last 3 letters in reverse
last_3_letters = str_manip[:-4:-1]
print(last_3_letters)


# forming a five letter word from the first 3 char and last 2 char
first_3_char = str_manip[:3]
last_2_char = str_manip[-2:]
print(first_3_char)
print(last_2_char)

new_word = first_3_char + last_2_char

print(new_word)

