The Challenge:

We use Trivy to scan container images for vulnerabilities. If any critical vulnerabilities are detected, the base image version needs to be updated to the latest version containing the fixes. Previously, this was a manual task, involving

1.Going into each microservice's repository
2.Updating the base image version in the Dockerfile
3.Creating and raising pull requests (PRs)

With dozens of microservices, this was time-consuming and error-prone.

The script should take a the following parameters:

1.A file containing microservice names (e.g., payment-service)
2.The new base image version (e.g., 6254-abc-867)
3.A Jira ticket number for tracking
4.Stash credentials (username and password)
5.A flag for dry-run (to preview changes without applying them)
6.Once all microservices are processed, the script outputs a list of PRs for the development team to review and approve. 



 

The logic the script should try to implement:

1.Loops through the microservice list
2.Clones the repository for each microservice (develop branch)
3.Creates a feature/<ticket-number> branch
4.Updates the base image version in the Dockerfile
5.If dry-run is enabled, it prints the git diff instead of committing changes
6.Saves the PR link into a file for easy tracking
