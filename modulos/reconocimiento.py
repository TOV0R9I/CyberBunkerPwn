# modulos/reconocimiento.py

import os

def reconocimiento_menu():
    while True:
        print("\n\U0001f4e1 RECONOCIMIENTO")
        print("1. \U0001f50e Whois Lookup")
        print("2. \U0001f6f0 DNS Recon (nslookup / dig)")
        print("3. \U0001f4cd GeoIP (ipinfo.io)")
        print("4. \U0001f575 Subdominios con Subfinder")
        print("5. \U0001f9e0 Información con WhatWeb")
        print("6. \U0001f519 Volver")

        opcion = input("\n\U0001f449 Elige una opción (1-6): ").strip()

        if opcion == "1":
            dominio = input("\U0001f310 Ingresa el dominio (ej: example.com): ").strip()
            os.system(f"whois {dominio} || read")
        elif opcion == "2":
            dominio = input("\U0001f310 Ingresa el dominio o IP: ").strip()
            os.system(f"nslookup {dominio} || read")
            os.system(f"dig {dominio} any +short || read")
        elif opcion == "3":
            ip = input("\U0001f9ed Ingresa la IP: ").strip()
            os.system(f"curl ipinfo.io/{ip} || read")
        elif opcion == "4":
            dominio = input("\U0001f310 Ingresa el dominio: ").strip()
            os.system(f"subfinder -d {dominio} -silent || read")
        elif opcion == "5":
            objetivo = input("\U0001f310 Ingresa el dominio o IP: ").strip()
            os.system(f"whatweb -v {objetivo} || read")
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")
