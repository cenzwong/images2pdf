# 🖼️ PNG2PDF

Combine multiple `.png` files into a single PDF — sorted naturally like “Screenshot 1, Screenshot 2, Screenshot 10”.

---

## 🚀 Installation

You can install **with either `pipx` (recommended)** or `pip`.

---

### 🧩 Option 1: Use pipx (recommended)

[`pipx`](https://pypa.github.io/pipx/) installs Python apps in **isolated environments**, so they won’t interfere with your global packages.

#### 🧰 Step 1: Install pipx (if not yet installed)

**macOS / Linux:**
```bash
python -m pip install --user pipx
python -m pipx ensurepath
# You may need to restart your terminal for the path change to take effect
````

**Windows (PowerShell):**

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
# Close and reopen PowerShell
```

#### 🧩 Step 2: Install PNG2PDF using pipx

- TLDR: just run this command once:
```bash
pipx run git+https://github.com/<username>/png2pdf.git images_folder
```


```bash
pipx install git+https://github.com/cenzwong/images2pdf.git
```

Then run it anywhere:

```bash
png2pdf /path/to/images_folder
```

---

### ⚙️ Option 2: Use pip

```bash
pip install git+https://github.com/cenzwong/images2pdf.git
```

Then run either:

```bash
python -m png2pdf /path/to/images_folder
# or
png2pdf /path/to/images_folder
```

---

## 💡 Usage

To see all available options:

```bash
python -m png2pdf -h
# or
png2pdf -h
```

Example:

```bash
png2pdf ./screenshots output.pdf
```

✅ Features:

* Natural numeric sorting (`1.png`, `2.png`, `10.png`, …)
* Automatically skips non-PNG files
* Generates a single PDF in seconds

---

## 🧰 Requirements

* Python ≥ 3.7
* [Pillow](https://pypi.org/project/Pillow/)

---

## 🧑‍💻 Development

Clone and install in editable mode:

```bash
git clone https://github.com/cenzwong/images2pdf.git
cd images2pdf
pip install -e .[dev]
```

Then test locally:

```bash
python -m png2pdf ./images
```

---

## 📜 License

MIT © [Cenz Wong](https://github.com/cenzwong)