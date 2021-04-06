from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import os
import io
import base64
from ml_model import TFModel
from PIL import Image

model = TFModel(model_dir='./ml-model/')
model.load()

app = Flask(__name__)

api = Api(app,version='1.0.0', title='Cat | Dog',
    description='Cat and Dog Image Classification Service')

img_input = api.model('Image', {
    'key': fields.String(required=True, description='key'),
    'base64': fields.String(required=True, description='base64 string')
})


@api.route('/classify')
class Classification(Resource):

    @api.expect(img_input)
    def post(self):

        key_string = api.payload['key']
        img_string = api.payload['base64']

        imgdata = base64.b64decode(img_string)
 
        image_temp = Image.open(io.BytesIO(imgdata))

        outputs = model.predict(image_temp)

        outputs['key'] = key_string

        return jsonify(outputs)

