def print_words_with_even_length(input_string):

    words = input_string.split()
    

    for word in words:
    
        if len(word) % 2 == 0:
            print(word)

input_string = "mike tyson"
print("Words with even length:")
print_words_with_even_length(input_string)
