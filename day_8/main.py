alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def caesar(text, shift, direction):
    final_word = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        if direction == "encode":
            shift_letter = letter_index + shift
        elif direction == "decode":
            shift_letter = letter_index - shift
        else:
            print("Wrong command!")
            break

        final_word += alphabet[shift_letter]
    print(f"The {direction}d text is {final_word}")


caesar(text, shift, direction)
