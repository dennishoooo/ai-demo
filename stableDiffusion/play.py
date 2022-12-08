# Ref1: https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/
# Ref2: https://keras.io/api/keras_cv/models/stable_diffusion/#stablediffusion-class

import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")

    plt.show()

# backed by significantly faster kernels than their float32 counterparts on modern NVIDIA GPUs.
# if you are using CPU mode, off this line
keras.mixed_precision.set_global_policy("mixed_float16")

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

images = model.text_to_image(
    "chainsaw man, a chainsaw occur in the head, tall with red body"
    "dead eyes, kill everything he have seen, cartoon",
    batch_size=1,
)

plot_images(images)

# Save images
Image.fromarray(images[0]).save("dsImages.png")