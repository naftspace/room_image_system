from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import logging
import time
import sys

# ref: https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e
# contab: http://x68000.q-e-d.net/~68user/unix/pickup?crontab

def snap_shot(filename):
    cmd = "fswebcam -save ~/Users/Kuroda/gdrive/%s -r 960x720" % (filename)
    os.system(cmd)

def get_file(drive,filename):
    files = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    files = [f for f in files if f["title"] == filename]
    if files == []:
        return None
    else:
        return files[0]


def main():
    # GoogleDriveを扱うオブジェクトを作成
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    # スクショを撮る
    print("Take a picture, cheese!")
    filename = "room_image.jpg"
    snap_shot(filename)
    
    # wait to save the file
    # time.sleep(20)

    # 過去にアップロードしたファイルタグをとってくる
    print("searching old file...")
    f = get_file(drive,filename)

    # ファイルがなければ新規に，あればそれに上書きする
    if f is None:
        print("Old file is not found. To make new file.")
        f = drive.CreateFile()

    # さっき撮った画像に移し替えてアップロード
    print("Uploading file...")
    f.SetContentFile(filename)
    f["title"] = filename
    f.Upload()


if __name__=="__main__":
#    sys.exit(0) 
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    logging.basicConfig(filename='log.txt',level=logging.DEBUG)
    logging.info("executed" + time.ctime())
    main()
    logging.info("end" + time.ctime())



