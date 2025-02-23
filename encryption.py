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
