import numpy as np

def generate_dataset(samples=10):

    # Age between 18 and 60
    age = np.random.randint(18, 60, samples)

    # Income between 20000 and 120000
    income = np.random.randint(20000, 120000, samples)

    # Experience between 0 and 40 years
    experience = np.random.randint(0, 40, samples)

    # Spending score between 1 and 100
    spending_score = np.random.randint(1, 100, samples)

    dataset = np.column_stack((age, income, experience, spending_score))

    return dataset