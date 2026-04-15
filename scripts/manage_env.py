"""Cross-platform environment management for the project."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = PROJECT_ROOT / ".venv"
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements-notebook.txt"


def venv_python_path() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def interpreter_hint() -> str:
    if os.name == "nt":
        return ".venv\\Scripts\\python.exe"
    return ".venv/bin/python"


def run_command(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=PROJECT_ROOT)


def ensure_venv(system_python: str) -> Path:
    venv_python = venv_python_path()

    if venv_python.exists():
        return venv_python

    create_args = [system_python, "-m", "venv"]

    if VENV_DIR.exists():
        print("Ambiente .venv existente nao corresponde a este sistema. Recriando...", flush=True)
        create_args.append("--clear")
    else:
        print("Criando ambiente virtual em .venv...", flush=True)

    create_args.append(str(VENV_DIR))
    run_command(create_args)

    venv_python = venv_python_path()
    if not venv_python.exists():
        raise RuntimeError("Nao foi possivel criar o ambiente virtual.")

    return venv_python


def setup_environment(system_python: str) -> None:
    venv_python = ensure_venv(system_python)

    print("Atualizando pip...", flush=True)
    run_command([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"])

    print("Instalando dependencias do projeto...", flush=True)
    run_command([str(venv_python), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)])

    print("", flush=True)
    print("Ambiente pronto.", flush=True)
    print(f"No VS Code, selecione o interpretador {interpreter_hint()}", flush=True)


def add_dependencies(packages: list[str]) -> None:
    venv_python = venv_python_path()

    if not venv_python.exists():
        raise RuntimeError("Ambiente .venv nao encontrado. Rode o setup antes.")

    print(f"Instalando: {', '.join(packages)}", flush=True)
    run_command([str(venv_python), "-m", "pip", "install", *packages])

    existing_lines: list[str] = []
    if REQUIREMENTS_FILE.exists():
        existing_lines = [
            line.strip()
            for line in REQUIREMENTS_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    updated_lines = list(existing_lines)
    for package in packages:
        if package not in updated_lines:
            updated_lines.append(package)

    REQUIREMENTS_FILE.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
    print("requirements-notebook.txt atualizado.", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage the project Python environment.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_parser = subparsers.add_parser("setup", help="Create/update the virtual environment.")
    setup_parser.add_argument(
        "--system-python",
        default=sys.executable,
        help="Python executable used to create the virtual environment.",
    )

    add_parser = subparsers.add_parser("add", help="Install new dependencies and update requirements.")
    add_parser.add_argument("packages", nargs="+", help="Packages to install.")

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        if args.command == "setup":
            setup_environment(args.system_python)
        elif args.command == "add":
            add_dependencies(args.packages)
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(exc, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
