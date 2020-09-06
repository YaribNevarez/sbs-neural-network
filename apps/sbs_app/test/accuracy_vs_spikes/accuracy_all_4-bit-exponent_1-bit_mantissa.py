#________SBS_ACCURACY_PLOT__________________________________________
import matplotlib.pyplot as pyplot

# 4-bit exponent, 1-bit mantissa
#________Accuracy_Vs_Spikes_________________________________________

#0% Noise
spikes_0 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_0 = [ 0.20, 0.76, 0.97, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_0, accuracy_0, label="0% Noise")
#______________________________________________

#5% Noise
spikes_1 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_1 = [ 0.26, 0.76, 0.96, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_1, accuracy_1, label="5% Noise")
#______________________________________________

#10% Noise
spikes_2 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_2 = [ 0.21, 0.75, 0.96, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_2, accuracy_2, label="10% Noise")
#______________________________________________

#15% Noise
spikes_3 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_3 = [ 0.23, 0.78, 0.97, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_3, accuracy_3, label="15% Noise")
#______________________________________________

#20% Noise
spikes_4 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_4 = [ 0.29, 0.77, 0.96, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_4, accuracy_4, label="20% Noise")
#______________________________________________

#25% Noise
spikes_5 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_5 = [ 0.26, 0.76, 0.95, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_5, accuracy_5, label="25% Noise")
#______________________________________________

#30% Noise
spikes_6 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_6 = [ 0.14, 0.73, 0.94, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_6, accuracy_6, label="30% Noise")
#______________________________________________

#35% Noise
spikes_7 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_7 = [ 0.27, 0.72, 0.95, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_7, accuracy_7, label="35% Noise")
#______________________________________________

#40% Noise
spikes_8 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_8 = [ 0.27, 0.74, 0.93, 0.97, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_8, accuracy_8, label="40% Noise")
#______________________________________________

#45% Noise
spikes_9 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_9 = [ 0.26, 0.72, 0.90, 0.96, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_9, accuracy_9, label="45% Noise")
#______________________________________________

#50% Noise
spikes_10 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_10 = [ 0.23, 0.68, 0.88, 0.94, 0.98, 0.98, 0.99, 1.00, 1.00, 1.00, 1.00 ]
pyplot.plot(spikes_10, accuracy_10, label="50% Noise")
#______________________________________________

#55% Noise
spikes_11 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_11 = [ 0.14, 0.62, 0.82, 0.81, 0.90, 0.91, 0.94, 0.95, 0.96, 0.97, 0.96 ]
pyplot.plot(spikes_11, accuracy_11, label="55% Noise")
#______________________________________________

#60% Noise
spikes_12 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_12 = [ 0.15, 0.40, 0.65, 0.76, 0.77, 0.84, 0.84, 0.85, 0.88, 0.86, 0.86 ]
pyplot.plot(spikes_12, accuracy_12, label="60% Noise")
#______________________________________________

#65% Noise
spikes_13 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_13 = [ 0.10, 0.18, 0.41, 0.54, 0.63, 0.64, 0.61, 0.65, 0.67, 0.64, 0.69 ]
pyplot.plot(spikes_13, accuracy_13, label="65% Noise")
#______________________________________________

#70% Noise
spikes_14 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_14 = [ 0.05, 0.09, 0.14, 0.30, 0.34, 0.37, 0.38, 0.40, 0.39, 0.40, 0.41 ]
pyplot.plot(spikes_14, accuracy_14, label="70% Noise")
#______________________________________________

#75% Noise
spikes_15 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_15 = [ 0.05, 0.04, 0.07, 0.09, 0.09, 0.13, 0.17, 0.14, 0.12, 0.16, 0.20 ]
pyplot.plot(spikes_15, accuracy_15, label="75% Noise")
#______________________________________________

#80% Noise
spikes_16 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_16 = [ 0.04, 0.02, 0.03, 0.04, 0.05, 0.07, 0.06, 0.08, 0.06, 0.10, 0.10 ]
pyplot.plot(spikes_16, accuracy_16, label="80% Noise")
#______________________________________________

#85% Noise
spikes_17 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_17 = [ 0.06, 0.02, 0.03, 0.03, 0.02, 0.02, 0.04, 0.02, 0.04, 0.03, 0.04 ]
pyplot.plot(spikes_17, accuracy_17, label="85% Noise")
#______________________________________________

#90% Noise
spikes_18 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_18 = [ 0.06, 0.04, 0.01, 0.02, 0.04, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02 ]
pyplot.plot(spikes_18, accuracy_18, label="90% Noise")
#______________________________________________

