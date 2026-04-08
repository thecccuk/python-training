# Python training

This repository has been created to hold python training materials for CCC colleagues. It will be added to over time.

## Structure

As things stand, there are two subsets of training materials, both contained in the ```lessons``` subfolder in this repository:

- The ```pre-training``` subset, which contains demo notebooks, as well as exercise notebooks with solutions for introductory python, pandas, and numpy concepts.
- The ```python-club``` subset, which contains exercises and solutions for the python club series. These will be added to over time.

## Getting set up

If you have been asked to complete exercises in this repository, there are two ways you can go about doing that.

#### The easy way

The first way is simple. It involves navigating to the correct subfolder after clicking on this link: https://mybinder.org/v2/gh/thecccuk/python-training/HEAD

#### The better way

The second way is more complicated, but will allow you to save your progress for posterity in a way that the binder environment will not. To do this, follow the instructions below:

First, you will need to clone the git repository. You can do this from the command line using the following commands:

```bash
git clone https://github.com/thecccuk/python-training.git
cd python-training
```

...or more straightforwardly in VS Code, following the instructions on this page: https://code.visualstudio.com/docs/sourcecontrol/repos-remotes


After this, you will need to set up a virtual environment into which to install the package dependencies. The best way to do this is using the following commands in a command prompt (note you will need to have installed conda for this to work):

```bash
conda create -n python-training
conda activate python-training
```

If you don't have conda, but you are able to pip install within our current IT setup, you could also use the python venv library:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Finally you will want to install the packages into your virtual environment. You can do this with the following command:

```bash
pip install -r requirements.txt
```

## Asking questions

If you encounter any issues with these setup instructions or with the training materials themselves, please contact Fergal Wraith (firstname.surname@theccc.org.uk).

