import numpy as np
from qutip import basis
import random

# define horizontal and vertical polarization states
H = basis(2,0)
V = basis(2,1)
# define alternative linear polarized basis vectors |+> and |-> 
P45 = 1 / np.sqrt(2) * (H + V)
M45 = 1 / np.sqrt(2) * (H - V)
# define circularly polarized basis vectors |L> and |R>
L = 1 / np.sqrt(2) * (H - 1.j * V)
R = 1 / np.sqrt(2) * (H + 1.j * V)

# define projection operators
Ph = H * H.dag()
Pv = V * V.dag()

# Encoding modes
basisHV = [H, V]
basisPM45 = [P45, M45]
modes = [basisHV, basisPM45]

def probability_amplitude(s1, s2):
    ''' calculate the probability amplitude of measuring state s1 in the basis of state s2 '''
    return s1.unit().overlap(s2.unit())

def measurement_probability(s1, s2):
    ''' calculate the probability of measuring state s1 in the basis of state s2 '''
    return abs(probability_amplitude(s1.unit(), s2.unit()))**2


class Photon:
    ''' Photon class that can be encoded with either one of the two modes for QKD. '''
    def __init__(self, state):
        self._state = state
        
    def measure(self, m_basis):
        ''' All information one can read is through measurement, which may change the state. '''        
        if np.random.rand() < measurement_probability(self._state, m_basis[0]):
            self._state = m_basis[0]
            return 0
        else:
            self._state = m_basis[1]
            return 1
    
    def __repr__(self):
        ''' A method that is invoked when a simple string representation of the class is needed, 
            as for example when printed. '''
        return("{}, {}".format(self._state[0], self._state[1]))

# # create a instance of a Photon class
# p = Photon(P45)
# 
# # To invoke the measure class method in the class instance
# print(p.measure(basisHV))
# print(p)

'''------------------- BB84 Protocol simulation -------------------'''

# generate random bits with length nb
def bit_generate(nb = 1):
    ''' Random initialize a bit, i.e., 0 or 1. '''
    return np.random.randint(0,2,nb)

# Alice's keys, randomly initialized.
nbits = 1000
Alice_bits = bit_generate(nbits)

def mode_select():
    ''' Randomly choose between mode HV and mode PM45. '''
    return np.random.randint(0,2)

# Alice: prepare photons to be tranmitted.
Alice_modes = []
Alice_prepared = []
for i in range(len(Alice_bits)):
    mode = mode_select()
    Alice_modes.append(mode)
    Alice_prepared.append(Photon(modes[mode][Alice_bits[i]]))

# Bob receives the photons, assume no environmental noise
Bob_received = Alice_prepared.copy()
Alice_prepared.clear()

# Bob randomly selects modes to measure the photons.
Bob_modes = []
Bob_bits = []
for p in Bob_received:
    mode = mode_select()
    Bob_modes.append(mode)
    Bob_bits.append(p.measure(modes[mode]))

# Alice and Bob compare their sequence of modes and sift the list of keys. 
keys = []
for am,bm,ab,bb in zip(Alice_modes,Bob_modes,Alice_bits,Bob_bits):
    if (am == bm): # compared modes through a classical channel
        assert ab == bb
        keys.append(ab)

print ('Sifted keys:', len(keys))
# 密钥太长了，暂时注释掉
# print(keys)

