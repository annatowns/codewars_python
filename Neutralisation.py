#Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:
#When positives and positives interact, they remain positive.
#When negatives and negatives interact, they remain negative.
#But when negatives and positives interact, they become neutral, and are shown as the number 0.



def neutralise(s1, s2):
    #index the parameters above
    #set a loop going and compare entry point 1 with entry point 2
    #within the loop set ifs for each outcome and each needs a separate return
    comparison = len(s1)
    current_character_index = 0
    list = []
    while current_character_index < comparison:
        string_one= s1[current_character_index]
        string_two= s2[current_character_index]
        if string_one != string_two:
            list.append(0)
        else:
            list.append(string_one)
        current_character_index = current_character_index+1
    return"".join(map(str, list))
