import requests
from io import BytesIO
from PIL import Image

image_url = "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg"
r = requests.get(image_url)

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save the image.")