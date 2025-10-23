#!/usr/bin/env python3
import argparse
import os
import sys
from Ioni_compiler.parser import ParserIoni
from Ioni_compiler.quantum_backend import BackendQuanticoIoni

def main():
    parser = argparse.ArgumentParser(description='Compilatore Ioni Language')
    parser.add_argument('file', help='File .Ioni da compilare')
    parser.add_argument('--meditate', action='store_true', help='Esegui meditazione')
    parser.add_argument('--shots', type=int, default=1024, help='Numero di esecuzioni quantistiche')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File non trovato: {args.file}")
        return 1

    # Leggi il file Ioni
    with open(args.file, 'r', encoding='utf-8') as f:
        codice = f.read()

    # Parsing
    print("🧘 Parsing codice Ioni...")
    parser_Ioni = ParserIoni()
    tessitore = parser_Ioni.parse(codice)

    print(f"📊 Sillabe registrate: {len(tessitore.sillabe_registry)}")

    # Esegui meditazione quantistica
    if args.meditate:
        print("🔮 Avviando meditazione quantistica...")
        backend = BackendQuanticoIoni()

        sillabe = list(tessitore.sillabe_registry.values())
        circuito = backend.crea_circuito_meditazione(sillabe)
        risultato = backend.esegui_meditazione(circuito, args.shots)

        print(f"🌈 Armonia raggiunta: {risultato['armonia']:.3f}")
        print(f"🎵 Entanglement: {risultato['entanglement']:.3f}")

        # Misura alcune sillabe
        print("\n📖 Rivelazioni:")
        for nome in list(tessitore.sillabe_registry.keys())[:3]:
            misura = tessitore.misura_sovrapposizione(nome)
            print(f"  - {misura}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
