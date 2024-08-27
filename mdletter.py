# created with gemini

import weasyprint
from weasyprint import HTML
import markdown
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

class DIN5002Letter:
    def __init__(self, recipient_address):
        self.recipient_address = recipient_address
        self.html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                /* Hier können Sie weitere CSS-Styles hinzufügen */
                body { font-family: Arial, sans-serif; }
                .recipient-address { font-weight: bold; }
                /* GitHub Markdown CSS */
                /* ... */
            </style>
        </head>
        <body>
            <div class="recipient-address">{}</div>
            {}
        </body>
        </html>
        """

    def write(self, markdown_content):
        """
        Schreibt den Markdown-Inhalt in das PDF.

        Args:
            markdown_content (str): Der Markdown-Text.
        """

        html = markdown.markdown(
            markdown_content,
            extensions=[
                ExtraExtension(),
                CodeHiliteExtension(use_pygments=True, style='github'),
                TocExtension(baselevel=2)
            ]
        )
        self.html_content = self.html_template.format(self.recipient_address, html)

    def save(self, file_object):
        """
        Speichert das PDF unter dem angegebenen Dateinamen.

        Args:
            filename (str, optional): Der Dateiname. Defaults to "brief.pdf".
        """
        html = HTML(string=self.html_content)

        # Without arguments, this method returns a byte string in memory. If you pass a file name or a writable file object, they will write there directly instead. (Warning: with a filename, these methods will overwrite existing files silently.)
        html.write_pdf(file_object, stylesheets=["https://cdn.jsdelivr.net/npm/github-markdown-css@4.0.0/github-markdown.css"])

if __name__ == "__main__":
    # Beispiel
    letter = DIN5002Letter("Max Mustermann\nMusterstraße 1\n12345 Musterstadt")
    letter.write("""
## Betreff: Wichtige Information

Hallo Max,

Dies ist ein Beispiel für einen Brief, der mit Markdown erstellt wurde. 

* **Fettdruck** und _Kursivschrift_ funktionieren.
* Auch Codeblöcke:
```python
print("Hallo Welt!")

```

Gruß,
Dein Name
""")
    letter.save("mein_brief.pdf")

