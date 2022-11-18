# Release procedure
 ## Pre-Release
- View the GitHub project for the next release and check the 
Status of all issues and PR's assigned to the project.
If there are any open issues or PR's, decide if you want to include them
them to be included in the upcoming release. Make sure that all changes are
are included in the development branch before proceeding to the next steps.
- Create a new folder named "vXXX" (release version) in the metadata and
test directory. 
	- In the metadata direcotry copy all files from latest to the 
	new folder then adapt all .py files to the latest version and
	update the id in schema.json.
	- In test copy all files from previous oder latest version folder 
	in test directory and adapt all tests (test_***.py files) to
	the latest version.
## Release
- 1 Checkout a new branch from devolop branch named: release/oem-vX.X.X
- 2 Update the following files: 
	- Make sure all changes are documented in the changelog.md.
	- Set the correct version number in the setup.py file.
- 3 Commit and Push the changes.
- 4 Create the Pull Request via the GitHub website and merge changes to 
develop then merge develop in master branch.
- 5 Create a new release via the GitHub website and tag the master branch.

# Publish and Deploy Release automation
We provide automation workflows that will build and upload PyPi Packages.

Keep in mind that specific package versions (as specified in the [setup.py](https://github.com/OpenEnergyPlatform/oemetadata/blob/5fc02df0a5efeb01cc8d9b78929c3dfe9eebd8cb/setup.py#L13)) can only be release once. This stands for test and official PyPi package index.

**Test workflows** are triggered when pushing commits to the permanent branch called `deployment-test`. 

**Release Deployment Workflow** is triggered as soon as one publishes a new github release.

- [Test Workflow](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/test-pypi-publish.yml): Update test PyPi (pip) Package [oemetadata pypi test](https://test.pypi.org/project/oemetadata/)
- [Release Deployment Workflow](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/pypi-publish.yml) Update the PyPi (pip) Package [oemetadata](https://pypi.org/project/oemetadata/)
