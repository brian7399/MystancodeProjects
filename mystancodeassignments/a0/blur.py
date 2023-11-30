"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            total_red, total_green, total_blue = 0, 0, 0
            count = 0

            # Iterate over the neighboring pixels
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x + i
                    pixel_y = y + j
                    # Check if the neighboring pixel is within bounds
                    if 0 <= pixel_x < img.width and 0 <= pixel_y < img.height:
                        pixel = img.get_pixel(pixel_x, pixel_y)
                        total_red += pixel.red
                        total_green += pixel.green
                        total_blue += pixel.blue
                        count += 1

            # Calculate the average RGB values
            avg_red = total_red // count
            avg_green = total_green // count
            avg_blue = total_blue // count

            # Set the average color to the corresponding pixel in the new image
            new_p = new_img.get_pixel(x, y)
            new_p.red = avg_red
            new_p.green = avg_green
            new_p.blue = avg_blue
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
