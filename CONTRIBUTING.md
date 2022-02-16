## Development

### Prerequisites

- [Git](https://git-scm.com/)


### Workflow

The workflow for contributing to this project has been inspired by the workflow described by [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/).

Here are the minimal procedure you should follow : 

#### Step 1: Describe the issue on GitHub

Create [an issue](https://help.github.com/en/articles/creating-an-issue)
on the GitHub repository, describing the problem you will then address
with your feature/fix. This is an important step as it forces one to
think about the issue (to describe an issue to others, one has to think
it through first).

#### Step 2: Solve the issue locally

0. Get the latest version of the `develop` branch

    ```bash
    git checkout dev
    ```
   
    ```bash
    git pull
    ```

1. Create a new (local) branch
    ```bash
    git checkout -b feature-1314-my-feature
    ```

**Naming convention** for branches: `type`-`issue-nr`-`short-description`

**type**

* master / main / stable - includes the current stable version
* dev - includes all current developments
* feature - includes the feature that will be implemented
* hotfix - includes small improvements before an release, should be branched from a release branch
* release - includes the current version to be released

The majority of the development will be done in `feature` branches.

**issue-nr**

The `issueNumber` should be taken from Step 1. Do not use the "#". 

**short-description**

Describe shortly what the branch is about. Avoid long and short descriptive names for branches, 2-4 words are optimal.

Other hints:
- Separate words with `-` (minus)
- Avoid using capital letters
- Do not put your name to the branch name, it's a collaborative project
- Branch names should be precise and informative


2. Try to follow [these conventions](https://chris.beams.io/posts/git-commit) for commit messages:
    - Keep the subject line [short](https://chris.beams.io/posts/git-commit/#limit-50) (i.e. do not commit more than a few changes at the time)
    - Use [imperative](https://chris.beams.io/posts/git-commit/#imperative) for commit messages 
    - Do not end the commit message with a [period](https://chris.beams.io/posts/git-commit/#end) 
        You can use 
        ```bash
        git commit --amend
        ```
        to edit the commit message of your latest commit (provided it is not already pushed on the remote server).
        With `--amend` you can even add/modify changes to the commit.

3. Push your local branch on the remote server `origin`
    ```bash
    git push
    ```
    If your branch does not exist on the remote server yet, git will provide you with instructions, simply follow them.


#### Step 3: Run tests locally

To run tests locally, 

1. create virtualenv in root folder of repo

```bash 
python -m venv venv
```

2. Activate virtualenv

    Linux:

    ```bash
    . venv/bin/activate
   ```

    Windows:

    ```bash
    . venv/Scripts/activate
   ```

3. Install requirements

```bash 
pip install -r requirements.txt 
```

4. Integration/unit tests 
    ```bash
    pytest
    ```
    And for a complete run in different environments:
    ```bash
    tox -v
    ```
5. Linting tests
    ```bash
    flake8
    ```
    and
    ```bash
    pylint
    ```
    You can fix the linting errors either manually or with the packages
    `autopep8` or `black` for example.
    
#### Step 4: Submit a pull request (PR)

Follow the [steps](https://help.github.com/en/articles/creating-a-pull-request) of the GitHub help to create the PR.
Please note that you PR should be directed from your branch (for example `myfeature`) towards the branch `dev`.

Add a line `Fix #<number of the issue created in Step 2.0>` in the
description of your PR, so that when it is merged, it automatically
closes the issue once your code gets merged into the default branch of
your repository.
[Here](https://help.github.com/en/github/managing-your-work-on-github/closing-issues-using-keywords)
is a list of other keywords you can use to automatically close the
issues

#### Step 5: Setup continuous integration

To have the test run automatically everytime you push to a pull request
you can add the bash commands under `# command to run tests` of the
`.travis.yml` file. For this you need to have an account by
[Travis](https://travis-ci.org/) and link your repo to their service.
Soon [GitHub action](https://github.com/features/actions) might take
care of this directly within GitHub.

In the `.travis.yml` file are many options commented out, you can have
very complexe schemes to test on many different python versions etc. For
more information look at Travis
[doc](https://docs.travis-ci.com/user/languages/python/) for python.

### If a Python interpreter version is missing:

Linux (Ubuntu):

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
# Install only missing interpreters:
sudo apt-get install python3.6
sudo apt-get install python3.7
```