#!/usr/bin/env python3
"""Install all required dependencies for the assignment."""

import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    print(f"\n{'='*60}")
    print(f"Installing {package}...")
    print('='*60)
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR installing {package}:")
        print(e.stdout)
        print(e.stderr)
        return False

def verify_installation():
    """Verify that all packages are installed."""
    packages = {
        'pandas': 'pd',
        'numpy': 'np',
        'matplotlib': None,
        'seaborn': None,
        'sklearn': None,
        'selenium': None
    }
    
    print("\n" + "="*60)
    print("VERIFYING INSTALLATION")
    print("="*60)
    
    all_installed = True
    for package, alias in packages.items():
        try:
            if alias:
                exec(f"import {package} as {alias}")
                version = eval(f"{alias if alias else package}.__version__")
            else:
                exec(f"import {package}")
                version = eval(f"{package}.__version__")
            print(f"✓ {package:15} - version {version}")
        except ImportError:
            print(f"✗ {package:15} - NOT INSTALLED")
            all_installed = False
        except Exception as e:
            print(f"? {package:15} - Error: {e}")
            all_installed = False
    
    return all_installed

if __name__ == "__main__":
    print("="*60)
    print("INSTALLING ASSIGNMENT DEPENDENCIES")
    print("="*60)
    
    # List of packages to install
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scikit-learn>=1.3.0",
        "selenium>=4.10.0",
        "webdriver-manager>=4.0.0",
        "jupyter>=1.0.0",
        "notebook>=6.5.0"
    ]
    
    # Install each package
    results = []
    for package in packages:
        success = install_package(package)
        results.append((package, success))
    
    # Summary
    print("\n" + "="*60)
    print("INSTALLATION SUMMARY")
    print("="*60)
    for package, success in results:
        status = "✓" if success else "✗"
        print(f"{status} {package}")
    
    # Verify installation
    if verify_installation():
        print("\n" + "="*60)
        print("SUCCESS! All packages are installed.")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("WARNING: Some packages may not be installed correctly.")
        print("Try running: python -m pip install --upgrade pip")
        print("Then run this script again.")
        print("="*60)
