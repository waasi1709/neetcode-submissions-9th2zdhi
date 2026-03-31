class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        super().__init__
        minimizer = init
        for i in range(iterations):
            derivative = 2 * minimizer
            minimizer = minimizer - learning_rate * derivative 

        return round(minimizer,5)
    