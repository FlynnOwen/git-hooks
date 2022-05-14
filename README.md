# git-hooks
Testing git hooks with a repository

Reference from this source:

https://www.atlassian.com/git/tutorials/git-hooks

## Creating a symlink between hooks/ and .git/hooks

From the root directory of the project run:
```
ln -sf $(pwd)/hooks $(pwd)/.git
```

This creates a symbolic link between the files in the hooks/ directory and the .git/hooks directory
