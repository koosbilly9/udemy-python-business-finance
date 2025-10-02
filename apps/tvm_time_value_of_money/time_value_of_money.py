from numbers import Number


class TimeValueOfMoney:
    def __init__(self,
                 present_value: Number = 0,
                 future_value: Number = 0,
                 interest: Number = 1,
                 period: Number = 1,
                 stock_price_at_start: Number = 100,
                 stock_price_at_end: Number = 110,
                 dividend_yield: Number = 2, ):
        self.present_value = present_value
        self.future_value = future_value
        self.interest = interest
        self.period = period
        self.stock_price_at_start = stock_price_at_start
        self.stock_price_at_end = stock_price_at_end
        self.dividend_yield = dividend_yield

    def __str__(self):
        string_result = f"""
        Time Value of Money (TVM)
        -------------------------
        present_value: {self.present_value}, future_value : {self.future_value}, interest: {self.interest}, period : {self.period}
        
        Future value = PV(1+R)**P   {self.present_value}x(1+{self.interest})**{self.period} = {self.fv()}
        Present value = FV/(1+R)**P {self.future_value}/(1+{self.interest})**{self.period} = {self.pv()}
        """

        return string_result

    # FV = PV(1+R)**P
    def fv_latex(self):
        return str(rf'''
        $$\text{{Future Value:}}$$
        
        $$FV = PV * (1+R)^{{P}}$$
        
        $$FV = R{self.present_value:.2f} * (1+{(self.interest) * 100} \%)^{{{self.period} _ {{(p.a)}} }}$$
        ''')

    def fv(self) -> float:
        return float(self.present_value * (1 + self.interest) ** self.period)

    # PV = FV/(1+R)**P
    def pv_latex(self):
        return str(rf'''
        $$\text{{Present Value:}}$$ 
        
        $$ PV = FV / (1+R)^{{P}}$$
        
        $$ PV = R{self.future_value:.2f} / (1+{self.interest * 100}\%)^{{{self.period} _ {{(p.a)}}}} $$
        ''')

    def pv(self) -> float:
        return float(self.future_value / (1 + self.interest) ** self.period)

    # Rate of Return R = (FV/PV)**1/N - 1
    def r_latex(self):
        return rf'''
        $$\text{{Rate of return:}}$$ 
        
        $$ R = (\frac{{FV}}{{PV}})^{{ \frac{{1}}{{P}} }} - 1 $$
        
        $$ R = (\frac{{{self.future_value}}}{{{self.present_value}}})^{{ \frac{{1}}{{{self.period}}} }} - 1 $$
        '''

    def r(self) -> float:
        return ((self.future_value / self.present_value) ** (1 / self.period)) - 1

    # r = (Pt+1 / Pt) - 1 (Pt = price @ start of time period / Pt+1 = price @ end of time period)
    def stock_return_price_return_latex(self):
        return rf'''
        $$\text{{Stock Return - Price Return aka Simple Return}}$$
        $$\text{{ }} $$
        $$(\frac{{ Pt_{{+1}} }}{{Pt}})^\frac{{1}}{{P}} - 1$$
        $$\text{{ }} $$
        $$(\frac{{ {self.stock_price_at_end} }}{{ {self.stock_price_at_start} }})^\frac{{1}}{{ {self.period} }} - 1$$
        '''

    def stock_return_price_return(self) -> float:
        return ((self.stock_price_at_end / self.stock_price_at_start)**(1 / self.period)) - 1

    # r = ((Pt+1 + Dt+1) / Pt ) - 1 (Pt+1 Price@end, Pt Price, Dt+1 Dividend@end)
    def stock_return_total_return_latex(self):
        return rf'''
        $$\text{{Stock Return - Total Return}}$$
        $$\text{{ }} $$
        $$(\frac{{ Pt_{{+1}} + Yt_{{+1}} }}{{Pt}})^\frac{{1}}{{P}} - 1$$
        $$\text{{ }} $$
        $$(\frac{{ {self.stock_price_at_end} + {{ {self.dividend_yield} }} }}{{ {self.stock_price_at_start} }})^{{\frac{{1}}{{ {self.period} }} }} - 1$$
        '''

    def stock_return_total_return(self) -> float:
        return float((( (self.stock_price_at_end + self.dividend_yield) / self.stock_price_at_start)**(1 / self.period)) - 1)
