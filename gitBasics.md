# Git Workflow

Here's a quick tutorial of how to get started. I won't go in to depth on how every git command I mention works (there's plenty of resources for that; though I don't suggest diving down those rabbit holes immediately). This should be enough to get you started. It's a very basic and standard git workflow. Git has a steep learning curve, so if you get stuck with git, please ask me or else you may end up doing something like losing all your work.

## How to get started:

 1. Fork the org repo to your own github repo (click on Fork on top right)
 2. Navigate to **your** github repo
 3. Click on clone or download and copy the link
 4. In your terminal, enter `$ git clone https://github.com/StephAlbArt/DS_Algos.git`
 5. `cd DS_Algos`
 6. Read the rest of this document before you start working


## Creating a new branch

If you're going to work on a new feature or fix a bug, you should always [cut a new branch](https://www.atlassian.com/git/tutorials/using-branches/), regardless of much code you think it will be. One reason for this is because we don't want to touch our single "source of truth" until we're certain we're ready to merge our changes (I'll explain this part later). Currently, there's nothing in the repo, and let's say I want to start working on the binary tree's.

Continuing from above, my command line should display something like `alberth8 (master) DS_Algos $`: meaning you're on the `master` branch. Now cut a new branch:

    $ git checkout -b [feature_or_bug_name]

(Without the brackets).

You'll automatically be thrown in to that branch, so now youre command line should display `albert8 (feature_or_bug_name) $`. So if I wanted to work on the insertion method for a binary tree, I would do something like `$ git checkout -b binaryTree-insertion` But before you do that, read on.

## How to commit your work

Everytime you create you crank out enough code to where you think you'd be sad if you lost that code, you should make a `commit`. As a general guideline, depending on how much you're coding, that could be one commit every 15-30 minutes. Commit messages should be clear, concise, in present tense, and prefixed by a description in parenthesis. For example, `(feat) create insertion method for binary tree`. Other prefixes include: (fix), (refactor), (cleanup), (test), and (doc). But before you make a commit, you have to stage your changes.

So let's say you've got a working method for a data structure and you're ready to commit your changes. First you should `git status`. This will show you what files have been added, changed, or updated. Then `git add` the relevant files. Do another `git status` just to make sure they got staged. (Don't worry, if you add the wrong ones, you can always unstage them).

    Aside: There may be times you forget to commit, and end up doing a lot of work, and changing a lot of files, do your best to add only the files that are relevant to a particular commit. This way it's easier to figure out what was changed with each commit, especially when you need to revert changes.

Now you need to use `git commit -m [your_message_here]` to "save" your work on your local machine.

To summarize:
 1. `git status`
 2. `git add binaryTree.py`
 3. `git status`
 4. `git commit -m "create Node class for binaryTree"`
 5. Read on...

## From your local to your remote repo

Now you've got to get it on to your Github repo by using `git push`. You don't have to push after every commit, after a coding session, before you take a break, a few times a day...Whatever works for you, but the more the merrier. 

If you were careful in cloning from your own repo, when you do `git remote -v`, you should see `origin http://www.github.com/[your_username]/DS_Algos`. Assuming that to be the case, then

    $ git push origin binaryTree-insertion

This assumes I preivously cut a branch called `binaryTree`. Be sure you push the corect branch name, and not something like `master`

## Rinse and repeat

Now you're free to keep on working! Let's recap really quick.

1. You've edited/added some stuff and you're ready to commit
2. `git status`
3. `git add [relevantFile_1.py] [relevantFile2.py]`
4. `git status`
5. `git commit -m "(test) add test for binaryTree.py for insertion method"`
6. `git push origin binaryTree`

If you want to continue working, then just rinse and repeat. If you decide to work on another method, be sure to cut a new branch.

## Combining all work

So you've got stuff on your remote repo, but since we're working on a team, we have to be working off the same code base -- meaning we have to merge our stuff together at some point. This is where a pull request comes in. You can think of a pull request as putting in a request to have your code merged.  

Ideally, we would do a family style pull request, where the person who is merging his/her code in to the single source of truth, walks us through their code, but since we're all remote, each of us are going to have to be doubly sure that our code doesn't break the code in the org repo. This also means that we have to be extra clear with our commenting/documentation.

When one person is ready to merge their stuff, and have submitted a pull request, the other team members should individually inspect the code, then someone else besides the author should merge the pull request.

#### How to make a pull request

Go to your github repo, and click on `New pull request`. Make sure on the drop down menus, you have:

    [base fork: org/repo][base: master] ... [head fork: your_username/repo][compare: the_branch_to_be_merged]


#### How to merge the pull request

We only merge the pull request after we're all okay with the new code/changes. To merge a pull request, from the org repo page, click on the tab that says "Pull requests". From there we can review the code, and at the bottom, you can click the button to merge the pull request. Just below that, you can leave a comment, and typically I'll write something like "Code submitted by [submitter]. Reviewed by [reviewer]".

## Rebasing

Always, always rebase before you start working because you want to work off of what is most recent in order to avoid conflicts. I[rebase](http://code.tutsplus.com/tutorials/rewriting-history-with-git-rebase--cms-23191) 








    



