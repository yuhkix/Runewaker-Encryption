from utility.util import clear_console, watermark, clipboard
from utility.xor import encode, decode

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