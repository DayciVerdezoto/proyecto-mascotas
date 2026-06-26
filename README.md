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

### 📅 Fecha en cada gasto
Cada gasto variable se registra con su **fecha** (por defecto la de hoy). En la
lista se muestra como una etiqueta `día/mes` y los gastos quedan ordenados por fecha.

### 📈 Distribución de gastos
Una **gráfica de dona** muestra qué porcentaje de tu dinero se va en cada categoría,
con su leyenda y montos. Se actualiza sola conforme registras pagos y gastos.

### 💱 Moneda
Elige tu moneda desde el **selector** en la parte inferior (`Q`, `$`, `€`, `MXN`,
`S/`, etc.). Queda guardada con tus datos.

### 💾 Respaldo
- **Exportar respaldo**: descarga un archivo con todos tus datos.
- **Importar respaldo**: restaura tus datos en este u otro dispositivo.

## 🌐 Usarla en línea (GitHub Pages)

El repositorio incluye un flujo automático (`.github/workflows/deploy-pages.yml`)
que publica la app en internet. Para activarlo **una sola vez**:

1. Ve a tu repositorio en GitHub → **Settings** → **Pages**.
2. En **Build and deployment → Source**, elige **GitHub Actions**.
3. Asegúrate de que estos cambios estén en la rama **main** (al fusionar el Pull
   Request se despliega solo).

Quedará disponible en `https://dayciverdezoto.github.io/proyecto-mascotas/` y podrás
abrirla desde el celular o la computadora sin el archivo.

> Nota: la versión en línea sigue guardando los datos **en cada dispositivo** (no se
> sincroniza sola entre celular y computadora). Para mover datos entre dispositivos,
> usa Exportar / Importar respaldo.

## Notas

- El umbral de alerta es el 80% (`const UMBRAL_ALERTA = 0.8;`); puedes ajustarlo
  al inicio del bloque `<script>` en `index.html`.
- Los datos viven en el navegador donde la usas. Si limpias el historial/datos del
  navegador, usa un respaldo para recuperarlos.
