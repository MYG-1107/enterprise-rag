cat > src/indexing/parsers/html.py <<'EOF'
from pathlib import Path


def parse_html(file_path: str) -> str:
    from bs4 import BeautifulSoup

    html = Path(file_path).read_text(
        encoding="utf-8"
    )

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    for element in soup(
        ["script", "style", "noscript"]
    ):
        element.decompose()

    return soup.get_text(
        separator="\n",
        strip=True,
    )
EOF