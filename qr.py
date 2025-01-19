from PIL import Image
import zxing  # ZXing is used for reading QR codes

# Load the image
image_path = "/mnt/data/Ekran görüntüsü 2024-11-05 214512.png"
img = Image.open(image_path)

# Initialize ZXing reader
reader = zxing.BarCodeReader()

# Decode the QR code
result = reader.decode(image_path)
result
