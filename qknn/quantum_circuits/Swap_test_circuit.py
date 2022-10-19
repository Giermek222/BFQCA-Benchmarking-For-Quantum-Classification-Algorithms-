from qiskit import QuantumCircuit


def Create_Single_Circuit(qc_alpha: QuantumCircuit, qc_beta: QuantumCircuit) -> QuantumCircuit:
    qc = QuantumCircuit(qc_alpha.num_qubits + qc_beta.num_qubits + 1, 1)

    alpha_qubit_names = [i + 1 for i in range(qc_alpha.num_qubits)]
    beta_qubit_names = [i + qc_alpha.num_qubits + 1 for i in range(qc_alpha.num_qubits)]

    qc.compose(qc_alpha, alpha_qubit_names, inplace=True)
    qc.compose(qc_beta, beta_qubit_names, inplace=True)

    return qc


def Create_Swap_test_Circuit(qc_alpha: QuantumCircuit, qc_beta: QuantumCircuit) -> QuantumCircuit:
    # qc = Create_Single_Circuit(qc_alpha, qc_beta)
    #
    # #     add Hadamarrd gates and Fredkin (cswap) gates
    # qc.h(0)
    # qubits_len = qc_alpha.num_qubits
    # if not qubits_len == qc_beta.num_qubits:
    #     raise ValueError(
    #         f"quantum circuits provided into Swap_1 Test Gate must be equal length. Got alpha with {qc_alpha.num_qubits} qubits, beta with {qc_beta.num_qubits} qubits")
    # for alpha_qubit in range(qubits_len):
    #     qc.cswap(0, alpha_qubit+1, alpha_qubit + qubits_len+1)
    #
    # qc.barrier()
    # # measure top qubit
    # qc.measure(0, 0)

    return SwaptestCircuit(qc_alpha, qc_beta)


class SwaptestCircuit(QuantumCircuit):

    def __init__(self,
                 qc_state_1: QuantumCircuit,
                 qc_state_2: QuantumCircuit,
                 name: str = None):
        n_total = qc_state_1.num_qubits + qc_state_2.num_qubits
        super().__init__(n_total + 1, 1, name=name)

        # range_qc1 = [i + 1 for i in range(qc_state_1.num_qubits)]
        # range_qc2 = [i + qc_state_1.num_qubits + 1 for i in range(qc_state_1.num_qubits)]

        self.compose(Create_Single_Circuit(qc_state_1, qc_state_2), inplace=True)

        # first apply hadamard
        self.h(0)
        # then perform controlled swaps
        for alpha_qubit in range(2):
            self.cswap(0, alpha_qubit + 1, 1 + alpha_qubit + 2)
        # eventually reapply hadamard
        self.h(0)

        # Measurement on the auxiliary qubit
        self.barrier()
        self.measure(0, 0)
