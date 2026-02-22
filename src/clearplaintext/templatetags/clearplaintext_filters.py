from django import template

register = template.Library()


@register.filter(name="clean_plaintext")
def clean_plaintext(value):
    """Normalize whitespace in a template block.

    Collapses real whitespace to a single space while converting escaped
    sequences (``\\n``, ``\\t``, ``\\s``) into their actual characters. Use as
    a ``{% filter clean_plaintext %}`` block around template content.
    """
    from clearplaintext.utils import clean_plaintext as _clean_plaintext

    return _clean_plaintext(value)


@register.filter(name="keep_whitespace")
def keep_whitespace(value):
    """Escape real whitespace in a value so it survives ``clean_plaintext``.

    Converts newlines to ``\\n``, tabs to ``\\t``, and spaces to ``\\s``.
    Apply this filter to dynamic values (e.g. from the database) before they
    enter a ``clean_plaintext`` block to prevent their whitespace from being
    collapsed.
    """
    if not isinstance(value, str):
        return value

    value = value.replace("\n", r"\n")
    value = value.replace("\t", r"\t")
    value = value.replace(" ", r"\s")

    return value
