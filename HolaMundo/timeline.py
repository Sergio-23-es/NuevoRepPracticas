from datetime import date

# Lista de eventos del timeline
timeline = [{"fecha": date(10, 26, 2025), "evento": "Inicio del Proyecto"},
    {"fecha": date(10, 27, 2025), "evento": "Creación del Repositorio"},
    {"fecha": date(10, 28, 2025), "evento": "Creación de holamundo.py"},
    {"fecha": date(10, 29, 2025), "evento": "Pull request"},
    {"fecha": date(11, 4, 2025),  "evento": "Creación de dockerfile"},
    {"fecha": date(11, 5, 2025), "evento": "Creación del Time Line"}]
   

# Generar timeline en formato Markdown
with open("TIMELINE.md", "w", encoding="utf-8") as f:
    f.write("# 🕒 Timeline del Proyecto\n\n")
    f.write("| Fecha | Evento |\n")
    f.write("|--------|--------|\n")
    for item in timeline:
        f.write(f"| {item['fecha']} | {item['evento']} |\n")

print("Archivo TIMELINE.md generado correctamente.")
