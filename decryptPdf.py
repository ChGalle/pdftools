from pypdf import PdfReader, PdfWriter
from sys import argv
from pathlib import PurePath
import stdiomask

# Prüfe, ob ein Dokument in den Argumenten angefügt ist.
if len(argv) > 1:
    fi = argv[1]
else:
    print("Es wurden keine Pfade angegeben.")
    quit()

reader = PdfReader(fi)
writer = PdfWriter()



# Generiere einen neuen Dateinamen für die Ausgabe mit dem Zusatz "_decrypted"
new_name = (f'{PurePath(fi).parents[0]}/{PurePath(fi).stem}_decrypted{PurePath(fi).suffix}')

if reader.is_encrypted:
    reader.decrypt(stdiomask.getpass(prompt="Bitte gib das Passwort ein: "))

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Save the new PDF to a file
with open(new_name, "wb") as f:
    writer.write(f)

print(f'Das Dokument wurde erfolgreich unter {new_name} ausgegeben.')