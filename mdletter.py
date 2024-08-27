# created with gemini

import fpdf
import markdown
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

class DIN5002Letter:
    def __init__(self, recipient_address):
        self.pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
        self.pdf.set_auto_page_break(auto=True, margin=15)

        # Briefkopf (Platzhalter)
        self.pdf.cell(w=0, h=10, txt='Dein Name', ln=1, align='C')
        self.pdf.cell(w=0, h=10, txt='Deine Adresse', ln=1, align='C')

        # Leerzeile
        self.pdf.cell(w=0, h=5, ln=1)

        # Datum
        self.pdf.cell(w=0, h=10, txt=self.pdf.date, ln=1, align='R')

        # Brieffenster
        self.pdf.cell(w=0, h=5, ln=1)
        self.pdf.cell(w=100, h=50, txt=recipient_address, border=1, ln=1)

        # Leerzeile
        self.pdf.cell(w=0, h=5, ln=1)

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
        self.pdf.write_html(html)

    def save(self, filename="brief.pdf"):
        """
        Speichert das PDF unter dem angegebenen Dateinamen.

        Args:
            filename (str, optional): Der Dateiname. Defaults to "brief.pdf".
        """
        self.pdf.output(filename)

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

