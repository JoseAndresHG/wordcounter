# Prueba Técnica de Automatización

> Repositorio dedicado a la prueba tecnica wordcounter.

---

## 📋 Índice
1. [Sobre el Proyecto](#-sobre-el-proyecto)
2. [Tecnologías Utilizadas](#%EF%B8%8F-tecnologías-utilizadas)
3. [Instalación y Configuración](#%EF%B8%8F-instalación-y-configuración)
4. [Ejecución de Pruebas](#-ejecución-de-pruebas)

---

## 🚀 Sobre el Proyecto
Esta prueba tecnica contiene los casos desarrollados.
*   **Automatización Web:** Desarrollada utilizando Selenium.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Herramienta / Framework |
| :--- | :--- |
| **IDE** | Visual Studio Code |
| **Core Web** | Selenium |
| **BDD Framework** | Behave / Cucumber |
| **Reporte** | Allure |

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para replicar el entorno de desarrollo y dejarlo listo para la ejecución:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/JoseAndresHG/wordcounter.git](https://github.com/JoseAndresHG/wordcounter.git)
   cd wordcounter

2. **Instalar dependencias:**
   ```bash
    pip install -r requirements.txt

3. **Ejecutar todos los test y genera reporte:**
   ```bash
    ./run.sh

4. **Ejecutar todos los test:**
   ```bash
    behave features/word_counter.feature
