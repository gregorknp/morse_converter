class MorseConverter:
    """
    Class that contains the logis to encode/decode morse code

    Methods
    -------
    encode:
        Method that encodes a human readable string into morse code.

    decode:
        Method that decodes a morse encoded string to get the original human readable string

    Attributes
    ----------
    char_to_morse:
        Dictionary that associates human readable symbols with it's corresponding morse code

    """

    # Dictionary that associates human readable symbols with it's corresponding morse code
    char_to_morse = {  # standard letters
                      'a': "·-", 'b': "-···", 'c': "-·-·", 'd': "-··", 'e': "·", 'f': "··-·", 'g': "--·", 'h': "····",
                      'i': "··", 'j': "·---", 'k': "-·-", 'l': "·-··", 'm': "--", 'n': "-.", 'o': "---", 'p': "·--·",
                      'q': "--·-", 'r': "·-·", 's': "···", 't': "-", 'u': "··-", 'v': "···-", 'w': "·--", 'x': "-··-",
                      'y': "-·--", 'z': "--··",
                      # numbers
                      '1': "·----", '2': "··---", '3': "···--", '4': "···-", '5': "·····", '6': "-····", '7': "--···",
                      '8': "---··", '9': "----·", '0': "-----",
                      # punctuation
                      ',': "--··--", '?': "··--··", ':': "---···", '-': "-····-", '"': "·-··-·", '(': "-·--·",
                      '=': "-···-", '.': "·-·-·-", ';': "-·-·-·", '/': "-··-·", "'": "·----·", '_': "··--·-",
                      ')': "-·--·-", '+': "·-·-·", '@': "·--·-·", " ": "······"
    }

    def encode(self, string_to_encode):
        """
        Method that encodes a human readable string into morse code.

        It iterates over each character in the string, uses char_to_morse dictionary to get its corresponding
        morse code and append it to a list. Finally, the encoded string is obtained using join on the list of
        encoded characters.

        Note. If the character being endoded does not exist in the dictionary it is ignored and the final encoded
        string is not modified.

        :param string_to_encode: Input string
        :return: Encoded string
        """
        list_encoded_chars = []
        for char in string_to_encode:
            try:
                list_encoded_chars.append(self.char_to_morse[char.lower()])
            except KeyError:
                continue

        return " ".join(list_encoded_chars)

    def decode(self, morse_string):
        """
        Method that decodes a morse encoded string to get the original human readable string

        Iterates over the morse encoded string and for each morse encoded character gets its corresponding human
        readable character.

        To get the dictionary key from the value, it first gets the position of the value in the dictionary and uses it
        to index the list of keys.

        :param morse_string: Morse encoded string
        :return: Original string in human readable format
        """
        encoded_list = morse_string.split(" ")
        decoded_string = []
        for encoded_char in encoded_list:
            decoded_string.append(list(self.char_to_morse.keys())[list(self.char_to_morse.values()).index(encoded_char)])

        return "".join(decoded_string)


if __name__ == '__main__':
    morse = MorseConverter()
    confirmation = 'y'
    while confirmation == 'y':
        input_string = input("Insert the string you want to convert to morse code: ")
        encoded_string = morse.encode(input_string)
        print(f"Morse code: {encoded_string}")
        confirmation = input("Would you like to convert another string [y/n]: ")
