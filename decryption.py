import cv2

def decrypt_image(image_path, message_length, password):
    img = cv2.imread(image_path)
    
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m, n, z = 0, 0, 0
    message = ""
    
    for i in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

if __name__ == "__main__":
    encrypted_image_path = "encryptedImage.jpg"
    message_length = int(input("Enter the length of the secret message: "))
    password = input("Enter passcode for Decryption: ")
    original_password = input("Enter the original passcode: ")  # Pass the original password from encryption

    if password == original_password:
        decrypted_message = decrypt_image(encrypted_image_path, message_length, password)
        print("Decrypted message:", decrypted_message)
    else:
        print("YOU ARE NOT auth")
