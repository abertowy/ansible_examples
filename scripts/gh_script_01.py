import argparse
import requests
import os


def gh_data():
    parser = argparse.ArgumentParser(description="Get pr data from")

    parser.add_argument("--gh-token", required=False)
    parser.add_argument("--branch", required=False)
    parser.add_argument("--pull-request", required=False)
    parser.add_argument("--username", required=False)

    args = parser.parse_args()
    # gh_token = os.environ.get("GITHUB_TOKEN")
    # PR
    # gh_url = f"https://cc-github.bmwgroup.net/api/v3/repos/{args.project}/pulls/{args.pull_request}"
    # Repo
    gh_url = f"https://api.github.com/users/{args.username}/repos/"
    gh_headers = {"Authorization": f"Bearer {args.gh_token}"}
    result = requests.get(gh_url, headers=gh_headers).json()
    print(result)


if __name__ == "__main__":
    gh_data()