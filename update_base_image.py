import os
import subprocess
import requests
import argparse
 
def clone_repo(microservice, stash_credentials):
    repo_url = fhttps://{stash_credentials['username']}:{stash_credentials['password']}@stash.example.com/scm/project/{microservice}.git
    subprocess.run(["git", "clone", repo_url, "--branch", "develop", microservice], check=True)
 
def create_feature_branch(microservice, ticket_number):
    os.chdir(microservice)
    subprocess.run(["git", "checkout", "-b", f"feature/{ticket_number}"], check=True)
 
def update_dockerfile(base_image_version):
    dockerfile_path = "Dockerfile"
    with open(dockerfile_path, "r") as file:
        lines = file.readlines()
 
    with open(dockerfile_path, "w") as file:
        for line in lines:
            if line.startswith("FROM"):
                file.write(f"FROM base-image:{base_image_version}\n")
            else:
                file.write(line)
 
def commit_changes(ticket_number):
    subprocess.run(["git", "add", "Dockerfile"], check=True)
    subprocess.run(["git", "commit", "-m", f"Update base image to {ticket_number}"], check=True)
 
def create_pull_request(microservice, ticket_number, stash_credentials):
    pr_url = fhttps://stash.example.com/rest/api/latest/projects/project/repos/{microservice}/pull-requests
    data = {
        "title": f"Update base image to {ticket_number}",
        "description": "Base image version update",
        "state": "OPEN",
        "open": True,
        "closed": False,
        "fromRef": {"id": f"refs/heads/feature/{ticket_number}"},
        "toRef": {"id": "refs/heads/develop"},
    }
    response = requests.post(pr_url, json=data, auth=(stash_credentials['username'], stash_credentials['password']))
    if response.status_code == 201:
        return response.json()["links"]["self"][0]["href"]
    else:
        response.raise_for_status()
 
def main():
    parser = argparse.ArgumentParser(description="Update base image for microservices.")
    parser.add_argument("microservices_file", help="File containing microservice names")
    parser.add_argument("base_image_version", help="Base image version")
    parser.add_argument("ticket_number", help="Ticket number")
    parser.add_argument("stash_username", help="Stash username")
    parser.add_argument("stash_password", help="Stash password")
    parser.add_argument("--dry-run", action="store_true", help="Dry run mode (print git diff only)")
    args = parser.parse_args()
 
    stash_credentials = {
        "username": args.stash_username,
        "password": args.stash_password,
    }
 
    with open(args.microservices_file, "r") as file:
        microservices = [line.strip() for line in file.readlines()]
 
    pr_links = []
 
    for microservice in microservices:
        print(f"Processing {microservice}...")
        clone_repo(microservice, stash_credentials)
        create_feature_branch(microservice, args.ticket_number)
        update_dockerfile(args.base_image_version)
 
        if args.dry_run:
            subprocess.run(["git", "diff"], check=True)
        else:
            commit_changes(args.ticket_number)
            subprocess.run(["git", "push", "origin", f"feature/{args.ticket_number}"], check=True)
            pr_link = create_pull_request(microservice, args.ticket_number, stash_credentials)
            pr_links.append(pr_link)
 
        os.chdir("..")
 
    if not args.dry_run:
        with open("pr_links.txt", "w") as file:
            for link in pr_links:
                file.write(link + "\n")
        print("Pull request links saved to pr_links.txt")
 
    print("Done!")
 
if __name__ == "__main__":
    main()
