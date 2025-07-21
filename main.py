from agents.doc_agent import generate_readme
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <github_repo_url>")
        exit(1)

    repo_url = sys.argv[1]
    readme = generate_readme(repo_url)

    with open("README_generated.md", "w") as f:
        f.write(readme)

    print("README_generated.md has been saved.")