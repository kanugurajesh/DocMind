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
        
        print("README.md generated successfully!")
        
    except Exception as e:
        print(f"Error generating README: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()