import re
from .models import SanitizedPayload

PATTERNS = {
    "cpr": re.compile(r"\b\d{6}[- ]?\d{4}\b"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone": re.compile(r"\b(?:\+45\s?)?(?:\d{2}[\s-]?){4}\b"),
}


def sanitize_text(text: str) -> SanitizedPayload:
    sanitized = text
    redactions: list[str] = []

    for label, pattern in PATTERNS.items():
        if pattern.search(sanitized):
            sanitized = pattern.sub(f"[{label.upper()}_REDACTED]", sanitized)
            redactions.append(label)

    return SanitizedPayload(
        original_text_present=bool(text),
        sanitized_text=sanitized,
        redactions=redactions,
    )
