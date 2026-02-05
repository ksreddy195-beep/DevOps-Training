import pandas as pd

df = pd.DataFrame([
    {
        "repo": repo["name"],
        "owner": repo["owner"]["login"],
        "visibility": repo["visibility"],
        "url": repo["url"]
    }
    for repo in user_repos
])

df.to_excel("github_repos.xlsx", index=False)