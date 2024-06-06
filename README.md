# DHIS2-login-qrcode-generation
# QR Code Generator Documentation

This script generates a QR code containing encoded information such as a server URL, username, and password. The QR code is then saved as an image file. The script utilizes the `qrcode` library in Python.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Overview](#code-overview)
5. [Output](#output)
6. [Author](#author)

## Requirements

- Python 3.x
- `qrcode` library

## Installation

To install the `qrcode` library, use the following command:

```bash
pip install qrcode[pil]
```

## Usage

1. Open the script file.
2. Replace the empty strings for `server_url`, `username`, and `password` with the actual information you want to encode.
3. Run the script.

```bash
python script_name.py
```

This will generate a QR code and save it as an image file named `qrcode.png` in the same directory as the script.

## Code Overview

The script performs the following steps:

1. **Import the `qrcode` Library**: This library is used to create and manipulate QR codes.
   ```python
   import qrcode
   ```

2. **Define the Information to be Encoded**:
   ```python
   server_url = ""
   username = ""
   password = ""
   ```

3. **Combine the Information**: Combine the server URL, username, and password into a single string.
   ```python
   data_to_encode = f"URL: {server_url}\nUsername: {username}\nPassword: {password}"
   ```

4. **Create a QRCode Instance**: Configure the QR code's version, error correction level, box size, and border.
   ```python
   qr = qrcode.QRCode(
       version=1,
       error_correction=qrcode.constants.ERROR_CORRECT_L,
       box_size=10,
       border=4,
   )
   ```

5. **Add Data to the QR Code**: Add the combined information to the QR code.
   ```python
   qr.add_data(data_to_encode)
   qr.make(fit=True)
   ```

6. **Create and Save the QR Code Image**: Generate the QR code image and save it to a file named `qrcode.png`.
   ```python
   img = qr.make_image(fill='black', back_color='white')
   img.save("qrcode.png")
   ```

7. **Print Confirmation**: Print a message indicating that the QR code has been generated and saved.
   ```python
   print("QR code generated and saved under the name 'qrcode.png'.")
   ```

## Output

The script generates a QR code image file named `qrcode.png`. This file contains the encoded server URL, username, and password.

## Author

This script was created by MEISSA RASSOUL SECK.
