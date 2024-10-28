def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text: The message to be encrypted or decrypted.
        shift: The number of positions to shift the letters.
        mode: The operation to perform ('encrypt' or 'decrypt').

    Returns:
        The encrypted or decrypted message.
    """

    shift %= 26  # Ensure shift is within 0-25

    if mode == 'decrypt':
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():
            # Calculate the shifted character's ASCII code
            shifted_code = ord(char) + shift
            if char.isupper():
                shifted_code = (shifted_code - 65) % 26 + 65
            else:
                shifted_code = (shifted_code - 97) % 26 + 97
            result += chr(shifted_code)
        else:
            result += char

    return result


# Get user input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value (1-25): "))
operation = input("Do you want to encrypt (e) or decrypt (d) the message? ").lower()

# Validate user input
if operation not in ['e', 'd']:
    print("Invalid operation. Please choose 'e' for encrypt or 'd' for decrypt.")
elif shift_value < 1 or shift_value > 25:
    print("Invalid shift value. Please enter a number between 1 and 25.")
else:
    # Perform the operation
    mode = 'encrypt' if operation == 'e' else 'decrypt'
    output_message = caesar_cipher(message, shift_value, mode=mode)
    print(f"The {mode}ed message is: {output_message}")