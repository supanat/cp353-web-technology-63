import requests
import base64
import argparse

parser = argparse.ArgumentParser(description="Predict a label for an image.")
parser.add_argument("key", help="Key")
parser.add_argument("image", help="Path to your image file.")
args = parser.parse_args()

image_key = args.key
file_name = args.image

with open(file_name, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')

url = 'http://127.0.0.1:5000/classify'
body = {'key': image_key,'base64': base64_message}

prediction = requests.post(url, json = body)

#print("prediction : ", prediction.json())
print("prediction : ",prediction.json()['predictions'][0]['label'])
print("confidence : ",prediction.json()['predictions'][0]['confidence'])
