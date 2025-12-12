import platform
import os
import time
import shutil
import subprocess
import sys
import ctypes
import importlib


print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░      ░░░         ░   ░░░░░░░░░   ░░░░░   ░░░░   ░   ░░░   ░░░░░░░░░░░░░   ░░░░   ░░░░░░░   ░      ░░░░░
▒   ▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒   ▒▒▒   ▒   ▒   ▒▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒   ▒  ▒   ▒▒▒    ▒   ▒▒▒   ▒▒
▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒ ▒   ▒   ▒▒▒▒   ▒
▓▓▓▓   ▓▓▓▓▓       ▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓  ▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓   ▓▓▓▓   ▓
▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓   ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓  ▓▓   ▓   ▓▓▓▓   ▓
▓   ▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓   ▓▓▓   ▓   ▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓▓   ▓▓▓   ▓   ▓▓▓▓▓▓▓   ▓   ▓▓▓   ▓▓
███      ███         ███████   ██████████     ███   █   █████   ██████████     ███   ███████   █      █████
███████████████████████████████████████████████████████████████████████████████████████████████████████████""")
print("""
░░    ░░ ░░░░░░░ ░░░░░░░ ░░░░░░      ░░░░░░  ░░ ░░░░░░░ ░░░░░░░░ ░░░░░░  ░░ ░░░░░░  ░░    ░░ ░░░░░░░░ ░░  ░░░░░░  ░░░    ░░ 
▒▒    ▒▒ ▒▒      ▒▒      ▒▒   ▒▒     ▒▒   ▒▒ ▒▒ ▒▒         ▒▒    ▒▒   ▒▒ ▒▒ ▒▒   ▒▒ ▒▒    ▒▒    ▒▒    ▒▒ ▒▒    ▒▒ ▒▒▒▒   ▒▒ 
▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒      ▒▒   ▒▒ ▒▒ ▒▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒  ▒▒ ▒▒▒▒▒▒  ▒▒    ▒▒    ▒▒    ▒▒ ▒▒    ▒▒ ▒▒ ▒▒  ▒▒ 
▓▓    ▓▓      ▓▓ ▓▓      ▓▓   ▓▓     ▓▓   ▓▓ ▓▓      ▓▓    ▓▓    ▓▓   ▓▓ ▓▓ ▓▓   ▓▓ ▓▓    ▓▓    ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  ▓▓ ▓▓ 
 ██████  ███████ ███████ ██   ██     ██████  ██ ███████    ██    ██   ██ ██ ██████   ██████     ██    ██  ██████  ██   ████ 

