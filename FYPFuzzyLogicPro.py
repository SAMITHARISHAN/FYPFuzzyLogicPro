import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# New Antecedent/Consequent objects hold universe variables and membership
# functions
vehicle = ctrl.Antecedent(np.arange(0, 25, 1), 'vehicle')
vSpeed = ctrl.Antecedent(np.arange(0, 60, 1), 'vSpeed')
pedestrian = ctrl.Antecedent(np.arange(0, 25, 1), 'pedestrian')
WaitingTime = ctrl.Antecedent(np.arange(0,100,1), 'WaitingTime')
signal = ctrl.Consequent(np.arange(0, 11, 1), 'signal')

# Auto-membership function population is possible with .automf(3, 5, or 7)

vehicle['low'] = fuzz.trimf(vehicle.universe, [0, 0, 13])
vehicle['medium'] = fuzz.trimf(vehicle.universe, [0, 13, 25])
vehicle['high'] = fuzz.trimf(vehicle.universe, [13, 25, 25])

WaitingTime['low'] = fuzz.trimf(WaitingTime.universe, [0, 0, 20])
WaitingTime['medium'] = fuzz.trimf(WaitingTime.universe, [0, 20, 40])
WaitingTime['high'] = fuzz.trimf(WaitingTime.universe, [20, 40, 100])

vSpeed['low'] = fuzz.trimf(vSpeed.universe, [0, 0, 20])
vSpeed['medium'] = fuzz.trimf(vSpeed.universe, [0, 20, 40])
vSpeed['high'] = fuzz.trimf(vSpeed.universe, [20, 40, 60])

pedestrian['low'] = fuzz.trimf(pedestrian.universe, [0, 0, 13])
pedestrian['medium'] = fuzz.trimf(pedestrian.universe, [0, 13, 25])
pedestrian['high'] = fuzz.trimf(pedestrian.universe, [13, 25, 25])

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


rule1 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['low'], signal['on'])
rule2 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['low'], signal['off'])
rule3 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['low'], signal['off'])
rule4 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['low'], signal['on'])
rule5 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['low'], signal['on'])
rule6 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['low'], signal['off'])
rule7 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['low'], signal['on'])
rule8 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['low'], signal['on'])
rule9 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['low'], signal['on'])

rule10 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule11 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule12 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule13 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule14 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule15 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['medium'], signal['off'])
rule16 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['medium'], signal['on'])
rule17 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['medium'], signal['on'])
rule18 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['medium'], signal['off'])

rule19 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule20 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule21 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule22 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule23 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule24 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule25 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule26 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['high'], signal['off'])
rule27 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['low'] & vSpeed['high'], signal['off'])

rule28 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule29 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule30 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['low'], signal['off'])
rule31 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule32 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule33 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule34 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule35 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['low'], signal['on'])
rule36 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['low'], signal['on'])

rule37 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['medium'], signal['on'])
rule38 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['medium'], signal['off'])
rule39 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['medium'], signal['off'])
rule40 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['medium'], signal['on'])
rule41 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['medium'], signal['off'])
rule42 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['medium'], signal['off'])
rule43 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['medium'], signal['on'])
rule44 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['medium'], signal['on'])
rule45 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['medium'], signal['off'])

rule46 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule47 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule48 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule49 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule50 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule51 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule52 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule53 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['high'], signal['off'])
rule54 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['medium'] & vSpeed['high'], signal['off'])

rule55 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule56 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule57 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule58 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule59 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule60 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule61 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule62 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['low'], signal['on'])
rule63 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['low'], signal['on'])

rule64 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule65 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule66 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['medium'], signal['off'])
rule67 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule68 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule69 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['medium'], signal['off'])
rule70 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule71 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['medium'], signal['on'])
rule72 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['medium'], signal['on'])

rule73 = ctrl.Rule(vehicle['low'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule74 = ctrl.Rule(vehicle['medium'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule75 = ctrl.Rule(vehicle['high'] & WaitingTime['low'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule76 = ctrl.Rule(vehicle['low'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule77 = ctrl.Rule(vehicle['medium'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule78 = ctrl.Rule(vehicle['high'] & WaitingTime['medium'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule79 = ctrl.Rule(vehicle['low'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['high'], signal['on'])
rule80 = ctrl.Rule(vehicle['medium'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['high'], signal['off'])
rule81 = ctrl.Rule(vehicle['high'] & WaitingTime['high'] & pedestrian['high'] & vSpeed['high'], signal['off'])


rule1.view()
plt.show()



signal_ctrl = ctrl.ControlSystem([rule1,rule2, rule3,
                                 rule4,rule5,rule6,
                                 rule7,rule8,rule9,

                                 rule10,rule11,rule12,
                                 rule13,rule14,rule15,
                                 rule16,rule17,rule18,

                                 rule19,rule20,rule21,
                                 rule22,rule23,rule24,
                                 rule25,rule26,rule27,

                                 rule28,rule29,rule30,
                                 rule31,rule32,rule32,
                                 rule34,rule35,rule36,

                                 rule37,rule38,rule39,
                                 rule40,rule41,rule42,
                                 rule43,rule44,rule45,

                                 rule46,rule47,rule48,
                                 rule49,rule50,rule51,
                                 rule52,rule53,rule54,

                                 rule55,rule56,rule57,
                                 rule58,rule59,rule60,
                                 rule61,rule62,rule63,

                                 rule64,rule65,rule66,
                                 rule67,rule68,rule69,
                                 rule70,rule71,rule72,

                                 rule73,rule74,rule75,
                                 rule76,rule77,rule78,
                                 rule79,rule80,rule81  ])


TLsignal = ctrl.ControlSystemSimulation(signal_ctrl)

TLsignal.input['vehicle'] = 5
TLsignal.input['pedestrian'] = 5 
TLsignal.input['vSpeed'] = 20
TLsignal.input['WaitingTime'] = 20


# Crunch the numbers
TLsignal.compute()

print(TLsignal.output['signal'])
signal.view(sim=TLsignal)
plt.show()
