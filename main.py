from pathlib import Path
from core.unit import Environment, GRAMMAR, parser
import sys

VERSION = "1.0"

def helpme():
    print("usage: own [-mf] <file1> [file2] ...\n")
    print(f"version: {VERSION}")

def main():
    args = sys.argv[1:]
    
    if not args:
        helpme()
        return

    if args[0] == "-mf":
        file_paths = args[1:]
        if not file_paths:
            print("Error: No files specified after -mf!")
            return
        
        base_dir = Path(file_paths[0]).parent
        env = Environment(base_dir)

        for file_path in file_paths:
            target = Path(file_path)
            if not target.is_file():
                print(f"Error: File {target} not found!")
                continue

            if target.suffix != ".own":
                print(f"Error: File {target} isn't a valid '.own' file!")
                continue

            source = target.read_text(encoding='utf-8')
            tree = parser.parse(source)
            env.visit(tree)

    else:
        file_path = args[0]
        target = Path(file_path)

        if not target.is_file():
            print(f"Error: File {target} not found!")
            return

        env = Environment(target.parent)
        source = target.read_text(encoding='utf-8')
        tree = parser.parse(source)
        env.visit(tree)

if __name__ == "__main__":
    main()