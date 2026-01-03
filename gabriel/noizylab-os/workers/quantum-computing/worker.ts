import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { QUANTUM_DB: D1Database; AI: any; }
const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// NOIZYLAB OS - QUANTUM COMPUTING WORKER
const QUANTUM_COMPUTING = {
    foundations: {
        qubit: { name: 'Qubit', significance: 'Quantum bit - superposition of 0 and 1' },
        superposition: { name: 'Superposition', significance: 'Quantum state existing in multiple states' },
        entanglement: { name: 'Entanglement', significance: 'Correlated quantum states (Einstein: "spooky action")' },
        decoherence: { name: 'Decoherence', significance: 'Loss of quantum state' },
        quantum_gates: { name: 'Quantum Gates', examples: ['Hadamard', 'CNOT', 'Pauli-X/Y/Z', 'Toffoli', 'SWAP'] }
    },
    algorithms: {
        shor: { name: "Shor's Algorithm", year: 1994, pioneer: 'Peter Shor', significance: 'Factor integers (breaks RSA)' },
        grover: { name: "Grover's Algorithm", year: 1996, pioneer: 'Lov Grover', significance: 'Quadratic speedup for search' },
        vqe: { name: 'VQE (Variational Quantum Eigensolver)', significance: 'Chemistry simulations' },
        qaoa: { name: 'QAOA', significance: 'Optimization problems' },
        qft: { name: 'Quantum Fourier Transform', significance: 'Core of many quantum algorithms' }
    },
    hardware: {
        ibm_quantum: { name: 'IBM Quantum', qubits: '1000+ (Condor)', technology: 'Superconducting transmons' },
        google_quantum: { name: 'Google Quantum AI', achievements: ['Sycamore (53 qubits)', 'Quantum supremacy 2019', 'Willow (2024)'] },
        ionq: { name: 'IonQ', technology: 'Trapped ions', qubits: '32+ algorithmic qubits' },
        rigetti: { name: 'Rigetti', technology: 'Superconducting', products: ['Aspen', 'Ankaa'] },
        dwave: { name: 'D-Wave', technology: 'Quantum annealing', qubits: '5000+', note: 'Not universal QC' },
        honeywell_quantinuum: { name: 'Quantinuum', technology: 'Trapped ions', features: 'Highest fidelity' },
        xanadu: { name: 'Xanadu', technology: 'Photonic', framework: 'PennyLane' },
        pasqal: { name: 'Pasqal', technology: 'Neutral atoms' },
        atom_computing: { name: 'Atom Computing', technology: 'Neutral atoms', qubits: '1000+' }
    },
    frameworks: {
        qiskit: { name: 'Qiskit', developer: 'IBM', language: 'Python', significance: 'Most popular QC framework' },
        cirq: { name: 'Cirq', developer: 'Google', significance: 'NISQ algorithms' },
        pennylane: { name: 'PennyLane', developer: 'Xanadu', significance: 'Quantum ML' },
        braket: { name: 'Amazon Braket', developer: 'AWS', significance: 'Multi-hardware access' },
        q_sharp: { name: 'Q#', developer: 'Microsoft', significance: 'Quantum programming language' },
        ocean: { name: 'Ocean', developer: 'D-Wave', significance: 'Quantum annealing' }
    },
    milestones: {
        supremacy_2019: { name: 'Google Quantum Supremacy', year: 2019, significance: '53 qubits, task in 200s vs 10,000 years classical' },
        advantage_2020: { name: 'D-Wave Advantage', year: 2020, qubits: 5000 },
        error_correction_2023: { name: 'Error Correction Progress', year: 2023, significance: 'Google/IBM QEC advances' },
        willow_2024: { name: 'Google Willow', year: 2024, significance: 'Below error correction threshold' }
    }
};

app.get('/api/quantum/categories', (c) => c.json({ success: true, categories: Object.keys(QUANTUM_COMPUTING) }));
app.get('/api/quantum/:cat', (c) => {
    const cat = c.req.param('cat') as keyof typeof QUANTUM_COMPUTING;
    return QUANTUM_COMPUTING[cat] ? c.json({ success: true, data: QUANTUM_COMPUTING[cat] }) : c.json({ error: 'Not found' }, 404);
});
app.get('/health', (c) => c.json({ status: 'healthy', worker: 'quantum-computing-worker' }));

export default app;
