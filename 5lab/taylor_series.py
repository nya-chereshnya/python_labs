class TaylorSeries:

    def __init__(self, x1, x2, deltax, E):
        self.x1 = x1
        self.x2 = x2
        self.deltax = deltax
        self.E = E

    def taylor_ln_function(self):
        dict_res = {}
        result = 0
        for x in range(self.x1, self.x2, self.deltax):
            result = 0
            diff = 1
            n = 0
            while diff > self.E:
                diff = 1 / ((2 * n + 1) * (2 * x + 1)**(2 * n + 1))
                result += diff
                n += 1
            dict_res[f"{x}"] = f"{result * 2}"
        return dict_res
