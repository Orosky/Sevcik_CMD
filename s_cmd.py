import platform
import os
import time
import shutil
import subprocess
import sys
import ctypes
import importlib
import urllib.request
import urllib.error
import webbrowser
import socket
try:
    import tkinter as tk
    from tkinter import messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False

# Pro tab completion
READLINE_AVAILABLE = False
readline = None
try:
    # Zkusíme importovat readline
    if platform.system() == "Windows":
        try:
            import pyreadline3 as readline
            READLINE_AVAILABLE = True
        except ImportError:
            try:
                import readline
                READLINE_AVAILABLE = True
            except ImportError:
                pass
    else:
        # Linux/macOS
        import readline
        READLINE_AVAILABLE = True
except ImportError:
    READLINE_AVAILABLE = False


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


Version = "0.0.2 [ALPHA TESTING VERSION]"
Distrubution = "User distribution"

# KONTROLA VERZE
def kontrola_verze():
    """
    Kontroluje verzi aplikace proti souborům na GitHubu.
    Vrací: 'aktualni', 'povolena', 'zakazana', nebo None (chyba)
    """
    # Zkusí nejdřív větev 'versions', pak fallback na 'main_cz'
    github_branches = [
        "https://raw.githubusercontent.com/Orosky/Sevcik_CMD/versions",
        "https://raw.githubusercontent.com/Orosky/Sevcik_CMD/main_cz"
    ]
    
    aktualni_verze = Version.strip()
    verze_seznamy = {}
    
    # Zkusí stáhnout soubory z různých větví
    for github_base in github_branches:
        soubory = {
            'aktualni': f"{github_base}/aktualni_verze.txt",
            'povolene': f"{github_base}/povolene_verze.txt",
            'zakazane': f"{github_base}/zakazane_verze.txt"
        }
        
        uspesne_stazeno = 0
        for typ, url in soubory.items():
            try:
                with urllib.request.urlopen(url, timeout=5) as response:
                    obsah = response.read().decode('utf-8').strip()
                    # Rozdělí na řádky a vyčistí prázdné řádky
                    verze_seznamy[typ] = [v.strip() for v in obsah.split('\n') if v.strip()]
                    uspesne_stazeno += 1
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    # Soubor neexistuje - to je v pořádku, zkusíme další větev
                    continue
            except Exception:
                # Jiná chyba (timeout, síť, atd.) - ignorujeme
                pass
        
        # Pokud se podařilo stáhnout alespoň jeden soubor, použijeme tuto větev
        if uspesne_stazeno > 0:
            break
    
    # Pokud se nepodařilo stáhnout žádný soubor
    if not verze_seznamy:
        return None
    
    # Kontrola zakázaných verzí (nejdřív, protože je to nejdůležitější)
    if 'zakazane' in verze_seznamy:
        for zakazana in verze_seznamy['zakazane']:
            if zakazana in aktualni_verze or aktualni_verze in zakazana:
                return 'zakazana'
    
    # Kontrola aktuální verze
    if 'aktualni' in verze_seznamy:
        for aktualni in verze_seznamy['aktualni']:
            if aktualni in aktualni_verze or aktualni_verze in aktualni:
                return 'aktualni'
    
    # Kontrola povolených verzí
    if 'povolene' in verze_seznamy:
        for povolena in verze_seznamy['povolene']:
            if povolena in aktualni_verze or aktualni_verze in povolena:
                return 'povolena'
    
    # Pokud verze není v žádném seznamu, považujeme ji za povolenou (kompatibilita)
    return 'povolena'

