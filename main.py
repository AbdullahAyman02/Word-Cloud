import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import ipywidgets


def calculate_frequencies(string):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "in", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "not", "on", "so", "for",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    string = string.translate({ord(letter): None for letter in punctuations})
    words = string.split()
    frequencies = {}
    for word in words:
        lower_word = word.lower()
        if lower_word not in uninteresting_words and lower_word.isalpha():
            if lower_word not in frequencies:
                frequencies[lower_word] = 1
            else:
                frequencies[lower_word] += 1
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("image.jpg")
    return cloud.to_array()


with open("C:/Users/Abdullah/Desktop/Pride and Prejudice by Jane Austen (1555).txt", 'r', encoding='utf8') as f:
    file_contents = f.read()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
