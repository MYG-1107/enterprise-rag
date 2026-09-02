cat > src/retrieval/embeddings.py <<'EOF'
class EmbeddingService:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        self.model_name = model_name
        self.model = None

    def load(self):

        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(
            self.model_name
        )

    def embed(
        self,
        texts: list[str],
    ):

        if self.model is None:
            self.load()

        return self.model.encode(
            texts,
            normalize_embeddings=True,
        )
EOF