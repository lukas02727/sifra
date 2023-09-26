import string


def ceasar_cypher(word, key):
    
    def move_char(char, move):
        char_code = ord(char.lower())
        char_code_moved = (char_code - 97 + move) % 26 + 97 
        char_new = chr(char_code_moved)
   
        return char_new


    cypher_text = ""
    for char in word:
        cypher_text += move_char(char, key)
        
    return cypher_text


def main():
    while True:
        is_wrong_word = False
        word = input("Zadej slovo k zašifrování: ")
        
        for char in word:
            if char not in string.ascii_letters:
                is_wrong_word = True
                break
            
        if is_wrong_word:
            print("Zadal jsi špatné znaky")
            continue
        else:
            break
        
    while True:
        try:
            key = int(input("Zadej klíč k posunutí: "))
            break
        except ValueError:
            print("Musíš zadat číslo")
           
        
    print(ceasar_cypher(word, key))
    
main()