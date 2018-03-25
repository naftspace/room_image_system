# 部室の監視システムを作ったお話
## 概要
NAFTには部室がありますが，誰かに会うことを期待して部室に行って誰も居ないとちょと寂しい気持ちになります．逆に作業するために部室に行って人が多すぎて困ることもあります．
そこで部室の状態をスマホから確認できるようにするシステムを作りました．

## システム構成
部室に設置されたカメラが10分ごとに部室の様子を撮影し，Google Driveにその画像をアップロードします．
画像を確認する手段として，2種類のUIを構成しました．
- Google Driveの My Driveディレクトリで直接確認する．
- NAFT_viewという専用のLINE botから確認する．

## ディレクトリの説明

<dl>
  <dt>uploading_program</dt>
  <dd>10分ごとに撮影し，Google Driveにアップロードするプログラム</dd>
  <dt>NAFT_viewbot</dt>
  <dd>NAFT_viewのLINE botプログラム</dd>
</dl>

詳細は各ディレクトリのREADME.mdファイルを確認してください．
