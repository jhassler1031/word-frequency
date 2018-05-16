
with open("sample2.txt") as infile:
    my_file = infile.read()

#Need to normalize all words in the file (remove numbers and punctuation)

my_file = my_file.lower()

#below is to change periods to spaces so to separate words after next phase of cleanup

my_file = my_file.replace( "." , " ")

#remove remaining punctuation and numbers

x = 0

while x < len(my_file):
    if my_file[x].isalpha() or my_file[x] == " ":
        x += 1
    else:
        y = my_file[x]
        my_file = my_file.replace(y , "")


#turn str my_file into iterable list, then add list items as keys and counter occurances

my_file_list = my_file.split()

word_count = {}

for word in my_file_list:
    if word not in word_count.keys():
        word_count[word] = 0
    word_count[word] += 1

#now have a dictionary of words with the count of how many times they are used

#now need to sort by occurance and print the top 20 words
#source for operator: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import operator

sorted_list = sorted(word_count.items(), key=operator.itemgetter(1), reverse = True)

for item in sorted_list:
    print(item)
    
