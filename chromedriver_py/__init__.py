
import subprocess
import sys
import os
from importlib.resources import files

def run_chromedriver():
    is_windows = sys.platform.startswith("win")
    binary_name = "chromedriver.exe" if is_windows else "chromedriver"
    binary_path = files('chromedriver_py').joinpath(binary_name)

    if not binary_path.exists():
        raise FileNotFoundError(f"Could not find chromedriver binary at {binary_path}")

    try:
        result = subprocess.run([str(binary_path)] + sys.argv[1:], check=False)
        sys.exit(result.returncode)
    except OSError as e:
        print(f"Error executing chromedriver: {e}")
        sys.exit(1)
