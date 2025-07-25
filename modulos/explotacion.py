# modulos/explotacion.py

import os

def explotacion_menu():
    while True:
        print("\n💣 EXPLOTACIÓN")
        print("1. 📦 Metasploit Framework")
        print("2. 🧨 Explotar Samba (user_map_script)")
        print("3. 🛠️ Searchsploit")
        print("4. 🚪 Netcat Listener")
        print("5. 🐚 Reverse Shell Cheat Sheet")
        print("6. 🔙 Volver")

        opcion = input("\n👉 Elige una opción (1-6): ").strip()

        if opcion == "1":
            print("💡 Consejo: Usa `msfconsole` y luego `search exploit` o `use exploit/...` para comenzar.")
            os.system("msfconsole || read")
        elif opcion == "2":
            print("💣 Explotación de Samba con user_map_script...")
            print("Requiere acceso a una máquina vulnerable como Metasploitable 2.")
            ip = input("🌐 Ingresa la IP del objetivo: ").strip()
            os.system(f"nmap --script smb-vuln* -p 445 {ip} || read")
            print("👉 Para ejecutar manualmente: utiliza metasploit con el módulo: exploit/linux/samba/usermap_script")
        elif opcion == "3":
            query = input("🔍 ¿Qué deseas buscar en Exploit-DB?: ").strip()
            os.system(f"searchsploit {query} || read")
        elif opcion == "4":
            puerto = input("📡 Ingresa el puerto para escuchar conexiones: ").strip()
            os.system(f"nc -lvnp {puerto} || read")
        elif opcion == "5":
            print("🌐 Accede a: https://www.revshells.com/ para obtener comandos de Reverse Shell.")
            os.system("xdg-open https://www.revshells.com/")
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")
