import random

class EightQueensGA:
    def __init__(self, population_size=100, mutation_rate=0.1, generations=500):
        self.n = 8  # تعداد وزیرها
        self.population_size = population_size  # (تعدادکروموزوم)اندازه جمعیت
        self.mutation_rate = mutation_rate  # نرخ جهش
        self.generations = generations  # تعداد نسل‌هایی که باید اجراشود
        self.population = self.initialize_population()  # جمعیت اولیه
        