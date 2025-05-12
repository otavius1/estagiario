import os
import platform
import subprocess
import sys

def main():
    print("\n==========================")
    print(" Estagiário Jurídico - Starter ")
    print("==========================\n")

    system = platform.system()
    print(f"Sistema detectado: {system}")

    # Ativa venv
    if system == "Windows":
        activate_cmd = r"venv\Scripts\activate.bat"
    elif system in ["Linux", "Darwin"]: 
        activate_cmd = ". venv/bin/activate"
    else:
        print("Sistema operacional não suportado.")
        sys.exit(1)

    print("\nAtivando ambiente virtual...")
    if system == "Windows":
        subprocess.call(["cmd.exe", "/k", f"{activate_cmd} && pip install -r requirements.txt && uvicorn api:app --reload"])
    else:
        os.system(f"{activate_cmd} && pip install -r requirements.txt && uvicorn api:app --reload")

if __name__ == "__main__":
    main()
