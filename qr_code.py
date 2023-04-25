import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=wr8roZmKXt8")
img.save("bestsong.png")