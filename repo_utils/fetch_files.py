import os
from github import Github
from github.GithubException import GithubException

def fetch_repo_files(repo_url):
    g = Github()  # No token = only public repos
    repo_name = repo_url.split("github.com/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
        
    repo = g.get_repo(repo_name)

    files = repo.get_contents("")
    
    result = []
    while files:
        file = files.pop(0)
        if file.type == "dir":
            files.extend(repo.get_contents(file.path))
        elif file.name.endswith((".py", ".js", ".ts", ".md", ".json")):
            result.append((file.path, file.decoded_content.decode("utf-8", errors="ignore")))

    return result

def update_or_create_readme(repo_url, content, commit_message="Update README.md"):
    """
    Update README.md in the given repo, or create it if it doesn't exist.
    Requires GITHUB_TOKEN in environment.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not set in environment.")
    g = Github(token)
    repo_name = repo_url.split("github.com/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
    repo = g.get_repo(repo_name)
    try:
        readme_file = repo.get_contents("README.md")
        repo.update_file(
            path=readme_file.path,
            message=commit_message,
            content=content,
            sha=readme_file.sha
        )
    except GithubException as e:
        if e.status == 404:
            # README.md does not exist, create it
            repo.create_file(
                path="README.md",
                message=commit_message,
                content=content
            )
        else:
            raise