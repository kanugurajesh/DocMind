# DocMind

## Description
DocMind, also known as the Auto-README Generator, is a powerful Python-based command-line interface (CLI) tool designed to automate the creation of detailed and structured `README.md` files for public GitHub repositories. By leveraging the advanced capabilities of Large Language Models (LLMs) via LangChain and integrating with the GitHub API, DocMind intelligently analyzes the content, structure, and purpose of a given repository.

It streamlines the documentation process for developers by synthesizing a comprehensive README that accurately reflects the project. This tool aims to significantly reduce the manual effort involved in creating initial project documentation, ensuring consistency and completeness.

## Installation

To set up DocMind on your local machine, follow these steps:

### Prerequisites
*   Python 3.8+
*   A Google API Key for Generative AI (e.g., Gemini).

### Steps

1.  **Clone the repository (or download the source code):**
    ```bash
    git clone https://github.com/your-repo/DocMind.git # Replace with actual repo URL
    cd DocMind
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *If `requirements.txt` is not provided, you can create one with the following content:*
    ```
    python-dotenv
    PyGithub
    langchain-google-genai
    langchain
    ```
    Then run: `pip install -r requirements.txt`

4.  **Set up your Google API Key:**
    Create a `.env` file in the root directory of the project and add your Google API Key:
    ```dotenv
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    ```

5.  **Prepare the Prompt File:**
    Ensure you have a `prompts` directory in the root of the project, containing a file named `readme_prompt.txt`. This file defines the prompt template used by the LLM to generate the README. A basic example could be:
    ```
    # prompts/readme_prompt.txt
    You are an expert technical writer. Your task is to generate a comprehensive README.md file for a GitHub repository.

    The repository contains the following files and their inferred purposes:
    {file_list}

    Based on the above, generate a detailed and structured README.md. Include sections like:
    - Project Title
    - Description
    - Installation
    - Usage
    - Features
    - Contributing
    - License
    ```

## Usage

To generate a `README.md` for a public GitHub repository, simply run the `main.py` script with the repository URL as an argument:

```bash
python main.py <github_repo_url>
```

**Example:**

```bash
python main.py https://github.com/octocat/Spoon-Knife
```

Upon successful execution, a new file named `README_generated.md` will be created in the current directory, containing the generated README content.

**Note:**
*   DocMind currently only supports public GitHub repositories due to the default GitHub API token configuration.
*   Ensure your `GOOGLE_API_KEY` is correctly set in the `.env` file.

## Features

*   **Automated README Generation:** Quickly generates comprehensive `README.md` files for GitHub repositories.
*   **LLM-Powered Content Synthesis:** Leverages Large Language Models (via LangChain and Google Generative AI) to intelligently analyze and summarize repository content.
*   **GitHub API Integration:** Fetches repository file lists and content directly from GitHub.
*   **Public Repository Support:** Designed to work seamlessly with any public GitHub repository.
*   **Structured Output:** Generates a well-organized README with standard sections (Description, Installation, Usage, Features, etc.).
*   **Extensible Prompting:** Utilizes a customizable prompt template (`prompts/readme_prompt.txt`) allowing users to fine-tune the README generation style and content.

## Example Code

To demonstrate how to run DocMind, here's a typical command-line invocation:

```bash
# Generate a README for the popular 'requests' library
python main.py https://github.com/psf/requests
```

After running the command, you would find a new file:

```
README_generated.md
```

This file will contain the automatically generated README content for the `requests` repository.

## Contributing

We welcome contributions to DocMind! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes and ensure the code adheres to the project's style.
4.  Write clear, concise commit messages.
5.  Push your branch to your fork (`git push origin feature/your-feature-name`).
6.  Open a Pull Request to the `main` branch of this repository, describing your changes in detail.

For reporting bugs or suggesting new features, please open an issue on the GitHub issue tracker.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
**Disclaimer:** This README was generated based on the provided project file structure and descriptions, inferring functionality and dependencies. Specific details like exact prompt content or additional configuration might vary in the actual project.
