cat > tests/unit/test_chunker.py <<'EOF'
from src.indexing.chunkers.recursive import (
    RecursiveChunker,
)


def test_chunker():

    chunker = RecursiveChunker(
        chunk_size=10,
        overlap=2,
    )

    chunks = chunker.chunk(
        "abcdefghijklmnopqrstuvwxyz"
    )

    assert len(chunks) > 1
EOF