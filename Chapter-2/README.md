# 2章 回帰の評価指標のコード
## データの準備

1. Kaggleのアカウントを持っていない方は、以下のURLでKaggleのアカウントを登録してログインします。
   - https://www.kaggle.com/
2. ログインが完了したら、以下のURLにアクセスします。
   - https://www.kaggle.com/competitions/recruit-restaurant-visitor-forecasting/data
3. 画面上部にある「Download All」ボタンをクリックして、zipファイル（recruit-restaurant-visitor-forecasting.zip）をダウンロードします。
4. ダウンロードしたファイルを解凍します。
   - Windows 10の場合は、エクスプローラーの圧縮フォルダーツールで「全て展開」ボタンをクリックし、展開先のフォルダーを選択して「展開」ボタンをクリックします。
   - macOSの場合は、Finderでzipファイルをダブルクリックします。
5. 解凍して得られたフォルダにある以下のファイルをさらに解凍します。
    - air_reserve.csv.zip
    - air_store_info.csv.zip
    - air_visit_data.csv.zip
    - date_info.csv.zip
6. 最終的に解凍したファイルを以下のような形で配置します。

```
.
├── README.md
├── data
│   ├── air_reserve.csv
│   ├── air_store_info.csv
│   ├── air_visit_data.csv
│   └── date_info.csv
└── notebook
    └── 回帰の評価指標.ipynb
```
