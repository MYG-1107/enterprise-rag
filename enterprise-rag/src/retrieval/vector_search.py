cat > src/retrieval/vector_search.py <<'EOF'
from dataclasses import dataclass


@dataclass
class SearchResult:

    chunk_id: str

    document_id: str

    text: str

    score: float

    metadata: dict


class VectorSearch:

    def __init__(self):
        self.documents = []

    def add(
        self,
        chunk_id: str,
        document_id: str,
        text: str,
        embedding,
        metadata=None,
    ):

        self.documents.append(
            {
                "chunk_id": chunk_id,
                "document_id": document_id,
                "text": text,
                "embedding": embedding,
                "metadata": metadata or {},
            }
        )

    def search(
        self,
        query_embedding,
        top_k: int = 5,
    ):

        import numpy as np

        results = []

        for document in self.documents:

            embedding = document["embedding"]

            score = float(
                np.dot(
                    query_embedding,
                    embedding,
                )
            )

            results.append(
                SearchResult(
                    chunk_id=document["chunk_id"],
                    document_id=document["document_id"],
                    text=document["text"],
                    score=score,
                    metadata=document["metadata"],
                )
            )

        results.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:top_k]
EOF