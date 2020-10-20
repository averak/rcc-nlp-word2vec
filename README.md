# Word2Vec

[![Twitter](https://img.shields.io/badge/Twitter-競馬AI班-blue?style=flat-square&logo=twitter)](https://twitter.com/search?q=%23rcc_nlp)

RCC 2020 年度プロジェクト活動

自然言語処理班

## 概要

単語の分散表現をWord2Vecを用いて体験します。

[学習済みモデル](https://drive.google.com/u/0/uc?id=14hrIPCaE9HhYfrKPOk9oSNDtTZHze1-V&export=download)を使って，サンプルコードを動かしてみましょう。

## 実行環境

- OS：問わない
- Python ~> 3.8

## インストールと学習

### データの準備

[学習済みモデル](https://drive.google.com/u/0/uc?id=14hrIPCaE9HhYfrKPOk9oSNDtTZHze1-V&export=download)をダウンロードし，展開する。

### インストール

```sh
$ git clone <this repo>
$ cd <this repo>

$ pip install -U pip
$ pip install -r requirements.txt
```

### デモ

```python
$ python
>>> import gensim
>>> model = gensim.models.KeyedVectors.load_word2vec_format('jawiki.word_vectors.100d.txt')
>>>
>>> model['日本'] # ベクトルを取り出す
[ 5.30889511e-01 -2.57213235e-01 -1.59220584e-02 -4.43872392e-01
>>> model.most_similar('日本') # 類似した単語を取り出す
[('日本国内', 0.72707200050354), ('アジア', 0.7265250086784363), ('海外', 0.7229053974151611)
```

他にも，単語の加減算を行う方法もありますので，興味があれば調べてみてください。

> 例: 父親 - 男性 + 女性 = 母親
