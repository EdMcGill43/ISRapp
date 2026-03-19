# 🧾 CFDI ISR Totalizer
💰 Suma automática del ISR en archivos XML de nómina (SAT).  
Herramienta desarrollada en Python para analizar múltiples archivos .xml de tipo CFDI (nómina) y calcular automáticamente el total de ISR retenido a partir de las deducciones registradas.

## Características
- 📂 Lectura masiva de archivos `.xml` (incluye subcarpetas)
- 🔎 Identificación específica del concepto **ISR**
- 💰 Suma automática de todos los importes de ISR encontrados
- 🧾 Compatible con CFDI de nómina (`nomina12`)
- ⚠️ Manejo de errores en XML inválidos o incompletos
- 📊 Resultado claro y directo en consola
  
---

## 🧠 ¿Qué busca exactamente el script?

Este script identifica nodos de deducción que cumplan con la siguiente estructura dentro del XML:

```xml
<nomina12:Deduccion Clave="ISPT" Concepto="ISR" Importe="XXXX.XX" TipoDeduccion="002"/>
```
---

## 🔎 Específicamente

- 🏷️ `Concepto="ISR"`
- 🔢 `Importe="XXXX.XX"` → valor que será sumado
- 🧾 Nodo dentro de `nomina12:Deducciones`

---

## 📌 Requisitos de los XML

Para que el script funcione correctamente, tus archivos deben:

- 📄 Ser CFDI de nómina válidos
- 🧩 Incluir el namespace `nomina12`
- 🏷️ Contener deducciones con concepto **ISR**
- 🔢 Tener el atributo `Importe` con formato numérico

---

## 🚀 Instrucciones de uso

1. 📂 Coloca todos tus archivos `.xml` en una carpeta  
2. ▶️ Ejecuta el script  
3. 💰 Obtén el total acumulado de ISR retenido  

---

## 💡 Casos de uso

- 🧾 Validación de ISR retenido en nómina  
- 📊 Conciliación fiscal rápida  
- 📁 Análisis de grandes volúmenes de CFDI  
- 🔍 Auditoría de deducciones  

---

## ⚙️ Tecnologías utilizadas

- 🐍 Python 3.10+  
- 📄 `xml.etree.ElementTree`  
- 🗂️ `os` / `pathlib`  

---

## 🔮 Futuras mejoras

- 🖥️ Interfaz gráfica (PyQt / TTKBootstrap)  
- 📤 Exportación a Excel  
- 📊 Desglose por empleado / fecha  
- ⚡ Barra de progreso  
- 🔎 Validación avanzada de CFDI  

---

## 🧩 Notas

- Este script está enfocado únicamente en el cálculo de ISR  
- Puede extenderse fácilmente para incluir otros conceptos (IMSS, subsidio, etc.)  
