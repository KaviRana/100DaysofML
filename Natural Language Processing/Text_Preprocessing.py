import pandas as pd
import re
import string

input_string = "Hello World!"
# Convert the string to lowercase
lowercase_string = input_string.lower()
data = {'text': ['Hello', 'WORLD', 'How', 'Are', 'You']}
df = pd.DataFrame(data)
# Convert the 'text' column to lowercase
df['text'] = df['text'].str.lower()

def remove_html_tags(text):
    pattern = r'<.*?>'
    text_without_tags = re.sub(pattern, '', text)
    return text_without_tags


def remove_urls(text):
    pattern = r'http\S+|www\S+'
    text_without_urls = re.sub(pattern, '', text)
    return text_without_urls

# Create a translation table to remove punctuations
translator = str.maketrans('', '', string.punctuation)
def remove_punctuations(text):
    # Use the translate() method to remove punctuations
    text_without_punctuations = text.translate(translator)

    return text_without_punctuations

chat_dict = {
    "u": "you",
    "2moro": "tomorrow",
    "gr8": "great",
    "lol": "laugh out loud",
    "brb": "be right back",
    # Add more chat words and their meanings as needed
}

def replace_chat_words(text, chat_dict):
    # Split the text into words
    words = text.split()

    # Replace chat words with their full forms using the chat dictionary
    replaced_words = [chat_dict.get(word, word) for word in words]

    # Join the words back into a single string
    replaced_text = " ".join(replaced_words)

    return replaced_text


from textblob import TextBlob


def correct_spelling(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Spelling correction
    corrected_text = blob.correct()

    return str(corrected_text)

"""Stopwords are common words that are often removed during text preprocessing in NLP tasks. They have little value in conveying the overall meaning. 
Removing stopwords can reduce dimensionality and speed up processing, but in some tasks, like sentiment analysis or named entity recognition, 
it may not be suitable as they carry contextual information. The decision to remove stopwords depends on the specific NLP task and language used."""
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


def remove_stopwords(text):
    words = nltk.word_tokenize(text
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
    processed_text = ' '.join(filtered_words)

    return processed_text


import re


def remove_emojis(text):
    # Emoji pattern (matches most common emojis)
    emoji_pattern = re.compile(
        pattern="["
                "\U0001F600-\U0001F64F"  # emoticons
                "\U0001F300-\U0001F5FF"  # symbols & pictographs
                "\U0001F680-\U0001F6FF"  # transport & map symbols
                "\U0001F700-\U0001F77F"  # alchemical symbols
                "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                "\U0001FA00-\U0001FA6F"  # Chess Symbols
                "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                "\U00002702-\U000027B0"  # Dingbats
                "\U000024C2-\U0001F251"  # Enclosed characters
                "]+",
        flags=re.UNICODE,
    )

    # Remove emojis from the text
    processed_text = emoji_pattern.sub(r'', text)

    return processed_text

def replace_emojis_with_sentiment(text):
    # Replace emojis with their corresponding sentiment labels
    def replace_emoji(match):
        emoji_unicode = match.group()
        emoji_text = emoji.demojize(emoji_unicode)
        sentiment_label = emoji_text.replace(":", " ").replace("_", " ")

        return sentiment_label

    processed_text = emoji_pattern.sub(replace_emoji, text)
    return processed_text
"""The process of breaking your text into smaller blocks like sentences , words , characters.
To tokenize a paragraph for text preprocessing, you can use the Natural Language Toolkit (nltk) library in Python. 
The **`nltk`** library provides various tokenizers, including word tokenization and sentence tokenization."""
import nltk
from nltk.tokenize import word_tokenize
# Sample paragraph
paragraph = "Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and human language."

# Tokenize the paragraph into words
tokens = word_tokenize(paragraph)
print(tokens)

"""In linguistics and grammar, inflection refers to the modification of words to convey different grammatical information, such as tense, number, gender, case, person, and mood. Inflectional changes are typically applied to nouns, verbs, adjectives, 
and pronouns to indicate their role in a sentence and to create different forms based on the context. 
Stemming is a natural language processing (NLP) technique used to reduce words to their base or root form, 
known as the "stem," by removing suffixes or prefixes. The resulting stem may not always be a valid word, but 
it represents the core meaning of the word."""
import nltk
from nltk.stem import PorterStemmer

words = ["running", "runs", "runner", "dogs", "cats", "jumping", "jumps"]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
"""Lemmatization is another natural language processing (NLP) technique used to reduce words to their base or dictionary form, known as the "lemma." Unlike stemming, 
lemmatization ensures that the resulting word is a valid word found in the dictionary, making it a more linguistically accurate process."""

import nltk
from nltk.stem import WordNetLemmatizer

# Sample words to be lemmatized
words = ["running", "runs", "runner", "dogs", "cats", "jumping", "jumps"]

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize each word and store the results in a list
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the lemmatized words
print(lemmatized_words)