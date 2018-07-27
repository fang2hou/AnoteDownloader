# AnoteDownloader
![](https://img.shields.io/badge/Ritsumei-Anote_Downloader-blue.svg?colorA=990000&colorB=444444&longCache=true&style=flat)  
![](https://img.shields.io/badge/Python-3.3+-blue.svg?longCache=true&style=flat)  ![](https://img.shields.io/badge/Library-requests-green.svg?longCache=true&style=flat)


AnoteDownloader とは、自動的に Anote をダウンロードできるスクリプトだ。  
購入が必要だが、PDF を作って友達にシェアすることができる。

## 実行環境
Python 3.3+  
ちなみに、requests ライブラリがない場合、下記のコマンドでインストールが出来る。  
```python
pip install requests
```

## 使い方
1. 通信監視アプリを用意  
「Thor」と「Surge」のような、パケット監視ツールをインストールすること。  
パソコンのパケット監視ツールを経由してネットワークに接続してもオッケーだ。  
<div align=center><img src="https://cdn.rawgit.com/fang2hou/AnoteDownloader/supportfiles/pic1.png"/></div>

1. パケットにあるデータを獲得  
監視開始後、普通に Anote アプリを利用して本を開くこと。  
ダウンロードに必要なファイルは `https://app.anote.jp/api/v3/pageListServlet` からの応答データで、`json` で保存する。  
<div align=center><img src="https://cdn.rawgit.com/fang2hou/AnoteDownloader/supportfiles/pic2.png"/></div>

1. 実行  
```bash
python Download.py respose.json
```

## License
MIT