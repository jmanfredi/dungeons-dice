from Die import Die
from Roller import Roller
import numpy as np
import matplotlib.pyplot as plt

d20 = Die(20)
dm = Roller()
numtrials = 100000
rolls = [d20.roll() for i in range(1,numtrials)]
adv = [dm.advantage() for i in range(1,numtrials)]
dis = [dm.disadvantage() for i in range(1,numtrials)]
advdis = [dm.advdis() for i in range(1,numtrials)]
disadv = [dm.disadv() for i in range(1,numtrials)]

bins = np.arange(1,22)

fig1, ax1 = plt.subplots()
ax1.hist(rolls, bins = bins, alpha = 0.5,label='d20')
ax1.set_xlim([0,22])

fig2, ax2 = plt.subplots()
ax2.hist(adv, bins = bins, alpha = 0.5,label='Adv')

fig3, ax3 = plt.subplots()
ax3.hist(dis, bins = bins, alpha = 0.5,label='Dis')

fig4, ax4 = plt.subplots()
ax4.hist(advdis, bins = bins, alpha = 0.5,label='AdvDis')

fig5, ax5 = plt.subplots()
ax5.hist(disadv, bins = bins, alpha = 0.5,label='DisAdv')

plt.show()