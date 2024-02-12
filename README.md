
# Encryption and Decryption Scripts: Caesar Cipher

This repository contains Python scripts for simple text encryption and decryption using a basic Caesar cipher. These scripts can be used to understand the basics of network security and cryptography.

## Introduction

The encryption script (`encryption.py`) takes a plaintext input and encrypts it using a predefined key, while the decryption script (`decryption.py`) reverses the process, converting the encrypted message back to its original form. This process utilizes a simple encryption formula based on shifting alphabet characters by a fixed number.

## Installation

No additional libraries are required to run these scripts beyond the Python standard library. Ensure you have Python installed on your system (Python 3.x is recommended).

## Usage

To use these scripts, follow the steps below for each script.

### Encryption

1. Open your terminal or command prompt.
2. Navigate to the directory containing `encryption.py`.
3. Run the script using Python with the following command:
   ```
   python encryption.py
   ```
   By default, the script will encrypt the phrase "network security and cryptography." You can modify the `textToEncrypt` variable in the script to encrypt a different phrase.

### Decryption

1. Follow the same steps as above but with `decryption.py`.
2. By default, the script will decrypt the phrase "qhwzrunbvhfxulw.bdqgbfu.swrjudsk.c". You can modify the `textToDecrypt` variable in the script to decrypt a different phrase.

## Examples

- Encrypting "network security and cryptography." will produce:
  ```
  textToEncrypt : network security and cryptography.
  encryptedText : qhwzrunbvhfxulw.bdqgbfu.swrjudsk.c
  ```

- Decrypting "qhwzrunbvhfxulw.bdqgbfu.swrjudsk.c" will produce:
  ```
  textToDecrypt : qhwzrunbvhfxulw.bdqgbfu.swrjudsk.c
  decryptedText : network security and cryptography.
  ```

## Contributing

Feel free to fork this repository and submit pull requests with improvements or fixes.
