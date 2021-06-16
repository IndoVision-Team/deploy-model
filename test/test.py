import requests

# API endpoint
API_ENDPOINT = "http://127.0.0.1:5000/"
# image path
IMAGE_PATH = "test/tas.jpg"

resp = requests.post(url = API_ENDPOINT, files={'file': open(IMAGE_PATH, 'rb')})

print(resp.json())










# import base64

# with open('test/lamp.JPG', "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())

# base64_decoded = base64.b64decode(encoded_string)
# im_file = BytesIO(base64_decoded)
# img = Image.open(im_file)


# resp = requests.post("http://127.0.0.1:5000/", files={'file': open(img, 'rb')})

# print(resp.json())

# filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
# with open(filename, 'wb') as f:
#         f.write(base64_decoded)