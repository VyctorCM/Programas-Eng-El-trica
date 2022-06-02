# Ensaio a Vazio

import math

# TRANSFORMADOR 1 (Refenciado à bobina secundária, BT)
# Dados do trafo 1
Ivz = 20.71
Vvz = 240
P = 14345.3 / 3  # Potência encontrada pela simulação de ensaio vz no FEMM (adaptado para monofásico)
# Cálculo dos itens (referentes ao circuito monofásico equivalente)
S = (Vvz * Ivz)
Fp = P / S
Arcos = math.acos(Fp)
Q = (P * math.tan(Arcos))
Z = Vvz / Ivz
Rc = (pow(Vvz, 2)) / P
Xm = (pow(Vvz, 2)) / Q
Lm = Xm / (120 * (math.pi))
print(f'Corrente:', Ivz, '\nTensão :', Vvz, '\nPotência Ativa:', round(P, 4), '\nPotência Aparente:', round(S, 4),
      '\nPotência Reativa:', round(Q, 4), '\nImpedância:', round(Z, 4), '\nResistência:', round(Rc, 4),
      '\nReatância de Magnetização:', round(Xm, 4), '\nIndutância:', round(Lm, 4))

import math

# TRANSFORMADOR 2 (Refenciado à bobina secundária, BT)

# Dados do trafo 2

Ivz2 = 5.4
Vvz2 = 240
P2 = 560.73 / 3  # Potência encontrada pela simulação de ensaio vz no FEMM (adaptado para monofásico)

# Cálculo dos itens (referentes ao circuito monofásico equivalente)
S2 = (Vvz2 * Ivz2)
Fp2 = P2 / S2
Arcos2 = math.acos(Fp2)
Q2 = (P2 * math.tan(Arcos2))

Z2 = Vvz2 / Ivz2
Rc2 = (pow(Vvz2, 2)) / P2
Xm2 = (pow(Vvz2, 2)) / Q2
Lm2 = Xm2 / (120 * math.pi)

print(f'Corrente:', Ivz2, '\nTensão :', Vvz2, '\nPotência Ativa:', round(P2, 4), '\nPotência Aparente:', round(S2, 4),
      '\nPotência Reativa:', round(Q2, 4), '\nImpedância:', round(Z2, 4), '\nResistência:', round(Rc2, 4),
      '\nReatância de Magnetização:', round(Xm2, 4), '\nIndutância:', round(Lm2, 4))

"""Referenciando para o lado primário

"""

# Relação entre as bobinas
a = 10
Rcref = Rc * (pow(a, 2))
Lmref = Lm * pow(a, 2)
Rcref2 = Rc2 * pow(a, 2)
Lmref2 = Lm2 * pow(a, 2)

print(f'Com os dados de referenciados para o lado primário: \nResistência do trafo1 :', round(Rcref, 4),
      'Indutância de Magnetização do trafo1:', round(Lmref, 4),
      '\nResistência do trafo2:', round(Rcref2, 4), 'Indutância de Magnetização do trafo2:', round(Lmref2, 4))

"""Ensaio Curto Circuito"""

import math

# TRANSFORMADOR 1 (Refenciado à bobina Primária, AT)
# Dados do Trafo 1 ensaio cc
Icc = 20.5
Vcc = 48
Pcc = 1848.85 / 3  # Potência encontrada pela simulação de ensaio cc no FEMM (adaptado para monofásico)

# Cálculo dos itens (referentes ao circuito monofásico equivalente)
Scc = (Vcc * Icc)
Fpcc = Pcc / Scc
Arcocc = math.acos(Fpcc)
Qcc = (Pcc * math.tan(Arcocc))

Rcceq = Pcc / (pow(Icc, 2))
Rcc1 = Rcceq / 2
Rcc2 = Rcceq / 2

Xcceq = Qcc / (pow(Icc, 2))
Lcceq = Xcceq / (120 * math.pi)
L1 = Lcceq / 2
L2 = Lcceq / 2

print(
    f'Corrente: {Icc}\nTensão :{Vcc}\nPotência Ativa: {round(Pcc, 4)} \nPotência Aparente: {round(Scc, 4)} \nPotência '
    f'Reativa: {round(Qcc, 4)}\nResistência Equivalente: {round(Rcceq, 4)}\nReatância de Dispersão: '
    f'{round(Xcceq, 4)} \nIndutância: {round(Lcceq, 4)} \nResistência1: {round(Rcc1, 4)}\nResistência2: '
    f'{round(Rcc2, 4)}\nIndutância1: {round(L1, 4)}\nIndutância2: {round(L2, 4)}')

import math

# TRANSFORMADOR 2 (Refenciado à bobina Primária, AT)
# Dados do trafo 2 ensaio cc
Icc2 = 20.5
Vcc2 = 162
Pcc2 = 9607.05 / 3  # Potência encontrada pela simulação no FEMM

# Cálculo dos itens (referentes ao circuito monofásico equivalente)
Scc2 = (Vcc2 * Icc2)
Fpcc2 = Pcc2 / Scc2
Arcocc2 = math.acos(Fpcc2)
Qcc2 = (Pcc2 * math.tan(Arcocc2))

Rcceq2 = Pcc2 / (pow(Icc2, 2))
Rcc1b = Rcceq2 / 2
Rcc2b = Rcceq2 / 2

Xcceq2 = Qcc2 / (pow(Icc2, 2))
Lcceq2 = Xcceq2 / (120 * math.pi)
L1b = Lcceq2 / 2
L2b = Lcceq2 / 2

print(
    f'Corrente: {Icc2}\nTensão :{Vcc2}\nPotência Ativa: {round(Pcc2, 4)} \nPotência Aparente: {round(Scc2, 4)} '
    f'\nPotência Reativa: {round(Qcc2, 4)}\nResistência Equivalente: {round(Rcceq2, 4)}\nReatância de Dispersão: '
    f'{round(Xcceq2, 4)} \nIndutância: {round(Lcceq2, 4)} \nResistência1: {round(Rcc1b, 4)}\nResistência2: '
    f'{round(Rcc2b, 4)}\nIndutância1: {round(L1b, 4)}\nIndutância2: {round(L2b, 4)}')
