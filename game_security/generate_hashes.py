import hashlib
import os

# --- CONFIGURATION ---
# List all the files you want to protect here (Relative to IGI 2 folder)
TARGET_FILES = [
    "igi2.exe",
    r"pc\HUMANPLAYER\humanplayer.qvm",
    r"pc\WEAPONS\weapon.qvm",
    r"pc\WEAPONS\ammo.qvm",
    # Add your maps here:
    r"pc\MISSIONS\multiplayer\Aim Map\objects.qvm",
    r"pc\MISSIONS\multiplayer\AREA27\objects.qvm", 
    r"pc\MISSIONS\multiplayer\Canyon\objects.qvm",
    r"pc\MISSIONS\multiplayer\chinesetemple\objects.qvm",
    r"pc\MISSIONS\multiplayer\Dark Hills\objects.qvm",
    r"pc\MISSIONS\multiplayer\de_dust2\objects.qvm",
    r"pc\MISSIONS\multiplayer\Finding the Bomb\objects.qvm",
    r"pc\MISSIONS\multiplayer\forestraid\objects.qvm",
    r"pc\MISSIONS\multiplayer\ghostcity\objects.qvm",
    r"pc\MISSIONS\multiplayer\Pribois Villa\objects.qvm",
    r"pc\MISSIONS\multiplayer\Production Facility\objects.qvm",
    r"pc\MISSIONS\multiplayer\Radar Base 1\objects.qvm",
    r"pc\MISSIONS\multiplayer\redstone\objects.qvm",
    r"pc\MISSIONS\multiplayer\sandstorm\objects.qvm",
    r"pc\MISSIONS\multiplayer\The Airfield 2024\objects.qvm",
    r"pc\MISSIONS\multiplayer\The Launch Pad\objects.qvm",
    r"pc\MISSIONS\multiplayer\timberland\objects.qvm", 
]

def get_hash(filepath):
    if not os.path.exists(filepath): return "FILE_NOT_FOUND"
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except: return "ERROR"

print("="*60)
print("      COPY THIS DICTIONARY INTO YOUR MAIN SCRIPT")
print("="*60)
print("VALID_HASHES = {")

for file_path in TARGET_FILES:
    file_hash = get_hash(file_path)
    # Convert backslashes to forward slashes for Python safety
    safe_path = file_path.replace("\\", "/") 
    print(f'    "{safe_path}": "{file_hash}",')

print("}")
print("="*60)
input("Press Enter to close...")