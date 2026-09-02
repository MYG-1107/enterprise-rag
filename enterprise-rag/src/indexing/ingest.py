cat > src/indexing/ingest.py <<'EOF'
import uuid
from pathlib import Path

from src.indexing.chunkers.recursive import (
    RecursiveChunker,
)
from src.indexing.parsers.pdf import parse_pdf
from src.indexing.parsers.docx import parse_docx
from src.indexing.parsers.html import parse_html


class IngestionService:

    def __init__(
        self,
        vector_search,
        lexical_search,
        embedding_service,
    ):

        self.vector_search = vector_search
        self.lexical_search = lexical_search
        self.embedding_service = (
            embedding_service
        )

        self.chunker = RecursiveChunker()

    def parse(self, file_path):

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return parse_pdf(file_path)

        if suffix == ".docx":
            return parse_docx(file_path)

        if suffix in (
            ".html",
            ".htm",
        ):
            return parse_html(file_path)

        if suffix in (
            ".txt",
            ".md",
        ):
            return path.read_text(
                encoding="utf-8"
            )

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )

    def ingest(
        self,
        file_path,
        document_id=None,
    ):

        document_id = (
            document_id
            or str(uuid.uuid4())
        )

        text = self.parse(file_path)

        chunks = self.chunker.chunk(
            text
        )

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = (
            self.embedding_service.embed(
                texts
            )
        )

        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):

            chunk_id = str(uuid.uuid4())

            metadata = {
                "source": str(file_path),
                "chunk_index": chunk.index,
            }

            self.vector_search.add(
                chunk_id=chunk_id,
                document_id=document_id,
                text=chunk.text,
                embedding=embedding,
                metadata=metadata,
            )

            self.lexical_search.add(
                chunk_id=chunk_id,
                document_id=document_id,
                text=chunk.text,
                metadata=metadata,
            )

        return {
            "document_id": document_id,
            "chunks": len(chunks),
            "status": "indexed",
        }
EOF