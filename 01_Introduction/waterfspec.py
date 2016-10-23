# -*- coding: utf-8 -*-
"""
Python implementation of the MATLAB code:

M_files_chap01/waterfspec.m

Authors: J. Schattschneider, U. Zölzer
waterfspec( signal, start, steps, N, fS, clippingpoint, baseplane)

shows short-time spectra of signal, starting
at k=start, with increments of STEP with N-point FFT 
dynamic range from -baseplane in dB up to 20*log(clippingpoint)
in dB versus time axis


from the book:
DAFX - Digital Audio Effects
Edited by Udo Zölzer
ISBN: 978-0-470-66599-2
Second Edition, John Wiley & Sons, 2011
Matlab files source:
http://ant-s4.unibw-hamburg.de/dafx/DAFX_Book_Page_2nd_edition/matlab.html

Python implementation by Jose R. Zapata
"""
#%% inilizacion de variables
def waterfspec(data,start,steps,N,fS,clippingpoint,baseplane):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import signal
    from matplotlib.collections import PolyCollection
    from mpl_toolkits.mplot3d import Axes3D
    
    if baseplane is None: baseplane=-100
    if clippingpoint is None: clippingpoint=0
    if fS is None: fS=44100
    if N is None: N=1024        # default FFT
    if steps is None: steps=round(len(data)/25)
    if start is None: start=0
   
    #%%    
    windoo = signal.blackman(N)            # window - default
    windoo = windoo*N/float(sum(windoo))    # scaling
    # Calculation of number of spectra nos
    n=len(data);
    rest=n-start-N;
    nos=round(rest/steps);
    if nos>rest/steps: nos=nos-1
    nos = int(nos)
    #vectors for 3D representation
    x = np.linspace(0, fS,N)
    data=data+0.0000001;  
    #%% Computation of spectra and visual representation
    verts = []
    for i in range(0,nos+1):
        spek = 20*np.log10(np.abs(np.fft.fft(windoo*data[start+i*steps:start+N+i*steps]))/(N)/0.5)
        spek = np.insert(spek,0,-200)
        #setting the clipping point and baseplane
        spek = spek.clip(min=baseplane, max=clippingpoint)
        #first and last point to the baseplane
        spek[0] = baseplane-10
        spek[N/2-1] = baseplane-10;
        xx = x[:N/2]
        verts.append(list(zip(xx, spek[:N/2])))
        
    #%% Plot figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    poly = PolyCollection(verts,facecolors='w')
    y = range(len(x/2))
    poly.set_alpha(1)
    ax.add_collection3d(poly, zs=y, zdir='y')
    ax.set_title('Waterfall Representation of Short-time FFTs')
    ax.set_xlabel('f in Hz')
    ax.set_xlim3d(0, fS/2)
    ax.set_ylabel('N')
    ax.set_ylim3d(1, 30)
    ax.set_zlabel('Magnitude in dB')
    ax.set_zlim3d(baseplane-10, 0)
    plt.tight_layout()
    plt.show()
