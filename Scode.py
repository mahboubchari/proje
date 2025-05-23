import random

class EightQueensGA:
    def __init__(self, population_size=100, mutation_rate=0.1, generations=500):
        self.n = 8  # تعداد وزیرها
        self.population_size = population_size  # (تعدادکروموزوم)اندازه جمعیت
        self.mutation_rate = mutation_rate  # نرخ جهش
        self.generations = generations  # تعداد نسل‌هایی که باید اجراشود
        self.population = self.initialize_population()  # جمعیت اولیه
        
    def initialize_population(self):
        """ایجاد جمعیت اولیه به صورت تصادفی."""
        return [self.random_solution() for _ in range(self.population_size)]

    
    def random_solution(self):    #لیستی از موقعیت وزیرها    
        """ایجاد یک راه‌حل تصادفی."""
        return random.sample(range(self.n), self.n) 

    def calculate_fitness(self, solution):
        """محاسبه برازندگی یک راه‌حل."""
        clashes = 0      #شمارش تداخل ها
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i: #بررسی تداخل
                    clashes += 1
        return 28 - clashes  # برازندگی حداکثر 28 برای 8 وزیر
