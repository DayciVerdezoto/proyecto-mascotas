# 💪 FitCoach — Tu entrenador de bolsillo

App web para **pérdida de grasa y ganancia muscular**. Es un **solo archivo**
(`fitness.html`): se abre en cualquier navegador (celular o computadora), sin
instalar nada, sin servidor y **100% privada** — todos tus datos se guardan solo
en tu dispositivo (`localStorage`).

Funciona como un reemplazo de un entrenador especializado en **nutrición,
deportología y acondicionamiento físico**: te entrevista, arma tu perfil y crea
un plan real, factible y con metas alcanzables.

## 🔒 Seguridad

Pensada para poder publicarse en un enlace público **sin exponer tus datos de salud**:

- **Acceso con usuario y contraseña** que tú creas la primera vez.
- La contraseña **nunca se guarda**. Con ella se **deriva una llave** usando
  **PBKDF2 (SHA-256, 250.000 iteraciones)**.
- Tus datos se guardan **cifrados con AES-256-GCM**. Sin tu contraseña son
  **ilegibles**, aunque alguien abra el archivo o el enlace.
- **Auto-bloqueo** tras 30 minutos de inactividad y opción de **cerrar sesión**.
- Si olvidas la contraseña **no hay recuperación** (ese es justamente el punto):
  solo puedes empezar de cero.
- La **copia de seguridad** que subes a Google Drive / iCloud también va
  **cifrada**: es el mismo cofre protegido por tu contraseña.

## ✨ Qué hace

- **Onboarding tipo entrevista**: te pregunta sexo, edad, altura, pesos,
  objetivo, actividad diaria (NEAT), ritmo y hábitos, y calcula tu plan.
- **Motor de balance energético**:
  - **TMB** (metabolismo basal) con la fórmula **Mifflin-St Jeor**.
  - **NEAT** (gasto por actividad diaria sin ejercicio).
  - **Ejercicio** con tablas de **METs** por actividad.
  - **TDEE** (gasto total) y **meta calórica** según objetivo y ritmo.
  - **Macros** objetivo (proteína alta para conservar/ganar músculo).
- **Registro de comidas**: base de alimentos con calorías y macros + tus
  **comidas frecuentes** guardadas para registro en 1 toque + entrada manual.
- **Registro de actividad física** y cálculo de quema calórica.
- **Tablero "Hoy"**: anillo de calorías (consumido vs. meta vs. ejercicio),
  macros y semáforo de cumplimiento diario.
- **Curva de peso**: gráfica de tendencia + progreso hacia tu meta.
- **Medidas corporales**: cuello, pecho, cintura, cadera, brazo, muslo,
  pantorrilla, con evolución.
- **Plan y metas**: proyección de fecha estimada, presupuesto energético,
  racha de cumplimiento, calendario de los últimos 14 días y consejos.
- **Copia de seguridad en la nube**: guarda una copia **cifrada** en tu
  **Google Drive o iCloud** con el menú de compartir del teléfono, y restaura
  desde ese archivo con tu contraseña (igual que la app de finanzas).

## 🧮 Cómo se calcula

| Concepto | Fórmula |
|---|---|
| TMB (hombre) | `10·kg + 6.25·cm − 5·edad + 5` |
| TMB (mujer) | `10·kg + 6.25·cm − 5·edad − 161` |
| Mantenimiento (TDEE) | `TMB × factor de actividad` |
| Meta (perder) | `TDEE − 300/500/700` (suave/moderado/agresivo) |
| Meta (ganar) | `TDEE + 200/300/450` |
| Meta (recomposición) | `TDEE − 200` con proteína alta |
| Quema ejercicio | `MET × peso(kg) × horas` |
| Cambio de peso | `≈ déficit·7 / 7700 kcal por kg de grasa` |

## 🚀 Uso

Abre `fitness.html` en tu navegador. La primera vez completas el onboarding;
después la app recuerda tu perfil y datos automáticamente.

> Nota: las estimaciones son orientativas y educativas. No sustituyen la
> valoración de un profesional de salud, especialmente si tienes condiciones
> médicas.
