import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

text = "Привіт, Світ!"
hash_object = hashlib.sha256(text.encode())
hex_dig = hash_object.hexdigest()

print(f"Оригінальний текст: {text}")
print(f"SHA-256 Геш: {hex_dig}")

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted_text = cipher.encrypt(text.encode())
decrypted_text = cipher.decrypt(encrypted_text).decode()

print(f"\nСиметричний ключ: {key}")
print(f"Зашифровано: {encrypted_text}")
print(f"Розшифровано: {decrypted_text}")

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

signature = private_key.sign(
    text.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(f"\nRSA Підпис (hex): {signature.hex()}")

try:
    public_key.verify(
        signature,
        text.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Перевірка підпису: Успішно")
except Exception as e:
    print("Перевірка підпису: Невдало")

print("\n--- Різниця між гешуванням і шифруванням ---")
print("Гешування - це односторонній процес (незворотний), який використовується для перевірки цілісності даних.")
print("Шифрування - це двосторонній процес (зворотний за допомогою ключа), який використовується для захисту конфіденційності даних.")