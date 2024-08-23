import os
import shutil

#下記の情報は.envなどを使用して管理することをお勧めします
move_from = "YOUR_PATH" #読み取りたいディレクトリのpath
MOVE_TO = "YOUR_PATH" #書き込みたいところのディレクトpath

# 仕分けした後のディレクトリの作成
os.makedirs(MOVE_TO, exist_ok=True)  # Trueを実装することで既存のディレクトリが存在してもエラーが出ないようにした

# 読み込みたい拡張子をリストに入れる　拡張子を追加したい場合以下のリストに拡張子を追加する
file_extensions = ["txt", "zip", "html", "scc", "jpg", "png", "pdf", "mp3", "mp4", "js", "docx", "xlsx", "pptx", "java", "csv", "cp", "cs"]

# 読み取りたいディレクトリパスを入れる
read_path = MOVE_FROM
read_files = os.listdir(read_path)

# 拡張子リストを取得する
for file_extension in file_extensions:
    file_list = []  # 一回リストの中を空にする
    for file_name in read_files:
        # 指定の拡張子のファイルをリストに追加
        if file_name.endswith(file_extension):
            file_list.append(file_name)
    
    # もしリストの中が０じゃないときファイルを作る
    if len(file_list) != 0:
        # 拡張子ごとにフォルダを作る
        os.makedirs(os.path.join(MOVE_TO, file_extension), exist_ok=True)
    
    # read_listから、指定の拡張子のファイルだけ指定のディレクトリに移動する
    for file_name in file_list:
        move_from = os.path.join(read_path, file_name)
        move_to = os.path.join(MOVE_TO, file_extension, file_name)
        # shutil.move("移動させたいフォルダーのパス, 移動場所のパス")
        shutil.move(move_from, move_to) 