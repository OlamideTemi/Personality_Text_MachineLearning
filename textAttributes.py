##Written in python 3

#Standard count
def word_count(string):
    tokens = string.split()
    n_tokens = len(tokens)
    return n_tokens

def avg_words_sentence(string):
    my_list = string.split()
    terminals= set([",","!","?"])
    terminal count = 0
    for item in mylist:
        #for w in item: if w in terminals
        if item in terminals:
            terminal_count +=1

    avg = len(my_list)/float(terminal_count)
    return avg

def greater_than_six(string):
    words = string.split()
    six_count = 0
    for w in words:
        letter_count = len(w)
        if letter_count > 6:
            six_count += 1
    return six_count

def negations:
    words = string.split()
    negating = set(["not","n't"])
    negated_words = 0
    for items in words:
        if item in negating:
            negated_words += 1
   return negated_words 

def articles:
    words = string.split()
    article = set(["a","an","the"])
    number_articles = 0
    for items in words:
        if item in article:
            number_articles += 1
   return number_articles

def numbers:
    mylist = string.split()
    new_list = []
    for value in my_list:
        try:
            new_list.append(int(value))
        except ValueError:
            continue
    number_of_numbers = len(new_list)
    return number_of_numbers