def zobraz_okno_verze(typ):
    """
    Zobrazí vyskakovací okno podle typu verze.
    typ: 'povolena' nebo 'zakazana'
    """
    if not TKINTER_AVAILABLE:
        # Fallback pro systémy bez tkinter
        if typ == 'zakazana':
            print("=" * 60)
            print("⚠️  VAROVÁNÍ: Vaše verze je zakázaná!")
            print("Je nutné provést aktualizaci.")
            print("=" * 60)
            volba = input("Chcete otevřít stránku pro stažení? (ano/ne): ").strip().lower()
            if volba == 'ano':
                webbrowser.open("https://smcd.ct.ws/download.php")
            print("Aplikace se ukončuje...")
            time.sleep(2)
            sys.exit(0)
        elif typ == 'povolena':
            print("=" * 60)
            print("ℹ️  INFO: K dispozici je nová verze aplikace.")
            print("Doporučujeme provést aktualizaci.")
            print("=" * 60)
            volba = input("Chcete otevřít stránku pro stažení? (ano/ne): ").strip().lower()
            if volba == 'ano':
                webbrowser.open("https://smcd.ct.ws/download.php")
        return
    
    # Vytvoří root okno (skryté)
    root = tk.Tk()
    root.withdraw()  # Skryje hlavní okno
    root.attributes('-topmost', True)  # Okno nahoře
    
    if typ == 'zakazana':
        # Zakázaná verze - nutná aktualizace
        root.title("Kritická aktualizace")
        volba = messagebox.askyesno(
            "⚠️ Kritická aktualizace",
            f"Vaše verze aplikace ({Version}) je zakázaná!\n\n"
            "Je nutné provést aktualizaci pro pokračování.\n\n"
            "Chcete otevřít stránku pro stažení aktualizace?",
            icon='error'
        )
        if volba:
            webbrowser.open("https://smcd.ct.ws/download.php")
        # Vždy ukončí aplikaci
        root.destroy()
        print("Aplikace se ukončuje kvůli zakázané verzi...")
        time.sleep(2)
        sys.exit(0)
    
    elif typ == 'povolena':
        # Povolená verze - doporučená aktualizace
        root.title("Dostupná aktualizace")
        volba = messagebox.askyesno(
            "ℹ️ Dostupná aktualizace",
            f"K dispozici je nová verze aplikace.\n\n"
            f"Vaše aktuální verze: {Version}\n\n"
            "Doporučujeme provést aktualizaci.\n\n"
            "Chcete otevřít stránku pro stažení aktualizace?",
            icon='warning'
        )
        if volba:
            webbrowser.open("https://smcd.ct.ws/download.php")
        root.destroy()

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
        print("----------------------------------------------")
        print("| {:<10} | {:<35} |".format("sevcik", "Práce se soubory a složkami."))
        print("----------------------------------------------")
        print("| {:<10} | {:<35} |".format("pripojuju", "Zobrazuje síťové nastavení."))
        print("----------------------------------------------")
        print("| {:<10} | {:<35} |".format("odlesk_plesky", "Silné příkazy s oprávněními."))
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

