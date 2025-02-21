<div align="left">
    <div style="display: inline-block;">
        <h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">GECKOTERMINAL_LAST_POOLS</h2>
        <p>
	<em>Uncover profits, seize opportunities, trade smarter.</em>
</p>
        <p>
	<img src="https://img.shields.io/github/license/BAIOGIT/geckoterminal_last_pools?style=default&logo=opensourceinitiative&logoColor=white&color=6da2ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/BAIOGIT/geckoterminal_last_pools?style=default&logo=git&logoColor=white&color=6da2ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/BAIOGIT/geckoterminal_last_pools?style=default&color=6da2ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/BAIOGIT/geckoterminal_last_pools?style=default&color=6da2ff" alt="repo-language-count">
</p>
        <p><!-- default option, no dependency badges. -->
</p>
        <p>
	<!-- default option, no dependency badges. -->
</p>
    </div>
</div>
<br clear="left"/>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Geckoterminallastpools is a cutting-edge project that identifies highly profitable trading opportunities within the Solana network. By analyzing trade data and wallet behaviors, it pinpoints wallets with over 200% profit potential, enabling users to stay ahead in the fast-paced world of cryptocurrency trading. Ideal for traders seeking real-time insights and lucrative investment prospects.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular design with separate components for data fetching, analysis, database management, and alerting.</li><li>Real-time data processing and continuous monitoring of profitable trading opportunities.</li><li>Integration with the Geckoterminal API for fetching new pools, trending pools, trades, and OHLCV data.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Well-structured codebase with clear separation of concerns.</li><li>Follows Python best practices and coding standards.</li><li>Uses libraries like `pandas`, `requests`, and `flask` for efficient data handling and web services.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation with a primary language of Python.</li><li>Includes detailed explanations of code files and their functionalities.</li><li>Usage of `requirements.txt` for managing project dependencies.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with the Geckoterminal API for fetching relevant data for analysis.</li><li>Potential for customization to trigger alerts via email, SMS, or webhooks.</li><li>Uses `sqlite3` for efficient database operations.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate modules for data analysis, database management, alerting, and API interactions.</li><li>Encourages reusability and maintainability of code components.</li><li>Facilitates easy scaling and future enhancements.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes testing commands using `pytest` for ensuring code reliability.</li><li>Test coverage to validate the functionality of different components.</li><li>Ensures the project's stability and correctness.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient data fetching and processing for real-time updates on profitable trading opportunities.</li><li>Optimized algorithms for analyzing trade data and identifying highly profitable wallets.</li><li>Ensures minimal latency in processing and alerting mechanisms.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secure database operations for managing sensitive financial data.</li><li>Potential for implementing secure alerting mechanisms to prevent unauthorized access.</li><li>Follows best practices for handling user data and API interactions.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages project dependencies using `pip` and `requirements.txt`.</li><li>Dependent on libraries like `pandas`, `requests`, and `flask` for core functionalities.</li><li>Ensures consistent environment setup and package management.</li></ul> |

---

## 📁 Project Structure

```sh
└── geckoterminal_last_pools/
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── alert.py
    │   ├── analysis.py
    │   ├── db_manager.py
    │   ├── detection.py
    │   └── fetch_data.py
    ├── main.py
    └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>GECKOTERMINAL_LAST_POOLS/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Enables project dependencies management for requests, pandas, sqlite3, and flask.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/main.py'>main.py</a></b></td>
				<td>- The code in main.py orchestrates fetching, analyzing, and storing data for new and trending pools in a database<br>- It identifies highly profitable wallets based on trade analysis and saves relevant information for further processing<br>- This script runs continuously, ensuring real-time updates on profitable trading opportunities.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/app/analysis.py'>analysis.py</a></b></td>
				<td>- Identifies highly profitable trades by analyzing trade data, organizing trades by wallet, and calculating net profit and percentage profit<br>- Determines wallets with over 200% profit, including transaction details and coin information<br>- Returns a list of very profitable wallets for further analysis.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/app/fetch_data.py'>fetch_data.py</a></b></td>
				<td>- Fetches data from the Geckoterminal API for new pools, trending pools, trades, and OHLCV data based on Solana network<br>- Handles different endpoints and parameters to retrieve relevant information for analysis and monitoring within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/app/db_manager.py'>db_manager.py</a></b></td>
				<td>- Manages database operations for profitable wallets, coin purchases, and transaction hashes<br>- Initializes tables, saves wallet data, retrieves profitable wallets based on profit percentage, and deletes old data<br>- Facilitates efficient data storage and retrieval for financial analysis and tracking of wallet activities.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/app/alert.py'>alert.py</a></b></td>
				<td>- The `send_alert` function notifies about new pools detected in the system, specifying the pool's address and associated token<br>- This function can be customized to trigger alerts via email, SMS, or webhooks.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/BAIOGIT/geckoterminal_last_pools/blob/master/app/detection.py'>detection.py</a></b></td>
				<td>- Detects and classifies wallet behavior as 'Insider', 'Bot', or 'Normal' based on trade patterns and profitability<br>- Saves insider classifications to the database, analyzing transaction history, frequency, intervals, and profit<br>- The main function iterates through wallets, updating or inserting classifications as needed.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with geckoterminal_last_pools, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install geckoterminal_last_pools using one of the following methods:

**Build from source:**

1. Clone the geckoterminal_last_pools repository:
```sh
❯ git clone https://github.com/BAIOGIT/geckoterminal_last_pools
```

2. Navigate to the project directory:
```sh
❯ cd geckoterminal_last_pools
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run geckoterminal_last_pools using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/BAIOGIT/geckoterminal_last_pools/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/BAIOGIT/geckoterminal_last_pools/issues)**: Submit bugs found or log feature requests for the `geckoterminal_last_pools` project.
- **💡 [Submit Pull Requests](https://github.com/BAIOGIT/geckoterminal_last_pools/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/BAIOGIT/geckoterminal_last_pools
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/BAIOGIT/geckoterminal_last_pools/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=BAIOGIT/geckoterminal_last_pools">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
