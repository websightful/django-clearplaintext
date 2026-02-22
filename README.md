# django-clearplaintext

Provides Django template filters that normalize plain text while allowing explicit whitespace control.

It collapses excessive whitespace but preserves intentional formatting using escaped sequences like `\n`, `\t`, and `\s`.

Perfect for:

* Plain text emails
* Notification templates
* Text exports
* System messages
* Markdown templates
* Structured text blocks inside Django templates

## What It Does

### `render_to_plaintext`

A utility function that renders a Django template to a string and then applies `clean_plaintext` normalization to the result. It accepts the same arguments as Django's `render_to_string`.

### `clean_plaintext`

* Collapses multiple spaces into a single space
* Limits consecutive blank lines to a maximum of two
* Strips leading and trailing whitespace on each line
* Removes empty lines at the beginning and end
* Converts escaped sequences:

  * `\n` → newline
  * `\t` → tab
  * `\s` → single space

This allows you to write readable Django templates while still controlling whitespace precisely.

### `keep_whitespace`

Escapes real whitespace characters in a value so they survive `clean_plaintext` normalization:

* `\n` → `\n` (literal)
* `\t` → `\t` (literal)
* ` ` → `\s` (literal)

Use this when passing database values or dynamic content that contains meaningful whitespace into a `clean_plaintext` block.

## Installation
```bash
pip install django-clearplaintext
```

## Setup

Add it to your Django project:
```python
INSTALLED_APPS = [
    ...
    "clearplaintext",
]
```

## Usage

Load the template tag:
```django
{% load clearplaintext_filters %}
```

### `clean_plaintext` — template block formatting

Use it as a filter block to normalize whitespace in your template while keeping explicit escape sequences:
```django
{% filter clean_plaintext %}
Hello {{ user.get_full_name }},\n

Your order has been confirmed.\n
{% for item in order.items %}
    \t- {{ item.name }} ({{ item.quantity }}x)\n
    {% if forloop.last %}\n{% endif %}
{% endfor %}

Best regards,\n
{{ company.name }}
{% endfilter %}
```

Output:
```
Hello John Smith,

Your order has been confirmed.
    - Widget (2x)
    - Gadget (1x)

Best regards,
Acme Inc.
```

### `keep_whitespace` — preserving whitespace from dynamic values

When a variable comes from the database and already contains meaningful whitespace, pipe it through `keep_whitespace` before passing it into a `clean_plaintext` block:
```django
{% filter clean_plaintext %}
{{ post.content|keep_whitespace }}
{% endfilter %}
```

This ensures that real newlines, tabs, and spaces in the value are escaped before normalization runs, so they are restored correctly in the output rather than being collapsed.

### `render_to_plaintext` — rendering templates directly from Python

Use this utility function when you want to render a template and get clean plain text back in a single call, for example when sending plain-text emails from a view or task:

```python
from clearplaintext.utils import render_to_plaintext

body = render_to_plaintext("emails/order_confirmed.txt", {"order": order}, request=request)
```

It accepts the same arguments as Django's `render_to_string` and applies `clean_plaintext` normalization to the result.

The template itself uses the same escaped sequences as the filter:

```
Hi {{ user.get_full_name }},\n\n

Your order #{{ order.id }} has been confirmed.\n
{% for item in order.items %}
    \t- {{ item.name }} ({{ item.quantity }}x)\n
    {% if forloop.last %}\n{% endif %}
{% endfor %}

Best regards,\n
{{ company.name }}
```

## Why Use This?

Django templates often produce messy whitespace because of:

* Template indentation
* Conditionals and loops
* Readability formatting
* Multi-line template blocks

This filter lets you:

* Keep templates readable
* Avoid ugly output formatting
* Still control exact whitespace when needed

It is especially useful for plain-text emails where formatting matters.

## Design Philosophy

* Minimal
* No external dependencies
* Focused on plain text formatting
* Safe and predictable behavior
* Suitable for reusable Django apps

## Escaped Sequences Supported

| Sequence | Result       |
| -------- | ------------ |
| `\n`     | Newline      |
| `\t`     | Tab          |
| `\s`     | Single space |

Escaped sequences are protected during normalization and restored afterward. The `keep_whitespace` filter converts real whitespace into these sequences so that dynamic values receive the same treatment.

## `django-clearplaintext` in Production

`django-clearplaintext` is used in production at

- [1st things 1st](https://www.1st-things-1st.com)
- [Remember Your People](https://remember-your-people.app)

## Testing

The package is tested against multiple Django versions using `tox`.

To run tests locally:
```bash
tox
```

## License

MIT License