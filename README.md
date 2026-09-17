# Currency Converter

A small [Streamlit](https://streamlit.io/) web app that converts an amount from one currency
to another using live exchange rates from [forex-python](https://github.com/MicroPyramid/forex-python).

## Features

- Convert between 9 currencies: USD, EUR, GBP, MXN, CZK, BRL, PLN, PHP, ZAR
- Simple two-column UI: pick a source currency/amount and a target currency
- Displays the converted amount with the target currency's symbol

## Demo

https://minulsandith-currency-converter-main-bpntbi.streamlitapp.com/

## Getting started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/MinulSandith/Currency-Converter.git
cd Currency-Converter
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

## Project structure

| File               | Purpose                                          |
|--------------------|---------------------------------------------------|
| `main.py`          | Streamlit app: UI and conversion logic            |
| `style.css`        | Custom styling (animated gradient background, etc.)|
| `requirements.txt` | Python dependencies                                |

## Known limitations

- `forex-python` fetches live rates from a free public API. If that API is
  unreachable or rate-limited, the app now shows an error message instead of
  crashing, but no conversion will be available until the service recovers.
- Only a fixed set of currencies is supported (see Features above).

## Troubleshooting

- **"Could not fetch the conversion rate" error**: the upstream rates API is
  temporarily down or unreachable from your network. Try again later.
- **`ModuleNotFoundError`**: make sure you ran `pip install -r requirements.txt`
  inside the environment you're using to run the app.

## Contributing

Bug reports and pull requests are welcome. Please open an issue describing
the problem (steps to reproduce, expected vs. actual behavior) before
submitting a fix.

## License

No license file is currently included in this repository.
