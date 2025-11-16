from datetime import date

# Lista de eventos del timeline
timeline = [{"fecha": date(2025, 10, 26), "evento": "Inicio del Proyecto"},
    {"fecha": date(2025, 10, 27), "evento": "Creación del Repositorio"},
    {"fecha": date(2025, 10, 28), "evento": "Creación de holamundo.py"},
    {"fecha": date(2025, 10, 29), "evento": "Pull request"},
    {"fecha": date(2025, 11, 4),  "evento": "Creación de dockerfile"},
    {"fecha": date(2025, 11, 5), "evento": "Creación del Time Line"}]
   

# Generar timeline en formato Markdown
with open("TIMELINE.md", "w", encoding="utf-8") as f:
    f.write("# 🕒 Timeline del Proyecto\n\n")
    f.write("| Fecha | Evento |\n")
    f.write("|--------|--------|\n")
    for item in timeline:
        f.write(f"| {item['fecha']} | {item['evento']} |\n")

print("Archivo TIMELINE.md generado correctamente.")
