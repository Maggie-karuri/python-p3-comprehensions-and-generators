#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        return []
    else:
        even_numbers = [n for n in num_list if n % 2 == 0] 
    return even_numbers


def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    else:
        add_exclamations = []
        for sentence in sentence_list:
            add_exclamations.append(sentence + '!')
    return add_exclamations

