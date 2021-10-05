# Git Blah: Demo repo

This is a demo repository for training on:

* comparing branches
* rebase demo-branch
* merge demo-branch
* fix conflicts

# What's in this repo?

A small python library with tests.

# Tutorial

# Setup

## Clone repository

`git clone git@github.com:gauteh/git-blah.git`

## Create conda python environment:

`conda env create -f environment.yml`

## Activate conda environment

`conda activate blah`

## Run tests

`pytest`

# Explore log

Try to figure out which commit id introduced the file `environment.yml`?

# Check out feature-1

## Checkout

`git checkout feature-less-mem`

## Inspect

`git clog main..HEAD`

## Diff

`git diff main`

## Review

`git difftool -y main`
`pytest`

## Merge into main

`git co main`
`git merge feature-less-mem`

# Check out feature-2

## Checkout

`git checkout feature-init-value`

* Inspect
* Diff
* Review

## Is this branch up-to-date?

Easiest is to try and rebase.

## Rebase

`git rebase main`

oh uh..

## Solving conflict:

`git status`
`git mergetool`

In rebase:

Left is our new changes (trying to rebase)
Middle is end-result
Right is other changes (current version)

* Fix conflicts

Mark as solved with:

`git add blah/model.py`

Continue rebasing with:

`git rebase --continue`


## You can now merge this branch into main

`git checkout main`
`git merge feature-init-value`

# Try the same using only merge and not rebase:

Start from scratch

1. merge feature-less-mem
2. merge feature-init-value

# References

* https://levelup.gitconnected.com/solving-2d-heat-equation-numerically-using-python-3334004aa01a
