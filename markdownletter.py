# created with gemini
import fitz  # pymupdf
import markdown
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

class DIN5002Letter:
    def __init__(self, recipient_address):
        self.recipient_address = recipient_address
        self.pdf_document = fitz.open()
        self.page = self.pdf_document.new_page(width=595, height=842)  # DIN A4 in Punkten

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

        # Erstelle ein HTML-Element für die Empfängeradresse
        recipient_address_html = f"<div class='recipient-address'>{self.recipient_address}</div>"

        # Füge den HTML-Inhalt zur Seite hinzu
        self.page.insert_html(
            0,
            html=recipient_address_html + html,
            font_name="Times-Roman",
            font_size=12,
            spacing=1.5
        )

    def save(self):
        """
        Speichert das PDF unter dem angegebenen Dateinamen.

        Args:
            filename (str, optional): Der Dateiname. Defaults to "brief.pdf".
        """
        return self.pdf_document.write()

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

