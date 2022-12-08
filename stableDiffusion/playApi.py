from sanic import Sanic
from sanic.response import text

import keras_cv
from tensorflow import keras
from PIL import Image
from sanic.response import file
from sanic.response import json

app = Sanic("MyHelloWorldApp")

keras.mixed_precision.set_global_policy("mixed_float16")
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

@app.post("/sd")
async def hello_world(request):

    try:
    
        genStr = request.json['data']
        if genStr is None:
            return json({
                "status": False,
                "msg": "Missing body with key data"
            })

        images = model.text_to_image(
            genStr,
            batch_size=1,
        )

        Image.fromarray(images[0]).save("dsImages.png")
        return await file("./dsImages.png")
    except:
        return json({
            "status": False,
            "msg": "Internal server Error"
        })
