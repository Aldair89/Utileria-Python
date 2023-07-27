import subprocess

def enable_wifi():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enabled'])

def disable_wifi():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])

def enable_bluetooth():
    subprocess.run(['bthprops.cpl'])

def disable_bluetooth():
    subprocess.run(['bthprops.cpl'])

def enable_firewall():
    subprocess.run(['netsh', 'advfirewall', 'set', 'currentprofile', 'state', 'on'])

def disable_firewall():
    subprocess.run(['netsh', 'advfirewall', 'set', 'currentprofile', 'state', 'off'])

def enable_defender():
    subprocess.run(['Set-MpPreference', '-EnableRealtimeMonitoring', 'Enabled'])

def disable_defender():
    subprocess.run(['Set-MpPreference', '-EnableRealtimeMonitoring', 'Disabled'])

def enable_airplane_mode():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'admin=enabled'])

def disable_airplane_mode():
    subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'admin=disabled'])

while True:
    print("1. Activar Wi-Fi")
    print("2. Desactivar Wi-Fi")
    print("3. Activar Bluetooth")
    print("4. Desactivar Bluetooth")
    print("5. Activar Firewall")
    print("6. Desactivar Firewall")
    print("7. Activar Windows Defender")
    print("8. Desactivar Windows Defender")
    print("9. Activar Modo Avión")
    print("10. Desactivar Modo Avión")
    print("11. Salir")
    
    choice = input("Ingrese el número de la opción que desea utilizar: ")
    
    if choice == "1":
        enable_wifi()
        print("Wi-Fi activado.")
    elif choice == "2":
        disable_wifi()
        print("Wi-Fi desactivado.")
    elif choice == "3":
        enable_bluetooth()
        print("Bluetooth activado.")
    elif choice == "4":
        disable_bluetooth()
        print("Bluetooth desactivado.")
    elif choice == "5":
        enable_firewall()
        print("Firewall activado.")
    elif choice == "6":
        disable_firewall()
        print("Firewall desactivado.")
    elif choice == "7":
        enable_defender()
        print("Windows Defender activado.")
    elif choice == "8":
        disable_defender()
        print("Windows Defender desactivado.")
    elif choice == "9":
        enable_airplane_mode()
        print("Modo Avión activado.")
    elif choice == "10":
        disable_airplane_mode()
        print("Modo Avión desactivado.")
    elif choice == "11":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
