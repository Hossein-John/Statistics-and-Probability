import numpy as np
def generate_population(distribution, params, population_size):
    if distribution == "normal":
        return np.random.normal(params["mean"], params["std"], population_size)
    elif distribution == "uniform":
        return np.random.uniform(params['low'], params['high'], population_size)
    else:
        raise ValueError("Unsupported distribution type. use 'normal' or 'uniform'")

def simple_random_sampling(population, sample_size, num_samples):
    
    if sample_size > len(population):
        raise ValueError("sample size is bigger than population!")
        
    else:
        a = []
        for i in range(num_samples):    
            x = np.random.choice(population, sample_size, replace = False)
            a.append(x)
            
    return np.array(a)

def calculate_bias(population, samples):
    if len(samples) == 0:
        raise ValueError("samples are empty")
        
    else:
        samples_mean = samples.mean(axis = 1)
        population_mean = population.mean()
        bias = samples_mean.mean() - population_mean

    return bias
