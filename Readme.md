# Currency Converter

This is a simple currency converter web application built using Streamlit. It allows users to convert between different currencies based on predefined conversion rates.

## Features

- Convert between various currencies including USD, EUR, GBP, JPY, AUD, CAD, and INR.
- Input amount to convert with support for decimal values.
- Select currencies to convert from and to using dropdown menus.
- Display the converted amount with two decimal places for accuracy.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd currency_converter
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # on macOS/Linux
   venv\Scripts\activate.bat  # on Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run currency_converter.py
   ```

5. Open your web browser and navigate to `http://localhost:8501` to access the currency converter application.

## Usage

1. Enter the amount to convert in the "Enter the amount to convert" field.
2. Select the currency to convert from using the dropdown menu.
3. Select the currency to convert to using the dropdown menu.
4. Click the "Convert" button to see the converted amount.
5. The converted amount will be displayed below the button.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
