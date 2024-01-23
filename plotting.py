import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
bandstructure_si = np.loadtxt('bandstructure_si.csv', delimiter=',')
bandstructure_ge = np.loadtxt('bandstructure_ge.csv', delimiter=',')
bandstructure_sn = np.loadtxt('bandstructure_sn.csv', delimiter=',')
bandstructure_gap = np.loadtxt('bandstructure_gap.csv', delimiter=',')
bandstructure_gaas = np.loadtxt('bandstructure_gaas.csv', delimiter=',')
bandstructure_alsb = np.loadtxt('bandstructure_alsb.csv', delimiter=',')
bandstructure_inp = np.loadtxt('bandstructure_inp.csv', delimiter=',')
bandstructure_gasb = np.loadtxt('bandstructure_gasb.csv', delimiter=',')
bandstructure_inas = np.loadtxt('bandstructure_inas.csv', delimiter=',')
bandstructure_insb = np.loadtxt('bandstructure_insb_fix.csv', delimiter=',')
bandstructure_zns = np.loadtxt('bandstructure_zns.csv', delimiter=',')
bandstructure_znse = np.loadtxt('bandstructure_znse.csv', delimiter=',')
bandstructure_znte = np.loadtxt('bandstructure_znte.csv', delimiter=',')
bandstructure_cdte = np.loadtxt('bandstructure_cdte.csv', delimiter=',')

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_si.shape[0]):
    plt.plot(bandstructure_si[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_si.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_si[i, scatter_indices], facecolors='none', edgecolors='black', s=30)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-6, 7)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-5, 6)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'Si', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.4, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 2.4, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.6, "L" + r'$_3$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.4, "Γ" + r'$_2$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{25}$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.5, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -3.5, "X" + r'$_4$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 1, "K" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3, "K" + r'$_2$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -4.8, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.5, "Γ" + r'$_2$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 3, "Γ" + r'$_{15}$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 0.5, "Γ" + r'$_{25}$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("Si",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_ge.shape[0]):
    plt.plot(bandstructure_ge[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_ge.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_ge[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-6, 8)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-5, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'Ge', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.5, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 1.5, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.6, "L" + r'$_3$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.4, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.9, "Γ" + r'$_2$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{25}$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.9, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -3, "X" + r'$_4$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.0, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 1, "K" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.7, "K" + r'$_2$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -4.3, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.5, "Γ" + r'$_2$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 3.9, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{25}$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("Ge",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_sn.shape[0]):
    plt.plot(bandstructure_sn[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_sn.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_sn[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-5, 7)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 6)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'Sn', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 0.9, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.2, "L" + r'$_3$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 3.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(37, 0.2, "Γ" + r'$_{25}$' + "'" + "&" + "Γ" + r'$_2$' + "'", ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.3, "X" + r'$_4$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.2, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 1, "K" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1, "K" + r'$_2$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.9, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 3.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("Sn",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_gap.shape[0]):
    plt.plot(bandstructure_gap[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_gap.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_gap[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-5, 8)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'GaP', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 6, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 2, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.6, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.7, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -3, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.3, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 2.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.5, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3.3, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 5.7, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 3.2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("Gap",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_gaas.shape[0]):
    plt.plot(bandstructure_gaas[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_gaas.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_gaas[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-5, 8)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'GaAs', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 5.5, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 2, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.9, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.3, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.8, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 2.7, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.5, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3.1, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.8, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.5, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("GaAs",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_alsb.shape[0]):
    plt.plot(bandstructure_alsb[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_alsb.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_alsb[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-5, 8)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'AlSb', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 5.2, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 2.3, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.5, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 2.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.3, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.4, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 2.9, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.2, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3.1, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.5, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("AlSb",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_inp.shape[0]):
    plt.plot(bandstructure_inp[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_inp.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_inp[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'InP', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.5, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 1.5, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.2, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 2.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.4, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.8, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.2, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.9, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3.1, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.9, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.9, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("InP",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_gasb.shape[0]):
    plt.plot(bandstructure_gasb[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_gasb.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_gasb[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 7)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 6)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'GaSb', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.5, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 1.3, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.9, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.2, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.7, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.0, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.9, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.9, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.7, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("GaSb",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_inas.shape[0]):
    plt.plot(bandstructure_inas[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_inas.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_inas[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-5, 8)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-4, 7)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'InAs', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.5, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 1.3, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.9, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.4, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.9, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.2, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.9, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -3.1, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.9, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("InAs",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_insb.shape[0]):
    plt.plot(bandstructure_insb[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_insb.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_insb[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 7)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 6)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 5, 'InSb', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 4.2, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 1.1, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 4.3, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.1, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 2.7, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 1.7, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.0, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.0, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.7, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.7, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 4.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.0, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("InSb",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_zns.shape[0]):
    plt.plot(bandstructure_zns[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_zns.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_zns[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 11)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 10)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 2.5, 'ZnS', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 8, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 4.5, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 8, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 6.5, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 4.5, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.3, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 9.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -0.5, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.9, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 8.0, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 3.2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("ZnS",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_znse.shape[0]):
    plt.plot(bandstructure_znse[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_znse.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_znse[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 10)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 9)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 2.5, 'ZnSe', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 7.2, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 3.9, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.1, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 7.2, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 2.2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 6, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 4, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -2.2, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 7.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 4.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -0.5, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.5, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 7.2, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 2.2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("ZnSe",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_znte.shape[0]):
    plt.plot(bandstructure_znte[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_znte.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_znte[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 9)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 9)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 7, 'ZnTe', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 6, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 3, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -1.3, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 6, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.9, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 5, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3.2, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -1.5, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 7.5, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 4.0, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -0.5, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -2.3, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 6, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 2, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("ZnTe",dpi=300)
plt.show()

indices = {
    'L': 0,
    'Γ': 25,
    'X': 75,
    'K': 90,
    'Γ_end': 129
}

# Assuming bandstructure_si is already defined

# Set the figure size
plt.figure(figsize=(8,6.5))  # Adjust the width and height as needed

# Plotting all bands using a loop
for i in range(bandstructure_cdte.shape[0]):
    plt.plot(bandstructure_cdte[i, :], label=f'Band {i+1}')

    # Selecting a subset of points for scatter plot
    step = 5  # Adjust this value to control the density of scatter points
    scatter_indices = range(0, bandstructure_znte.shape[1], step)

    # Plotting scatter points (hollow style)
    plt.scatter(scatter_indices, bandstructure_cdte[i, scatter_indices], facecolors='none', edgecolors='black', s=20)
plt.xticks(list(indices.values()), list(indices.keys()))
y_tick_positions = [i for i in range(-3, 9)]  # Adjust as needed
plt.yticks(y_tick_positions)
plt.xlabel('k')
plt.ylabel('E (eV)')
plt.ylim(-3, 8)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.text(65, 6, 'CdTe', ha='center', va='center', backgroundcolor='none', fontsize = 20)
plt.text(2, 6.2, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, 3, "L" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(2, -0.7, "L" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 6, "Γ" + r'$_{15}$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 1.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(25, 0.3, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 5, "X" + r'$_3$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, 3.5, "X" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(75, -1.5, "X" + r'$_5$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 6.2, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 3.9, "K" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, 0, "K" + r'$_2$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(90, -1.7, "K" + r'$_1$' , ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 6, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, 1.3, "Γ" + r'$_1$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.text(130, -0.5, "Γ" + r'$_{15}$', ha='center', va='center', backgroundcolor='none', fontsize=13)
plt.savefig("CdTe",dpi=300)
plt.show()

