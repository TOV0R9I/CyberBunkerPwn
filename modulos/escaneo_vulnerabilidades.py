# modulos/escaneo_vulnerabilidades.py

import os

def escaneo_vulnerabilidades_menu():
    while True:
        print("\n🐞 ESCANEO DE VULNERABILIDADES")
        print("1. 🚀 Nmap Vuln Scan")
        print("2. 🔬 Nikto (Web Server Scan)")
        print("3. ⚡ Nuclei (Plantillas CVE)")
        print("4. 🐍 SQLMap (Inyección SQL)")
        print("5. 🌐 WhatWeb (Fingerprint CMS)")
        print("6. 🦠 OpenVAS (Escaneo completo)")
        print("7. 💣 WPScan (WordPress)")
        print("8. 🐙 XSStrike (XSS)")
        print("9. 🚪 Dirb (Fuerza bruta directorios)")
        print("10. 🔙 Volver")

        opcion = input("\n👉 Elige una opción (1-10): ").strip()

        if opcion == "1":
            objetivo = input("🔎 Ingresa IP o dominio: ").strip()
            os.system(f"nmap -sV --script vuln {objetivo} || read")
        elif opcion == "2":
            objetivo = input("🌐 Ingresa la URL: ").strip()
            os.system(f"nikto -h {objetivo} || read")
        elif opcion == "3":
            objetivo = input("🌐 Ingresa la URL o IP: ").strip()
            os.system(f"nuclei -u {objetivo} || read")
        elif opcion == "4":
            url = input("🌐 Ingresa la URL vulnerable con parámetro (ej: http://x.com?id=1): ").strip()
            os.system(f"sqlmap -u \"{url}\" --batch --risk=3 --level=5 || read")
        elif opcion == "5":
            objetivo = input("🌐 Ingresa el dominio o IP: ").strip()
            os.system(f"whatweb -v {objetivo} || read")
        elif opcion == "6":
            print("🔧 Ejecuta OpenVAS con el comando: sudo gvm-check-setup y sudo gvm-start")
        elif opcion == "7":
            objetivo = input("🌐 Ingresa el dominio WordPress: ").strip()
            os.system(f"wpscan --url {objetivo} --enumerate vp || read")
        elif opcion == "8":
            objetivo = input("🌐 Ingresa la URL con parámetro (ej: http://x.com?q=): ").strip()
            os.system(f"cd XSStrike && python3 xsstrike.py -u {objetivo} || read")
        elif opcion == "9":
            objetivo = input("🌐 Ingresa la URL: ").strip()
            os.system(f"dirb {objetivo} || read")
        elif opcion == "10":
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")
