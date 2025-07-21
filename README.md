# Auto-README Generator

## Project Title
**Auto-README Generator**

## Description
The Auto-README Generator is a Python-based command-line tool designed to automatically generate detailed and structured `README.md` files for public GitHub repositories. Leveraging the power of Large Language Models (LLMs) via LangChain and the GitHub API, this tool analyzes the contents and structure of a given repository to synthesize a comprehensive README.

It simplifies the documentation process for developers by fetching relevant code files, understanding their purpose, and then crafting a professional `README.md` complete with sections like Description, Installation, Usage, Features, and more.

## Installation

To set up the Auto-README Generator locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/auto-readme-generator.git
    cd auto-readme-generator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` is not provided, but based on the code, it would contain `langchain-google-genai`, `PyGithub`, `python-dotenv`, `langchain`)*.
    You might need to install them manually if `requirements.txt` is missing:
    ```bash
    pip install langchain-google-genai PyGithub python-dotenv langchain
    ```

4.  **Set up your API Key:**
    This project uses a Google Generative AI model. You'll need to obtain an API key from Google AI Studio.
    Create a `.env` file in the root directory of the project and add your API key:
    ```
    GOOGLE_API_KEY="your_google_gemini_api_key_here"
    ```

5.  **Prepare the Prompt File:**
    The tool relies on a prompt template. Create a directory named `prompts` in the root of the project and inside it, create a file named `readme_prompt.txt`.
    A basic example of `prompts/readme_prompt.txt` content could be:
    ```
    Generate a detailed and structured README.md for a GitHub repository based on the following file list and their descriptions.
    
    File List:
    {file_list}
    
    File Descriptions:
    {descriptions}
    
    The README should include the following sections:
    - Project Title
    - Description
    - Installation
    - Usage
    - Features
    - Example Code (if applicable)
    - Contributing
    - License
    
    Ensure the language is clear, concise, and professional.
    ```
    *Adjust the prompt as needed for desired README structure and content.*

## Usage

To generate a `README.md` for a GitHub repository, run the `main.py` script from your terminal, providing the repository's URL as an argument:

```bash
python main.py <github_repo_url>
```

**Example:**

```bash
python main.py https://github.com/octocat/Spoon-Knife
```

Upon successful execution, a new file named `README_generated.md` will be created in the project's root directory, containing the automatically generated README content.

## Features

*   **Automated README Generation:** Quickly generates a comprehensive `README.md` for any public GitHub repository.
*   **LLM-Powered Content Synthesis:** Utilizes a Large Language Model (specifically Google Generative AI via LangChain) to analyze code and generate human-readable descriptions and instructions.
*   **GitHub Repository File Fetching:** Connects to the GitHub API to recursively fetch file paths and content from the specified repository.
*   **Structured Output:** Generates a `README.md` with standard sections like Description, Installation, Usage, Features, Contributing, and License, ensuring a professional and organized document.
*   **Customizable Prompt:** Allows for customization of the README generation logic via a prompt template file (`prompts/readme_prompt.txt`).
*   **Support for Public Repositories:** Designed to work with any publicly accessible GitHub repository.

## Example Code

This section demonstrates how to run the `main.py` script and what to expect.

**Running the script:**

```python
# main.py
import sys
import os
from agents.doc_agent import generate_readme

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <github_repo_url>")
        sys.exit(1)
    
    repo_url = sys.argv[1]
    print(f"Generating README for: {repo_url}")
    
    try:
        readme = generate_readme(repo_url)
        
        # Write with UTF-8 encoding to handle Unicode characters
        with open("README_generated.md", "w", encoding="utf-8") as f:
            f.write(readme)
        print(f"README generated successfully! Check README_generated.md")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Command Line Execution:**

```bash
python main.py https://github.com/openai/openai-cookbook
```

**Expected Output:**

```
Generating README for: https://github.com/openai/openai-cookbook
README generated successfully! Check README_generated.md
```

A file named `README_generated.md` will be created in your project directory, containing the newly generated README.

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to good practices and includes appropriate tests where necessary.

## License

This project is open-source and available under the MIT License. See the `LICENSE` file (if present) for full details.

*(Note: A `LICENSE` file was not provided in the given file list. The MIT License is a common choice for open-source projects.)*