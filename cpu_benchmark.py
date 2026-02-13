import multiprocessing
import time

def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci de manière récursive."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_fibonacci_task(start_n, count):
    """Exécute le calcul de Fibonacci pour une plage de nombres."""
    results = {}
    for i in range(start_n, start_n + count):
        results[i] = fibonacci(i)
    return results

def main():
    num_threads = 16  # Optimisé pour Ryzen 9 6900HX (16 threads)
    fib_numbers_to_calculate = 35 # Nombre de Fibonacci à calculer pour chaque thread (peut être ajusté)
    
    print(f"Démarrage du benchmark Fibonacci avec {num_threads} threads...")
    print(f"Chaque thread calculera le {fib_numbers_to_calculate}-ième nombre de Fibonacci.")

    pool = multiprocessing.Pool(processes=num_threads)
    
    # Créer des tâches pour chaque thread. Pour cet exemple, chaque thread calcule le même nombre de Fibonacci.
    # Dans un scénario réel, on pourrait distribuer des tâches différentes ou des plages différentes.
    tasks = [(fib_numbers_to_calculate, 1) for _ in range(num_threads)]
    
    start_time = time.time()
    
    # Exécuter les tâches en parallèle
    # Ici, nous utilisons map pour simplifier, mais pour des tâches plus complexes, apply_async ou imap serait plus approprié.
    # Pour un benchmark, nous voulons que chaque thread fasse un travail similaire.
    results = pool.starmap(run_fibonacci_task, [(fib_numbers_to_calculate, 1) for _ in range(num_threads)])
    
    pool.close()
    pool.join()
    
    end_time = time.time()
    
    print("\nRésultats (un exemple par thread):")
    for i, res in enumerate(results):
        print(f"Thread {i+1}: Fibonacci({fib_numbers_to_calculate}) = {res.get(fib_numbers_to_calculate)}")
        
    print(f"\nBenchmark terminé en {end_time - start_time:.4f} secondes.")

if __name__ == "__main__":
    main()