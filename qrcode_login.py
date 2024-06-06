import qrcode
# Information to be encoded in the QR code
# by MEISSA RASSOUL SECK
server_url = ""
username = ""
password = ""
# Combine information in a single channel
data_to_encode = f"URL: {server_url}\nUsername: {username}\nPassword: {password}"
# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# Add data to the QR code
qr.add_data(data_to_encode)
qr.make(fit=True)
# Créez une image du QR code
img = qr.make_image(fill='black', back_color='white')
# Sauvegardez l'image dans un fichier
img.save("qrcode.png")
print("QR code generated and saved under the name 'qrcode.png'.")
