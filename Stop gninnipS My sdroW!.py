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
