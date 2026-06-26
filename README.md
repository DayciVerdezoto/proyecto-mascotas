# 💰 Mi Presupuesto

Aplicación web sencilla para llevar tu presupuesto personal mensual. No necesita
instalación ni internet: es **un solo archivo** (`index.html`) que abres en
cualquier navegador, en la computadora o el celular. Tus datos se guardan en el
propio dispositivo.

## Cómo usarla

1. Abre el archivo **`index.html`** (doble clic, o arrástralo al navegador).
2. ¡Listo! Empieza a registrar.

## Qué puedes hacer

### 📥 Ingresos
- Registra tus ingresos por categoría (Salario, Freelance, Bono, etc.).
- El **total se suma automáticamente**.

### 📤 Categorías de gasto y presupuesto
Cada categoría tiene un **presupuesto asignado** y es de uno de dos tipos:

- **Pago fijo** (renta, servicios básicos, préstamos, tarjetas, niños): la marcas
  como **pagada** y la tarjeta se pinta de **verde** ✅.
- **Gasto variable** (alimentación, comidas fuera de casa, transporte): registras
  cada gasto y el presupuesto **se va devengando**. Una barra muestra cuánto llevas.

Vienen precargadas las categorías que sueles usar; puedes **editarlas, borrarlas o
agregar nuevas**.

### 🚦 Semáforo y alertas
- **Verde**: vas bien o ya está pagado.
- **Amarillo**: llegaste o pasaste el **80%** del presupuesto → aparece una alerta.
- **Rojo**: te **excediste** del presupuesto.

Las alertas se muestran arriba de todo para que no se te pasen.

### 📊 Resumen del mes
Arriba ves cuatro indicadores: **ingresos**, **presupuesto asignado**,
**gastado/pagado** y **saldo disponible**.

### 🗓️ Por mes
Usa las flechas `‹ ›` del encabezado para moverte entre meses. Cada mes es
independiente. Con **“Copiar presupuesto del mes anterior”** reutilizas tus
categorías y montos sin tener que volver a escribirlos.

### 💾 Respaldo
- **Exportar respaldo**: descarga un archivo con todos tus datos.
- **Importar respaldo**: restaura tus datos en este u otro dispositivo.

## Notas

- La moneda por defecto es el Quetzal (`Q`). Para cambiarla, edita la línea
  `const MONEDA = "Q";` al inicio del bloque `<script>` en `index.html`
  (por ejemplo `"$"`).
- El umbral de alerta es el 80% (`const UMBRAL_ALERTA = 0.8;`); puedes ajustarlo.
- Los datos viven en el navegador donde la usas. Si limpias el historial/datos del
  navegador, usa un respaldo para recuperarlos.
