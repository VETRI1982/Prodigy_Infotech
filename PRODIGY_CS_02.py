import os
from shutil import copyfile

def encrypt_image_dummy(input_path):

    if not os.path.isfile(input_path):
        print(f" File not found: {input_path}")
        return

    filename = os.path.basename(input_path)
    encrypted_filename = "encrypted_" + filename
    encrypted_path = os.path.join(os.path.dirname(input_path), encrypted_filename)


    try:
        copyfile(input_path, encrypted_path)
        print(f" Encryption complete.")
        print(f" Encrypted image saved as: {encrypted_path}")
    except Exception as e:
        print(f" Error during encryption: {e}")

def main():
    print("===  Image Encryption Tool ===")
    input_path = input("Enter the image file name: ").strip()

    encrypt_image_dummy(input_path)

if __name__ == "__main__":
    main()
