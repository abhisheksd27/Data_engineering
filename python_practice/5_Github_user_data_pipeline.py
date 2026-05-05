"""
Fetch GitHub user data using GitHub API,
save selected fields (including followers count) to CSV,
and print follower count in terminal.
"""

import requests
import pandas as pd
from datetime import datetime
import numpy as np

# GitHub usernames
usernames = ["octocat", "torvalds", "mojombo", "abhisheksd27"]

# Empty list to store processed user data
rows = []

for username in usernames:
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Select only required fields
        user_info = {
            "username": data["login"],
            "name": data.get("name"),
            "followers": data["followers"],   # follower count
            "following": data["following"],
            "public_repos": data["public_repos"],
            "profile_url": data["html_url"],
            "account_created": data["created_at"],
            "extracted_at": datetime.now()
        }
        
        rows.append(user_info)
        
        # Print follower count in terminal
        print(f"{username} has {data['followers']} followers")
    
    else:
        print(f"Failed to fetch data for {username}: {response.status_code}")

# Create DataFrame
df = pd.DataFrame(rows)

# Convert followers column to integer
df["followers"] = df["followers"].astype(int)

# Categorize users based on followers
df["followers_category"] = np.where(
    df["followers"] > 1000,
    "Popular",
    "Not Popular"
)

# Save to CSV
df.to_csv("github_users.csv", index=False)

print("\nCSV file saved successfully as github_users.csv\n")

# Print final DataFrame
print(df[["username", "followers", "followers_category"]])

print("")