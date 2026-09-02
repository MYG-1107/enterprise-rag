cat > src/synthesis/rag.py <<'EOF'
from src.retrieval.hybrid import reciprocal_rank_fusion
from src.retrieval.reranker import Reranker
from src.synthesis.context_builder import ContextBuilder
from src.synthesis.citation_engine import create_citations


class RAGPipeline:

    def __init__(
        self,
        vector_search,
        lexical_search,
        embedding_service,
        llm,
    ):

        self.vector_search = vector_search
        self.lexical_search = lexical_search
        self.embedding_service = embedding_service
        self.llm = llm

        self.reranker = Reranker()

        self.context_builder = (
            ContextBuilder()
        )

    def answer(
        self,
        question: str,
    ):

        # --------------------------------
        # 1. Embed query
        # --------------------------------

        query_embedding = (
            self.embedding_service.embed(
                [question]
            )[0]
        )

        # --------------------------------
        # 2. Vector search
        # --------------------------------

        vector_results = (
            self.vector_search.search(
                query_embedding,
                top_k=10,
            )
        )

        # --------------------------------
        # 3. Lexical search
        # --------------------------------

        lexical_results = (
            self.lexical_search.search(
                question,
                top_k=10,
            )
        )

        # --------------------------------
        # 4. Hybrid retrieval
        # --------------------------------

        hybrid_results = reciprocal_rank_fusion(
            [
                vector_results,
                lexical_results,
            ]
        )

        # --------------------------------
        # 5. Rerank
        # --------------------------------

        ranked_results = (
            self.reranker.rerank(
                question,
                hybrid_results,
                top_k=5,
            )
        )

        # --------------------------------
        # 6. Build context
        # --------------------------------

        context = (
            self.context_builder.build(
                ranked_results
            )
        )

        # --------------------------------
        # 7. Generate answer
        # --------------------------------

        answer = self.llm.generate(
            question,
            context,
        )

        # --------------------------------
        # 8. Citations
        # --------------------------------

        citations = create_citations(
            ranked_results
        )

        return {
            "answer": answer,
            "citations": citations,
        }
EOF