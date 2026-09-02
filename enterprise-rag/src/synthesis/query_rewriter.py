cat > src/synthesis/query_rewriter.py <<'EOF'
class QueryRewriter:

    def rewrite(
        self,
        question: str,
        history: list | None = None,
    ):

        # Start simple.
        #
        # Later this can call an LLM to transform:
        #
        # "What about contractors?"
        #
        # into:
        #
        # "What is the remote work policy for contractors?"

        return question.strip()
EOF