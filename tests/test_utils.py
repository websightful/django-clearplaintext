from django.test import SimpleTestCase, override_settings

from clearplaintext.utils import render_to_plaintext

LOCMEM_TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "loaders": [
                (
                    "django.template.loaders.locmem.Loader",
                    {
                        "email.txt": (
                            r"Hi {{ name }},\n\n"
                            r"Your order #{{ order_id }} has been confirmed.\n"
                            r"Total: ${{ total }}\n\n"
                            r"Best regards,\n"
                            r"{{ company }}"
                        ),
                        "whitespace.txt": (
                            "   \n"
                            "   Hello   {{ name }}   \n"
                            "   \n"
                            "   Your message has been received.   \n"
                            "   \n"
                        ),
                    },
                )
            ],
        },
    }
]


@override_settings(TEMPLATES=LOCMEM_TEMPLATES)
class RenderToPlaintextTest(SimpleTestCase):
    def test_renders_template_and_applies_clean_plaintext(self):
        result = render_to_plaintext(
            "email.txt",
            {"name": "John", "order_id": 123, "total": "49.90", "company": "ACME Inc."},
        )

        expected = (
            "Hi John,\n\n"
            "Your order #123 has been confirmed.\n"
            "Total: $49.90\n\n"
            "Best regards,\n"
            "ACME Inc."
        )

        self.assertEqual(result, expected)

    def test_collapses_real_whitespace(self):
        result = render_to_plaintext("whitespace.txt", {"name": "Alice"})

        self.assertEqual(result, "Hello Alice Your message has been received.")

    def test_no_context(self):
        result = render_to_plaintext("whitespace.txt")

        self.assertEqual(result, "Hello Your message has been received.")
