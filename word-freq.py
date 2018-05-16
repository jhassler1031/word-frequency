
with open("sample2.txt") as infile:
    my_file = infile.read()

#Need to normalize all words in the file (remove numbers and punctuation)

my_file = my_file.lower()

x = 0

while x < len(my_file):
    if my_file[x].isalpha() or my_file[x] == " ":
        x += 1
    else:
        y = my_file[x]
        my_file = my_file.replace(y , "")

#below is what was originally used for cleanup
"""

my_file_list = my_file.split()

index_counter = 0

while index_counter < len(my_file_list):
    x = 0
    word = my_file_list[index_counter]
    while x < len(word):
        if word[x].isalpha():
            x += 1
        else:
            y = word[x]
            word = word.replace(y , "")
    my_file_list[index_counter] = word
    index_counter += 1
"""

#var my_file should be clean at this point

#turn str my_file into iterable list, then add list items as keys and counter occurances

my_file_list = my_file.split()

word_count = {}

for word in my_file_list:
    if word not in word_count.keys():
        word_count[word] = 0
    word_count[word] += 1

print(word_count)
