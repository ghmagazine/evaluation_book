# 3章 二値分類における評価指標のコード
## データの準備

1. Kaggleのアカウントを持っていない方は、以下のURLでKaggleのアカウントを登録してログインします。
   - https://www.kaggle.com/
2. ログインが完了したら、以下のURLにアクセスします。
   - https://www.kaggle.com/arashnic/hr-ana
3. 画面上部にある「Download (5MB)」ボタンをクリックして、zipファイル（archive.zip）をダウンロードします。
4. ダウンロードしたファイルを解凍します。
   - Windows 10の場合は、エクスプローラーの圧縮フォルダーツールで「全て展開」ボタンをクリックし、展開先のフォルダーを選択して「展開」ボタンをクリックします。
   - macOSの場合は、Finderでzipファイルをダブルクリックします。
5. Banking Datasetでも同様の手順で解凍します。
   - https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets
6. 最終的に解凍したファイルを以下のような形で配置します。

```
.
├── README.md
├── data
│   ├── banking_dataset
│   │   ├── test.csv
│   │   └── train.csv
│   ├── test.csv  # hr-anaのtest.csv
│   └── train.csv # hr-anaのtrain.csv
└── notebook
    └── 二値分類における評価指標.ipynb
```
