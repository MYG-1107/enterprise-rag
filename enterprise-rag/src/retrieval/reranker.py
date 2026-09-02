cat > src/retrieval/reranker.py <<'EOF'
class Reranker:

    def rerank(
        self,
        query,
        results,
        top_k=5,
    ):

        # Initial implementation:
        # preserve hybrid ranking.

        results = sorted(
            results,
            key=lambda x: x.score,
            reverse=True,
        )

        return results[:top_k]
EOF