#95% Noise
spikes_19 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_19 = [ 0.06, 0.02, 0.03, 0.02, 0.02, 0.02, 0.03, 0.02, 0.02, 0.02, 0.02 ]
pyplot.plot(spikes_19, accuracy_19, label="95% Noise")
#______________________________________________

#100% Noise
spikes_20 = [ 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 ]
accuracy_20 = [ 0.04, 0.02, 0.02, 0.02, 0.03, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03 ]
pyplot.plot(spikes_20, accuracy_20, label="100% Noise")
#______________________________________________

pyplot.xlabel('Spikes')
pyplot.ylabel('Accuracy')
pyplot.title('Inference')
pyplot.legend()
pyplot.grid()
pyplot.show()



#________Accuracy_Vs_Noise__________________________________________

#spikes = 200
noise_0 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_0 = [ 0.20, 0.26, 0.21, 0.23, 0.29, 0.26, 0.14, 0.27, 0.27, 0.26, 0.23, 0.14, 0.15, 0.10, 0.05, 0.05, 0.04, 0.06, 0.06, 0.06, 0.04 ]
pyplot.plot(noise_0, accuracy_0, label="200 Spikes")
#______________________________________________

#spikes = 300
noise_1 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_1 = [ 0.76, 0.76, 0.75, 0.78, 0.77, 0.76, 0.73, 0.72, 0.74, 0.72, 0.68, 0.62, 0.40, 0.18, 0.09, 0.04, 0.02, 0.02, 0.04, 0.02, 0.02 ]
pyplot.plot(noise_1, accuracy_1, label="300 Spikes")
#______________________________________________

#spikes = 400
noise_2 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_2 = [ 0.97, 0.96, 0.96, 0.97, 0.96, 0.95, 0.94, 0.95, 0.93, 0.90, 0.88, 0.82, 0.65, 0.41, 0.14, 0.07, 0.03, 0.03, 0.01, 0.03, 0.02 ]
pyplot.plot(noise_2, accuracy_2, label="400 Spikes")
#______________________________________________

#spikes = 500
noise_3 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_3 = [ 1.00, 1.00, 1.00, 1.00, 0.99, 0.99, 0.99, 0.99, 0.97, 0.96, 0.94, 0.81, 0.76, 0.54, 0.30, 0.09, 0.04, 0.03, 0.02, 0.02, 0.02 ]
pyplot.plot(noise_3, accuracy_3, label="500 Spikes")
#______________________________________________

#spikes = 600
noise_4 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_4 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.99, 0.98, 0.90, 0.77, 0.63, 0.34, 0.09, 0.05, 0.02, 0.04, 0.02, 0.03 ]
pyplot.plot(noise_4, accuracy_4, label="600 Spikes")
#______________________________________________

#spikes = 700
noise_5 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_5 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.98, 0.91, 0.84, 0.64, 0.37, 0.13, 0.07, 0.02, 0.02, 0.02, 0.02 ]
pyplot.plot(noise_5, accuracy_5, label="700 Spikes")
#______________________________________________

#spikes = 800
noise_6 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_6 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.99, 0.94, 0.84, 0.61, 0.38, 0.17, 0.06, 0.04, 0.02, 0.03, 0.02 ]
pyplot.plot(noise_6, accuracy_6, label="800 Spikes")
#______________________________________________

#spikes = 900
noise_7 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_7 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.95, 0.85, 0.65, 0.40, 0.14, 0.08, 0.02, 0.02, 0.02, 0.02 ]
pyplot.plot(noise_7, accuracy_7, label="900 Spikes")
#______________________________________________

#spikes = 1000
noise_8 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_8 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.96, 0.88, 0.67, 0.39, 0.12, 0.06, 0.04, 0.02, 0.02, 0.02 ]
pyplot.plot(noise_8, accuracy_8, label="1000 Spikes")
#______________________________________________

#spikes = 1100
noise_9 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_9 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.97, 0.86, 0.64, 0.40, 0.16, 0.10, 0.03, 0.02, 0.02, 0.03 ]
pyplot.plot(noise_9, accuracy_9, label="1100 Spikes")
#______________________________________________

#spikes = 1200
noise_10 = [ 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 ]
accuracy_10 = [ 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.96, 0.86, 0.69, 0.41, 0.20, 0.10, 0.04, 0.02, 0.02, 0.03 ]
pyplot.plot(noise_10, accuracy_10, label="1200 Spikes")
#______________________________________________

pyplot.xlabel('Noise')
pyplot.ylabel('Accuracy')
pyplot.title('Inference')
pyplot.legend()
pyplot.grid()
pyplot.show()

#________END__________________________________________


