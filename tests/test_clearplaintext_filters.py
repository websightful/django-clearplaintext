from types import SimpleNamespace

from django.template import Context, Template
from django.test import SimpleTestCase


class CleanPlaintextFilterTest(SimpleTestCase):
    def test_clean_plaintext_template(self):
        template_string = r"""
{% load clearplaintext_filters %}{% filter clean_plaintext %}
Hi {{ user.name }},\n\n

{% if order.is_urgent %}
⚠️ URGENT: Your order requires immediate attention!\n\n
{% endif %}

Your order #{{ order.id }} has been confirmed.\n
Items:\n
{% for item in order.items %}
\t- {{ item.name }} ({{ item.quantity }}x)\n
{% if forloop.last %}\n{% endif %}
{% endfor %}

Total: ${{ order.total }}\n\n

Best regards,\n
{{ company.name }}
{% endfilter %}
""".strip()

        template = Template(template_string)

        context = Context(
            {
                "user": SimpleNamespace(name="John"),
                "order": SimpleNamespace(
                    id=123,
                    is_urgent=True,
                    total="49.90",
                    items=[
                        SimpleNamespace(name="Widget", quantity=2),
                        SimpleNamespace(name="Gadget", quantity=1),
                    ],
                ),
                "company": SimpleNamespace(name="ACME Inc."),
            }
        )

        rendered = template.render(context)

        expected = (
            "Hi John,\n\n"
            "⚠️ URGENT: Your order requires immediate attention!\n\n"
            "Your order #123 has been confirmed.\n"
            "Items:\n"
            "\t- Widget (2x)\n"
            "\t- Gadget (1x)\n\n"
            "Total: $49.90\n\n"
            "Best regards,\n"
            "ACME Inc."
        )

        self.assertEqual(rendered, expected)
