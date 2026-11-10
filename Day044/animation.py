from PIL import Image

frames = []

for color in ["red", "green", "blue", "yellow"]:

    image = Image.new("RGB", (300, 300), color)

    frames.append(image)

frames[0].save(
    "animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0
)