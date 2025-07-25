# 🛡️ CyberBunkerPwn - www.cyberbunker.cl

**CyberBunkerPwn** es una plataforma de **pentesting automatizado** todo-en-uno diseñada para Red Team y Blue Team. Ideal para laboratorios controlados, Hack The Box, pruebas de seguridad educativa y entornos de formación profesional.

> 🎯 Automatiza, organiza y aprende cada fase del pentesting sin complicaciones.

---

## 🎮 Características principales

- 🔴 **Red Team**:
  - 🔍 Reconocimiento
  - 🌐 Enumeración Web
  - 🐞 Escaneo de Vulnerabilidades
  - 💣 Explotación (en desarrollo)
- 🔵 **Blue Team** (próximamente)
- ⚙️ Verificación automática de herramientas
- ✅ Instalación por arquitectura: Intel, AMD, ARM
- 📦 100% Offline Ready (sin necesidad de Docker ni entornos virtuales)

---

## 🚀 Captura de Pantalla

![CyberBunkerPwn](https://raw.githubusercontent.com/TOV0R9I/CyberBunkerPwn/main/assets/banner.png)  
*Interfaz principal en terminal con selección modular y ASCII personalizado.*

---

## 📦 Instalación

```bash
git clone https://github.com/TOV0R9I/CyberBunkerPwn.git
cd CyberBunkerPwn
sudo python3 main.py


CyberBunkerPwn/
├── core/
│   └── tool_checker.py         # Verifica herramientas e instala si faltan
├── modules/
│   ├── reconocimiento.py       # Módulo de Reconocimiento
│   ├── enumeracion_web.py      # Módulo de Enumeración Web
│   └── escaneo_vulnerabilidades.py # Módulo de Escaneo
├── XSStrike/                   # Herramienta integrada para XSS
├── main.py                     # Menú principal y ejecución
├── README.md
└── .gitignore


🧠 Créditos

Creado por TOV0R9I para la comunidad de ciberseguridad ética y profesional.

🛠️ Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
