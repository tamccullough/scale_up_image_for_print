from PIL import Image

with Image.open("convert.png") as im:

    while True:
        try:
            # Provide the target width and height of the image
            print('Enter the size you want to scale the image to in pixels')
            size_to_scale_to = int(input('example. 4000: '))
            break
        except ValueError:
            print('Enter an integer, please.')
    im_resized = im.resize((size_to_scale_to, size_to_scale_to), resample = Image.NEAREST)
    im_resized.save('upscaled.png',quality=100)
