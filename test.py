import re
def remove_punctuation(document):
    document = re.sub(r'[^\w\s]', '', document)
    return document.strip()

def case_folding(document):
    return document.lower()

print(remove_punctuation("Schindler's List"))