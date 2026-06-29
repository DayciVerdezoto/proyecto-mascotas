# 🔐 Presupuestos

Aplicación web para llevar tu **presupuesto personal mensual**, con una **capa de
seguridad real**: acceso con usuario y contraseña, y **todos tus datos cifrados**
en tu propio dispositivo. Es **un solo archivo** (`index.html`): se abre en
cualquier navegador (celular o computadora), sin instalar nada.

## 🔒 Seguridad

Pensada para poder publicarse en un enlace público **sin exponer tu información**:

- **Acceso con usuario y contraseña** que tú creas la primera vez.
- La contraseña **nunca se guarda**. Con ella se **deriva una llave** usando
  **PBKDF2 (SHA-256, 250.000 iteraciones)**.
- Tus datos se guardan **cifrados con AES-256-GCM** (estándar de cifrado fuerte).
  Sin tu contraseña, son **ilegibles**, aunque alguien tenga acceso a tu dispositivo
  o al archivo.
- **Bloqueo automático** tras 15 minutos de inactividad y botón **🔒 Salir**.
- **Cambio de contraseña** que vuelve a cifrar todos tus datos.
- **Respaldo cifrado**: el archivo de exportación también queda protegido por tu
  contraseña.

> ⚠️ **Importante:** como la seguridad es real, **si olvidas tu contraseña no hay
> forma de recuperar los datos**. Guarda tu contraseña en un lugar seguro y haz
> respaldos.

### ¿Por qué cifrado y no solo "una pantalla de contraseña"?

Una app que vive en una página pública no puede ocultar su código, así que una
contraseña que solo tape la pantalla podría saltarse. Por eso la protección de
verdad está en **cifrar los datos**: lo único que vería un extraño en el enlace
público es una pantalla de inicio de sesión; tu información sigue cifrada y solo
en tu dispositivo (nunca se sube a internet).

## Cómo usarla

1. Abre **`index.html`** (doble clic) o el enlace publicado.
2. La **primera vez**: crea tu usuario y contraseña → se genera tu cuenta cifrada.
3. Las siguientes veces: inicia sesión con tu usuario y contraseña.

## Funciones de presupuesto

- **📥 Ingresos por categoría** con total automático.
- **📤 Categorías de gasto con presupuesto**, de dos tipos:
  - **Pago fijo** (renta, servicios, préstamos, tarjetas, niños): se marca como
    pagada → se pinta de **verde** ✅.
  - **Gasto variable** (alimentación, comidas fuera, transporte): registras cada
    gasto (con su fecha) y el presupuesto **se va devengando**.
- **🚦 Semáforo + alerta al 80%**: verde / amarillo (≥80%, con aviso) / rojo (excedido).
- **📊 Resumen**: ingresos, presupuesto asignado, gastado/pagado y saldo disponible.
- **📈 Gráfica de dona** con la distribución de gastos por categoría.
- **💱 Selector de moneda** (Q, $, €, MXN, S/, etc.).
- **🗓️ Manejo por mes** + copiar el presupuesto del mes anterior.
- **💾 Exportar / Importar respaldo** (cifrado).

## 🌐 Publicar en línea (GitHub Pages)

El repositorio incluye `.github/workflows/deploy-pages.yml`, que publica la app
automáticamente. Para que el sitio quede accesible se requiere que el repositorio
sea **público** (o un plan que permita Pages en repos privados). Una vez público,
el flujo activa Pages solo y la app queda en:

`https://dayciverdezoto.github.io/proyecto-mascotas/`

Gracias al cifrado, publicarla en un enlace público **no expone tus datos**.

> Nota: los datos se guardan **en cada dispositivo** (no se sincronizan solos entre
> celular y computadora). Para moverlos, usa **Exportar / Importar respaldo**.
