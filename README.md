# currency-converter
# 💱 Currency Converter

A simple command-line currency converter written in Python.

The program uses the **Frankfurter API** to get the latest available exchange rates and convert one currency into another.

## ✨ Features

* Convert currencies using current exchange rates
* Supports multiple international currencies
* Case-insensitive currency input (`usd`, `USD`, `Usd` all work)
* Handles unsupported currencies
* Automatically repeats after an invalid input
* Simple command-line interface

## 🛠️ Technologies

* **Python 3**
* **Requests**
* **Frankfurter API**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install the required dependency:

```bash
pip install requests
```

Then run the program:

```bash
python main.py
```

## 💰 Supported Currencies

The converter uses currencies supported by the Frankfurter API.

Currently supported currencies include:

| Code | Currency             |
| ---- | -------------------- |
| AUD  | Australian Dollar    |
| BGN  | Bulgarian Lev        |
| BRL  | Brazilian Real       |
| CAD  | Canadian Dollar      |
| CHF  | Swiss Franc          |
| CNY  | Chinese Yuan         |
| CZK  | Czech Koruna         |
| DKK  | Danish Krone         |
| EUR  | Euro                 |
| GBP  | British Pound        |
| HKD  | Hong Kong Dollar     |
| HUF  | Hungarian Forint     |
| IDR  | Indonesian Rupiah    |
| ILS  | Israeli New Shekel   |
| INR  | Indian Rupee         |
| ISK  | Icelandic Króna      |
| JPY  | Japanese Yen         |
| KRW  | South Korean Won     |
| MXN  | Mexican Peso         |
| MYR  | Malaysian Ringgit    |
| NOK  | Norwegian Krone      |
| NZD  | New Zealand Dollar   |
| PHP  | Philippine Peso      |
| PLN  | Polish Złoty         |
| RON  | Romanian Leu         |
| SEK  | Swedish Krona        |
| SGD  | Singapore Dollar     |
| THB  | Thai Baht            |
| TRY  | Turkish Lira         |
| USD  | United States Dollar |
| ZAR  | South African Rand   |

> Currency availability depends on the currencies provided by the Frankfurter API.

## 🚀 Usage

Run the program and enter the currencies you want to convert:

```text
Welcome to the currency converter.

choose value (usd, eur, etc...): USD
choose value (usd, eur, etc...): EUR

1 USD = 0.85 EUR
```

The program accepts both lowercase and uppercase currency codes.

For example:

```text
usd
USD
Usd
```

all work the same way.

## ❌ Unsupported Currency

If an unsupported currency is entered, the program will display an error message instead of crashing:

```text
Sorry, unsupported currency!
```

The program then allows the user to try again.

## 🌐 API

This project uses the **Frankfurter API**, a free API for exchange rates.

API endpoint:

```text
https://api.frankfurter.app/latest
```

Exchange rates are provided by the Frankfurter service and ultimately sourced from the European Central Bank.

## 📁 Project Structure

```text
currency-converter/
│
├── main.py
├── README.md
└── requirements.txt
```

## 📄 requirements.txt

The project requires the `requests` package:

```text
requests
```