""")
print("")
print("")
print("")


Version = "0.0.1 [ALPHA TESTING VERSION]"
Distrubution = "User distribution"

# HELP COMMANDY
class pls:
    @staticmethod
    def helpni():
        print("Help příkazy:")
        print("pls.helpniclass pro pomoc s classami")

    @staticmethod
    def helpniclass():
        print("==============================================")
        print("| {:<10} | {:<35} |".format("Třída", "Popis"))
        print("==============================================")
        print("| {:<10} | {:<35} |".format("pls", "Pomáhá a udává samotné informace"))
        print("|            | dotazovacím jazyku Ševčík.            |")
        print("----------------------------------------------")
        print("| {:<10} | {:<35} |".format("mluvic", "Spravuje nastavení konzole."))
        print("----------------------------------------------")
        print("| {:<10} | {:<35} |".format("pleska", "Čte informace ze systému."))
        print("==============================================")

    @staticmethod
    def info_o_tobe():
        print(f"Verze této aplikace je: {Version}")
        print(f"Gitbook nápověda:    https://sevcik-cmd.gitbook.io/sevcik-cmd-docs")
        print(f"Webová stránka:     (zatím není k dispozici)")
        print(f"Vaše distrubuce:    {Distrubution}")
        if Distrubution == "User distribution":
            print("Neplacená verze")
        else:
            print("Placená distribuce")


# COMMANDY PRO PRÁCI S KONZOLÍ
class mluvic:
    @staticmethod
    def vycisti():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def rekni(to_rekni):
        print("Ševčík CMD:      ", to_rekni)


# COMMANDY PRO VYPSÁNÍ OBECNÝCH INFORMACÍ
class pleska:
    @staticmethod
    def infosys():
        print("System:", platform.system())
        print("Node name:", platform.node())
        print("Release:", platform.release())
        print("Version:", platform.version())
        print("Machine:", platform.machine())
        print("Processor:", platform.processor())

    @staticmethod
    def kdo_su_ja():
        try:
            user = os.getlogin()
            print("Aktuálně přihlášený uživatel:", user)
        except Exception as e:
            print("Nepodařilo se zjistit uživatele:", e, "zkus zkontrolovat oprávnění!")

    @staticmethod
    def jaky_cislo_jsi():
        print(Version)
    

# STŘEDNĚ KOMPLEXNÍ COMMANDY KTERÉ PRACUJÍ S PC
class sevcik:
    # PRÁCE SE SOUBORY A SLOŽKAMI
    @staticmethod
    def vypis_slozky_ve_slozce(cesta_od_rootu):
        if not os.path.isabs(cesta_od_rootu):
            print("Chyba: Zadej absolutní cestu (od rootu, např. /home/uzivatel).")
            return

        if not os.path.exists(cesta_od_rootu):
            print(f"Chyba: Cesta '{cesta_od_rootu}' neexistuje.")
            return

        print(f"Složky v: {cesta_od_rootu}")
        for polozka in os.listdir(cesta_od_rootu):
            cela_cesta = os.path.join(cesta_od_rootu, polozka)
            if os.path.isdir(cela_cesta):
                print(f"📁 {polozka}")

    @staticmethod
    def co_je_tu(cesta_od_rootu):
        if not os.path.isabs(cesta_od_rootu):
            print("Chyba: Zadej absolutní cestu (od rootu, např. /home/uzivatel).")
            return

        if not os.path.exists(cesta_od_rootu):
            print(f"Chyba: Cesta '{cesta_od_rootu}' neexistuje.")
            return

        print(f"Soubory v: {cesta_od_rootu}")
        for polozka in os.listdir(cesta_od_rootu):
            cela_cesta = os.path.join(cesta_od_rootu, polozka)
            if os.path.isfile(cela_cesta):
                print(f"📄 {polozka}")

    @staticmethod
    def otevri_soubor(cesta_k_souboru):
        if not os.path.isabs(cesta_k_souboru):
            print("Chyba: Zadej absolutní cestu k souboru (od rootu).")
            return
        if not os.path.isfile(cesta_k_souboru):
            print(f"Chyba: Soubor '{cesta_k_souboru}' neexistuje.")
            return

        try:
            system = platform.system()
            if system == "Windows":
                os.startfile(cesta_k_souboru)  # Otevře asociovaným programem
            elif system == "Darwin":  # macOS
                subprocess.run(["open", cesta_k_souboru])
            else:  # Linux a další
                subprocess.run(["xdg-open", cesta_k_souboru])
            print(f"Otevírám soubor: {cesta_k_souboru}")
        except Exception as e:
            print(f"Chyba při otevírání souboru: {e}")

    @staticmethod
    def zkopiruj_soubor_do(cesta_k_souboru, cilova_slozka):
        if not os.path.isfile(cesta_k_souboru):
            print(f"Chyba: Soubor '{cesta_k_souboru}' neexistuje.")
            return
        if not os.path.exists(cilova_slozka):
            os.makedirs(cilova_slozka)
        nazev = os.path.basename(cesta_k_souboru)
        cilova_cesta = os.path.join(cilova_slozka, nazev)
        shutil.copy2(cesta_k_souboru, cilova_cesta)
        print(f"Soubor zkopírován do: {cilova_cesta}")
        return cilova_cesta  # vrátí cestu kopie
    
    @staticmethod
    def znovunacti():
        print("⏳ Znovunačítám Ševčík CMD...")
        time.sleep(1)
        try:
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit(0)
        except Exception as e:
            print("❌ Nepodařilo se znovunačíst CMD:", e)

# COMMANDY UDĚLUJÍCÍ OPRÁVNĚNÍ A SILNÉ COMMANDY    
class odlesk_plesky:

    @staticmethod
    def bud_buh():
        vazne = input("Opravdu chceš spustit tento příkaz? Příkazy z této třídy jsou silné v oprávnění! (ano/ne): ").strip().lower()
        if vazne == "ano":
            if os.name != "nt":
                print("Tato funkce funguje pouze na Windows.")
                return

            # cesta k python skriptu
            skript = os.path.abspath(sys.argv[0])
            params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])

            try:
                # ShellExecute s "runas" spustí program jako admin
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{skript}" {params}', None, 1)
                sys.exit(0)  # ukončí současný proces
            except Exception as e:
                print(f"Nepodařilo se spustit jako admin: {e}")
        else:
            print("Příkaz zrušen uživatelem.")

def main():
    print("Ševčík CMD je aktuálně spuštěna, pokud chceš pomoct napiš pls.helpni().")
    while True:
        cmd = input("&#> ").strip()
        if cmd.lower() == "koncim_s_tebou":
            print("Tak čus.")
            time.sleep(4)
            break
        try:
            # Vyhodnotí příkaz jako Python výraz
            result = eval(cmd)
            # Pokud funkce něco vrátí, vypíše to
            if result is not None:
                print(result)
        except Exception as e:
            print("Chyba při provádění příkazu:", e)

if __name__ == "__main__":
    main()
