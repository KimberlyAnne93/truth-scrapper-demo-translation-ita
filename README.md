# Truth Scrapper

## Getting set up with GitHub

To begin, there are two main methods for using Git and GitHub. The first is through GitHub's application, GitHub Desktop, and the second will be through your code editor itself. We'll go through the process of using GitHub desktop, as it takes care of a lot of the extra setup automatically. I'll also give a brief summary of how the process works for adding your code editor.

### GitHub Desktop

GitHub Desktop is an application for Windows and Mac that's designed to make the process of syncing files on your computer with the online repository easier. You'll first need to download the GitHub desktop application, which you can find here: https://desktop.github.com/

You can then log in with your GitHub username and password and give it permission to access your repositories. From there you should be able to see **USER_NAME/REPOSITORY_NAME** under your list of repositories, and if you select it there will be an option at the bottom allowing you to **Clone USER_NAME/REPOSITORY_NAME**. It will let you select where you want to download the repository to on your computer.

* If you don't see a list of your current repositories, you can also hit File -> Clone repository... and the repository should be listed there.
* You also must clone the repository into an empty folder. You can transfer any changed files from wherever your current local copy of the game is later, but GitHub needs an empty folder so it can set up a special `.git` folder with files to connect it to the online repository.

When it's finished cloning the repository, you should see a screen with three options at the top that say something like **Current Repository**, **Current branch**, and **Fetch Origin**. Now that you have a copy of the repository, in the future you can use the **Fetch origin** button to sync your copy with any changes that have been made instead of downloading the whole repository or individually picking out the modified files. If you make any modifications to the script or files locally, you'll also be able to sync those changes to the repository using this screen as well.

Whenever you make a change to your files, it will show up on the left and you'll be able to click it to see a comparison of the things you've changed since you last synced your files to the repository. You can individually select/deselect sections on this screen as well to pick-and-choose what you upload. If you decide you don't want to include a change after all, you can also revert your updates by right-clicking the file and selecting **Discard changes...**.

**Typical GitHub Desktop Workflow:**

* First, you'll make some changes to your files. If other people are working on your project as well, you should also use **Fetch origin** frequently to ensure you have the latest updates.
* Next, you can review all your changes in the sidebar. There's room for a commit message at the bottom of the screen; this is useful so you know what was changed/updated each time you sync your files. If you're pushing a lot of changes, you might want to select only a few at a time, write a description/summary of the updates, then commit them until you've committed all your changes.
* Once you've committed the files you want to sync, hit the **Push** button at the top of the screen. That will sync your files to the repository on GitHub.

And that's the basics! There are several other useful features you can take advantage of, such as the issue tracker and wiki features. For multiple people making changes to the files at once, you may also want to create a *branch* to work on new features, and then merge the changes once everything is working properly. To do this in GitHub Desktop, you can click on the **Current branch** button along the top bar. From there you can switch to a different branch or create a new one. If you have uncommitted changes in your current branch, you'll be prompted to either bring them along to the new branch or to leave those changes uncommitted on the main branch.

In the new branch, you can make commits and pull changes like you would in the main branch of the repository. When you're done working on your feature/addition/changes and want to merge it with the main branch, you'll need to open a pull request. If you've committed all your changes, GitHub might prompt you to do this with a **Create Pull Request** button. You can also go online to the repository and go to the **Code** tab, and you'll see a little branch icon at the top along with the current branch (likely **main**). Use the dropdown to select your new branch, and there will be an option on the right to create a **Pull request**.

If all has gone well, you should be able to compare the changes and create the request. You can also assign other team members to review a request before it is merged. Lastly, you'll Merge the pull request; while there are a few options for how to do this, the most commonly used is **Create a merge commit**. Hit **Merge pull request** and then **Confirm merge**. If all was successful, GitHub should offer to safely delete the branch you were working on since it's now part of the main branch. This is usually a good idea for organization, and you can restore the branch later if you realize you need it.

### GitHub + your code editor

If you'd like to integrate your code editor with your GitHub repository to easily sync files without leaving your editor, then I recommend VS Code. You can also set up git integration with Atom, though support for Atom has ended and it is no longer being developed. I have a small section in my tutorial on getting started with Ren'Py which goes over installing VS Code for use with Ren'Py script files: https://feniksdev.com/getting-started-with-renpy/#Editing_Your_Project

To begin with VS Code, you'll need to have git installed on your computer and set it up with your GitHub account. Here are some instructions on that: https://www.geeksforgeeks.org/how-to-install-git-in-vs-code/

Then you can make use of the **Source Control** tab. Then, when you open up a folder which has the special **.git** folder (aka it was initialized as a git repository like you did above through GitHub desktop), you'll see a list of the files you've changed much like on GitHub desktop. The process is the same here with comparing and adding files to a commit and then pushing them to sync with the online repository. If you're feeling comfortable with the process of committing changes and pulling from the repository, then this can be a very useful shortcut to push your changes right where you're editing code.

## Final Notes

The **.gitignore** will ensure that unnecessary files aren't synced to the repository, such as save files and error logs. For development, it also ignores **rpyc** files, as it isn't important to sync those between contributors before release. For release, however, you should make sure to use the **Distributions -> Actions: Update old-game** option to update rpyc files in the `old-game` folder. Ren'Py uses these to remember what the game script used to look like so it can correctly load old save games even if the script changes.

In essence, rpyc files contain information on each line's virtual "location" and will update it rather than overwriting it when typos are fixed, lines are changed around, etc. This allows save files to be compatible even if you push bug fixes and patches later on. You should update the old-game/ folder with the rpyc files from the regular game/ folder before each release!
