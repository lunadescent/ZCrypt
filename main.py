def generate_key():
    import os

    key = os.urandom(256)
    with open("key.zcr", "wb") as key_file:
        key_file.write(key)
    print("Encryption key was generated.")

def encrypt_file(file_path, key):
    import os

    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = bytearray()

    for i in range(len(file_data)):
        encrypted_byte = file_data[i] ^ key[i % len(key)]
        encrypted_data.append(encrypted_byte)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print("File encrypted successfully.")

def decrypt_file(file_path, key):
    import os

    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = bytearray()

    for i in range(len(encrypted_data)):
        decrypted_byte = encrypted_data[i] ^ key[i % len(key)]
        decrypted_data.append(decrypted_byte)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully.")

def main():
    while True:
        print("	ZCrypt\n")
        print("1. Generate encryption key")
        print("2. Encrypt file")
        print("3. Decrypt file")
        print("4. Help")
        choice = input("\n=> ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_path = input("Enter file path: ")
            key_file_path = "key.zcr"
            #Using defolt key.zcr to encrypt
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
            encrypt_file(file_path, key)
        elif choice == "3":
            file_path = input("Enter file path: ")
            key_file_path = input("Enter key file path: ")
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
            decrypt_file(file_path, key)
        elif choice == "4":
            print("\n<-------------\nAvalable functions:\n\nEncoding and Decoding.\nTo encrypt a file, firstly create a encrypt key using option 1. Decrypting is possible only with generated key.\n\nGithub: @BotHerbert\n-------------->\n\n")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()