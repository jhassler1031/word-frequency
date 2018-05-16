
with open("sample2.txt") as infile:
    my_file = infile.read()

#Need to normalize all words in the file (remove numbers and punctuation)
my_file = my_file.lower()

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




print(my_file_list)
