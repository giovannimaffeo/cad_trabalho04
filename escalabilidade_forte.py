import subprocess
import matplotlib.pyplot as plt
import time

# Tamanho da matriz
matrix_size = 1000

# Números de threads (potências de 2)
num_threads = [2**i for i in range(6)]

# Lista para armazenar os tempos de execução
execution_times = []

# Executa o programa para cada número de threads
for threads in num_threads:
    command = ["./jacobi_omp", "-n", str(matrix_size), "-t", str(threads)]
    
    start_time = time.time()
    subprocess.run(command)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Plota o gráfico de tempo versus número de threads
plt.plot(num_threads, execution_times, marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Escalabilidade Forte')
plt.grid(True)
plt.show()
