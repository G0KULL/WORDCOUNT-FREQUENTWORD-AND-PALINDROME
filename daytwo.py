def read_file(filename):
    try:
        with open(filename,'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print('File not found')
        return ""
    
def word_count(text):
    words = text.split()
    return len(words)

def frequent_words(text,top=5):
    freq ={}
    words = text.lower().split()
    for word in words:
        word = word.strip(',.\(){}[]"!?')
        if word:
            freq[word]=freq.get(word,0)+1
    sort = sorted(freq.items(),key=lambda x:x[1],reverse=True)
    return sort[:top]

def palindrome_count(text):
    words = text.lower().split()
    palindromes = set()
    for word in words:
        word = word.strip('.,\()[]{}"!?')
        if word and word == word[::-1] and len(word)>1:
            palindromes.add(word)
    return list(palindromes)

filename = 'sample.txt'
text = read_file(filename)

print('Total Words :',word_count(text))
print('Frequent words :')
for word,freq in frequent_words(text):
    print(f" -{word}: {freq} Times")

print('Palindrome Words are :')
palindromes = palindrome_count(text)
print(palindromes)