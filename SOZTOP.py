import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters , word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter

def play():
    word = get_word()
    word_lettens = set(word)
    user_letters = ""
    print(f"Men {len(word)} xonali son o'yladim. Topa olasizmi?")
    
    while len(word_lettens)>0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"Shu vaqtgacha kiritgan harflaringiz {user_letters}")
            
        letter = input("Xarf kiriting: ").upper()
        if letter in user_letters:
            print("bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue
        elif letter in word:
            word_lettens.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("Bunday harf yo'q.")
        user_letters += letter
    print(f"Tabriklayman {word} so'zini {user_letters} ta urinish bilan toptingiz !")
    
play()
    
        