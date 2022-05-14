# git-hooks
Testing git hooks with a repository - unfortunately the .git directory isn't tracked remotely, thus we create a folder called hooks/ to keep version control the hooks for this repo.

Reference from this source:

https://www.atlassian.com/git/tutorials/git-hooks

## Creating a symlink between hooks/ and .git/hooks

From the root directory of the project run:
```
ln -sf $(pwd)/hooks $(pwd)/.git
```

This creates a symbolic link between the files in the hooks/ directory and the .git/hooks directory
