
# coding: utf-8




from PIL import Image
sourceFileName = 'cesc.jpg'
image         = Image.open(sourceFileName)
image = image.convert("RGBA")
image = image.resize((int(image.size[0]*0.75), int(image.size[1]*0.5)))
image.show()
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def transform(image):
    res = ''
    unit = (256.0 + 1) / len(ascii_char);
    for h in range(0, image.size[1]):
        for w in range(0, image.size[0]):
            g, r, b, a = image.getpixel((w, h))
            gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
            res = res + ascii_char[int(gray/unit)]
        res = res + '\r\n'
    return res

res = transform(image)

tmp = open('tmp.txt','w')
tmp.write(res)
tmp.close()




