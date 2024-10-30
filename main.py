from utility.util import clear_console, watermark, clipboard

def encode(password: str, key: str) -> str:
    """Encode password using XOR with the provided key."""
    return ''.join(f"{ord(password[i]) ^ ord(key[(i + 1) % len(key)]):02x}" for i in range(len(password)))

def get_hex(hex_str: str) -> int:
    """Convert a 2-character hex string to its integer value."""
    return int(hex_str, 16)

def decode(encoded_password: str, key: str) -> str:
    """Decode encoded password using XOR with the provided key."""
    decoded_chars = []
    key_len = len(key)
    for i in range(0, len(encoded_password), 2):
        value = int(encoded_password[i:i + 2], 16)
        decoded_char = chr(value ^ ord(key[(i // 2 + 1) % key_len]))
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)

while True:
    clear_console()
    watermark()

    print("\nSelect an option:")
    print(f"1. Encode password")
    print(f"2. Decode password")
    print(f"3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        clear_console()
        watermark()
        password = input("Enter the password to encode: ")
        key = input("Enter the key: ")
        encoded_password = encode(password, key)
        clipboard(encoded_password)
        input("\nPress Enter to continue...")
    elif choice == "2":
        clear_console()
        watermark()
        encoded_password = input("Enter the encoded password to decode: ")
        key = input("Enter the key: ")
        decoded_password = decode(encoded_password, key)
        clipboard(decoded_password)
        input("\nPress Enter to continue...")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")