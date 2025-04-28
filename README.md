The script should take a the following parameters:

1.File containing microservice names (eg. payment-service)
2.NewBase image version (eg. 8.3.32-fe16b27)
3.Jira ticket number
4.Stash credentials (user name and password)
5.Falg for dry-run (true/false)

 

The logic the script should try to implement:

1.Loop over the file with microservices names
2.Clone the repository for the given the mocroservice (develop branch)
3.Create feature/<ticket number> branch
4.Modify Docker file and update base images versions within
5.In case of dry run , just print git diff
6.Save PR link into a file
7.Move to the next microservice and repeat loop
8.Once all the microservice , print the list of PRs, So Dev team can review and approve easily.

