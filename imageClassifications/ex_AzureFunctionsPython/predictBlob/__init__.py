import logging
import json
import numpy as np
import io
from PIL import Image
import time

import tensorflow as tf
import azure.functions as func

# your model labels array
labels = ['apple', 'orange', 'banana']

# Your models locations
loaded_model = tf.keras.models.load_model("./models/YOUR_MODEL_NAME.h5")

# Your original training models input size
image_size = 240

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        satrt_time = time.time()

        # In azure, we suggest you to use logging.info rather than print()
        logging.info('Python HTTP trigger function processed a request.')

        message = req.get_json()
        image_raw = message.get('data')

        # Raw uint8 images
        arr_image = np.array([ image_raw[v] for v in image_raw ], dtype="uint8")

        # PLI array images
        pli_image = np.array(Image.open(io.BytesIO(arr_image))) 
        data = Image.fromarray(pli_image)
        data = data.resize( (image_size,image_size) )

        # Images to tensor
        input_arr = tf.keras.preprocessing.image.img_to_array(data)
        input_arr = np.array([input_arr])

        # Predict utilis
        prediction = loaded_model.predict(input_arr)
        predictionArgsort = np.argsort(prediction[0])
        predictionArgsortReverse = predictionArgsort[::-1]

        end_time = time.time()
        data = {
            "status": True, 
            "timeTaken": str(end_time - satrt_time),
            "timeTakenOffset": ""
        }

        # Get top5 predictions
        for i in range(5):
            data['top' + str(i + 1)] = {
                "label": labels[ predictionArgsortReverse[i] ],
                "confident": str(prediction[0][ predictionArgsortReverse[i] ])
            }

        return func.HttpResponse(
            json.dumps(data, separators=(',', ':')),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:

        data = {
            "top1": {},
            "top2": {},
            "top3": {},
            "top4": {},
            "top5": {},
            "status": False,
            "timeTaken": "",
            "timeTakenOffset": "" 
        }

        return func.HttpResponse(
            json.dumps(data, separators=(',', ':')),
            mimetype="application/json",
            status_code=500
        )
