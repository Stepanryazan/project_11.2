def str_title(word):
    """делает все буквы заглавными"""
    return word.upper()

word = str(input())
print(str_title(word))


def word_title(word):
    """делпет первые буквы заглавными"""
    return word.title()


word = str(input())
print(word_title(word))
