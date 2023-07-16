import subprocess
import matplotlib.pyplot as plt
import numpy as np
import time

# Tamanho inicial da matriz e número inicial de threads
matrix_size = 500
num_threads = 1

# Listas para armazenar os tamanhos de matriz e tempos de execução
matrix_sizes = []
execution_times = []

# Executa o programa para cada tamanho de matriz e número de threads
while matrix_size <= 16000 and num_threads <= 32:
    command = ["./jacobi_omp", "-n", str(matrix_size), "-t", str(num_threads)]
    
    start_time = time.time()
    subprocess.run(command)
    end_time = time.time()

    execution_time = end_time - start_time

    matrix_sizes.append(matrix_size)
    execution_times.append(execution_time)

    # Dobra o tamanho da matriz e o número de threads
    matrix_size *= 2
    num_threads *= 2

# Plota o gráfico de tempo versus tamanho da matriz
plt.plot(matrix_sizes, execution_times, marker='o', label='Dados')
plt.xlabel('Tamanho da Matriz')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Escalabilidade Fraca')

# Ajuste quadrático dos dados
coefficients = np.polyfit(matrix_sizes, execution_times, 2)
fit = np.poly1d(coefficients)
x = np.linspace(min(matrix_sizes), max(matrix_sizes), 100)
plt.plot(x, fit(x), '--', label='Ajuste Quadrático')

plt.legend()
plt.grid(True)
plt.show()
