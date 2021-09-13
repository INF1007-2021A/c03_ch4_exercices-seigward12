#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    even_len=None
    if len(string)%2==0:
        even_len=True
    else:
        even_len=False
    return even_len


def remove_third_char(string: str) -> str:
    string_without3=string[:2]+string[3:]
    return string_without3


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_list=list(string)
    verif_w=0
    while verif_w<len(new_list):
        if new_list[verif_w]=="w":
            new_list[verif_w]="z"
        else: 
            verif_w+=1
    creer_liste=0
    new_string=""
    while creer_liste<len(new_list):
        new_string+=new_list[creer_liste]
        creer_liste+=1
    return new_string


def get_nb_char(string: str, char: str) -> int:
    nb_char=0
    for letter in string:
       if (letter==char):
           nb_char+=1
    return nb_char


def get_nb_words(sentence: str) -> int:
    nb_words=1
    for letter in sentence:
        if letter==" ":
            nb_words+=1
    return nb_words


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
