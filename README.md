Steganography Project : 
This project demonstrates a simple approach to steganography using image encryption and decryption with Python.

Overview : 
Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. In this project, we use Python to hide a secret message inside an image and then retrieve it using decryption.

Features : 
Image Encryption: Embeds a secret message inside an image.
Image Decryption: Retrieves the secret message from the encrypted image.

Requirements
Python 3.x,
OpenCV,
OS module

Setup
1. Clone the repository:
git clone https://github.com/yourusername/steganography-project.git
cd steganography-project

2. Install the required dependencies:
pip install opencv-python

Usage
Encryption
To encrypt a message into an image:

1. Ensure the image is in the same directory as your script.
2. Run the encrypt_image.py script and follow the prompts:

python encrypt_image.py

3. Enter the secret message and a passcode. The encrypted image will be saved as encryptedImage.jpg.

Sample Code:
import cv2
import os
def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    d = {}
    for i in range(255):
        d[chr(i)] = i

    m, n, z = 0, 0, 0
    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    os.system(f"start {encrypted_image_path}")  # Use 'start' to open the image on Windows
    return encrypted_image_path

if __name__ == "__main__":
    image_path = "mypic.jpg"  # Replace with the correct image path
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(image_path, message, password)

    Decryption
To decrypt a message from an encrypted image:

1. Ensure the encrypted image (encryptedImage.jpg) is in the same directory as your script.
2. Run the decrypt_image.py script and follow the prompts:

python decrypt_image.py
Enter the length of the secret message and the passcode. If the passcode is correct, the decrypted message will be displayed.

Sample Code:

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
        
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to submit a pull request.
