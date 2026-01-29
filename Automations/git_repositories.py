import pandas as pd
import subprocess
import json

def run_gh(cmd):
    result = subprocess.run(
        ["gh"] + cmd,
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout

# ---------- USER REPOS ----------
user_repos_json = run_gh([
    "repo", "list",
    "--limit", "1000",
    "--json", "name,owner,visibility,url"
])
print(type(user_repos_json))

user_repos = json.loads(user_repos_json)
print(type(user_repos[0]))
print("User repositories:")
for repo in user_repos:
    print(f"{repo['owner']['login']}/{repo['name']} ({repo['visibility']})")

df = pd.DataFrame([
    {
        "repo": repo["name"],
        "owner": repo["owner"]["login"],
        "visibility": repo["visibility"],
        "url": repo["url"]
    }
    for repo in user_repos
])

df.to_excel("repos_in_github.xlsx", index=True)
