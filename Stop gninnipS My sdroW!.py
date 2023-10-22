#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. 
#Spaces will be included only when more than one word is present.

def spin_words(sentence):
    initial_words = sentence.split()
    final_reversed_words = []
    for word in initial_words:
        word_count = len(word)
        if word_count >= 5 :
            reversed_word= word[::-1]
            final_reversed_words.append(reversed_word)
        else:
            final_reversed_words.append(word)
    final_string= " ".join(final_reversed_words)      
    return final_string  
