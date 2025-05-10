import subprocess
import sys
import os

def check_python_version():
    if sys.version_info < (3, 9):
        print("Python 3.9 or higher is required")
        sys.exit(1)

def install_requirements():
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("requirements.txt not found in the current directory.")
        sys.exit(1)

    try:
        # Upgrade pip first
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        
        # Install requirements
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        
        print("\nDependencies installed successfully!")
        print("\nYou can now run your food computer scripts.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_python_version()
    install_requirements() 