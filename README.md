# 🖼️ PNG to PDF Converter

A simple Python module that combines multiple `.png` images into a single `.pdf` file — with **natural sorting** so files like  
`Screenshot 1.PNG`, `Screenshot 2.PNG`, … `Screenshot 10.PNG` are ordered correctly.

---

## 📦 Requirements

Make sure you have **Python 3.7+** and install the required library:

```bash
pip install pillow
```

---

## 🚀 Usage

1. Place your `.PNG` files inside a folder (e.g. `images/`).

2. Run the module directly:

```bash
python -m png2pdf ./images
```

3. You’ll get a file named `combined.pdf` in the same directory.

You can also specify a custom output filename:

```bash
python -m png2pdf ./images my_output.pdf
```

---

## 🧠 How It Works

- Reads all `.png` files in the target folder.
- Sorts them **naturally** (so numeric parts are in correct order).
- Converts each image to RGB.
- Combines all into a single multi-page PDF.

---

## 📝 License

Open source and free to use for personal or commercial purposes.
