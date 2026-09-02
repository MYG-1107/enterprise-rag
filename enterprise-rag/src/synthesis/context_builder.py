cat > src/synthesis/context_builder.py <<'EOF'
class ContextBuilder:

    def build(
        self,
        results,
        max_chunks=5,
    ):

        results = results[:max_chunks]

        context_parts = []

        for index, result in enumerate(
            results,
            start=1,
        ):

            context_parts.append(
                f"""
[SOURCE {index}]
Document: {result.document_id}
Chunk: {result.chunk_id}

{result.text}
"""
            )

        return "\n".join(
            context_parts
        )
EOF