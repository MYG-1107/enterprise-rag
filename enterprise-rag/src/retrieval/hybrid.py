cat > src/retrieval/hybrid.py <<'EOF'
def reciprocal_rank_fusion(
    result_lists,
    k=60,
):

    scores = {}

    documents = {}

    for results in result_lists:

        for rank, result in enumerate(
            results,
            start=1,
        ):

            chunk_id = result.chunk_id

            scores[chunk_id] = (
                scores.get(chunk_id, 0)
                + 1 / (k + rank)
            )

            documents[chunk_id] = result

    ranked = sorted(
        documents.keys(),
        key=lambda x: scores[x],
        reverse=True,
    )

    output = []

    for chunk_id in ranked:

        result = documents[chunk_id]

        result.score = scores[chunk_id]

        output.append(result)

    return output
EOF