import qrcode
import pyotp

def gen_qrcode(username, secret_key):
    totp = pyotp.TOTP(secret_key)
    qrcode_data = totp.provisioning_uri(name=username, issuer_name='OW HPC')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2,
    )
    qr.add_data(qrcode_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="green")
    img.save("qrcode_"+username+".png")

secret_key = pyotp.random_base32()
print(secret_key)
gen_qrcode("username",secret_key)