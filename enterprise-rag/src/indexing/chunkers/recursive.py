cat > src/indexing/chunkers/recursive.py <<'EOF'
from dataclasses import dataclass


@dataclass
class TextChunk:
    text: str
    index: int


class RecursiveChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 150,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list[TextChunk]:

        if not text:
            return []

        chunks = []

        start = 0
        index = 0

        while start < len(text):

            end = min(
                start + self.chunk_size,
                len(text),
            )

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(
                    TextChunk(
                        text=chunk_text,
                        index=index,
                    )
                )

                index += 1

            if end >= len(text):
                break

            start = end - self.overlap

        return chunks
EOF