# This is a sample Python script.
import numbers


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# FV Future Value = PV(1+R)**N
def fv(PV: numbers.Number, R: numbers.Number, N: numbers.Number) -> numbers.Number:
    return PV*(1+R)**N

#PV Present Value = FV/(1+R)**N
def pv(FV: numbers.Number, R: numbers.Number, N: numbers.Number) -> numbers.Number:
    return FV(1+R)**N

def irr(principal: numbers.Number, future_value: numbers.Number, period: numbers.Number) -> numbers.Number:
    irr_result = ((future_value - principal)**1/period) / principal
    return f"principal {principal} retuns future_value {future_value} over {period} periods  = IRR {irr_result}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(f"{fv(principal=300000, interest=.1, period=2)}")
    print(f"{pv(future_value=fv(principal=300000, interest=.1, period=2), interest=.1, period=2)}")
    print(f"{irr(principal=300000, future_value=fv(principal=300000, interest=.1, period=2), period=2)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
