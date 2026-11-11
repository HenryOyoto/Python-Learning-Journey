"""Rotate and blur an image using Pillow."""

from PIL import Image, ImageFilter


def main():
    """Rotate the image by 180 degrees, find edges, apply blur, and save the result."""
    with Image.open("wave.jpg") as img:
        img = img.rotate(180)
        img1 = img.filter(ImageFilter.FIND_EDGES)
        img = img.filter(ImageFilter.BLUR)
        img.save("out2.jpeg")
        img1.save("out3.jpeg")


if __name__ == "__main__":
    main()
