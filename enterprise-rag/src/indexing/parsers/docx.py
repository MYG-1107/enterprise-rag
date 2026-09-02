cat > src/indexing/parsers/docx.py <<'EOF'
from pathlib import Path


def parse_docx(file_path: str) -> str:
    from docx import Document

    document = Document(Path(file_path))

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n\n".join(paragraphs)
EOF