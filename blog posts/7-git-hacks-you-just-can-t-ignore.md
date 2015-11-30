> 程序开发中的版本控制必不可少，Python开发也一样。而版本控制系统中，目前使用最广泛的，可能就是Git，而它最著名的代表就是Github。本篇译文为大家介绍了7个Git使用技巧，目的都是方便程序员弥补自己在开发中所犯的错误。

与其他技术相比，Git应该拯救了更多开发人员的饭碗。只要你经常使用Git保存自己的工作，你就一直有机会可以将代码退回到之前的状态，因此就可以挽回那些你深夜里迷迷糊糊犯下的错误。

尽管这么说，Git的命令行界面可是出了名的难掌握。接下来，就给大家介绍7个小技巧，最大限度发挥Git的作用。


![photo credit: xkcd](https://cdn-images-1.medium.com/max/800/0*n2QYqEj3coS_yKNl.png)


通常，大部分时间我们都只会用到`add`、`commit、`branch和`push`/`pull`这些命令。大部分人熟悉这套只往一个方向运转的工作流。你们有没有想过，如果自己往仓库中添加了错误的文件，或是将代码提交到了错误的分支，而且提交信息还写错了的话，自己怎样才能取消之前的操作？如果你也是按照上面漫画中所描绘的一样操作的（即删除本地项目文件夹，再重新下载仓库），那么你就有必要了解下面这些Git使用技巧了。

## 1. 修改错误的提交信息（commit message）

提交信息很长时间内会一直保留在你的代码库（code base）中，所以你肯定希望通过这个信息正确地了解代码修改情况。
下面这个命令可以让你编辑最近一次的提交信息，但是你必须确保没有对当前的代码库（working copy）做修改，否则这些修改也会随之一起提交。


	$ git commit --amend -m ”YOUR-NEW-COMMIT-MESSAGE”

假如你已经将代码提交（git commit）推送（git push）到了远程分支，那么你需要通过下面的命令强制推送这次的代码提交。

	$ git push <remote> <branch> --force

你可以关注[Stack Overflow网站上的这条问答](http://stackoverflow.com/questions/179123/edit-an-incorrect-commit-message-in-git/179147#179147)， 获取更多详情。

## 2. 提交之前撤销`git add`

如果你往暂存区（staging area）中加入了一些错误的文件，但是还没有提交代码。你可以使用一条简单的命令就可以撤销。如果只需要移除一个文件，那么请输入：

	$ git reset <文件名>

或者如果你想从暂存区移除所有没有提交的修改：

	$ git reset

你可以关注[Stack Overflow网站上的这条问答](http://stackoverflow.com/questions/348170/undo-git-add-before-commit/348234#348234)， 获取更多详情。

## 3. 撤销最近一次代码提交

有时候你可能会不小心提交了错误的文件或一开始就遗漏了某些东西。下面这三步操作可以帮助你解决这个问题。

	$ git reset --soft HEAD~1
	# 对工作文件进行必要的更改
	$ git add -A .
	$ git commit -c ORIG_HEAD

你执行第一个命令时，Git会将`HEAD`指针（pointer）后移到此前的一次提交，之后你才能移动文件或作必要的修改。

然后你就可以添加所有的修改，而且当你执行最后的命令时，Git会打开你的默认文本编辑器，其中会包含上一次提交时的信息。如果愿意的话，你可以修改提交信息，或者你也可以在最后的命令中使用`-C`而不是`-c`，来跳过这一步。


![Git + spaghetti = spagitty](https://cdn-images-1.medium.com/max/1200/1*eiuAyfDRLIr6ZKutQWbJZQ.gif)

## 4. Git仓库撤销至前一次提交时的状态

“撤销”（revert）在许多情况下是非常有必要的——尤其是你把代码搞的一团糟的情况下。最常见的情况是，你想回到之前代码版本，检查下那个时候的代码库，然后再回到现在状态。这可以通过下面的命令实现：

	$ git checkout <SHA>

“<SHA>”是你想查看的提交拥有的哈希值（Hash Code）中前8至10个字符。 
这个命令会使`<HEAD>`指针脱离（detach），可以让你在不检出（check out）任何分支的情况下查看代码——脱离HEAD并不像听上去那么可怕。如果你想在这种情况下提交修改，你可以通过创建新的分支来实现：

	$ git checkout -b <SHA>

要想回到当前的工作进度，只需要检出（check out）你之前所在的分支即可。

你可以关注[Stack Overflow网站上的这条问答](http://stackoverflow.com/questions/4114095/revert-git-repo-to-a-previous-commit/4114122#4114122)， 获取更多详情。

## 5. 撤销合并（Merge）

要想撤销合并，你可能必须要使用恢复命令（HARD RESET）回到上一次提交的状态。“合并”所做的工作基本上就是重置索引，更新working tree（工作树）中的不同文件，即当前提交（<commit>）代码中与`HEAD`游标所指向代码之间的不同文件；但是合并会保留索引与working tree之间的差异部分（例如那些没有被追踪的修改）。

	$ git checkout -b <SHA>

当然，Git中总是有其他的实现办法，你可以查看看[这篇文章](http://stackoverflow.com/questions/2389361/undo-a-git-merge?rq=1)继续了解。

## 6. 从当前Git分支移除未追踪的本地文件

假设你凑巧有一些未被追踪的文件（因为不再需要它们），不想每次使用`git status`命令时让它们显示出来。下面是解决这个问题的一些方法：

	$ git clean -f -n         # 1
	$ git clean -f            # 2
	$ git clean -fd           # 3
	$ git clean -fX           # 4
	$ git clean -fx           # 5

- (1): 选项-n将显示执行（2）时将会移除哪些文件。
- (2): 该命令会移除所有命令（1）中显示的文件。
- (3): 如果你还想移除文件件，请使用选项-d。
- (4): 如果你只想移除已被忽略的文件，请使用选项-X。
- (5): 如果你想移除已被忽略和未被忽略的文件，请使用选项-x。

请注意最后两个命令中X的区别。

更多详情，请查看官方文档中关于[git-clean的介绍](http://git-scm.com/docs/git-clean)。

![Photo credit: xkcd](https://cdn-images-1.medium.com/max/800/1*bLtPTIsKUeAQHPo2eGrKpw.png)

## 7. 删除本地和远程Git分支

删除本地分支：

	$ git branch --delete --force <branchName>

# 或者使用选项-D作为简写：

	$ git branch -D

删除远程分支：

	$ git push origin --delete <branchName>


建议：要想更好地掌握Git的用法，请仔细阅读Git官方文档。
