import re

from django.template.loader import render_to_string


def clean_plaintext(value):
    """Normalize whitespace in a plain-text string.

    Collapses real whitespace to a single space while preserving intentional
    formatting expressed as escaped sequences: ``\\n`` (newline), ``\\t`` (tab),
    and ``\\s`` (single space). Non-string values are returned unchanged.
    """
    if not isinstance(value, str):
        return value

    # Replace escaped sequences with unique placeholders
    escaped_chars = {
        r"\n": "\n",
        r"\t": "\t",
        r"\s": " ",
    }

    for idx, (esc, char) in enumerate(list(escaped_chars.items())):
        placeholder = f"\x01{idx}\x01"
        value = value.replace(esc, placeholder)
        escaped_chars[placeholder] = char

    # Collapse real whitespace in non-placeholder segments
    placeholders = [p for p in escaped_chars if p.startswith("\x01")]
    escaped_placeholders = map(re.escape, placeholders)
    pattern = f"({'|'.join(escaped_placeholders)})"

    parts = re.split(pattern, value)
    value = "".join(
        part if part in placeholders else re.sub(r"\s+", " ", part).strip()
        for part in parts
    )

    # Restore placeholders
    for ph, char in escaped_chars.items():
        if ph.startswith("\x01"):
            value = value.replace(ph, char)

    # Remove whitespace between control characters (\n, \t)
    value = re.sub(r"(?<=[\n\t])\s+(?=[\n\t])", "", value)

    return value


def render_to_plaintext(template_name, context=None, request=None, using=None):
    """Render a Django template and apply ``clean_plaintext`` to the result.

    Accepts the same arguments as Django's ``render_to_string``.
    """
    rendered = render_to_string(template_name, context=context, request=request, using=using)
    return clean_plaintext(rendered)
