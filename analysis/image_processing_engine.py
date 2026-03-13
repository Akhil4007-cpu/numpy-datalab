import numpy as np

def create_random_image():

    # simulate grayscale image
    image = np.random.randint(0, 255, (5,5))

    return image


def increase_brightness(image, value=50):

    bright = image + value

    # clip values to valid pixel range
    bright = np.clip(bright, 0, 255)

    return bright


def invert_image(image):

    inverted = 255 - image

    return inverted