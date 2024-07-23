# Wikipy Spider

Welcome to **Wikipy Spider** – a web scraping project built using the Scrapy framework. This spider scrapes country information from a sample site.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

**Wikipy Spider** is a Scrapy spider designed to scrape information about countries, including their names, capitals, and populations. This project demonstrates how to use Scrapy to collect structured data from a website.

## Features

- **Scraping Country Information**: Extracts the name, capital, and population of each country from the target website.
- **Item Loaders**: Utilizes Scrapy's ItemLoader for clean and efficient data extraction and processing.

## Installation

To get started with **Wikipy Spider**, follow these steps:

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/wikipy-spider.git
    cd wikipy-spider
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    Ensure you have Python 3.x installed, then install Scrapy using `pip`:

    ```bash
    pip install scrapy
    ```

## Usage

1. **Define Your Item**:

    Ensure you have an `items.py` file in your project (`p1` folder) with the following content:

    ```python
    import scrapy

    class P1Item(scrapy.Item):
        name = scrapy.Field(output_processor=TakeFirst())
        capital = scrapy.Field(output_processor=TakeFirst())
        population = scrapy.Field(output_processor=TakeFirst())
    ```

2. **Run the Spider**:

    ```bash
    scrapy crawl wikipy
    ```

    The spider will start crawling the specified start URL and extract country information.

3. **View the Output**:

    The extracted data will be displayed in the console or saved to the specified output file if you use an output option, for example:

    ```bash
    scrapy crawl wikipy -o output.json
    ```

## Project Structure

Here's an overview of the important files in this project:

- `wikipy_spider.py`: Contains the spider code for scraping country information.
- `items.py`: Defines the data structure for the scraped items.
- `pipelines.py` (optional): Can be used to process the scraped data.
- `settings.py`: Configures settings for the Scrapy project.

## Example Output

Here is a sample output for the spider:

```json
[
    {
        "name": "Canada",
        "capital": "Ottawa",
        "population": "37000000"
    },
    {
        "name": "United States",
        "capital": "Washington, D.C.",
        "population": "327000000"
    }
]
