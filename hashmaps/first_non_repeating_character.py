#first non repeating character

word = 'aabbccddeffg'

def first_non_repeat(word):
    dup_check={}
    for i in word:
        if i in dup_check:
            dup_check[i]+=1

        else:
            dup_check[i]=1

    for key,value in dup_check.items():
        if value == 1:
            return key
        
print(first_non_repeat(word))