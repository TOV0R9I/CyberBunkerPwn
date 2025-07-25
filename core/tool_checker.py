import os
import shutil
from typing import List

herramientas = [
    {"nombre": "go", "verificar": "go", "instalar": "sudo apt install golang -y"},
    {"nombre": "unzip", "verificar": "unzip", "instalar": "sudo apt install unzip -y"},
    {"nombre": "wget", "verificar": "wget", "instalar": "sudo apt install wget -y"},
    {"nombre": "curl", "verificar": "curl", "instalar": "sudo apt install curl -y"},
    {"nombre": "snapd", "verificar": "snap", "instalar": "sudo apt install snapd -y"},
    {"nombre": "nmap", "verificar": "nmap", "instalar": "sudo apt install nmap -y"},
    {"nombre": "chisel", "verificar": "chisel", "instalar": "sudo apt install chisel -y"},

   {
    "nombre": "xsstrike",
    "verificar": "xsstrike",
    "instalar": (
        "echo '[+] Instalando XSStrike con pipx...'; "
        "if ! command -v pipx &>/dev/null; then "
        "echo '[*] pipx no encontrado. Instalando...'; "
        "sudo apt install pipx -y && pipx ensurepath; "
        "fi; "
        "pipx install git+https://github.com/s0md3v/XSStrike.git && "
        "echo '[✔] XSStrike instalado correctamente con pipx.'"
    ),
    "mensaje_error": (
        "⚠ No se pudo instalar XSStrike.\n"
        "👉 Asegúrate de tener pipx instalado con: sudo apt install pipx -y\n"
        "🔧 Luego ejecuta: pipx install git+https://github.com/s0md3v/XSStrike.git"
    )
},

    {"nombre": "dalfox", "verificar": "dalfox", "instalar": "go install github.com/hahwul/dalfox/v2@latest"},
    {"nombre": "ffuf", "verificar": "ffuf", "instalar": "sudo apt install ffuf -y"},
    {"nombre": "httpx", "verificar": "httpx", "instalar": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"},
    {"nombre": "masscan", "verificar": "masscan", "instalar": "sudo apt install masscan -y"},
    {"nombre": "nikto", "verificar": "nikto", "instalar": "sudo apt install nikto -y"},
    {"nombre": "sqlmap", "verificar": "sqlmap", "instalar": "sudo apt install sqlmap -y"},
    {"nombre": "whatweb", "verificar": "whatweb", "instalar": "sudo apt install whatweb -y"},
    {"nombre": "gobuster", "verificar": "gobuster", "instalar": "sudo apt install gobuster -y"},
    {"nombre": "amass", "verificar": "amass", "instalar": "sudo snap install amass"},
    {"nombre": "theHarvester", "verificar": "theHarvester", "instalar": "sudo apt install theharvester -y"},
    {"nombre": "subfinder", "verificar": "subfinder", "instalar": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"},
    {"nombre": "dirsearch", "verificar": "dirsearch", "instalar": "git clone https://github.com/maurosoria/dirsearch.git"},
    {"nombre": "wpscan", "verificar": "wpscan", "instalar": "sudo gem install wpscan"},
    {"nombre": "msfconsole", "verificar": "msfconsole", "instalar": "sudo apt install metasploit-framework -y"},
    {"nombre": "seclists", "verificar": "/usr/share/seclists", "instalar": "sudo apt install seclists -y"},
    {"nombre": "dirb", "verificar": "dirb", "instalar": "sudo apt install dirb -y"},
    {"nombre": "john", "verificar": "john", "instalar": "sudo apt install john -y"},
    {"nombre": "hydra", "verificar": "hydra", "instalar": "sudo apt install hydra -y"},
    {"nombre": "openvas", "verificar": "gvm", "instalar": "sudo apt install gvm -y"},
    {"nombre": "nessus", "verificar": "/opt/nessus", "instalar": "echo 'Descargar manualmente desde https://www.tenable.com/products/nessus'"},
    {"nombre": "rustscan", "verificar": "rustscan", "instalar": "sudo snap install rustscan"},
    {"nombre": "winpeas.bat", "verificar": "/root/winPEAS.bat", "instalar": "wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEAS.bat -O /root/winPEAS.bat"},

    {
        "nombre": "nuclei",
        "verificar": "nuclei",
        "instalar": (
            "ARCH=$(uname -m); "
            "echo '[*] Arquitectura detectada: $ARCH'; "
            "if [ \"$ARCH\" = \"x86_64\" ] || [ \"$ARCH\" = \"amd64\" ]; then "
            "echo '[+] Instalando nuclei para amd64...'; "
            "wget https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei_3.4.7_linux_amd64.zip && "
            "unzip nuclei_3.4.7_linux_amd64.zip && "
            "sudo mv nuclei /usr/local/bin/ && chmod +x /usr/local/bin/nuclei && "
            "rm nuclei_3.4.7_linux_amd64.zip; "
            "elif [ \"$ARCH\" = \"aarch64\" ] || [ \"$ARCH\" = \"arm64\" ]; then "
            "echo '[+] Instalando nuclei desde Go para ARM...'; "
            "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && "
            "sudo mv ~/go/bin/nuclei /usr/local/bin/ && chmod +x /usr/local/bin/nuclei; "
            "else "
            "echo '[!] Arquitectura no soportada automáticamente. Instala nuclei manualmente.'; "
            "exit 1; "
            "fi"
        )
    },

    {"nombre": "nodejs", "verificar": "node", "instalar": "sudo apt install nodejs npm -y"},
    {"nombre": "hakrawler", "verificar": "hakrawler", "instalar": "go install github.com/hakluke/hakrawler@latest && sudo mv ~/go/bin/hakrawler /usr/local/bin/"},

    {
        "nombre": "Webanalyze",
        "verificar": "webanalyze",
        "instalar": (
            "echo '[+] Instalando webanalyze...'; "
            "cd ~ && "
            "git clone https://github.com/rverton/webanalyze.git && "
            "cd webanalyze && "
            "go build -o webanalyze && "
            "chmod +x webanalyze && "
            "sudo mv webanalyze /usr/local/bin/ && "
            "cd .. && rm -rf webanalyze && "
            "echo '[✔] Webanalyze instalado en /usr/local/bin/webanalyze'"
        ),
        "mensaje_error": (
            "⚠ Webanalyze no se ejecutó correctamente.\n"
            "📌 Asegúrate de tener Go instalado y compilarlo con:\n"
            "   git clone https://github.com/rverton/webanalyze.git && cd webanalyze && go build -o webanalyze\n"
            "🔧 Luego mueve el binario a una ruta válida:\n"
            "   sudo mv webanalyze /usr/local/bin/ && chmod +x /usr/local/bin/webanalyze\n"
            "👉 Verifica luego con: webanalyze -h"
        )
    }
]

def verificar_herramientas_basicas():
    for herramienta in herramientas:
        nombre = herramienta["nombre"]
        verificar = herramienta["verificar"]
        instalar = herramienta["instalar"]

        existe = shutil.which(verificar) if not verificar.startswith("/") else os.path.exists(verificar)
        if existe:
            print(f"[✔] {nombre} está instalado.")
        else:
            print(f"[✘] {nombre} no está instalado.")
            print(f"[+] Instalando {nombre}...")
            resultado = os.system(instalar)
            if resultado == 0:
                print(f"[✔] Instalación de {nombre} finalizada.\n")
            else:
                print(f"[!] Error al instalar {nombre}.\n")
