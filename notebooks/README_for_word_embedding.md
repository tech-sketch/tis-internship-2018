# 有価証券報告書を使った単語分散表現の計算
まずは以下からコーパスをダウンロードします。
* [annual_report_corpus.zip](https://storage.googleapis.com/chakki/datasets/public/annual_report_corpus.zip)

```bash
$ wget https://storage.googleapis.com/chakki/datasets/public/annual_report_corpus.zip
$ unzip unzip annual_report_corpus.zip
```

ダウンロードが終わったらスクリプトを実行します。

```bash
$ python word_embeddings.py annual_report_corpus model.bin
```

学習が始まるので10分ほど待ちましょう。