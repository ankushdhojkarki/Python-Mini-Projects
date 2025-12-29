import qrcode

img = qrcode.make('https://www.youtube.com')
type(img)
img.save("YouTube.png")