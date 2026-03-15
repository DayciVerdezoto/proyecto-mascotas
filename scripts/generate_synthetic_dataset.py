from __future__ import annotations

import csv
import random
from pathlib import Path

random.seed(42)
N = 280

breeds = ["Labrador", "Golden Retriever", "Pastor Alemán", "French Bulldog", "Mestizo", "Beagle", "Boxer"]
sexes = ["M", "F"]
repro = ["entero", "esterilizado"]
sizes = ["pequeno", "mediano", "grande"]
motivos = ["masa palpable", "cojera", "perdida de apetito", "chequeo general", "sangrado local"]
ant = ["ninguno", "dermatitis", "cirugia previa", "obesidad", "endocrinopatia"]
ubicaciones = ["piel", "mama", "cavidad oral", "tejido subcutaneo", "extremidad", "bazo"]
formas = ["nodular", "irregular", "lobulada", "difusa"]
consistencias = ["blanda", "firme", "dura"]
movilidades = ["movil", "semi-fija", "fija"]
bordes = ["definidos", "irregulares", "infiltrativos"]
crecimiento = ["lento", "moderado", "rapido"]
estudios = ["examen clinico", "citologia", "biopsia", "imagen"]
diag_cito = ["benigno", "sospechoso", "maligno", "no concluyente"]
diag_histo = ["benigno", "maligno", "inflamatorio", "no realizado"]
tipo_tumor = ["adenoma", "mastocitoma", "carcinoma", "lipoma", "linfoma", "sarcoma"]
grado = ["bajo", "intermedio", "alto", "no aplica"]
pleomorfismo = ["leve", "moderado", "severo", "no aplica"]
progresion = ["estable", "progresiva", "regresiva"]
pronostico = ["favorable", "reservado", "desfavorable"]
tratamiento = ["observacion", "cirugia", "quimioterapia", "cirugia+quimio", "paliativo"]
respuesta = ["sin tratamiento", "buena", "parcial", "mala"]
seguimiento = ["1 mes", "3 meses", "6 meses", "12 meses"]

rows = []
for _ in range(N):
    row = {
        "edad": round(random.uniform(1, 16), 1),
        "raza": random.choice(breeds),
        "sexo": random.choice(sexes),
        "estado_reproductivo": random.choice(repro),
        "peso": round(random.uniform(3, 45), 1),
        "tamano_corporal": random.choice(sizes),
        "motivo_consulta": random.choice(motivos),
        "antecedentes_medicos_previos": random.choice(ant),
        "masa_tumoral_previa": random.random() < 0.35,
        "tiempo_evolucion_lesion": round(random.uniform(0.2, 14), 1),
        "tratamientos_previos": random.choice(["ninguno", "antiinflamatorios", "antibioticos", "cirugia previa"]),
        "numero_lesiones": random.choice([1, 1, 1, 2, 2, 3]),
        "ubicacion_anatomica_tumor": random.choice(ubicaciones),
        "tamano_lesion": round(random.uniform(0.3, 9.0), 2),
        "forma_tumor": random.choice(formas),
        "consistencia": random.choice(consistencias),
        "movilidad": random.choice(movilidades),
        "bordes": random.choice(bordes),
        "velocidad_crecimiento": random.choice(crecimiento),
        "ulceracion": random.random() < 0.3,
        "invasion_tejidos_cercanos": random.random() < 0.22,
        "tipo_estudio_diagnostico": random.choice(estudios),
        "citologia_realizada": random.random() < 0.7,
        "biopsia_realizada": random.random() < 0.55,
        "histopatologia_realizada": random.random() < 0.5,
        "diagnostico_citologico": random.choice(diag_cito),
        "diagnostico_histopatologico": random.choice(diag_histo),
        "tipo_tumor": random.choice(tipo_tumor),
        "grado_tumoral": random.choice(grado),
        "indice_mitotico": round(random.uniform(0, 18), 1),
        "pleomorfismo_celular": random.choice(pleomorfismo),
        "necrosis_tumoral": random.random() < 0.28,
        "metastasis": random.random() < 0.18,
        "compromiso_ganglionar": random.random() < 0.24,
        "recurrencia_tumoral": random.random() < 0.21,
        "progresion_enfermedad": random.choice(progresion),
        "pronostico_clinico": random.choice(pronostico),
        "tipo_tratamiento": random.choice(tratamiento),
        "respuesta_tratamiento": random.choice(respuesta),
        "seguimiento_clinico": random.choice(seguimiento),
    }
    risk = 0
    risk += 1.2 if row["edad"] > 9 else 0
    risk += 1.5 if row["velocidad_crecimiento"] == "rapido" else 0
    risk += 1.2 if row["bordes"] in {"irregulares", "infiltrativos"} else 0
    risk += 1.8 if row["metastasis"] else 0
    risk += 1.2 if row["necrosis_tumoral"] else 0
    risk += 1.4 if row["invasion_tejidos_cercanos"] else 0
    risk += 1.3 if row["indice_mitotico"] >= 8 else 0
    risk += 0.8 if row["tamano_lesion"] >= 4 else 0
    risk += 1.4 if row["diagnostico_citologico"] == "maligno" else 0
    risk += 1.5 if row["diagnostico_histopatologico"] == "maligno" else 0
    risk -= 1.6 if row["tipo_tumor"] in {"adenoma", "lipoma"} else 0
    risk -= 1.2 if row["diagnostico_citologico"] == "benigno" else 0
    p = 1 / (1 + (2.71828 ** -(risk - 2.8)))
    row["cancer_confirmado"] = 1 if random.random() < p else 0

    for nullable in ["diagnostico_histopatologico", "grado_tumoral", "indice_mitotico", "respuesta_tratamiento"]:
        if random.random() < 0.07:
            row[nullable] = ""
    rows.append(row)

out = Path("data/sample/canine_cancer_dataset.csv")
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Dataset generated at {out} with {len(rows)} rows")
