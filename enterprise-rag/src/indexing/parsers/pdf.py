cat > src/indexing/parsers/pdf.py <<'EOF'
from pathlib import Path


def parse_pdf(file_path: str) -> str:
    from pypdf import PdfReader

    path = Path(file_path)

    reader = PdfReader(path)

    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return "\n\n".join(pages)
EOF