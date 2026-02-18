import sys
import subprocess
import importlib
import os

# --- DEL 1: AUTOMATISK INSTALLATION AV PAKET ---
def install_and_import(package):
    """
    Kollar om ett paket finns. Om inte, installeras det.
    """
    try:
        importlib.import_module(package)
        # print(f"✅ {package} är redan installerat.") # Avkommentera om du vill se detta
    except ImportError:
        print(f"📦 Paketet '{package}' saknas. Installerar det nu...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installerat!")
        except Exception as e:
            print(f"❌ Kunde inte installera {package}. Fel: {e}")

# Lista på paket vi behöver
required_packages = ["pandas", "matplotlib", "requests"]

print("--- 1. Kontrollerar paket... ---")
for pkg in required_packages:
    install_and_import(pkg)

# Nu importerar vi biblioteken
import pandas as pd
import matplotlib.pyplot as plt

# --- DEL 2: HÄMTA, STÄDA OCH VISA DATA ---
def main():
    print("\n--- 2. Laddar ner dataset... ---")
    url = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/USArrests.csv"

    try:
        # Läs in CSV-filen från nätet
        df = pd.read_csv(url)

        # --- FIXEN: DYNAMISK KOLUMN-HANTERING ---
        # Vi tar reda på vad den allra första kolumnen heter just nu
        original_col_name = df.columns[0]
        
        # Vi döper om den till 'Stat' så vi vet vad vi ska kalla den i koden sen
        df.rename(columns={original_col_name: 'Stat'}, inplace=True)
        # ----------------------------------------

        print("✅ Data hämtad!")
        print(f"📊 Datasetets storlek: {df.shape[0]} rader, {df.shape[1]} kolumner")
        print("Här är de första 5 raderna:")
        print(df.head())

        # --- DEL 3: VISUALISERING ---
        print("\n--- 3. Skapar diagram... ---")
        
        # Sortera datan så vi ser de farligaste staterna först (Topp 15)
        df_sorted = df.sort_values('Murder', ascending=False).head(15)

        plt.figure(figsize=(12, 6)) # Bestäm storlek på fönstret
        
        # Skapa stapeldiagrammet
        plt.bar(df_sorted['Stat'], df_sorted['Murder'], color='darkred', alpha=0.8)
        
        # Snygga till diagrammet med texter
        plt.title('Antal mord per 100,000 invånare (Topp 15 Stater i USA - 1973)', fontsize=14)
        plt.xlabel('Stat', fontsize=12)
        plt.ylabel('Antal mord', fontsize=12)
        plt.xticks(rotation=45) # Lutar texten så den blir läsbar
        plt.grid(axis='y', linestyle='--', alpha=0.5) # Rutnät i bakgrunden
        
        # Justera layout så inget klipps bort
        plt.tight_layout()
        
        # Visa diagrammet (detta pausar koden tills du stänger fönstret)
        print("📈 Visar diagrammet nu! (Stäng fönstret för att fortsätta)")
        plt.show()

        # --- DEL 4: SPARA TILL FIL ---
        print("\n--- 4. Sparar data... ---")
        filename = "brottsstatistik.csv"
        df.to_csv(filename, index=False)
        
        # Visa vart filen hamnade
        current_folder = os.getcwd()
        full_path = os.path.join(current_folder, filename)
        print(f"💾 Filen sparad som: {filename}")
        print(f"📂 Den ligger här: {full_path}")

    except Exception as e:
        print(f"\n❌ Något gick fel: {e}")
        # Hjälp för felsökning om det kraschar
        if 'df' in locals():
            print(f"Tillgängliga kolumner i datan var: {df.columns.tolist()}")

if __name__ == "__main__":
    main()