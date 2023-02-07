from pypdf import PdfReader, PdfWriter
from sys import argv
from pathlib import PurePath

# Prüfe, ob ein Dokument in den Argumenten angefügt ist.
if len(argv) > 1:
    fi = argv[1]
else:
    print("Es wurden keine Pfade angegeben.")
    quit()


reader = PdfReader(fi)
writer = PdfWriter()


# Generiere einen neuen Dateinamen für die Ausgabe mit dem Zusatz "_compressed"
new_name = (f'{PurePath(fi).parents[0]}/{PurePath(fi).stem}_compressed{PurePath(fi).suffix}')


for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open(new_name, "wb") as f:
    writer.write(f)

print(f'Das Dokument wurde erfolgreich unter {new_name} ausgegeben.')