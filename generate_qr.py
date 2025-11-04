import qrcode
import os

# الرابط الذي سيتم توليد رمز QR له
url = "https://8000-ima7y65lfdue6i66nwfke-334c29d9.manusvm.computer/social_links.html"
# مسار حفظ الصورة
file_path = "assets/images/linda_qr_code.png"

# التأكد من وجود مجلد الصور
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# توليد رمز QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# إنشاء الصورة وتلوينها (لون وردي ناعم)
img = qr.make_image(fill_color="#E91E63", back_color="white") # لون وردي ناعم
img.save(file_path)

print(f"QR Code generated and saved to: {file_path}")
