from PIL import Image, ImageDraw, ImageFont
import os

# Dimensione immagine
width, height = 1000, 1000

# Colori
bg_color = (255, 255, 255)    # bianco
text_color = (200, 0, 0)      # verde

# Carica il font Titillium Bold a 150px
font_path = "TitilliumWeb-Bold.ttf"  # Assicurati che il file sia qui
font_size = 150
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("⚠️ Impossibile caricare il font TitilliumWeb-Bold.ttf. Assicurati che sia nella cartella.")
    exit()

# Genera le immagini
for i in range(1, 11):
    text = f"img{i} setC"

    # Crea immagine bianca
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Calcola posizione centrata
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)

    # Disegna il testo
    draw.text(position, text, fill=text_color, font=font)

    # Salva immagine
    filename = f"img{i}_setC.png"
    img.save(filename)

print("✅ Immagini generate con successo.")

