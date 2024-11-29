def is_palindrome(string):
    string=string.lower().replace(" ","")
    return string==string[::-1]
word="radar"
print(f"{word} is a palindrome: {is_palindrome(word)}")

#-----------------------2----------------------------
def count_vowels(string):
    vovels="aeiouAEIOU"
    count=sum(1 for char in string if char in vovels)
    return count
text="Hello World"
print(f"number of vowels in '{text}': {count_vowels(text)}")



def count_vovels(string):
    vowels="aeiouAEIOU"
    count=sum(1 for char in string if char in vowels)
    return count
text="Maaz and Hanzlah are best friends"
print(f"number of vowels are '{text}': {count_vovels(text)}")


def find_longest_word(sentence):
    words=sentence.split()
    longest_word=max(words,key=len)
    return longest_word
sentence="Python is amazing programing language"
print(f"longest_word: {find_longest_word(sentence)}")



def Randikhana():
    name1="Alia"
    price1=200
    name2="shruti"
    price2=140
    print(name1)
    print(price1)
    print(name2)
    print(price2)
Randikhana()