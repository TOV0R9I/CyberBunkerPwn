import os
from core.tool_checker import verificar_herramientas_basicas
from modulos.reconocimiento import reconocimiento_menu
from modulos.enumeracion_web import enumeracion_web_menu
from modulos.escaneo_vulnerabilidades import escaneo_vulnerabilidades_menu
from modulos.explotacion import explotacion_menu

def banner():
    os.system("clear")
    print(r"""
             .-"      "-.
            /            \
           |              |
           |,  .-.  .-.  ,|
           | )(_o/  \o_)( |
           |/     /\     \|
           (_     ^^     _)
            \__|IIIIII|__/
             | \IIIIII/ |
             \          /
              `--------`

     💀 CYBERBUNKERPWN - PENTESTING AUTOMATIZADO 💀
""")
    print("\u2500" * 60)
    print("Una herramienta modular todo-en-uno para Red Team y Blue Team.")
    print("Realiza cada fase del pentesting de forma automática, organizada")
    print("y educativa, ideal para entornos como Hack The Box y laboratorios.\n")
    print("\U0001f916 Automatiza tareas, ejecuta herramientas clave y exporta resultados.")
    print("\U0001f9ea Perfecta para estudiantes, pentesters y entornos controlados.")
    print("\U0001f310 www.cyberbunker.cl")
    print("\u2500" * 60 + "\n")

def red_team_menu():
    while True:
        print("\n🔴 RED TEAM - FASE DE ATAQUE")
        print("1. 🔍 Reconocimiento")
        print("2. 🌐 Enumeración Web")
        print("3. 🐞 Escaneo de Vulnerabilidades")
        print("4. 💣 Explotación")
        print("5. 🔙 Volver al menú principal")

        opcion = input("\n👉 Elige una opción (1-5): ").strip()

        if opcion == "1":
            reconocimiento_menu()
        elif opcion == "2":
            enumeracion_web_menu()
        elif opcion == "3":
            escaneo_vulnerabilidades_menu()
        elif opcion == "4":
            explotacion_menu()
        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

def menu_principal():
    while True:
        print("\n🚩 MENÚ PRINCIPAL")
        print("¿De qué team eres?")
        print("1. 🔴 Red Team (Ataque)")
        print("2. 🔵 Blue Team (Defensa) [en desarrollo]")
        print("3. 🔧 Verificar herramientas instaladas")
        print("4. ❌ Salir")

        opcion = input("\n👉 Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            red_team_menu()
        elif opcion == "2":
            print("\n🔧 Módulo Blue Team en construcción. ¡Próximamente!")
        elif opcion == "3":
            verificar_herramientas_basicas()
        elif opcion == "4":
            print("\n👋 Saliendo de CyberBunkerPwn. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

def main():
    banner()
    menu_principal()

if __name__ == "__main__":
    main()
