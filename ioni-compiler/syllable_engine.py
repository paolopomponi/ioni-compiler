import numpy as np
from dataclasses import dataclass
from typing import List, Dict
import math

@dataclass
class Sillaba:
    suono: str
    silenzio: float  # 0-1, ampiezza del broccato
    fase: float      # fase in radianti
    entanglement: List[str] = None

    def __post_init__(self):
        if self.entanglement is None:
            self.entanglement = []

    def stato_quantico(self):
        """Converte la sillaba in uno stato quantistico"""
        alpha = math.sqrt(1 - self.silenzio)  # ampiezza |1⟩ (nodo)
        beta = math.sqrt(self.silenzio)       # ampiezza |0⟩ (broccato)

        # Applica la fase
        beta *= np.exp(1j * self.fase)

        return np.array([alpha, beta])

class TessitoreSillabico:
    def __init__(self):
        self.sillabe_registry = {}
        self.circuiti_quantistici = []

    def registra_sillaba(self, nome: str, sillaba: Sillaba):
        self.sillabe_registry[nome] = sillaba

    def annoda(self, sillaba_a: str, sillaba_b: str):
        """Crea entanglement tra due sillabe"""
        if sillaba_a in self.sillabe_registry and sillaba_b in self.sillabe_registry:
            self.sillabe_registry[sillaba_a].entanglement.append(sillaba_b)
            self.sillabe_registry[sillaba_b].entanglement.append(sillaba_a)
            return f"Annodate {sillaba_a} ↔ {sillaba_b}"
        return "Sillaba non trovata"

    def misura_sovrapposizione(self, sillaba_nome: str):
        """Simula la misurazione quantistica"""
        if sillaba_nome not in self.sillabe_registry:
            return None

        sillaba = self.sillabe_registry[sillaba_nome]
        stato = sillaba.stato_quantico()

        # Probabilità di collasso in |1⟩ (nodo)
        prob_nodo = abs(stato[0]) ** 2

        # Simula misurazione
        if np.random.random() < prob_nodo:
            return f"|NODO⟩ - {sillaba.suono} manifestato"
        else:
            return f"|BROCCATO⟩ - {sillaba.suono} in potenziale"