# COMMANDY PRO SÍŤOVÉ NASTAVENÍ
class pripojuju:
    def vazne_jsem_onlajn(cil="google"):
        """
        Testuje připojení pomocí ping na různé testovací adresy.
        Podporované hodnoty:
            "google"     -> 8.8.8.8
            "cloudflare" -> 1.1.1.1
            "opendns"    -> 208.67.222.222
            "quad9"      -> 9.9.9.9
            "mojeip"     -> 1.1.1.1 (alias)
        Pokud není nic vyplněno, pingne google DNS.
        """

        testy = {
            "google": "8.8.8.8",
            "cloudflare": "1.1.1.1",
            "opendns": "208.67.222.222",
            "quad9": "9.9.9.9",
            "mojeip": "1.1.1.1"
        }

        cil = cil.lower().strip() if isinstance(cil, str) else "google"
        ip = testy.get(cil, testy["google"])  # default google

        system = platform.system()
        prikaz = ["ping", "-c", "1", ip] if system != "Windows" else ["ping", "-n", "1", ip]

        try:
            vysledek = subprocess.run(prikaz, capture_output=True)
            if vysledek.returncode == 0:
                print(f"✔️  Online (odpověď od {ip})")
                return True
            else:
                print(f"❌  Offline (žádná odpověď od {ip})")
                return False
        except Exception as e:
            print("Chyba při pingování:", e)
            return False
    
    @staticmethod
    def kudy_jdes(ip=None):
        """
        Provede traceroute na zadanou IP adresu nebo doménu.
        Pokud není zadána žádná IP, použije se google.com jako výchozí.
        """
        if ip is None:
            cil = "google.com"
        else:
            cil = str(ip).strip()
        
        system = platform.system()
        
        print(f"🛤️  Provádím traceroute na {cil}...")
        print("=" * 60)
        
        try:
            if system == "Windows":
                # Windows používá tracert
                vysledek = subprocess.run(["tracert", cil], 
                                         capture_output=False,
                                         text=True)
            else:
                # Linux a macOS používají traceroute
                vysledek = subprocess.run(["traceroute", cil], 
                                         capture_output=False,
                                         text=True)
            
            print("=" * 60)
        except FileNotFoundError:
            print(f"❌ Chyba: Příkaz pro traceroute není k dispozici na tomto systému.")
            print("Na Windows použijte 'tracert', na Linux/macOS 'traceroute'.")
        except Exception as e:
            print(f"❌ Chyba při provádění traceroute: {e}")
    
    @staticmethod
    def ktera_ip_je_moje():
        """
        Zobrazí síťové nastavení podobně jako ipconfig.
        """
        system = platform.system()
        
        print("=" * 60)
        print("🌐 SÍŤOVÉ NASTAVENÍ")
        print("=" * 60)
        
        # Získání hostname
        try:
            hostname = socket.gethostname()
            print(f"Název počítače: {hostname}")
        except Exception as e:
            print(f"Název počítače: Nelze zjistit ({e})")
        
        # Získání IP adresy
        try:
            # Získá IP adresu připojením k externímu serveru (zobrazí lokální IP)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            print(f"Lokální IP adresa: {local_ip}")
        except Exception as e:
            print(f"Lokální IP adresa: Nelze zjistit ({e})")
        
        # Získání všech IP adres
        try:
            print("\n📡 Všechny síťové rozhraní:")
            hostname = socket.gethostname()
            ip_addresses = socket.gethostbyname_ex(hostname)[2]
            for ip in ip_addresses:
                if not ip.startswith("127."):
                    print(f"  - {ip}")
        except Exception as e:
            print(f"  Nelze zjistit další IP adresy: {e}")
        
        # Detailní informace pomocí systémového příkazu
        print("\n" + "=" * 60)
        print("📋 DETAILNÍ SÍŤOVÉ INFORMACE")
        print("=" * 60)
        
        if system == "Windows":
            try:
                result = subprocess.run(["ipconfig", "/all"], 
                                      capture_output=True, 
                                      text=True, 
                                      encoding='utf-8',
                                      errors='ignore')
                print(result.stdout)
            except Exception as e:
                print(f"Chyba při získávání detailních informací: {e}")
                print("Zkuste spustit 'ipconfig /all' v příkazovém řádku.")
        elif system == "Linux" or system == "Darwin":
            try:
                if system == "Linux":
                    result = subprocess.run(["ip", "addr"], 
                                          capture_output=True, 
                                          text=True, 
                                          encoding='utf-8',
                                          errors='ignore')
                else:  # macOS
                    result = subprocess.run(["ifconfig"], 
                                          capture_output=True, 
                                          text=True, 
                                          encoding='utf-8',
                                          errors='ignore')
                print(result.stdout)
            except Exception as e:
                print(f"Chyba při získávání detailních informací: {e}")
        else:
            print(f"Systém {system} není podporován pro detailní síťové informace.")
        
        print("=" * 60)

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

# TAB COMPLETION FUNKCE
def ziskej_dostupne_prikazy():
    """
    Vrací seznam všech dostupných příkazů (třídy a jejich metody).
    """
    prikazy = []
    
    # Třídy a jejich metody
    tridy = {
        'pls': ['helpni', 'helpniclass', 'info_o_tobe'],
        'mluvic': ['vycisti', 'rekni'],
        'pleska': ['infosys', 'kdo_su_ja', 'jaky_cislo_jsi'],
        'sevcik': ['vypis_slozky_ve_slozce', 'co_je_tu', 'otevri_soubor', 'zkopiruj_soubor_do', 'znovunacti'],
        'pripojuju': ['vazne_jsem_onlajn', 'kudy_jdes', 'ktera_ip_je_moje'],
        'odlesk_plesky': ['bud_buh']
    }
    
    # Přidá názvy tříd
    prikazy.extend(tridy.keys())
    
    # Přidá třídy.metody
    for trida, metody in tridy.items():
        for metoda in metody:
            prikazy.append(f"{trida}.{metoda}")
    
    return prikazy

