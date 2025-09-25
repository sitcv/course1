# Git Practice

このディレクトリは、Gitの基本的なコマンドを練習するためのものです。
以下の手順に従って、Gitの操作を学んでいきましょう。

## 1. 最初のコミット

1.  `story.txt`という名前のファイルがこのディレクトリにあります。
2.  `git status`コマンドを実行して、現在のリポジトリの状態を確認してください。`story.txt`が "untracked files" として表示されるはずです。
3.  `git add story.txt`コマンドを実行して、`story.txt`をステージングエリアに追加してください。
4.  再度`git status`を実行し、状態が "changes to be committed" に変わったことを確認してください。
5.  `git commit -m "Add initial story file"`コマンドを実行して、最初のコミットを作成してください。

## 2. ファイルの変更とコミット

1.  `story.txt`を開き、好きな物語の冒頭を数行書き加えて保存してください。
2.  `git status`を実行して、`story.txt`が "modified" と表示されることを確認してください。
3.  `git diff`コマンドを実行して、前回のコミットからどのような変更があったかを確認してください。
4.  `git add story.txt`と`git commit -m "Continue the story"`を実行して、変更をコミットしてください。

## 3. ブランチの作成とマージ

1.  `git branch`コマンドを実行して、現在のブランチ一覧を確認してください。（`* main` または `* master` と表示されるはずです）
2.  `git checkout -b new-feature`コマンドを実行して、`new-feature`という名前の新しいブランチを作成し、そのブランチに切り替えてください。
3.  `story.txt`に物語の続きを書き加えてください。
4.  変更をコミットしてください。（例: `git commit -am "Add a new character"`）
5.  `git checkout main`（または`master`）コマンドで、メインブランチに戻ってください。
6.  `git merge new-feature`コマンドを実行して、`new-feature`ブランチの変更をメインブランチに取り込んでください。
7.  `story.txt`を開き、変更が正しく取り込まれていることを確認してください。

## 4. コンフリクトの解決（応用）

1.  `main`ブランチ（または`master`）で`story.txt`の特定の行を編集し、コミットしてください。
2.  `git checkout -b another-change`で新しいブランチを作成します。
3.  `another-change`ブランチで、**同じ行**を別の内容に編集し、コミットしてください。
4.  `git checkout main`（または`master`）でメインブランチに戻ります。
5.  `git merge another-change`を実行すると、マージコンフリクトが発生します。
6.  `story.txt`を開き、コンフリクトマーカー（`<<<<<<<`, `=======`, `>>>>>>>`）を手動で編集してコンフリクトを解決してください。
7.  `git add story.txt`と`git commit`を実行して、マージコミットを作成してください。

これで基本的なGitの練習は完了です。
