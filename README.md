# Step Analyzer

fabnavi で撮影された工程ごとに解析を行う API Server

## Environment

- Linux
- Python 3.6.5
- OpenCV 3.4.0
- Darknet + Yolo v3
- sox
- ffmpeg

このファイル全体を `${PATH}/darknet/python` 以下にコピーして使用する必要がある．darknet を python で使うスクリプトがそこにあるため．
[この辺り](https://github.com/pjreddie/darknet/blob/61c9d02ec461e30d55762ec7669d6a1d3c356fb2/python/darknet.py#L151) を自分で学習させた config データに書き換える．

## Run

必要なもの install して `python index.py` して終わり．

## Scripts

### `index.py`

中心となるファイル．API の定義とか書いてある．以下 API 一覧

- `/analyze` ... 本番で使う API URL．param と response は以下
  - Param: `movie_url`(String) ... 解析したい工程の動画 URL
  - Response(JSON):
    - transcription ... 音声解析の結果
    - detection ... 物体検出の結果
- `/analyze/narration` ... テスト用 API URL．音声解析結果のみ return する．
  - Param: `movie_url`(String) ... 解析したい工程の動画 URL
  - Response(JSON):
    - transcript_result ... 音声解析の結果
- `/analyze/detection` ... テスト用の API URL．物体検出結果のみ return する．
  - Param: `movie_url`(String) ... 解析したい工程の動画 URL
  - Response(JSON):
    - detection ... 物体検出の結果

ポートは 5000 で起動

### `Downloader.py`

url から動画をダウンロードする．ダウンロートした動画は `/download/movie` に保存される

### ナレーション解析を行うスクリプト

`ExtractAudio.py`, `UploadStorage.py`, `AudioToText.py`, `Analyzer.py` の 4 つを使って解析する．

- `ExtractAudio.py`: 動画から  音声を mp3 で分離，flac に変換
- `UploadStorage.py`: 分離した音声を Google Cloud Storage にアップロード
- `AudioToText.py`: Cloud Storage URL を Google Cloud Speech Text API に request する
- `Analyzer.py`: 文字起こしの結果を形態素解析する

#### Response

編集中...

### [WIP]: 物体検出を行うスクリプト

`ExtractImage.py`, `BackgroundSubstraction.py`, `darknet.py`, `SanitizedResult.py` の 4 つを使って解析する．

- `ExtractImage.py`: 動画の 1 フレーム目を抽出する．
- `BackgroundSubstraction.py`: OpenCV を使って `default.jpg` をベースに背景差分を抽出する
- `darknet.py`: Yolo で物体検出
- `SanitizedResult.py`: 背景差分の結果と Yolo の結果を合わせて綺麗にする

#### Response

編集中...
