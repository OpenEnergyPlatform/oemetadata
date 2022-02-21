# Release prozedur
 ## Pre-Release
- View the GitHub project for the next release and check the 
Status of all issues and PR's assigned to the project.
If there are any open issues or PR's, decide if you want to include them
them to be included in the upcoming release. Make sure that all changes are
are included in the development branch before proceeding to the next steps.
## Release
- 1 Checkout a new branch from devolop branch named: release/oem-vX.X.X
- 2 Update the following files: 
	- Make sure all changes are documented in the changelog.md.
	- Set the correct version number in the setup.py file.
- 3 Commit and Push the changes.
- 4 Create the Pull Request via the GitHub website and merge changes to 
develop then merge develop in master branch.
- 5 Create a new release via the GitHub website and tag the master branch.
- 6 Update the PyPi (pip) Package [oep-metadata](https://pypi.org/project/oep-metadata/)