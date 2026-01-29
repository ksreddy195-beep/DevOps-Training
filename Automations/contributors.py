import pandas as pd
import subprocess
import json
import paginate

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


def get_contributor_count(owner, repo):
    try:
        contributors_json = run_gh([
            "api",
            f"repos/{owner}/{repo}/contributors",
            "--paginate"
        ])
        contributors = json.loads(contributors_json)
        return len(contributors)
    except subprocess.CalledProcessError:
        # Happens for empty repos, archived repos, or permission issues
        return 0

print(get_contributor_count)
# ---------- ADD CONTRIBUTORS COUNT ----------
df["contributors_count"] = df.apply(
    lambda row: get_contributor_count(row["owner"], row["repo"]),
    axis=1
)

# Save updated Excel
df.to_excel("repos_in_github_with_contributors.xlsx", index=False)
