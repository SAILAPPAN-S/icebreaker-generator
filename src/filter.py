import re

FORBIDDEN_PATTERNS = [
    r"(phone|number|whatsapp|contact|instagram|snapchat|social)",    
    r"(religion|politics|vote|church|temple|mosque)",
    r"(salary|income|job title|where do you live|address|area you live)",
    r"(sex|sexy|hot|nsfw|dirty)",
    r"(race|ethnicity|caste)",
]


def is_valid_icebreaker(text: str) -> bool:
    """Returns False if the text contains restricted content."""
    t = text.lower()

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, t, re.IGNORECASE):
            return False

    # length guard
    if len(text.split()) > 20:
        return False    

    return True


def filter_icebreakers(lines: list[str]) -> list[str]:
    """Return only the safe icebreakers."""
    return [line for line in lines if is_valid_icebreaker(line)]
