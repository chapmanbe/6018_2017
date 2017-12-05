# Installing Python

Moving into adolescent programmers, you will need to have Python installed on your own computer. There are two approaches that I would recommend.

## Using Anaconda

Anaconda is the most popular distribution of Python and comes with what is considered the best package management system (`conda`) available. You can find binary installs for Windows, OS X, and Linux [here](https://www.anaconda.com/download/#macos).A

Anaconda comes with the [Spyder](https://pythonhosted.org/spyder/) integrated development environment (IDE). A more powerful and popular IDE is [pyCharm](https://www.jetbrains.com/pycharm-edu/), which is commercial but has a free educational version.

Separate from an IDE, you should probably have a Python-aware text editor. I use both [VIM](http://www.vim.org/) and [Atom](https://atom.io/). If you are not VIM savvy, I recommend using Atom.

## Using Docker

Another approach to using Python on your comptuer is to use [Docker](https://www.docker.com/). Our Jupyterhub environment is actually built around Docker and you could replicate the environment on your computer. We use the [Juypter Data Science Stack Notebook](https://hub.docker.com/r/jupyter/datascience-notebook/).
