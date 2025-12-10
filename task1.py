import re

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("1. Все конструкции'Fig. #':")
    pattern1 = r'(?:Fig\.)\s*\d+'
    matches1 = re.findall(pattern1, content, re.IGNORECASE)
    
    for match in matches1:
        print(f"  - {match}")
    pattern2 = r'\b[A-Za-z]{4}\b'
    matches2 = re.findall(pattern2, content)
    unique_words = sorted(set(matches2))
    
    for word in unique_words:
        print(f"  - {word}")
    print(f"\nCлов из 4 букв: {len(unique_words)}")
    return matches1, unique_words

figures, four_letter_words = process_file('task1-en.txt')