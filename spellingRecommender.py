from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import nltk

nltk.download('words')
from nltk.corpus import words

correct_spelling = words.words()
import pandas as pd

# get input from user

while True:
    txt = input("Type something to test this out: ")
    is_letter = False

    if not txt.isalpha():
        print('Input can consist of alphabetical letters only. Please try again.')
        continue
    else:
        is_letter = True
        break


def clean_text(input_txt, correct_word):
    input_txt = '#' + input_txt
    correct_word = '#' + correct_word
    distance_array = pd.DataFrame(data=0, index=list(input_txt), columns=list(correct_word), dtype=None, copy=False)

    for i in range(len(distance_array.index)):
        distance_array.iloc[i, 0] = i

    for j in range(len(distance_array.columns)):
        distance_array.iloc[0, j] = j

    for i in range(1, len(distance_array.index)):
        for j in range(1, len(distance_array.columns)):
            if j == 0:
                distance_array.iloc[0, j] = i
            elif i == 0:
                distance_array.iloc[i, 0] = j
            else:
                del_dist = distance_array.iloc[i - 1, j] + 1
                ins_dist = distance_array.iloc[i, j - 1] + 1
                sub_dist = distance_array.iloc[i - 1, j - 1] + 0 if distance_array.index[i] == distance_array.columns[
                    j] else distance_array.iloc[i - 1, j - 1] + 2
                distance_array.iloc[i, j] = min(del_dist, ins_dist, sub_dist)

    min_dist = distance_array.iloc[len(distance_array.index) - 1, len(distance_array.columns) - 1]

    return min_dist


current_minimum_distance = 1000
for word in correct_spelling:
    minimum_distance = clean_text(txt, word)
    if minimum_distance < current_minimum_distance:
        current_minimum_distance = minimum_distance
        nearest_word = word

if current_minimum_distance == 0:
    print('your spelling is impeccable! ', nearest_word)
else:
    print('it appears that you might have misspelled your word. The nearest correctly spelled word to your input is: ', nearest_word)



'''

# Note that in version 3, the print() function
# requires the use of parenthesis.
# print("Is this what you just said? ", txt)

# txt = '#' + txt


# examples
distance_array = clean_text('Pantastomina', 'Pantastomina')

print(distance_array)

distance_array = clean_text('Pantastomina', 'pantastomina')

print(distance_array)


print(txt)

for i in txt:
    print(i)

print(list(txt))

for word in correct_spelling:
    print(word)
'''

# distance_array = clean_text('intention', 'execution')

'''

#print(distance_array)
#print(distance_array)
#        print(distance_array)


        for i in input_txt:
            for j in word:
                delete_dist =
        
        

    for (l in X)
    
    delete_dist =
    
for i in distance_array.index:
    for j in distance_array.columns:
        print(distance_array.iloc[i, j])
        
    for i in range(len(distance_array.index)):
        for j in range(len(distance_array.columns)):
            print(i, j)
            print(distance_array.iloc[i,j])            
            
for i in range(len(distance_array.index)):
        for j in range(len(distance_array.columns)):
            if i == 0 and j == 0:
                distance_array.iloc[i,j] = 0
            else:
                del_dist = distance_array.iloc[i - 1, j] + 1
                ins_dist = distance_array.iloc[i, j - 1] + 1
                sub_dist = distance_array.iloc[i - 1, j - 1] + 0 if distance_array.index[i] == distance_array.columns[j] else distance_array.iloc[i - 1, j - 1] + 2             
'''
