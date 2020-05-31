from Die import Die
from Roller import Roller
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['lines.markersize'] = 5
numtrials = 1000000

d20 = Die(20)
dm = Roller()
norm = (1/numtrials)*100
rolls = [d20.roll() for i in range(1,numtrials)]
adv = [dm.advantage() for i in range(1,numtrials)]
dis = [dm.disadvantage() for i in range(1,numtrials)]
advdis = [dm.advdis() for i in range(1,numtrials)]
disadv = [dm.disadv() for i in range(1,numtrials)]
# advadvdis = [dm.advadvdis() for i in range(1,numtrials)]
# advdisadv = [dm.advdisadv() for i in range(1,numtrials)]
# disadvdis = [dm.disadvdis() for i in range(1,numtrials)]
# disdisadv = [dm.disdisadv() for i in range(1,numtrials)]

print("Expected values: ")
print(f"D20: {sum(rolls)/len(rolls)}")
print(f"Adv: {sum(adv)/len(adv)}")
print(f"Dis: {sum(dis)/len(dis)}")
print(f"AdvDis: {sum(advdis)/len(advdis)}")
print(f"DisAdv: {sum(disadv)/len(disadv)}")

bins = [x - 0.5 for x in np.arange(1,22) ]
bin_length = len(bins)

# Draw two paneled figure for regular D20 roll
fig1, ax1 = plt.subplots(2,sharex=True)
counts1, bins1, patches1= ax1[0].hist(rolls, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls))
counts1c, bins1c, patches1c=ax1[1].hist(rolls, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
scatterX = [x + 0.5 for x in np.delete( bins1c,[bin_length-1] ) ]
cleanup = [b.remove() for b in patches1]
cleanup = [b.remove() for b in patches1c]
ax1[0].scatter(scatterX,counts1,marker='o',facecolors='none',edgecolors='b')
ax1[0].grid(axis='x',linestyle='dotted')
ax1[0].set_axisbelow(True)
ax1[0].set_ylim(0.01,10)
ax1[0].set_ylabel("Prob. of rolling N (%)")
ax1[1].scatter(scatterX,counts1c,marker='s',facecolors='b')
ax1[1].set_axisbelow(True)
ax1[1].set_ylabel("Prob. of beating N (%)")
ax1[1].set_xlabel("N")
ax1[1].set_xlim(0.5,20.5)
ax1[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.subplots_adjust(hspace=.0)
ax1[1].grid(axis='x',linestyle='dotted')
fig1.savefig('d20.png',dpi=300)

# Draw two paneled figure for advantage and disadvantage
fig2, ax2 = plt.subplots(2,sharex=True)
counts2, bins2, patches2=ax2[0].hist(adv, bins = bins, alpha = 0.5,label='Adv',weights=norm*np.ones_like(rolls))
counts2c, bins2c, patches2c=ax2[1].hist(adv, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
counts3, bins3, patches3=ax2[0].hist(dis, bins = bins, alpha = 0.5,label='Dis',weights=norm*np.ones_like(rolls))
counts3c, bins3c, patches3c=ax2[1].hist(dis, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
cleanup = [b.remove() for b in patches2]
cleanup = [b.remove() for b in patches2c]
cleanup = [b.remove() for b in patches3]
cleanup = [b.remove() for b in patches3c]
l2_1 = ax2[0].scatter(scatterX,counts2,marker='o',facecolors='none',edgecolors='g')
l2_2 = ax2[0].scatter(scatterX,counts3,marker='o',facecolors='none',edgecolors='r')
ax2[0].grid(axis='x',linestyle='dotted')
ax2[0].set_axisbelow(True)
ax2[0].set_ylim(0.01,10)
ax2[0].set_ylabel("Prob. of rolling N (%)")
l2_3 = ax2[1].scatter(scatterX,counts2c,marker='s',facecolors='g',label='Advantage')
l2_4 = ax2[1].scatter(scatterX,counts3c,marker='s',facecolors='r',label='Disadvantage')
ax2[1].set_axisbelow(True)
ax2[1].set_ylabel("Prob. of beating N (%)")
ax2[1].set_xlabel("N")
ax2[1].set_xlim(0.5,20.5)
ax2[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.subplots_adjust(hspace=.0)
ax2[1].grid(axis='x',linestyle='dotted')
handles2 = [(l2_1,l2_3),(l2_2,l2_4)]
_, labels2 = ax2[1].get_legend_handles_labels()
ax2[1].legend(handles = handles2, labels=labels2, loc='upper right', 
          handler_map = {tuple: mpl.legend_handler.HandlerTuple(None)})
fig2.savefig('advantage-vs-disadvantage.png',dpi=300)

# Draw two paneled figure for advantage of disadvantage and vice versa
fig3, ax3 = plt.subplots(2,sharex=True)
counts4, bins4, patches4=ax3[0].hist(advdis, bins = bins, alpha = 0.5,label='AdvDis',weights=norm*np.ones_like(rolls))
counts4c, bins4c, patches4c=ax3[1].hist(advdis, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
counts5, bins5, patches5=ax3[0].hist(disadv, bins = bins, alpha = 0.5,label='DisAdv',weights=norm*np.ones_like(rolls))
counts5c, bins5c, patches5c=ax3[1].hist(disadv, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
cleanup = [b.remove() for b in patches4]
cleanup = [b.remove() for b in patches4c]
cleanup = [b.remove() for b in patches5]
cleanup = [b.remove() for b in patches5c]
l3_1 = ax3[0].scatter(scatterX,counts4,marker='o',facecolors='none',edgecolors='c')
l3_2 = ax3[0].scatter(scatterX,counts5,marker='o',facecolors='none',edgecolors='m')
ax3[0].grid(axis='x',linestyle='dotted')
ax3[0].set_axisbelow(True)
ax3[0].set_ylim(0.01,10)
ax3[0].set_ylabel("Prob. of rolling N (%)")
l3_3 = ax3[1].scatter(scatterX,counts4c,marker='s',facecolors='c',label='AdvDis')
l3_4 = ax3[1].scatter(scatterX,counts5c,marker='s',facecolors='m',label='DisAdv')
ax3[1].set_axisbelow(True)
ax3[1].set_ylabel("Prob. of beating N (%)")
ax3[1].set_xlabel("N")
ax3[1].set_xlim(0.5,20.5)
ax3[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.subplots_adjust(hspace=.0)
ax3[1].grid(axis='x',linestyle='dotted')
handles3 = [(l3_1,l3_3),(l3_2,l3_4)]
_, labels3 = ax3[1].get_legend_handles_labels()
ax3[1].legend(handles = handles3, labels=labels3, loc='upper right', 
          handler_map = {tuple: mpl.legend_handler.HandlerTuple(None)})
fig3.savefig('advdis-vs-disadv.png',dpi=300)

# Draw two paneled figure for everything (kind of busy)
fig4, ax4 = plt.subplots(2,sharex=True)
counts4, bins4, patches4=ax4[0].hist(advdis, bins = bins, alpha = 0.5,label='AdvDis',weights=norm*np.ones_like(rolls))
counts4c, bins4c, patches4c=ax4[1].hist(advdis, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
counts5, bins5, patches5=ax4[0].hist(disadv, bins = bins, alpha = 0.5,label='DisAdv',weights=norm*np.ones_like(rolls))
counts5c, bins5c, patches5c=ax4[1].hist(disadv, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
cleanup = [b.remove() for b in patches4]
cleanup = [b.remove() for b in patches4c]
cleanup = [b.remove() for b in patches5]
cleanup = [b.remove() for b in patches5c]
ax4[0].scatter(scatterX,counts4,marker='o',facecolors='none',edgecolors='c')
ax4[0].scatter(scatterX,counts5,marker='o',facecolors='none',edgecolors='m')
ax4[0].scatter(scatterX,counts1,marker='o',facecolors='none',edgecolors='b')
ax4[0].scatter(scatterX,counts2,marker='o',facecolors='none',edgecolors='g')
ax4[0].scatter(scatterX,counts3,marker='o',facecolors='none',edgecolors='r')
ax4[0].grid(axis='x',linestyle='dotted')
ax4[0].set_axisbelow(True)
ax4[0].set_ylim(0.01,10)
ax4[0].set_ylabel("Prob. of rolling N (%)")
ax4[1].scatter(scatterX,counts4c,marker='s',facecolors='c')
ax4[1].scatter(scatterX,counts5c,marker='s',facecolors='m')
ax4[1].scatter(scatterX,counts1c,marker='s',facecolors='b')
ax4[1].scatter(scatterX,counts2c,marker='s',facecolors='g')
ax4[1].scatter(scatterX,counts3c,marker='s',facecolors='r')
ax4[1].set_axisbelow(True)
ax4[1].set_ylabel("Prob. of beating N (%)")
ax4[1].set_xlabel("N")
ax4[1].set_xlim(0.5,20.5)
ax4[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.subplots_adjust(hspace=.0)
ax4[1].grid(axis='x',linestyle='dotted')

# Draw probability of beating target roll figure for all
fig5, ax5 = plt.subplots()
ax5.scatter(scatterX,counts4c,marker='s',facecolors='c',label='AdvDis')
ax5.scatter(scatterX,counts5c,marker='s',facecolors='m',label='DisAdv')
ax5.scatter(scatterX,counts1c,marker='s',facecolors='b',label='D20')
ax5.scatter(scatterX,counts2c,marker='s',facecolors='g',label='Advantage')
ax5.scatter(scatterX,counts3c,marker='s',facecolors='r',label='Disadvantage')
ax5.set_axisbelow(True)
ax5.set_ylabel("Prob. of beating N (%)")
ax5.set_xlabel("N")
ax5.set_xlim(0.5,20.5)
ax5.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.subplots_adjust(hspace=.0)
ax5.grid(axis='x',linestyle='dotted')
ax5.legend()
fig5.savefig('comparison-all.png',dpi=300)
plt.show()

# # Draw two paneled figure for another layer deeper
# fig6, ax6 = plt.subplots(2,sharex=True)
# counts6, bins6, patches6=ax6[0].hist(disadvdis, bins = bins, alpha = 0.5,label='DisAdvDis',weights=norm*np.ones_like(rolls))
# counts6c, bins6c, patches6c=ax6[1].hist(disadvdis, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
# counts7, bins7, patches7=ax6[0].hist(advdisadv, bins = bins, alpha = 0.5,label='AdvDisAdv',weights=norm*np.ones_like(rolls))
# counts7c, bins7c, patches7c=ax6[1].hist(advdisadv, bins = bins, alpha = 0.5,label='d20',weights=norm*np.ones_like(rolls),cumulative=-1)
# cleanup = [b.remove() for b in patches6]
# cleanup = [b.remove() for b in patches6c]
# cleanup = [b.remove() for b in patches7]
# cleanup = [b.remove() for b in patches7c]
# l6_1 = ax6[0].scatter(scatterX,counts6,marker='o',facecolors='none',edgecolors='c')
# l6_2 = ax6[0].scatter(scatterX,counts7,marker='o',facecolors='none',edgecolors='m')
# ax6[0].grid(axis='x',linestyle='dotted')
# ax6[0].set_axisbelow(True)
# ax6[0].set_ylim(0.01,10)
# ax6[0].set_ylabel("Prob. of rolling N (%)")
# l6_3 = ax6[1].scatter(scatterX,counts6c,marker='s',facecolors='c',label='DisAdvDis')
# l6_4 = ax6[1].scatter(scatterX,counts7c,marker='s',facecolors='m',label='AdvDisAdv')
# ax6[1].set_axisbelow(True)
# ax6[1].set_ylabel("Prob. of beating N (%)")
# ax6[1].set_xlabel("N")
# ax6[1].set_xlim(0.5,20.5)
# ax6[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# plt.subplots_adjust(hspace=.0)
# ax6[1].grid(axis='x',linestyle='dotted')
# handles6 = [(l6_1,l6_3),(l6_2,l6_4)]
# _, labels6 = ax6[1].get_legend_handles_labels()
# ax6[1].legend(handles = handles6, labels=labels6, loc='upper right', 
#           handler_map = {tuple: mpl.legend_handler.HandlerTuple(None)})
# plt.show()



