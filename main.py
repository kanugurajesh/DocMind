import sys
import os
from agents.doc_agent import generate_readme
from repo_utils.fetch_files import update_or_create_readme

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
        
        print("README.md generated locally as README_generated.md!")
        
        # Update or create README.md in the GitHub repo
        try:
            update_or_create_readme(repo_url, readme, commit_message="Automated: Update README.md with DocMind")
            print("README.md updated/created in the GitHub repository!")
        except Exception as github_e:
            print(f"Failed to update/create README.md in GitHub: {github_e}")
        
    except Exception as e:
        print(f"Error generating README: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()