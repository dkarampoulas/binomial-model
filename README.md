# Binomial Option Pricing & Black-Scholes 📈

A quick Python script I put together to play around with the **Binomial Tree Model** for pricing options and see how it stacks up against the classic **Black-Scholes** formula.

## What it does
- **Binomial Tree:** Builds a price tree for options using backwards induction (working our way back from the future to today).
- **European vs. American Options:** Handles both, showing the difference when early exercise is allowed (`am=1`).
- **Black-Scholes Comparison:** Runs a 1,000-step tree to show how closely the binomial model converges to the analytical Black-Scholes price.

## How to run it
You just need `numpy` installed:

```bash
pip install numpy
python binomial_model.py
