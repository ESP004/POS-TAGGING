# POS Tagging & Grammar Analyzer

A desktop application built with **Python**, **CustomTkinter**, and **NLTK** for performing Part-of-Speech (POS) tagging and basic grammar analysis on English text.

The application provides an intuitive graphical interface to analyze text, visualize POS tag distributions, load documents, and export analysis results.

---

## Features

- POS tagging using NLTK
- Grammar summary generation
- POS tag meaning lookup
- Interactive GUI built with CustomTkinter
- Bar Chart visualization
- Pie Chart visualization
- Import text from:
  - TXT
  - PDF
  - DOCX
- Export analysis results to CSV
- Light / Dark theme switch
- Toast notifications for user feedback
- Responsive desktop layout

---

## Screenshots

_Add screenshots of the application here._

Example:

```
screenshots/
    Screensort_dark_barchart.png
    Screensort_dark_pirchart.png
    Screensort_light.png
```

---

## Project Structure

```
POS-TAGGING/
│
├── core/
│   ├── tokenizer.py
│   ├── pos_tagger.py
│   ├── grammar_analyzer.py
│   ├── tag_dictionary.py
│   ├── file_loader.py
│   └── csv_exporter.py
│
├── gui/
│   ├── app.py
│   ├── input_frame.py
│   ├── results_frame.py
│   ├── summary_frame.py
│   ├── chart_frame.py
│   └── toast.py
│
├── assets/
│
├── download_nltk.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10 or later
- Windows, Linux or macOS

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/ESP004/POS-TAGGING.git

cd POS-TAGGING
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

---

## 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Download required NLTK datasets

```bash
python download_nltk.py
```

This downloads all required NLTK corpora used by the application.

---

## 6. Run the application

```bash
python main.py
```

---

# Supported File Formats

The application can load text from:

- TXT
- PDF
- DOCX

---

# Export

Analysis results can be exported as a CSV file containing:

- Word
- POS Tag
- POS Meaning

---

# Visualization

Two visualization modes are available.

### Bar Chart

Displays the count of each detected Part of Speech.

### Pie Chart

Displays the percentage distribution of detected POS tags.

---

# Technologies Used

- Python
- CustomTkinter
- NLTK
- Matplotlib
- PyPDF2
- python-docx
- CSV

---

# Dependencies

Installed automatically through:

```bash
pip install -r requirements.txt
```

---

# Future Improvements

- Sentence-level grammar analysis
- Readability score
- Named Entity Recognition (NER)
- Dependency Parsing
- Parse Tree Visualization
- Export to PDF
- Export to Excel
- Drag & Drop file support
- Word frequency visualization
- Search within results

---

# License

This project is intended for educational purposes.

---

# Author

**Gourab Shaw**

Computer Science & Engineering

Built using Python, CustomTkinter and NLTK.