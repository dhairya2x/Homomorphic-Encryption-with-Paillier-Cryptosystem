from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa


publickey, privkey = Pa.generate_keys()
print(publickey.__repr__())

im = Image.open(r"D:\SRI\IP_IMG\BE.jpg") 

db = []
firstname = []
lastname = []
gender = []
studentid = []
encrypt_image = IC.ImgEncrypt(publickey,im)
inc_bright = IC.homomorphicBrightness(publickey,encrypt_image,30)
im = IC.ImgDecrypt(publickey,privkey,inc_bright)
im.save("encrypted-images/LenaDecrypted.png")
im.show()
ij = IC.saveEncryptedImg(inc_bright,"LenaEncrypted.png")
