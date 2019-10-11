class Bin_apply:
    def __init__(self, data=None, model=None):
        self.data = data
        self.model = model

    def generalApply(self, index):
        for i in range(len(self.data)):
            for min_max in self.model:
                if min_max[0] <= self.data[i] <= min_max[1]:
                    self.data[i] = "%d-%d" %(min_max[0], min_max[1])
                    break
        if index == 8:
            for i in range(len(self.data)):
                if self.data[i] == "0-0":
                    self.data[i] = "No-capital-gain"
                elif self.data[i] == "1-99998":
                    self.data[i] = "Gain-some-capital"
                else:
                    self.data[i] = "Gain-vast-capital"
        elif index == 9:
            for i in range(len(self.data)):
                if self.data[i] == "0-0":
                    self.data[i] = "No-capital-loss"
                else:
                    self.data[i] = "Loss-some-capital"
        elif index == 10:
            for i in range(len(self.data)):
                if self.data[i] == "0-0":
                    self.data[i] = "Not-working"
                elif self.data[i] == "1-34":
                    self.data[i] = "Part-time"
                elif self.data[i] == "35-40":
                    self.data[i] = "Full-time"
                else:
                    self.data[i] = "Over-time"
        
        return self.data
