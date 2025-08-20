str1 = "listen"
str2 = "silent"



def anagram_checker(str1,str2):
    str1dict={}
    str2dict={}
    cleaned_str1=str1.lower()
    cleaned_str2=str2.lower()
    for i in cleaned_str1:
        if i in str1dict:
            str1dict[i]+=1
        else:
            str1dict[i]=1

    for j in cleaned_str2:
        if j in str2dict:
            str2dict[j]+=1
        else:
            str2dict[j]=1

    if str1dict==str2dict:
        return True

    return False

print(anagram_checker(str1,str2))

