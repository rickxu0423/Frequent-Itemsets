class Replace:
    def __init__(self, data):
        self.data = data
    
    def replace(self, index):
        if index == 0:
            if self.data % 10 == 0:
                self.data = "%d-%d" %((int(self.data / 10) - 1) * 10 + 1, self.data)
            else:
                self.data = "%d-%d" %((int(self.data / 10) * 10 + 1, ((int(self.data / 10) + 1) * 10)))
        if index == 8:
            if self.data == 0:
                self.data = "No-capital-gain"
            elif 0 < self.data < 99999:
                self.data = "Gain-some-capital"
            else:
                self.data = "Gain-vast-capital"
        if index == 9:
            if self.data == 0:
                self.data = "No-capital-loss"
            else:
                self.data = "Loss-some-capital"
        if index == 10:
            if self.data == 0:
                self.data = "Not-working"
            elif 0 < self.data < 35:
                self.data = "Part-time"
            elif 35 <= self.data <= 40:
                self.data = "Full-time"
            else: 
                self.data = "Over-time"

        return self.data