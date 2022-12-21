"""
Project: Word Replacement
Author: Krystella Rattan
"""

def replace_word():
    str = "hi, this is my first time here in VS Code"
    word_to_replace = input ("Enter the word to be replaced: ")
    replacement = input ("Enter the word you would like to replace it with: ")
    print(str.replace(word_to_replace, replacement))
replace_word()