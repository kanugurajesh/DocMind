# DocMind: The Auto-README Generator

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GitHub API](https://img.shields.io/badge/GitHub_API-Integrated-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Used-green.svg)
![LLM](https://img.shields.io/badge/LLM-Powered-orange.svg)

DocMind, also known as the Auto-README Generator, is a powerful Python-based command-line interface (CLI) tool designed to automate the creation of detailed and structured `README.md` files for public GitHub repositories. By leveraging the advanced capabilities of Large Language Models (LLMs) via LangChain and integrating with the GitHub API, DocMind intelligently analyzes the content, structure, and purpose of a given repository to generate comprehensive documentation.

It streamlines the documentation process, saving developers time and ensuring consistency across projects.

## Description

DocMind simplifies the often tedious task of writing comprehensive `README.md` files. It works by:

1.  **Fetching Repository Content:** Utilizing the GitHub API, DocMind accesses the file structure and content of a specified public repository.
2.  **Analyzing with LLMs:** The fetched information, including file names and inferred descriptions, is fed into a Large Language Model (e.g., Google GenerativeAI via LangChain).
3.  **Generating README:** The LLM processes this data, along with a sophisticated prompt, to generate a well-structured and informative `README.md` file tailored to the repository's content and purpose.

This tool is ideal for developers, open-source contributors, and teams looking to quickly generate high-quality documentation for their public projects.

## Installation

To get DocMind up and running, follow these steps:

1.  **Prerequisites:**
    *   Python 3.8+
    *   `pip` (Python package installer)

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/DocMind.git # Replace with actual repo URL
    cd DocMind
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is assumed for standard Python projects. It would typically contain `langchain`, `langchain-google-genai`, `PyGithub`, `python-dotenv`.)*

5.  **Set Up API Key:**
    DocMind uses a Large Language Model (e.g., Google GenerativeAI). You need to provide your API key.
    *   Obtain a `GOOGLE_API_KEY` from your Google Cloud Console or AI Studio.
    *   Create a `.env` file in the root directory of the `DocMind` project:
        ```
        GOOGLE_API_KEY="your_google_api_key_here"
        ```

## Usage

DocMind is a command-line tool. You simply provide the GitHub repository URL as an argument.

```bash
python main.py <github_repo_url>
```

**Example:**

```bash
python main.py https://github.com/octocat/Spoon-Knife
```

Upon successful execution, a new file named `README_generated.md` will be created in the current directory, containing the automatically generated README content for the specified repository.

**Important Note:** DocMind currently supports only **public** GitHub repositories, as it accesses repository content without requiring authentication tokens by default.

## Features

*   **Automated README Generation:** Generates comprehensive `README.md` files with a single command.
*   **LLM-Powered Analysis:** Leverages advanced Large Language Models for intelligent content understanding and documentation creation.
*   **GitHub API Integration:** Seamlessly fetches repository structure and file contents.
*   **Public Repository Support:** Designed to work with any public GitHub repository.
*   **Structured Output:** Produces well-organized and readable markdown files.
*   **Extensible Prompt System:** Uses a separate prompt file (`prompts/readme_prompt.txt`) allowing for easy customization of the README generation style.

## Example Code

To generate a README for the popular `Hello-World` repository:

```bash
# From the project root directory
python main.py https://github.com/octocat/Hello-World
```

This command will fetch the contents of `https://github.com/octocat/Hello-World`, process them using the configured LLM, and save the generated README to `README_generated.md` in your current working directory.

## Contributing

We welcome contributions to DocMind! If you'd like to contribute, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/issue-description`.
3.  **Make your changes.**
4.  **Write tests** for your changes (if applicable).
5.  **Ensure your code adheres to the project's coding style.**
6.  **Commit your changes** with a clear and concise message.
7.  **Push your branch** to your forked repository.
8.  **Open a Pull Request** to the `main` branch of the original repository.

Please ensure your pull requests are well-documented and address a specific issue or feature.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
*(Note: A `LICENSE` file is assumed for standard open-source projects. If not present, specify "No License" or suggest adding one.)*