# This script was used to generate color_map.png
# It contains every single color in rgb space
# The image is 128 wide rather than 256 wide. This is to make the image a bit smaller.

from PIL import Image

WIDTH = 128
HEIGHT = WIDTH**2
DEL = int(256/WIDTH)

def main():
    img  = Image.new(mode = "RGB", size = (WIDTH, HEIGHT))
    pixels = img.load()
    for r in range(WIDTH):
        for g in range(WIDTH):
            for b in range(WIDTH):
                x = r
                y = g + (b*WIDTH)
                pixels[x, y] = (r*DEL, g*DEL, b*DEL)

    img.save("color_map.png")

main()