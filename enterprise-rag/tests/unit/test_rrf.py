cat > tests/unit/test_rrf.py <<'EOF'
from src.retrieval.hybrid import (
    reciprocal_rank_fusion,
)


class Result:

    def __init__(
        self,
        chunk_id,
        score,
    ):

        self.chunk_id = chunk_id
        self.score = score


def test_rrf():

    results = reciprocal_rank_fusion(
        [
            [
                Result("A", 1),
                Result("B", 0.8),
            ],
            [
                Result("B", 1),
                Result("C", 0.7),
            ],
        ]
    )

    assert results[0].chunk_id == "B"
EOF