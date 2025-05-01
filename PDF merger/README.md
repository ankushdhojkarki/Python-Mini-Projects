# 📎 PDF Merger – Combine Multiple PDF Files Using Python

This is a simple terminal-based Python script that merges multiple PDF files into a single PDF. It uses the `pypdf` library to handle the merging process, making it useful for organizing documents, notes, or reports.

---

## 📌 How It Works

- The script asks the user how many PDF files they want to merge.
- The user enters the filenames (with extension) one by one.
- The script merges all provided PDF files in the entered order.
- The final merged PDF is saved as `merged-pdf.pdf` in the current directory.

---

## 📁 Files Included

- `pdf_merger.py` — The main script that merges multiple PDF files.

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Install the required library by running:

   ```bash
      pip install pypdf
   
3. Place pdf_merger.py in your project folder.

4. Put the PDF files you want to merge in the same folder.

5. Open your terminal or command prompt and run:
      python pdf_merger.py
