from qiskit import QuantumCircuit, Aer, execute
import numpy as np

class BackendQuanticoIoni:
    def __init__(self):
        self.simulator = Aer.get_backend('statevector_simulator')

    def crea_circuito_meditazione(self, sillabe):
        """Crea un circuito quantistico per la meditazione Ioni"""
        n_qubits = len(sillabe)
        qc = QuantumCircuit(n_qubits)

        # Inizializza in sovrapposizione
        for i, sillaba in enumerate(sillabe):
            # Angolo basato sul silenzio della sillaba
            theta = 2 * np.arccos(np.sqrt(sillaba.silenzio))
            qc.ry(theta, i)

            # Applica fase
            qc.rz(sillaba.fase, i)

        # Crea entanglement tra sillabe consecutive
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)

        return qc

    def esegui_meditazione(self, circuito, shots=1024):
        """Esegue la meditazione quantistica"""
        job = execute(circuito, self.simulator, shots=shots)
        result = job.result()
        statevector = result.get_statevector()

        return {
            'stato': statevector,
            'entanglement': self.calcola_entanglement(statevector),
            'armonia': self.calcola_armonia(statevector)
        }

    def calcola_entanglement(self, statevector):
        """Calcola il grado di entanglement"""
        return np.abs(statevector).std()

    def calcola_armonia(self, statevector):
        """Calcola l'armonia del stato (basato sulla coerenza)"""
        return np.mean(np.abs(statevector))
