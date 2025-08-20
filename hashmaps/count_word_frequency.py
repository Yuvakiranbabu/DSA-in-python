# count word frequency

sample_text="THIS is a TEST this"
word_count = {}

def word_frequency(sample):
    cleaned_word = sample.lower()
    word_list = cleaned_word.split(" ")

    for word in word_list:
        if word in word_count:
            word_count[word] +=1
        
        else:
            word_count[word]=1

    return word_count

print(word_frequency(sample_text))