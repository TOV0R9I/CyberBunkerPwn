# modulos/enumeracion_web.py

import os

def enumeracion_web_menu():
    while True:
        print("\n\U0001f310 ENUMERACIÓN WEB")
        print("1. \U0001f4dc Encabezados HTTP (curl)")
        print("2. \U0001f4c2 Fuerza bruta de archivos con FFUF")
        print("3. \U0001f9e0 CMS Detect con Webanalyze")
        print("4. \U0001f578 Links con hakrawler")
        print("5. \U0001f4d1 HTTP Methods (curl)")
        print("6. \U0001f519 Volver")

        opcion = input("\n\U0001f449 Elige una opción (1-6): ").strip()

        if opcion == "1":
            objetivo = input("\U0001f310 Ingresa la URL: ").strip()
            os.system(f"curl -I {objetivo} || read")
        elif opcion == "2":
            objetivo = input("\U0001f310 Ingresa la URL (ej: https://ejemplo.com): ").strip()
            wordlist = "/usr/share/seclists/Discovery/Web-Content/common.txt"
            os.system(f"ffuf -u {objetivo}/FUZZ -w {wordlist} -e .php,.html,.bak -t 30 || read")
        elif opcion == "3":
            objetivo = input("\U0001f310 Ingresa la URL (ej: https://ejemplo.com): ").strip()
            resultado = os.system(f"webanalyze -host {objetivo}")
            if resultado != 0:
                print("\n⚠ Webanalyze no se ejecutó correctamente.")
                print("📌 Asegúrate de tener permisos de ejecución o de haber instalado el binario correctamente.")
                print("👉 Puedes verificar con: chmod +x webanalyze")
        elif opcion == "4":
            objetivo = input("\U0001f310 Ingresa la URL: ").strip()
            os.system(f"hakrawler -url {objetivo} || read")
        elif opcion == "5":
            objetivo = input("\U0001f310 Ingresa la URL: ").strip()
            os.system(f"curl -X OPTIONS -i {objetivo} || read")
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")
