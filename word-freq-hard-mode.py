
with open("sample.txt") as infile:
    my_file = infile.read()

my_file = my_file.lower()

my_file = my_file.replace( "." , " ")

x = 0

while x < len(my_file):
    if my_file[x].isalpha() or my_file[x] == " ":
        x += 1
    else:
        y = my_file[x]
        my_file = my_file.replace(y , "")

my_file_list = my_file.split()

#Hard mode req: remove ignored words

ignore_words = ["a" , "able" , "about" , "across" , "after" , "all" , "almost" , "also" , "am" , "among" , "an" , "and" , "any" , "are" , "as" , "at" ,
"be", "because" , "been" , "but" , "by" , "can" , "cannot" , "could" , "dear" , "did" , "do" , "does" , "either" , "else" , "ever" , "every" ,
"for" , "from" , "get" , "got" , "had" , "has" , "have" , "he" , "her" , "hers" , "him" , "his" , "how" , "however" , "i" , "if" , "in" , "into" , "is" ,
"it" , "its" , "just" , "least" , "let" , "like" , "likely" , "may" , "me" , "might" , "most" , "must" , "my" , "neither" , "no" , "nor" ,
"not" , "of" , "off" , "often" , "on" , "only" , "or" , "other" , "our" , "own" , "rather" , "said" , "say" , "says" , "she" , "should" ,
"since" , "so" , "some" , "than" , "that" , "the" , "their" , "them" , "then" , "there" , "these" , "they" , "this" , "tis" , "to" , "too" ,
"twas" , "us" , "wants" , "was" , "we" , "were" , "what" , "when" , "where" , "which" , "while" , "who" , "whom" , "why" , "will" , "with" ,
"would" , "yet" , "you" , "your"]


word_count = {}

for word in my_file_list:
    if word not in word_count.keys() and word not in ignore_words:
        word_count[word] = 0
    elif word in ignore_words:
        word_count[word] = 0
    word_count[word] += 1

#now have a dictionary of words with the count of how many times they are used

#now need to sort by occurance and print the top 20 words
#source for operator: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import operator

sorted_list = sorted(word_count.items(), key=operator.itemgetter(1), reverse = True)

count = 0

#following if statement is in case the txt file has less than 20 words

if len(sorted_list) > 20:
    for count in range(20):
        print(sorted_list[count])
else:
    for item in sorted_list:
        print(item)
