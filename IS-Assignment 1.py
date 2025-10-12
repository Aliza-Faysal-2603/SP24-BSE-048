from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes
key = get_random_bytes(32)        # Make password
nonce = get_random_bytes(8)       # Make unique number
user_text = input("Enter message: ")  # Gets string
message = user_text.encode()          # Convert to bytes for encryption

cipher = Salsa20.new(key=key, nonce=nonce)
secret = cipher.encrypt(message)  # Hide message

cipher = Salsa20.new(key=key, nonce=nonce)
original = cipher.decrypt(secret) # Get back message

print(f"Original: {message}")
print(f"Ciphertext: {secret.hex()}")
print(f"Decrypted text: {original}")
print(f"Works: {message == original}")

# Adversarial Attack: Nonce Reuse!
# Messages with clear differences
msg1 = b"Send  ABC  to X"
msg2 = b"Send  XYZ  to X"

print("Original Messages:")
print("Message 1:", msg1)
print("Message 2:", msg2)
print()

# Encrypt (wrong way)
c1 = Salsa20.new(key=key, nonce=nonce).encrypt(msg1)
c2 = Salsa20.new(key=key, nonce=nonce).encrypt(msg2)

# Attack
xor_result = bytes(a ^ b for a, b in zip(c1, c2))

print("🎯 HACKER'S DISCOVERY:")
print("By XORing both encrypted messages, hacker sees:")
print("XOR Result:", xor_result)
print("As text:", xor_result)
print()

print("📖 HACKER CAN READ:")
print("Where result is 0: Messages are IDENTICAL")
print("Where result not 0: Messages are DIFFERENT")
print()
print("In this case, hacker sees:")
print("- Both messages start with 'Send  '")
print("- Middle part differs (ABC vs XYZ)") 
print("- Both end with '  to X'")
print()
print("✅ Hacker learned the message structure without the key!")