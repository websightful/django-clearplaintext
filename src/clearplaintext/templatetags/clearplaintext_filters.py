import re
from django import template

register = template.Library()


@register.filter(name="clean_plaintext")
def clean_plaintext(value):
    if not isinstance(value, str):
        return value

    # 1️⃣ Replace escaped sequences with unique placeholders
    escaped_chars = {
        r"\n": "\n",
        r"\t": "\t",
        r"\s": " ",
    }

    for idx, (esc, char) in enumerate(list(escaped_chars.items())):
        placeholder = f"\x01{idx}\x01"
        value = value.replace(esc, placeholder)
        escaped_chars[placeholder] = char

    # 2️⃣ Collapse real whitespace in non-placeholder segments
    placeholders = [p for p in escaped_chars if p.startswith("\x01")]
    escaped_placeholders = map(re.escape, placeholders)
    pattern = f"({'|'.join(escaped_placeholders)})"

    parts = re.split(pattern, value)
    value = "".join(
        part if part in placeholders else re.sub(r"\s+", " ", part).strip()
        for part in parts
    )

    # 3️⃣ Restore placeholders
    for ph, char in escaped_chars.items():
        if ph.startswith("\x01"):
            value = value.replace(ph, char)

    # 4️⃣ Remove whitespace between control characters (\n, \t)
    value = re.sub(r"(?<=[\n\t])\s+(?=[\n\t])", "", value)

    return value


@register.filter(name="keep_whitespace")
def keep_whitespace(value):
    if not isinstance(value, str):
        return value

    value = value.replace("\n", r"\n")
    value = value.replace("\t", r"\t")
    value = value.replace(" ", r"\s")

    return value
