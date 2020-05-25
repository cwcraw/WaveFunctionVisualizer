import numpy as np
import matplotlib.pyplot as plt

def WaveCalc(pot):
    m = 200
    x= range(m)
    V= [0]*m
    if pot == 'Morse':
        # Morse potential
        for n in range(0,m):
            V[n] = .01*(1-(2.718)**(-.1*(n/4-10)))**2
    elif pot == 'Bar':
        # rectangular barrier high energy
        for n in range(80,120):
            V[n] = .1
    elif pot == 'Box':
        # Change in pot
        for n in range(100,200):
            V[n] = .01
    elif pot == 'HO':
        # Harmonic Oscilator
        for n in range(0,m):
            V[n] = .0001*(n-m/2+.5)**2
    elif pot == 'Open':
        for n in range(0,m):
            V[n] = 0    

    tmp_arr=[]
    output_mat = []
    for n in range(0, m):
        tmp_arr = [0]*m
        if n == 0:
            tmp_arr[0] = 2 + V[0]
            tmp_arr[1] = -1
        elif n == m-1:
            tmp_arr[m-2] = -1
            tmp_arr[m-1] = 2 +V[m-1]
        else:
            tmp_arr[n-1] = -1
            tmp_arr[n] = 2+V[n]
            tmp_arr[n+1] = -1
        output_mat.append(tmp_arr)

    # print(output_mat)
    np.array(output_mat)
    # print(output_mat)
    output_mat
    E_val_1, E_vec_1 = np.linalg.eig(output_mat)

    for i in range(1,len(E_val_1)-2):
        for j in range(0,len(E_val_1)-i):
            if (E_val_1[j] > E_val_1[j+1]):
                E_val_1[j], E_val_1[j+1] = E_val_1[j+1], E_val_1[j]
                for k in range(0,len(E_val_1)):
                    E_vec_1[k,j], E_vec_1[k,j+1] = E_vec_1[k,j+1], E_vec_1[k,j]

    # print(E_val_1/E_val_1[0])
    return E_val_1, E_vec_1, V, x

# plt.axis([0,200,0,.051])
# plt.plot(x,V)
# plt.show()
# plt.plot(x,E_vec_1[:,0]**2,marker='x')
# print(E_vec_1[:,0]**2)
# plt.show()
# plt.plot(x,E_vec_1[:,1]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,2]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,3]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,4]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,5]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,6]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,7]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,8]**2,marker='x')
# plt.show()
# plt.plot(x,E_vec_1[:,9]**2,marker='x')
# plt.show()