cat > src/models/document.py <<'EOF'
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Document:
    id: str
    title: str
    source: str
    document_type: str
    department: Optional[str] = None
    version: Optional[str] = None
    metadata: dict = field(default_factory=dict)


@dataclass
class Chunk:
    id: str
    document_id: str
    text: str
    chunk_index: int
    page: Optional[int] = None
    section: Optional[str] = None
    metadata: dict = field(default_factory=dict)
EOF