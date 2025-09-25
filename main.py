
from apps.tvm_time_value_of_money.time_value_of_money import TimeValueOfMoney

if __name__ == '__main__':
    print("👋 Hi World")

    tvm = TimeValueOfMoney(present_value=25000,
                           future_value=420000,
                           interest=.12,
                           period=5)

    print(tvm)

    print(TimeValueOfMoney(future_value=90000,
                           interest=.12,
                           period=5))




