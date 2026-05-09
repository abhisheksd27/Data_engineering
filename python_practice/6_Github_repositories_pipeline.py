import numpy as np
import pandas as pd
import requests


usernames = ["octocat", "torvalds", "mojombo", "abhisheksd27"]


for username in usernames:
    url =f"https://api.github.com/users/{username}/repos"
    res = requests.get(url)
    data =res.json()

    df=pd.DataFrame(data)
    print(f"{username} has {len(df)} repositories")

df = df[['name', 'language', 'stargazers_count', 'created_at', 'forks_count']]

df["repo_score"]=df['stargazers_count']* df['forks_count']
df["repo_category"]=np.where(df["repo_score"]>100, "High Score", "Low Score")

df.to_csv("github_repositories.csv", index=False)

print(df.head())