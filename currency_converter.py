import streamlit as st

# Define conversion rates (as of 2022-01-01)
conversion_rates = {
    'USD': {'USD': 1.0, 'EUR': 0.87, 'GBP': 0.75, 'JPY': 114.45, 'AUD': 1.32, 'CAD': 1.27, 'INR': 75.0},
    'EUR': {'USD': 1.15, 'EUR': 1.0, 'GBP': 0.86, 'JPY': 130.81, 'AUD': 1.52, 'CAD': 1.46, 'INR': 86.71},
    'GBP': {'USD': 1.33, 'EUR': 1.16, 'GBP': 1.0, 'JPY': 151.57, 'AUD': 1.76, 'CAD': 1.69, 'INR': 100.02},
    'JPY': {'USD': 0.009, 'EUR': 0.008, 'GBP': 0.007, 'JPY': 1.0, 'AUD': 0.012, 'CAD': 0.011, 'INR': 0.66},
    'AUD': {'USD': 0.76, 'EUR': 0.66, 'GBP': 0.57, 'JPY': 81.43, 'AUD': 1.0, 'CAD': 0.96, 'INR': 56.81},
    'CAD': {'USD': 0.79, 'EUR': 0.68, 'GBP': 0.59, 'JPY': 88.87, 'AUD': 1.04, 'CAD': 1.0, 'INR': 59.16},
    'INR': {'USD': 0.013, 'EUR': 0.012, 'GBP': 0.01, 'JPY': 1.51, 'AUD': 0.018, 'CAD': 0.017, 'INR': 1.0}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    else:
        conversion_rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount

def main():
    st.title("Currency Converter")
    st.subheader("Created by- Anjil Singh Thakur")

    amount = st.number_input("Enter the amount to convert:", min_value=0.01, step=0.01)

    from_currency = st.selectbox("Select the currency to convert from:", ['INR', 'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD'])
    to_currency = st.selectbox("Select the currency to convert to:", ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'INR'])

    if st.button("Convert"):
        converted_amount = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
