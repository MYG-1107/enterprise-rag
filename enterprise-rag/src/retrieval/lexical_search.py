cat > src/retrieval/lexical_search.py <<'EOF'
import re

from src.retrieval.vector_search import SearchResult


class LexicalSearch:

    def __init__(self):
        self.documents = []

    def add(
        self,
        chunk_id,
        document_id,
        text,
        metadata=None,
    ):

        self.documents.append(
            {
                "chunk_id": chunk_id,
                "document_id": document_id,
                "text": text,
                "metadata": metadata or {},
            }
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_words = set(
            re.findall(
                r"\w+",
                query.lower(),
            )
        )

        results = []

        for document in self.documents:

            words = set(
                re.findall(
                    r"\w+",
                    document["text"].lower(),
                )
            )

            score = len(
                query_words.intersection(words)
            )

            if score > 0:

                results.append(
                    SearchResult(
                        chunk_id=document["chunk_id"],
                        document_id=document["document_id"],
                        text=document["text"],
                        score=float(score),
                        metadata=document["metadata"],
                    )
                )

        results.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:top_k]
EOF