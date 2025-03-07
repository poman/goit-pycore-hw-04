import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(path, indent=''):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + '    ')
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission Denied{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python filename.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist or is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
