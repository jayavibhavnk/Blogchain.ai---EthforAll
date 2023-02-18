from pysteg_new.usage_example import image_encryptor,image_decryptor

in_path = r"C:\Users\jayav\Desktop\ethforall\blockchain\image.jpg"
out_path = "new_imge.png"
password = "12345678"
message = "My secret message!"

image_encryptor(in_path,out_path,password,message)

print("image encrypted")

image_decryptor(password,out_path)