class MorseConverter:
    """
    Class that contains the logis to encode/decode morse code
    """
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

        It iterates over each character in the string, uses char_to_morse dictionary to get the corresponding
        morse code and append it to a list. Finally, the encoded string is obtained using join on the list of
        encoded characters

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


if __name__ == '__main__':
    morse = MorseConverter()
    confirmation = 'y'
    while confirmation == 'y':
        input_string = input("Insert the string you want to convert to morse code: ")
        encoded_string = morse.encode(input_string)
        print(f"Morse code: {encoded_string}")
        confirmation = input("Would you like to convert another string [y/n]: ")
