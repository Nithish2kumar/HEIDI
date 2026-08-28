# 🕵️ HEIDI — Image Steganography

A simple Python project for **hiding and extracting secret messages inside images** using **LSB (Least Significant Bit) steganography**.

## ✨ Features

* 🖼️ Hide text inside PNG images
* 🔓 Extract hidden messages
* 🔢 LSB-based encoding
* 🐍 Built with Python and Pillow
* 🎓 Simple implementation for learning

## 📁 Structure

```text
HEIDI/
├── image stego/
│   ├── encoder.py
│   └── decoder.py
|   └── main.py
├── network stego/
|   ├──receiver.py
|   └──sender.py  
├── samples/
├── requirements.txt
└── README.md
```
## 🖼️ Output screenshot
<img width="1455" height="560" alt="2026_08_25_18_28_45_screenshot" src="https://github.com/user-attachments/assets/9eda274b-6fd8-4327-a7f5-633234d7008d" />


## 🚀 Usage

Install the dependency:

```bash
pip install pillow
pip install rich 
```

Encode/Decode a message on Image:

```bash
sudo python3 image\ steg/main.py 
```

Send/Receive message on Network:

```bash
sudo python3 network\ steg/receiver.py
sudo python3 network\ steg/sender.py
```

## 🔐 How It Works

Image:

```text
Secret Message
      ↓
   Binary
      ↓
Image Pixel LSBs
      ↓
  Stego Image
```

Network:

'''Secret Message
      ↓
    Binary
      ↓
 Packet Timing
      ↓
  Network Traffic
      ↓
 Receiver
      ↓
 Extract Timing
      ↓
    Binary
      ↓
 Secret Message
'''


The secret message is stored by modifying the **least significant bits of image pixel values**, causing minimal visible changes.

## 📌 Status

🚧 **Currently under development**

More steganography techniques and security analysis will be added later.

## 📄 License

This project is for **educational purposes**.
