import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

suhu = ctrl.Antecedent(np.arange(0, 40), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 100), 'kelembaban')
kecepatanKipas = ctrl.Consequent(np.arange(0, 100), 'kecepatanKipas')

suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['Panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembaban['Rendah'] = fuzz.trimf(kelembaban.universe, [0, 0, 50])
kelembaban['Normal'] = fuzz.trimf(kelembaban.universe, [30, 50, 70])
kelembaban['Tinggi'] = fuzz.trimf(kelembaban.universe, [50, 100, 100])

kecepatanKipas['Rendah'] = fuzz.trimf(kecepatanKipas.universe, [0, 0, 50])
kecepatanKipas['Normal'] = fuzz.trimf(kecepatanKipas.universe, [30, 50, 70])
kecepatanKipas['Tinggi'] = fuzz.trimf(kecepatanKipas.universe, [50, 100, 100])

aturan1 = ctrl.Rule(suhu['Dingin'] & kelembaban['Rendah'], kecepatanKipas['Rendah'])
aturan2 = ctrl.Rule(suhu['Normal'] | kelembaban['Normal'], kecepatanKipas['Normal'])
aturan3 = ctrl.Rule(suhu['Panas'] | kelembaban['Tinggi'], kecepatanKipas['Tinggi'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

system.input['suhu'] = 28
system.input['kelembaban'] = 60
system.compute()
print(system.output['kecepatanKipas'])

kecepatanKipas.view(sim=system)
input("Tekan ENTER untuk melanjutkan")