from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(ROOT / 'build.py')], check=True)

verification = ROOT / 'google02c383ec58048d5e.html'
if verification.exists():
    shutil.copy2(verification, ROOT / 'dist' / verification.name)
    print(f'Copied Search Console verification file: {verification.name}')
