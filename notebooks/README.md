# Overview
本チュートリアルでは、アスペクトベース評価分析のデータセットを用いて、評価分析を行います。はじめに、データセットを探索した後、ベースラインとなるモデルを作成します。

## What you need
本チュートリアルには以下の知識が必要です。
* 基礎的なPythonの構文
* 基礎的なLinuxコマンド

Pythonに関する基礎知識がない場合は、はじめに以下のチュートリアルを行うことをおすすめします。
* [icoxfog417/python_exercises](https://github.com/icoxfog417/python_exercises)

## What you learn
本チュートリアルでは、アスペクトベース評価分析のデータセットを用いて、以下の内容を学ぶことができます。
* Pythonとscikit-learnを用いた評価分析の方法


# Setup

* Gitリポジトリのクローン
* 仮想環境の構築
* 依存ライブラリのインストール

## Gitリポジトリのクローン

本チュートリアルで用いるコードは以下のGitリポジトリに含まれています。リポジトリをクローンし、ディレクトリを移動してください。そこで、以下の環境構築を行なっていきます。

```bash
$ git clone https://github.com/tech-sketch/tis-internship-2018.git
$ cd tis-internship-2018
```

## 仮想環境の構築

まずは、`virtualenv`を用いて仮想環境を構築しましょう。仮想環境を構築することで、プロジェクトごとにPythonのバージョンを変えたり、必要なパッケージを分けてインストールすることができます。

```bash
$ virtualenv venv --python=python3
$ source venv/bin/activate
```

virtualenvがインストールされていない場合は、以下のコマンドを実行してインストールしましょう。
```bash
$ pip install virtualenv
```


## 依存ライブラリのインストール

まず、本チュートリアルに必要なライブラリをインストールします。具体的には以下の4つのライブラリをインストールします。

* numpy ―― 数値計算を効率的に行うための機能を提供するライブラリ
* scipy ―― 科学技術計算を行うための機能を提供するライブラリ
* scikit-learn ―― オープンソースの機械学習ライブラリ
* Janome ―― 形態素解析器
* pandas -- データ分析用の機能を提供するライブラリ
* seaborn -- データ可視化用ライブラリ
* Jupyter Notebook -- データ分析をインタラクティブに進めるためのツール 

上記のライブラリは、以下のコマンドを実行することでインストールできます。

```bash
$ pip install numpy scipy scikit-learn janome pandas seaborn jupyter
```

インストールが完了したら、ライブラリが読み込めるかテストしましょう。Pythonインタプリタを起動し、4つのライブラリをインポートしてみてください。

```bash
$ python
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import janome
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
>>> import seaborn
```

# データセットのダウンロード

学習を始める前に、モデルの学習やテストに使うためのデータセットをダウンロードします。以下のコマンドを実行して、アスペクトベース評価分析のデータセットをダウンロードします。

```bash
$ wget https://storage.googleapis.com/chakki/datasets/public/chABSA/chABSA-dataset.zip
$ unzip chABSA-dataset.zip -d data
$ rm chABSA-dataset.zip
```

これで、アスペクトベース評価分析のデータセットをローカル環境に用意できました。以下のコマンドを実行して、データセットが存在するか確認してみましょう。

```bash
$ ls data/chABSA-dataset
```

コマンドを実行すると、以下のようにファイル名が表示されます。

```bash
e00008_ann.json
e00024_ann.json
e00030_ann.json
e00034_ann.json
...
```

# データセットの探索とベンチマークの作成

ここでは以下のタスクを進めていきます。
* データセットの探索
* 学習/検証/テスト用データセットの作成
* ベンチマークの作成と性能評価

`notebooks/`ディレクトリに移動し。`tutorial.ipynb`を開いてください。

```bash
$ cd notebooks
$ jupyter notebook
```

# Next steps

以上でチュートリアルは完了です。おつかれさまでした！
これで評価分析の世界へ一歩踏み出しました。

今回、学習に用いたscikit-learnについてより深く知りたい場合は[scikit-learnのWebサイト](http://scikit-learn.org/stable/)や[GitHubリポジトリ](https://github.com/scikit-learn/scikit-learn)を見るとよいでしょう。そこには、チュートリアルやデータセットといったscikit-learnに関する様々なリソースがあります。

また、もし深層学習に興味があれば、[TensorFlow](https://www.tensorflow.org/)や[Keras](https://keras.io/)といった深層学習用の機能を提供しているライブラリを使って、評価分析をすることもできます。ぜひチャレンジしてみてください。
