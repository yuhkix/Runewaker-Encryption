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