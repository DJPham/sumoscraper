# Sumo Web Scraper
## Description
> A project aimed to improve programming skills by scraping data from the Sumo Association website, storing it in a database, and creating visualizations to analyze the results found.

#### Objective: Create a functioning web scraper on the Sumo Association website
#### Objective 2: Create a database to store any results
#### Objective 3: Develop visualizations based on results found
***
#### Languages: Python, SQL

---
### Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Structure](#data-structure)
6. [Visualizations](#visualizations)
7. [License](#license)
8. [Contact](#contact)

### Introduction
Creating a web scraper using Python and the Scrapy library to collect data on sumo wrestlers from the Sumo Association website. The data is to be then stored in a database and visualized into meaningful illustrations. 

### Features

- Web scraping of sumo wrestling data
- Storage of scraped data in a database
- Data visualization
- Data analytics

### Installation
* Python 3.6+
* Virtual Environment (i.e., Visual Studio Code, optional but recommended)

### Usage

To use this project, follow these steps:
1. **Clone the repository:**
```sh
git clone https://github.com/DJPham/sumoscraper.git
```
2. **Install dependencies:**
```sh
pip install -r requirements.txt
```
3. **Run the code**

### Data Structure

All scraped data are stored in a 'sumo_data.db' SQLite database with a 'rikishi' table.

| Column   | Type    | Description                      |
|----------|---------|----------------------------------|
| id       | INTEGER | Primary key, auto-incremented    |
| name     | TEXT    | Name of the sumo wrestler        |
| ranking  | TEXT    | Ranking of the sumo wrestler     |
| origin   | TEXT    | Origin of the sumo wrestler      |
| stable   | TEXT    | Stable (training organization)   |

Each row in the rikishi table represents a sumo wrestler with their name, ranking, origin, and stable with an unique ID attached.

### Visualizations

### License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any questions or inquiries, please get in touch with my GitHub and I will reach out as soon as possible. Thank you.
