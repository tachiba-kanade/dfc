
# Simple DCF Calculator in Python

A beginner-friendly Python project that calculates the **Discounted Cash Flow**, or **DCF**, value of a project.

The goal of this project is to understand whether a project or investment is financially attractive by calculating its **Net Present Value**, also called **NPV**.

---

## What This Project Does

This project helps answer a simple question:

> If a project generates money in the future, what is that money worth today?

Future money is worth less than money today because of risk, inflation, and opportunity cost. DCF helps convert future cash flows into today’s value.

---

## Example Scenario

Suppose a project requires an initial investment of ₹10,00,000.

It is expected to generate the following cash flows:

| Year | Cash Flow |
|---|---:|
| Year 1 | ₹2,50,000 |
| Year 2 | ₹3,00,000 |
| Year 3 | ₹4,00,000 |
| Year 4 | ₹4,50,000 |
| Year 5 | ₹5,00,000 |

If the discount rate is 10%, this project calculates the present value of each future cash flow and then calculates the final NPV.

---

## Key Finance Concepts

### Discounted Cash Flow

Discounted Cash Flow is a method used to estimate the value of future cash flows in today’s terms.

### Present Value

Present value tells us what future money is worth today.

Formula:

```text
Present Value = Future Cash Flow / (1 + Discount Rate) ^ Year

NPV = Total Present Value of Cash Flows - Initial Investment

If NPV > 0: Accept the project
If NPV < 0: Reject the project
If NPV = 0: Project breaks even

Phase 1: Simple DCF Calculator in Python
Phase 2: Startup Valuation using Discounted Cash Flow