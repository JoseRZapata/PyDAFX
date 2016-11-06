01 Introduction - PyDAFX (Python implementation of DAFX Matlab code)
========================================================== 

In order to study the theory and code of the book DAFX - Digital Audio Effects and python for audio processing,
I'm doing the Python implementation of the MATLAB code from the book.

<b>Run the code for this Repo on Binder:</b> [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/joserzapata/pydafx)

Book Reference:
<b>DAFX - Digital Audio Effects</b> <br>
Edited by Udo Zölzer<br>
ISBN: 978-0-470-66599-2<br>
Second Edition, John Wiley & Sons, 2011<br>
Matlab files source: http://ant-s4.unibw-hamburg.de/dafx/DAFX_Book_Page_2nd_edition/matlab.html

Code
--------
1. [figure1_03](figure1_03.ipynb) Different time representations for digital audio signals. **(it has to be called figure1_12)**
 	
2. [figure1_17](figure1_17.ipynb) Zero-padding to increase frequency resolution.

3. [figure1_18](figure1_18.ipynb) Spectrum analysis of digital signals.
 
4. [figure1_19](figure1_19.ipynb) Reduction of the leakage effect by window functions.

5. [figure1_22](figure1_22.ipynb) Waterfall representation via FFT of weighted segments.
 	
6. [figure1_33](figure1_33.ipynb) FIR system: (a) impulse response, (b) magnitude response, (c) pole/zero plot and (d) phase response
 	
7. [DirectForm01](DirectForm01.ipynb) Impulse response of 2nd order IIR filter Sample-by-sample algorithm

8. [sbs_alg](sbs_alg.ipynb) A basic algorithm for weighting of a sound x(n) by a constant factor a (in this example is by 2)

9. [waterfspec](waterfspec.py) Funtionc to plot the Waterfall representation via FFT of weighted segments.
 	
10. [plot_zplane](plot_zplane.py) Plot poles and zeros in Z plane for a transfer function by [Christopher Felton](https://gist.github.com/endolith/4625838)
 	

Software and packages
---------------------
- Python 2.7.6
- Ipython 5.1.0
- Matplotlib 1.5.3
- Scipy 0.18.1
- Numpy 1.11.2
