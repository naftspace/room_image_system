## 概要
このディレクトリには設置されたカメラから部室の様子を10分ごとに撮影し，Google Driveにアップロードするプログラムが置いてあります．

## Webカメラを使って写真をとる
今回はサクッとプログラムを書きたかったのでPythonを利用しました．
PythonからはOpenCVのVideoCaptureを使うことで利用できるのですが，使用しているUbuntuではうまく動作しませんでした．OpenCVを再インストールすればできる見込みがあるようですが，面倒なのでfswebcamというコマンドを利用しました．

```Python
import os

def snap_shot(filename):
    cmd = "fswebcam -save ./%s -r 960x720" % (filename)
    os.system(cmd)
```

なおsubprocessを使ったほう徳が高いらしいです．

## GoogleDriveにアップロードする
ローカルの画像をGoogleDriveにアップロードするのはPyDriveを利用した良い記事があるのでそれを参考にしました．

[PythonでGoogleドライブに画像をアップロード - Qiita](https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e)

ファイル名が"room_image.jpg"のファイルを探してきて，それを編集するという形でアップロードするようにしました．

## crontabを使って10分ごとにアップロードするように設定
crontabの設定に以下の一行を書き加えます．

```
*/10 * * * * python3 ~/hogehoge/main.py
```

これでGoogleDriveから写真が見られるようになりました．
