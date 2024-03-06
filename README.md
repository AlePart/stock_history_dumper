## Stock History Dumper

This tool allows you to retrieve historical stock data and save it to a CSV file.

### Prerequisites

Before using this tool, make sure you have the following installed:

- Python 3
- pip

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AlePart/stock_history_dumper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd stock_history_dumper
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To use the tool, run the following example:

    ```bash
    python3 main.py ENWD.MI 1990-1-1 2023-1-1
    ```