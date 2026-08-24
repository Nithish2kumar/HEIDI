from PIL import Image

def encode(inI,outI,msg):

    #----Processing the input file-----

    image= Image.open(inI).convert("RGB")#convert each pixel into RGB value
    msg+="<<<END>>>"#to stop the loop while decoding
    binary=''.join(format(ord(char),'08b') for char in msg)#msg to 8bit binary
    pix=list(image.getdata())#Full RGB value of picture

    if len(binary)>len(pix)*3:#checking whether the image is small or large
        raise ValueError("Message is too large")

    #----Processing the output file-----

    newPix=[]
    bitIndex=0#Tells the index msg bit

    for pi in pix:#iterate RGB
        newPi=[]
        for value in pi:#iterate the value in RGB
            if bitIndex<len(binary):
                value=(value&0xFE)|int(binary[bitIndex])#Steganography
                bitIndex+=1
            newPi.append(value)
        newPix.append(tuple(newPi))

    image.putdata(newPix)#Modified image
    image.save(outI)
    print("Successfully hidden")

encode("../samples/DP.jpeg","../samples/out.png","Hello NK")