# AI-Powered README Generator

This project provides a command-line tool that leverages Large Language Models (LLMs) and GitHub's API to automatically generate detailed `README.md` files for public GitHub repositories. By analyzing the repository's file structure and content, the tool aims to produce a comprehensive README that describes the project, its installation, usage, and features.

## Description

The `AI-Powered README Generator` is designed to streamline the documentation process for developers. Given a GitHub repository URL, it connects to GitHub to fetch the repository's file list and structure. This information, along with the project's context, is then fed into a sophisticated LLM (powered by Google's Generative AI via LangChain) to synthesize a well-structured and informative `README.md`.

This tool is particularly useful for:
*   Quickly generating initial READMEs for new projects.
*   Updating existing READMEs with fresh content based on current repository structure.
*   Learning how to integrate LLMs with external APIs for practical applications.

## Installation

To set up and run this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    (Replace `<repository_url>` and `<repository_name>` with the actual details of this project's repository.)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is not explicitly provided in the file list, but the dependencies can be inferred from the code. You would typically create one with: `langchain-google-genai`, `PyGithub`, `python-dotenv`)*
    
    If `requirements.txt` is missing, manually install:
    ```bash
    pip install langchain-google-genai PyGithub python-dotenv
    ```

4.  **Set up your Google Gemini API Key:**
    The project uses Google's Generative AI. You need to obtain an API key from Google AI Studio.
    
    Create a `.env` file in the root directory of the project and add your API key:
    ```
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```
    Replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual API key.

5.  **Ensure Prompt File Exists:**
    The `doc_agent.py` script expects a prompt file at `prompts/readme_prompt.txt`. You will need to create this directory and file, and populate it with a suitable prompt for the LLM.

    Example `prompts/readme_prompt.txt` content (you can customize this extensively):
    ```
    You are an expert technical writer. Your task is to generate a comprehensive and engaging README.md for a GitHub repository.

    The repository name is: {repo_name}
    The list of files and their descriptions (where available) in the repository is:
    {file_list}

    Based on this information, generate a detailed README.md file that includes:
    - A clear and concise description of the project.
    - Installation instructions.
    - Usage examples.
    - Key features.
    - Contributing guidelines.
    - Licensing information.

    Focus on clarity, accuracy, and user-friendliness. Use markdown formatting.
    ```

## Usage

To generate a README for a GitHub repository, run the `main.py` script from your terminal, providing the GitHub repository URL as an argument:

```bash
python main.py <github_repo_url>
```

**Example:**

```bash
python main.py https://github.com/octocat/Spoon-Knife
```

After execution, a new file named `README_generated.md` will be created in the root directory of this project, containing the generated README content.

## Features

*   **AI-Powered Generation**: Leverages Google's Generative AI through LangChain to create contextually relevant READMEs.
*   **GitHub Integration**: Fetches repository file structures directly from GitHub using the PyGithub library.
*   **Command-Line Interface**: Simple and intuitive command-line usage for quick README generation.
*   **Modular Design**: Separates concerns into `agents` (for AI logic) and `repo_utils` (for GitHub interactions).
*   **Environment Variable Support**: Securely loads API keys using `python-dotenv`.

## Example Code

To demonstrate how to run the tool, here's the typical command you would execute:

```bash
# Generate a README for the 'langchain-ai' repository by LangChain
python main.py https://github.com/{username}/{repo_name}
```

Upon successful execution, a file named `README_generated.md` will appear in the current directory, containing the newly generated documentation.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  **Fork the repository.**
2.  **Create a new branch** (`git checkout -b feature/YourFeature` or `fix/BugFix`).
3.  **Make your changes.**
4.  **Commit your changes** (`git commit -m 'Add YourFeature'`).
5.  **Push to your branch** (`git push origin feature/YourFeature`).
6.  **Open a Pull Request.**

Please ensure your code adheres to good practices and includes relevant tests if applicable.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file (if present, or assume MIT if none is explicitly provided) for more details.
