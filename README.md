# Cryptocurrency Candle Downloader
## Overview
The Cryptocurrency Candle Downloader is a Python-based tool designed to simplify the process of fetching historical candle data for various cryptocurrencies. Leveraging the powerful CCXT library, this script offers access to a wide range of exchanges, providing users with the flexibility to select their preferred source of data. The intuitive interface, built with tkinter and customtkinter, ensures a seamless user experience from start to finish.

## Features
- Wide Exchange Support: Utilizes CCXT to fetch data from a majority of cryptocurrency exchanges.
- Customizable Timeframes: Users can specify the granularity of the candle data (e.g., 5min, 15min, 30min, 1hr, etc.).
- Selectable Period: Define the start and end dates for the data you wish to download.
- Easy-to-Use GUI: Built with tkinter and customtkinter, offering a straightforward and friendly user interface.
- CSV Export: Downloads the candle data into a neatly formatted CSV file, facilitated by pandas for ease of use and analysis.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- pip for installing dependencies

## Usage
1) Launch the script:
``` python main.py ```
2) Follow the GUI prompts to select your desired exchange, cryptocurrency symbol/ticker, and timeframe for the candle data.
3) Choose the start and end dates for the period you're interested in.
4) Review your selections and click the "Download" button to fetch the data. The script will download the candle data into a CSV file for your analysis.

## Contributing
Contributions to the Cryptocurrency Candle Downloader are welcome! Whether it's submitting bugs, requesting features, or contributing code, your input is highly appreciated. Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- Thanks to the CCXT team for their incredible library that made this tool possible.
- Gratitude to the tkinter and customtkinter communities for providing the tools to build our GUI.