# Globální proměnná pro ukládání matches při tab completion
_tab_matches = []

def dokonci_prikaz(text, stav):
    """
    Funkce pro tab completion - readline API.
    text: aktuálně zadaný text
    stav: index návrhu (0, 1, 2, ...)
    """
    global _tab_matches
    
    # Pokud je stav 0, znovu načte matches
    if stav == 0:
        dostupne = ziskej_dostupne_prikazy()
        
        # Pokud text končí tečkou (např. "pls."), přidáme i metody bez tečky
        if text.endswith('.'):
            # Najdeme třídu
            trida = text[:-1]  # odstraníme tečku
            # Přidáme metody této třídy
            tridy = {
                'pls': ['helpni', 'helpniclass', 'info_o_tobe'],
                'mluvic': ['vycisti', 'rekni'],
                'pleska': ['infosys', 'kdo_su_ja', 'jaky_cislo_jsi'],
                'sevcik': ['vypis_slozky_ve_slozce', 'co_je_tu', 'otevri_soubor', 'zkopiruj_soubor_do', 'znovunacti'],
                'pripojuju': ['vazne_jsem_onlajn', 'kudy_jdes', 'ktera_ip_je_moje'],
                'odlesk_plesky': ['bud_buh']
            }
            if trida in tridy:
                _tab_matches = [f"{trida}.{metoda}" for metoda in tridy[trida]]
            else:
                _tab_matches = []
        else:
            # Normální filtrování
            _tab_matches = [cmd for cmd in dostupne if cmd.startswith(text)]
        
        if not _tab_matches:
            return None
    
    # Vrací návrh na daném indexu nebo None, pokud už nejsou žádné
    try:
        return _tab_matches[stav]
    except IndexError:
        return None

def nastav_tab_completion():
    """
    Nastaví tab completion pomocí readline, pokud je dostupné.
    """
    if not READLINE_AVAILABLE:
        return False
    
    try:
        # Nastaví completer funkci
        readline.set_completer(dokonci_prikaz)
        # Nastaví tab jako klávesu pro completion
        readline.parse_and_bind("tab: complete")
        return True
    except Exception:
        return False

def input_s_completion(prompt):
    """
    Wrapper pro input() s podporou tab completion.
    """
    if READLINE_AVAILABLE:
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            raise
    else:
        # Fallback na normální input
        return input(prompt)

def je_admin_rezim():
    """
    Zjistí, zda je aplikace spuštěna s administrátorskými oprávněními.
    Vrací True pokud je v admin režimu, jinak False.
    """
    if platform.system() == "Windows":
        try:
            # Zkontroluje, zda má uživatel administrátorská oprávnění
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    else:
        # Na Unix systémech zkontroluje, zda je UID 0 (root)
        try:
            return os.geteuid() == 0
        except:
            return False

def ziskej_prompt():
    """
    Vrací prompt podle aktuálního režimu.
    Admin režim: #$>
    Normální režim: &#>
    """
    if je_admin_rezim():
        return "#$> "
    else:
        return "&#> "

def main():
    # Kontrola verze při spuštění
    try:
        stav_verze = kontrola_verze()
        if stav_verze == 'zakazana':
            zobraz_okno_verze('zakazana')
            return  # Aplikace se ukončí v zobraz_okno_verze
        elif stav_verze == 'povolena':
            zobraz_okno_verze('povolena')
        # Pokud je None (chyba stahování) nebo 'aktualni', pokračuje dál bez upozornění
    except Exception:
        # Tichá chyba - aplikace pokračuje
        pass
    
    # Nastaví tab completion
    if nastav_tab_completion():
        print("💡 Tip: Stiskni Tab pro automatické doplnění příkazů!")
    
    print("Ševčík CMD je aktuálně spuštěna, pokud chceš pomoct napiš pls.helpni().")
    if je_admin_rezim():
        print("⚠️  ADMIN REŽIM: Aplikace běží s administrátorskými oprávněními!")
    
    while True:
        cmd = input_s_completion(ziskej_prompt()).strip()
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
