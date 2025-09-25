from numbers import Number


class TimeValueOfMoney:
    def __init__(self,
                 present_value: Number = 0,
                 future_value: Number = 0,
                 interest:Number = 1,
                 period:Number = 1):
        self.present_value = present_value
        self.future_value = future_value
        self.interest = interest
        self.period = period

    def __str__(self):
        string_result = f"""
        Time Value of Money (TVM)
        -------------------------
        present_value: {self.present_value}, future_value : {self.future_value }, interest: {self.interest}, period : {self.period}
        
        Future value = PV(1+R)**P   {self.present_value}x(1+{self.interest})**{self.period} = {self.fv()}
        Present value = FV\(1+R)**P {self.future_value}\(1+{self.interest})**{self.period} = {self.pv()}
        """

        return string_result

    # FV = PV(1+R)**P
    def fv(self):
         return self.present_value * (1+self.interest)**self.period

    # PV = FV/(1+R)**P
    def pv(self):
        return self.future_value / (1+self.interest)**self.period

