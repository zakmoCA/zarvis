import pymupdf

def load_path(path: str) -> tuple[str, dict]:
    p = path.lower()
    if p.endswith(".pdf"):
        return _load_pdf(path), {"pages": None}
    
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(), {}

def _load_pdf(pdf_path: str) -> str:
    try:
        doc = pymupdf.open(pdf_path)
        return "\n".join(page.get_text() for page in doc).strip()
    except Exception as e:
        return f"error reading {pdf_path}: {e}"