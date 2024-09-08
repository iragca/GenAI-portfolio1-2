def translate(text):
    """
    Translates a given English text into Pig Latin.
    Parameters:
    text (str): The English text to be translated.

    Returns:
    str: The translated text in Pig Latin.
    """
    split = text.split(' ')

    def translate1(split):
        text = split
        vowels = 'aeiou'

        # If the word starts with a consonant and 'qu', move 'qu' to the end and add 'ay'
        if (text[0] not in vowels) and ('qu' in text):
            for letter in text:
                if letter in 'aeio':
                    num = text.find(letter)
                    return text[num:] + text[:num] + 'ay'

        # If the word starts with a vowel or 'x', 'y', 'r', or 't', simply add 'ay'
        if (text[0] in vowels) or (text[:2] in 'xryt'):
            return text + 'ay'

        # If the word starts with a consonant, move the consonant cluster to the end and add 'ay'
        if (text[0] not in vowels):
            for index, letter in enumerate(text):
                if letter in vowels:
                    return text[index:] + text[:index] + 'ay'

        # If the word ends with 'y', move 'y' to the end and add 'ay'
        for index, letter in enumerate(text):
            if letter == 'y':
                return text[index:] + text[:index] + 'ay'

    return_array = []

    for word in split:
        return_array.append(translate1(word))

    return ' '.join(return_array)