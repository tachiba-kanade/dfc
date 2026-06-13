"""
TODO PHASE 1:

1. Ask user for inputs
2. Call DCF calculation functions
3. Show results
4. Create chart

Initial investment: ₹10,00,000
Year 1 cash flow: ₹2,50,000
Year 2 cash flow: ₹3,00,000
Year 3 cash flow: ₹4,00,000
Discount rate: 10%

DFC CAL WILL CALCULATE

Present value of each future cash flow
Total project value
Net Present Value, also called NPV
Whether the project is worth investing in

So if someone says:
“This project will give ₹5 lakh after 3 years”

DCF asks:
“Okay, but what is that ₹5 lakh worth today?”

That's what you'll calculate.
If the DCF is higher than the current cost of the investment, the opportunity could result in positive returns and may be worthwhile.
Companies typically use the weighted average cost of capital (WACC) for the discount rate because it accounts for the rate of return expected by shareholders.


The time value of money assumes that a dollar that you have today is worth more than a dollar that you receive 
tomorrow because it can be invested. 
As such, a DCF analysis can be useful in any situation where a person is paying money in the present with expectations 
of receiving more money in the future.

Take every future cash flow, reduce it based on time and risk, then add everything together.


User enters assumptions
        ↓
Python stores cash flows
        ↓
Python discounts each future cash flow
        ↓
Python calculates total present value
        ↓
Python subtracts initial investment
        ↓
Python shows whether project is profitable
        ↓
Python visualizes cash flows and value


meaning:

User enters initial investment.
User enters future cash flows for 5 years.
User enters discount rate.
Python calculates present value for each year.
Python calculates NPV.
Python prints a decision: accept or reject.
Python plots cash flows using a chart.


Year 1 cash flow: ₹250,000
Present value: ₹227,272.73

Year 2 cash flow: ₹300,000
Present value: ₹247,933.88

Year 3 cash flow: ₹400,000
Present value: ₹300,525.92

Total present value: ₹775,732.53
Initial investment: ₹1,000,000

NPV: -₹224,267.47
Decision: Reject project

"""


# phase : 1. Simple DCF Calculator in Python

import matplotlib.pyplot as plt

def intial_investments():
    money =  float(input("initial investment: "))

    cash_flow = []
    for year in range(1, 6):
        cf = float(input(f"cash flow for Year {year}: "))
        cash_flow.append(cf)

    discount = float(input("discount rate (%): ")) / 100


    # calculate NVP

    present = []
    for year in range(1, 6):
        pv = cash_flow[year - 1] / ((1 + discount) ** year)
        present.append(pv)

    npv = sum(present) - money


    print("\nPresent Values:")

    for year in range(1, 6):
        print(f"Year {year}: {present[year - 1]}")

    print(f"\nNPV = {npv:.2f}")

    # Decision
    if npv > 0:
        print("Decision: ACCEPT the project")
    else:
        print("Decision: REJECT the project")

    # Plot Cash Flows
    years = ["Y1", "Y2", "Y3", "Y4", "Y5"]

    plt.bar(years, cash_flow)
    plt.title("Future Cash Flows")
    plt.xlabel("Year")
    plt.ylabel("Cash Flow")
    plt.show()

