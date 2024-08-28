import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

def plot_signal(attenuation, noise_std, amplitude, wavelength, curve_type):
    t = np.linspace(0, 1, 1000)
    
    if curve_type == 'Senoide':
        signal_original = amplitude * np.sin(2 * np.pi * (1/wavelength) * t)
    elif curve_type == 'Gaussiana':
        signal_original = amplitude * np.exp(-0.5 * ((t - 0.5) / wavelength) ** 2)
    elif curve_type == 'Quadrada':
        signal_original = amplitude * np.sign(np.sin(2 * np.pi * (1/wavelength) * t))

    signal_attenuated = attenuation * signal_original

    noise = np.random.normal(0, noise_std, t.shape)
    final_signal = signal_attenuated + noise

    ax.clear()
    ax.plot(t, final_signal, label=f'{curve_type} (Atenuation: {attenuation:.3f}, Noise: {noise_std:.3f})', color='blue')
    
    ax.set_title(f'{curve_type} com atenuação e ruído')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_ylim([-1.5 * amplitude, 1.5 * amplitude])
    ax.set_xlim([0, 1])
    ax.grid(True)
    fig.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35)

initial_attenuation = 0.75
initial_noise = 0.05
initial_amplitude = 1.0
initial_wavelength = 0.1
initial_curve_type = 'Senoide'

ax_attenuation = plt.axes([0.3, 0.0, 0.25, 0.03], facecolor='lightgoldenrodyellow')
ax_noise = plt.axes([0.3, 0.05, 0.25, 0.03], facecolor='lightgoldenrodyellow')
ax_amplitude = plt.axes([0.3, 0.15, 0.25, 0.03], facecolor='lightgoldenrodyellow')
ax_wavelength = plt.axes([0.3, 0.2, 0.25, 0.03], facecolor='lightgoldenrodyellow')

fig.text(0.33, 0.1, 'Interferência', fontsize=12)
fig.text(0.3, 0.25, 'Parâmetros da Onda', fontsize=12)

slider_attenuation = Slider(ax_attenuation, 'Atenuação', 0.1, 1.0, valinit=initial_attenuation, valstep=0.001)
slider_noise = Slider(ax_noise, 'Ruído', 0.0, 1.0, valinit=initial_noise, valstep=0.001)
slider_amplitude = Slider(ax_amplitude, 'Amplitude', 0.1, 2.0, valinit=initial_amplitude, valstep=0.001)
slider_wavelength = Slider(ax_wavelength, 'Comp. de onda', 0.01, 0.5, valinit=initial_wavelength, valstep=0.001)

ax_curve_type = plt.axes([0.8, 0.1, 0.15, 0.15], facecolor='lightgoldenrodyellow')
radio_curve_type = RadioButtons(ax_curve_type, ('Senoide', 'Gaussiana', 'Quadrada'), active=0)

def update(val):
    plot_signal(slider_attenuation.val, slider_noise.val, slider_amplitude.val, slider_wavelength.val, radio_curve_type.value_selected)

slider_attenuation.on_changed(update)
slider_noise.on_changed(update)
slider_amplitude.on_changed(update)
slider_wavelength.on_changed(update)
radio_curve_type.on_clicked(update)

plot_signal(initial_attenuation, initial_noise, initial_amplitude, initial_wavelength, initial_curve_type)
plt.show()
