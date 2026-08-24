from PIL import Image

def decode(inI):
    image= Image.open(inI).convert("RGB")
    bin=""

    for pix in image.getdata():
        for val in pix:
            bin+=str(val&1)#Gives the last bit what we inserted on encrytpion
    msg=""

    for i in range(0, len(bin),8):
        byte=bin[i:i+8]#Split 8bits

        if len(byte)<8:
            break

        char=chr(int(byte,2))#binary value of 8bits
        msg+=char
        if msg.endswith("<<<END>>>"):
            return msg[:-9]

    return msg


message=decode("../samples/out.jpeg")

