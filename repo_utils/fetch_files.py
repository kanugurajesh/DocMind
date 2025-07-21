from github import Github

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