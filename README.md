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
├── src/
│   ├── encoder.py
│   └── decoder.py
|   └── main.py
├── samples/
├── requirements.txt
└── README.md
```

## 🚀 Usage

Install the dependency:

```bash
pip install pillow
pip install rich 
```

Encode a message:

```bash
sudo python src/main.py
```

## 🔐 How It Works

```text
Secret Message
      ↓
   Binary
      ↓
Image Pixel LSBs
      ↓
  Stego Image
```

The secret message is stored by modifying the **least significant bits of image pixel values**, causing minimal visible changes.

## 📌 Status

🚧 **Currently under development**

More steganography techniques and security analysis will be added later.

## 📄 License

This project is for **educational purposes**.
