#!/usr/bin/env python3
"""Test script to verify selenium installation."""

import sys

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print()

try:
    import selenium
    print(f"✓ SUCCESS: Selenium is installed!")
    print(f"  Version: {selenium.__version__}")
    print(f"  Location: {selenium.__file__}")
except ImportError as e:
    print(f"✗ FAILED: Selenium is NOT installed")
    print(f"  Error: {e}")
    print()
    print("Trying to install selenium...")
    import subprocess
    result = subprocess.run([sys.executable, "-m", "pip", "install", "selenium"], 
                          capture_output=True, text=True)
    print("Installation output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    print(f"Return code: {result.returncode}")
    
    # Try importing again
    try:
        import selenium
        print(f"\n✓ SUCCESS: Selenium is now installed!")
        print(f"  Version: {selenium.__version__}")
    except ImportError:
        print("\n✗ FAILED: Still cannot import selenium after installation attempt")
