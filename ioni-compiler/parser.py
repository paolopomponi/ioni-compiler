import re
from .syllable_engine import Sillaba, TessitoreSillabico

class ParserSouf:
    def __init__(self):
        self.tessitore = TessitoreSillabico()
        self.risultati = []

    def parse(self, codice: str):
        linee = codice.split('\n')

        for linea in linee:
            linea = linea.strip()

            # Ignora commenti e linee vuote
            if not linea or linea.startswith('//'):
                continue

            # Parsing delle sillabe
            if 'crea_sillaba' in linea:
                self._parse_crea_sillaba(linea)

            # Parsing degli annodamenti
            elif 'annoda' in linea:
                self._parse_annoda(linea)

            # Parsing delle risonanze
            elif 'risuona' in linea:
                self._parse_risuona(linea)

        return self.tessitore

    def _parse_crea_sillaba(self, linea: str):
        match = re.search(r'crea_sillaba\("([^"]+)", silenzio: ([0-9.]+), fase: ([^)]+)\)', linea)
        if match:
            nome, silenzio, fase = match.groups()

            # Converti fase (supporta π)
            fase = fase.replace('π', 'math.pi').replace('pi', 'math.pi')
            try:
                fase_val = eval(fase)
            except:
                fase_val = float(fase)

            sillaba = Sillaba(
                suono=nome,
                silenzio=float(silenzio),
                fase=float(fase_val)
            )
            self.tessitore.registra_sillaba(nome, sillaba)

    def _parse_annoda(self, linea: str):
        match = re.search(r'annoda\("([^"]+)", "([^"]+)"\)', linea)
        if match:
            a, b = match.groups()
            risultato = self.tessitore.annoda(a, b)
            self.risultati.append(risultato)

    def _parse_risuona(self, linea: str):
        # Implementa la risonanza
        self.risultati.append("Risonanza applicata")
