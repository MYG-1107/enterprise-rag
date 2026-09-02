cat > src/synthesis/citation_engine.py <<'EOF'
def create_citations(results):

    citations = []

    for index, result in enumerate(
        results,
        start=1,
    ):

        citations.append(
            {
                "citation": f"[{index}]",
                "document_id": result.document_id,
                "chunk_id": result.chunk_id,
                "page": result.metadata.get(
                    "page"
                ),
                "section": result.metadata.get(
                    "section"
                ),
            }
        )

    return citations
EOF