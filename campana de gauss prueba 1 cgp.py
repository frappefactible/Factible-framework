import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Simula el lanzamiento de dos dados y devuelve la suma de los resultados
    dice_rolls = np.random.randint(1, 7, size=(num_rolls, 2))
    sum_of_rolls = np.sum(dice_rolls, axis=1)
    return sum_of_rolls

def plot_gaussian_distribution(data):
    # Crea un histograma y ajusta una curva de campana de Gauss
    plt.hist(data, bins=range(2, 14), density=True, alpha=0.6, color='g')
    
    mu, sigma = np.mean(data), np.std(data)
    x = np.linspace(2, 13, 100)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    
    plt.plot(x, y, '--', color='b')
    plt.title('Distribución de la Suma de Dos Dados')
    plt.xlabel('Suma de los Dados')
    plt.ylabel('Frecuencia Normalizada')
    plt.show()

# Simula 10000 lanzamientos de dos dados
num_simulations = 10000
dice_sum_results = simulate_dice_rolls(num_simulations)

# Representa los resultados en una campana de Gauss
plot_gaussian_distribution(dice_sum_results)
