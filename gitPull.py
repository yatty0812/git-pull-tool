import os
import glob


def git_pull_app():
    """\
    カレントディレクトリ配下の全プロジェクトに対してgit pullを実行する

    タイトルの通りです
    """

    # 処理ルート
    proc_root_dir = os.path.dirname(os.path.abspath(__file__))

    # 処理ルートディレクトリループ
    directories = glob.glob(f"{proc_root_dir}/*")
    for sv_dir in directories:
        # 自分自身はスルー（先頭のドットはカットする必要あり）
        if os.path.isdir(sv_dir):
            print("-------------------------------")
            print(f"{sv_dir}のGit Pull開始")
            print("-------------------------------")
            # ディレクトリ掘る
            os.chdir(sv_dir)
            # git pull
            os.system(f'git pull')
            # ディレクトリのぼる
            os.chdir("../")

    print("完了！")

if __name__ == '__main__':
    git_pull_app()
