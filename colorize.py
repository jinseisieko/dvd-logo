from PIL import Image
from PIL import ImageOps


def tint_image(src, color="#FFFFFF"):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    result = ImageOps.colorize(gray, (0, 0, 0, 0), color)
    result.putalpha(alpha)
    return result


img = Image.open("image.png")
tinted = tint_image(img, "#33b5e5")
