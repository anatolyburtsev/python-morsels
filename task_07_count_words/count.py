from collections import Counter


def count_words(text):
    counter = Counter(filter(
        lambda t: str.isalpha(t) or str.isspace(t),
                             text.lower()).split(" "))
    return counter

print(count_words("oh what a day what a lovely day"))