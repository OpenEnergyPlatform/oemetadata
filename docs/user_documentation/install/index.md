# Install

## Environment (Conda)

With conda, you can create, export, list, remove, and update environments
that have different versions of Python and/or packages installed in them. <br>
Switching or moving between environments is called activating the environment.
You can also share an environment file and import from 📝 `requirements.txt`.

    💻 `conda env create -f environment.yaml` Create conda environment <br>
    💻 `conda activate py310` Activate environment <br>
    💻 `python --version` Check python version

Delete existing environment: <br>
    💻 `conda deactivate` <br>
    💻 `conda remove --name py310 --all`

## Requirements

In Python the 📝 `requirements.txt` file helps manage dependencies. <br>
It's a text file that lists the packages that the Python project depends on. <br>
All listed packages will be installed in the conda environment.

💻 `pip install -r requirements.txt` Install from file

## PyProject

This python package contains a `pyproject.toml` file that contains
build system requirements and information, which are
[used by pip](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
to build the package.
It contains the metadata of the software project.

## astral-uv

Astral UV is a modern Python package manager designed for flexibility and speed.
Efficient package management is crucial for maintaining consistency and
compatibility in Python projects.
Tools like `pip` and `virtual environments` help manage dependencies,
while advanced tools like `astral-uv` streamline package management workflows further.
It focuses on optimizing dependency resolution, improving installation times,
and ensuring reproducible builds.

Its key features include:

- **Fast Dependency Resolution**: Reduces conflicts and speeds up package resolution.
- **Reproducibility**: Ensures consistent environments across different machines or deployments.
- **Integration with CI/CD Pipelines**: Tailored for seamless integration into automated workflows.

Install: <br>
    💻 `pip install uv` Install package <br>
    💻 `uv` Check package

Use: <br>
    💻 `uv python list` View available Python versions <br>
    💻 `uv run` Run a command in the project environment

Build and publish (not implemented yet): <br>
    💻 `uv build` Build the project into distribution archives <br>
    💻 `ls dist/` View created distribution <br>
    💻 `uv publish` Build the project into distribution archives

See the official documentation at [astral.sh](https://docs.astral.sh/uv/getting-started/features/#features)

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
