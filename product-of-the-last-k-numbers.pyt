class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Start with a dummy product of 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset on zero
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # If k is too large, return 0
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]
