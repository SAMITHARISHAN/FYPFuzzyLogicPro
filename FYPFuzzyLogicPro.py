import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions
vehicle = ctrl.Antecedent(np.arange(0, 11, 1), 'vehicle')
vSpeed = ctrl.Antecedent(np.arange(0, 11, 1), 'vSpeed')
pedestrian = ctrl.Antecedent(np.arange(0, 11, 1), 'pedestrian')
signal = ctrl.Consequent(np.arange(0, 11, 1), 'signal')

# Auto-membership function population is possible with .automf(3, 5, or 7)
# quality.automf(3)
# service.automf(3)

vehicle['low'] = fuzz.trimf(vehicle.universe, [0, 0, 13])
vehicle['medium'] = fuzz.trimf(vehicle.universe, [0, 13, 25])
vehicle['high'] = fuzz.trimf(vehicle.universe, [13, 25, 25])

vSpeed['low'] = fuzz.trimf(vSpeed.universe, [0, 0, 20])
vSpeed['medium'] = fuzz.trimf(vSpeed.universe, [0, 20, 40])
vSpeed['high'] = fuzz.trimf(vSpeed.universe, [20, 40, 60])

pedestrian['low'] = fuzz.trimf(pedestrian.universe, [0, 0, 13])
pedestrian['medium'] = fuzz.trimf(pedestrian.universe, [0, 13, 25])
pedestrian['high'] = fuzz.trimf(pedestrian.universe, [13, 25, 25])
# Custom membership functions can be built interactively with a familiar,
# Pythonic API
signal['off'] = fuzz.trimf(signal.universe, [0, 0, 6])
signal['on'] = fuzz.trimf(signal.universe, [0, 6, 10])



# You can see how these look with .view()
vehicle.view()
plt.show()

vSpeed.view()
plt.show()

pedestrian.view()
plt.show()

signal.view()
plt.show()


rule1 = ctrl.Rule(vehicle['low'] | pedestrian['low'] & vSpeed['high'], signal['off'])
rule2 = ctrl.Rule(vehicle['medium'] & pedestrian['low'] & vSpeed['high'],signal['off'])
rule3 = ctrl.Rule(vehicle['high'] | pedestrian['high'] & vSpeed['low'], signal['on'])
rule4 = ctrl.Rule(vehicle['high'] | pedestrian['low'] & vSpeed['high'], signal['off'])
rule5 = ctrl.Rule(vehicle['high'] | pedestrian['high'] & vSpeed['medium'], signal['on'])

rule1.view()
plt.show()



signal_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])


TLsignal = ctrl.ControlSystemSimulation(signal_ctrl)

TLsignal.input['vehicle'] = 5
TLsignal.input['pedestrian'] = 5 
TLsignal.input['vSpeed'] = 20


# Crunch the numbers
TLsignal.compute()

print(TLsignal.output['signal'])
signal.view(sim=TLsignal)
plt.show()
