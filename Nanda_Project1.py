### Python Project #1
## Nandakumar Balakrishnan
import time

# Creating an empty dictionary
word_dict = dict()

#Function to read files
def read_file(fileName): 
    file = open(fileName,"r")
    return (file.read())

#Funtion to strip key (Word) and values (Nouns/ Verb/ Adverb/ Adjective) and assign to dictionary
#Checks for empty words and multilevel n grams and removes them

def insert_data(word_dict, files, type):

    ### USING SORTING INSTEAD OF PERMUTATION of one word since it is a MORE EFFICIENT methodology for this case.
    # The words are sorted, converted to uppercase and stored as keys in dictionary, along with the values being its original word and word type.
    for line in files:
        
        if '_' not in line:
            word, _ = line.split('|')
            
            # Coverting entered word to upper case.
            if not (word.isspace()):
                sorted_word = (''.join(sorted(word))).upper()
                
                if sorted_word in word_dict:
                    (word_dict[sorted_word]).append([word,type])
                else:
                    word_dict[sorted_word] = [[word,type]]
                    
                    
def find_word(jumbled_word,word_dict):
    return(word_dict.get(''.join(sorted(jumbled_word))))



#Reading the files
nouns_split = read_file("NounsIndex.txt").split()
verbs_split = read_file("VerbsIndex.txt").split()
adj_split   = read_file("AdjIndex.txt").split()
adv_split   = read_file("AdvIndex.txt").split()

#Inserting the data inside the dictionary
insert_data(word_dict, nouns_split, "Noun")
insert_data(word_dict, verbs_split, "Verb")
insert_data(word_dict, adj_split, "Adjective")
insert_data(word_dict, adv_split, "Adverb")

# Entering a loop to get the jumbled word from user and process the word without having to create the dictionary again
while True:

    # Lower casing the entered jumble word
    jumbled_word = (input("Enter the Jumble Puzzle Word: (<enter> to quit) ")).upper()

    # Exits loop if no word is entered
    if jumbled_word == "":
        break

    print("Start time: " + time.strftime("%H:%M:%S", time.localtime()))
    
    answers = find_word(jumbled_word,word_dict)

    # If word is found, print out the results
    if answers is not None:    
        for ans in answers:
            print(str(ans[0]).upper() + " " + str(ans[1]).upper())
    else:
        print("<<Not found>>")

    print("Finish time: " + time.strftime("%H:%M:%S", time.localtime()))
    print()



