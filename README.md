# 🧾 Receipt Analyzer – Full Stack Mini App 

A complete full-stack application for uploading receipts and extracting structured insights using OCR, rule-based logic, and algorithmic processing. 

---

## 🚀 Features

### ✅ Core Functionalities
- Upload and process receipts in `.jpg`, `.png`, `.pdf`, and `.txt` formats.
- Extracts:
  - Vendor/Biller
  - Date of Transaction
  - Amount
  - Currency (Multi-currency support ✅)
- Parses and stores normalized data in SQLite.
- Built-in type-checking with **Pydantic**.
- Clean, modular backend architecture using **FastAPI**.

### 🧠 Algorithmic Implementations
- **Search**: Keyword-based, range-based, pattern-based.
- **Sorting**: Custom quicksort / Timsort over numerical and categorical fields.
- **Aggregation**:
  - Total spend, mean, median, mode
  - Vendor frequency
  - Monthly spend trend (time-series with sliding windows)

### 🎨 Frontend Dashboard
- Built with **Streamlit**
- Upload interface + data summary
- Tabular view
- JSON preview
- Auto MIME type handling for accurate backend compatibility

### 💎 Bonus Goals Implemented
- ✅ Currency detection / multi-currency handling
- 🌐 Supports `.pdf`, `.txt`, `.jpg`, `.png` files
- 🚫 Graceful handling of empty or malformed inputs
- ✅ Tests for parsing, logic, and API endpoints

---

## 🛠️ Tech Stack

| Layer     | Tech                    |
|-----------|-------------------------|
| Backend   | FastAPI, SQLite, Pydantic |
| Frontend  | Streamlit               |
| Parsing   | Tesseract OCR, Regex    |
| Testing   | Pytest, TestClient      |
| Storage   | SQLite (with Indexing)  |

---

## 🧱 Architecture

```plaintext
📦 Record_Receipts
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app + endpoint
│   │   ├── ingestion.py     # File type validation
│   │   ├── parser.py        # OCR, regex parsing
│   │   ├── utils.py         # Search, sort, stats, trends
│   │   ├── models.py        # Pydantic schemas
│   │   └── database.py      # SQLite setup
├── frontend/
│   └── streamlit_app.py     # UI for uploading + summaries
├── data/
│   ├── sample.jpg           # Dummy receipt image
│   └── sample.txt           # Dummy text receipt
├── tests/
│   ├── test_parser.py
│   ├── test_utils.py
│   └── test_endpoints.py

```
### ⚙️ Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/asmitannu/Receipt-Analyzer.git
cd Receipt-Analyzer
```

### 2. **Create a virtual Emvironment**
```bash
python -m venv .venv
```

- Activate it:
  - **Windows**:
    ```bash
    .venv\Scripts\activate
    ```
  - **Mac/Linux**:
    ```bash
    source .venv/bin/activate
    ```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Install Tesseract OCR**
- Download and install from: https://github.com/tesseract-ocr/tesseract/wiki
- After installation, make sure to add the install path (e.g., `C:\Program Files\Tesseract-OCR`) to your system's environment variables.

## 🚀 Running the App

### Run Backend (Flask API)
```bash
cd backend
python run.py
```

### Run Frontend (Streamlit App)
Open a new terminal window:

```bash
cd frontend
streamlit run streamlit_app.py
```
# 🧑‍💻 Author
[Asmi Tannu](https://github.com/asmitannu)
