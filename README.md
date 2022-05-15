# git-hooks
Testing git hooks with a repository - unfortunately the .git directory isn't tracked remotely, thus we create a folder called hooks/ to keep version control the hooks for this repo.

Reference from this source:

https://www.atlassian.com/git/tutorials/git-hooks

# Usage

## First, create a symlink between hooks/ and .git/hooks

From the root directory of the project run:
```
ln -sf $(pwd)/hooks $(pwd)/.git
```

This creates a symbolic link between the files in the hooks/ directory and the .git/hooks directory

## Current hooks
Currently, two hooks are enabled:

### 1. prepare-commit-msg (.git/hooks/prepare-commit-msg)
flake8 linting is run whenever a commit is made

### 2. pre-push (.git/hooks/pre-push)
'pyest' is run to unit test all python files whenever a push is made

## To enable hooks for different sets of git commands:
- Remove '.sample' suffix from the desired file in .git/hooks/
- Change the code / commands for that command as you see fit!
