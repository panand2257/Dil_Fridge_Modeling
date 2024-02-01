import numpy as np
import matplotlib.pyplot as plt

# Using readlines()
file = open('data.txt', 'r')
Lines = file.readlines()

name = []
d1 = []
d2 = []
d3 = []

th = []
att4 = []
att300 = []

Len = [20, 29, 25, 17, 14] #in cm # {50K, 4K, Still, CP, MXC}
Temp = [300, 35, 2.85, 0.882, 0.082, 0.006] #in K {50K, 4K, Still, CP, MXC}
P_50 = []
P_4 = []
P_Still = []
P_CP = []
P_MXC = []

L_50 = []
L_4 = []
L_Still = []
L_CP = []
L_MXC = []

F_50 = []
F_4 = []
F_Still = []
F_CP = []
F_MXC = []

types = []


for L in Lines[1:]:

    data = L.split()  
    name.append(str(data[0]))
    d1.append(float(data[1]))
    d2.append(float(data[2]))
    d3.append(float(data[3]))
    th.append(float(data[4]))
    att4.append(float(data[5]))
    att300.append(float(data[6]))


for i in np.arange(len(name)):
    
    # in mW
    P_50.append(((np.pi * th[i] * (d3[i])**2 * (Temp[0]**2 - Temp[1]**2)) * 1e-2 * 1e3/(32 * Len[0])))
    P_4.append(((np.pi * th[i] * (d3[i])**2 * (Temp[1]**2 - Temp[2]**2)) * 1e-2 *1e3/(32 * Len[1])))
    P_Still.append(((np.pi * th[i] * (d3[i])**2 * (Temp[2]**2 - Temp[3]**2)) * 1e-2 * 1e3/(32 * Len[2])))
    P_CP.append(((np.pi * th[i] * (d3[i])**2 * (Temp[3]**2 - Temp[4]**2)) * 1e-2 * 1e3/(32 * Len[3])))
    P_MXC.append(((np.pi * th[i] * (d3[i])**2 * (Temp[4]**2 - Temp[5]**2)) * 1e-2 * 1e3/(32 * Len[4])))

    A = (att300[i] - att4[i])/296.0
    B = (300*att4[i] - 4*att300[i])/296.0

    b1 = (Temp[0] - Temp[1])/Len[0]
    b2 = (Temp[1] - Temp[2])/Len[1]
    b3 = (Temp[2] - Temp[3])/Len[2]
    b4 = (Temp[3] - Temp[4])/Len[3]
    b5 = (Temp[4] - Temp[5])/Len[4]

    L_50.append( 0.01*(A*Temp[0] + B)*Len[0] - 0.01*A * b1 * (Len[0]**2)/2)
    L_4.append( 0.01*(A*Temp[1] + B)*Len[1] - 0.01* A * b2 * (Len[1]**2)/2)
    L_Still.append( 0.01*(A*Temp[2] + B)*Len[2] - 0.01*A * b3 * (Len[2]**2)/2)
    L_CP.append( 0.01*(A*Temp[3] + B)*Len[3] - 0.01*A * b4 * (Len[3]**2)/2)
    L_MXC.append( 0.01*(A*Temp[4] + B)*Len[4] - 0.01*A * b5 * (Len[4]**2)/2)

    F_50.append( (0.01*(A*Temp[0] + B)*Len[0] - 0.01*A * b1 * (Len[0]**2)/2) / ((np.pi * th[i] * (d3[i])**2 * (Temp[0]**2 - Temp[1]**2)) * 1e-2 * 1e3/(32 * Len[0])) )
    F_4.append( (0.01*(A*Temp[1] + B)*Len[1] - 0.01* A * b2 * (Len[1]**2)/2) / ((np.pi * th[i] * (d3[i])**2 * (Temp[1]**2 - Temp[2]**2)) * 1e-2 *1e3/(32 * Len[1])))
    F_Still.append( (0.01*(A*Temp[2] + B)*Len[2] - 0.01*A * b3 * (Len[2]**2)/2) / ((np.pi * th[i] * (d3[i])**2 * (Temp[2]**2 - Temp[3]**2)) * 1e-2 * 1e3/(32 * Len[2])))
    F_CP.append( (0.01*(A*Temp[3] + B)*Len[3] - 0.01*A * b4 * (Len[3]**2)/2) / ((np.pi * th[i] * (d3[i])**2 * (Temp[3]**2 - Temp[4]**2)) * 1e-2 * 1e3/(32 * Len[3])))
    F_MXC.append( (0.01*(A*Temp[4] + B)*Len[4] - 0.01*A * b5 * (Len[4]**2)/2) / ((np.pi * th[i] * (d3[i])**2 * (Temp[4]**2 - Temp[5]**2)) * 1e-2 * 1e3/(32 * Len[4])))


    types.append(name[i])
    
#Plotting
#plt.figure(figsize=(10, 10))

categories = ['50K', '4K', 'Still', 'CP', 'MXC']
values_HL = np.array([P_50, P_4, P_Still, P_CP, P_MXC])
values_att = np.array([L_50, L_4, L_Still, L_CP, L_MXC])
values_F = np.array([F_50, F_4, F_Still, F_CP, F_MXC])

# Set up the positions for bars within each category
positions = 4*np.arange(len(categories))

# Set up the width for each bar
bar_width = 0.1  # Adjust this value based on your preferences

# Create grouped bar plot
for i, type_label in enumerate(types):
    colors = plt.cm.plasma(i / len(types))
    plt.bar(positions + i * bar_width, values_F[:, i], bar_width, label=type_label, color=colors)


# Add labels and title
plt.xlabel('Stages')
#plt.ylabel('Passive heat load (mW)')
#plt.ylabel('Attenuation (dB)')
plt.ylabel('Figure of Merit')
plt.yscale('log')
plt.title('Coax Co. RF Cables')
plt.xticks(positions + 0.5*len(name)*bar_width , categories)

plt.legend(ncol=3)

# Show the plot
plt.show()