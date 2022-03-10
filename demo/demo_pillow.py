from typing import Optional, Any

from PIL import Image

# im: Image.Image = Image.open("./image/u.jpg")
# print(im.format, im.size, im.mode)
# # im.show()
# im.save("1.png")
im: Image.Image = Image.open("1.png")
im.save("2.jpg")
