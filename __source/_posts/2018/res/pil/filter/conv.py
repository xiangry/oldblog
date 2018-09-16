from PIL import Image
from PIL import ImageFilter
from PIL import ImageFont
from PIL import ImageDraw
import math

im = Image.open("BIG.png")
out = im.copy().resize((152, 152), Image.ANTIALIAS)
out.save("NONE.png")

ImageFilter_KEYS = {
    "BLUR":ImageFilter.BLUR,
    "CONTOUR":ImageFilter.CONTOUR,
    "DETAIL":ImageFilter.DETAIL,
    "EDGE_ENHANCE":ImageFilter.EDGE_ENHANCE,
    "EDGE_ENHANCE_MORE":ImageFilter.EDGE_ENHANCE_MORE,
    "EMBOSS":ImageFilter.EMBOSS,
    "FIND_EDGES":ImageFilter.FIND_EDGES,
    "SMOOTH":ImageFilter.SMOOTH,
    "SMOOTH_MORE":ImageFilter.SMOOTH_MORE,
    "SHARPEN":ImageFilter.SHARPEN,
}

im = Image.open("NONE.png")
size = im.size

filters = ("NONE", "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SMOOTH", "SMOOTH_MORE", "SHARPEN")

count = len(filters)

column = int(math.floor(1024 / size[1]))
row = int(math.ceil(1.0 * count / column))

print column, row
height = size[1] + 20


image = Image.new('RGB', (size[0] * column, height * row), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Arial.ttf', 12)

for index in xrange(0, count):
    _filter_name = filters[index]
    _filter = ImageFilter_KEYS.get(_filter_name)
    out = im
    if _filter:
        out = im.copy().filter(_filter)

    y = int(math.floor(index / column))
    x = int(index - y * column)

    image.paste(out, (size[0] * x, height * y))
    draw.text((size[0] * x, height * y + size[1]), _filter_name, font=font, fill=(0, 0, 0), anchor=(0.5, 1))

image.save("all.png")