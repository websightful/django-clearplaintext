# django-clearplaintext

Provides a Django template filter that normalizes plain text while allowing explicit whitespace control.

It collapses excessive whitespace but preserves intentional formatting using escaped sequences like `\n`, `\t`, and `\s`.

Perfect for:

* Plain text emails
* Notification templates
* Text exports
* System messages
* Markdown templates
* Structured text blocks inside Django templates

## ✨ What It Does

The `clean_plaintext` filter:

* Collapses multiple spaces into a single space
* Limits consecutive blank lines to a maximum of two
* Strips leading and trailing whitespace on each line
* Removes empty lines at the beginning and end
* Converts escaped sequences:

  * `\n` → newline
  * `\t` → tab
  * `\s` → single space

This allows you to write readable Django templates while still controlling whitespace precisely.

## 📦 Installation

```bash
pip install django-clearplaintext
```

## 🔧 Setup

Add it to your Django project:

```python
INSTALLED_APPS = [
    ...
    "clearplaintext",
]
```

## 🚀 Usage

### Input

Load the template tag:

```django
{% load clearplaintext_filters %}
```

Use it as a filter block:

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

### Output

```
Hello John Smith,

Your order has been confirmed.
Items:
    - Widget (2x)
    - Gadget (1x)

Best regards,
Acme Inc.
```

## 🎯 Why Use This?

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

## 🧠 Design Philosophy

* Minimal
* No external dependencies
* Focused on plain text formatting
* Safe and predictable behavior
* Suitable for reusable Django apps

## 🔍 Escaped Sequences Supported

| Sequence | Result       |
| -------- | ------------ |
| `\n`     | Newline      |
| `\t`     | Tab          |
| `\s`     | Single space |

Escaped sequences are protected during normalization and restored afterward.

## 🧪 Testing

The package is tested against multiple Django versions using `tox`.

To run tests locally:

```bash
tox
```

## 📄 License

MIT License
