# movie_similarity
文章のリストから最も似ている文章を探すプログラムです。  
以下の３つの方法で実装していますが、機能はほとんど同じです。手法の比較のために作りました。

- Bag Of Words(BOW)
- Doc2Vec
- fastText

## 使い方
- 文章のリストは各自用意のこと
- bag_of_words, doc2vec, fasttextのうち使いたい手法のディレクトリに以下のディレクトリを作成してください
  - `/model` : 学習モデルを入れる用のディレクトリ。モデルは各自用意。ネット上に転がっているもので良い。
  - `/train` : `make_train_csv.py` の実行結果を入れるためのディレクトリ。文章を各手法で扱えるようにmecabで形態素解析したcsvが入ります。
- `make_train_csv.py` を実行して文章リストを単語レベルに分割します。
- `similar_movie_finder.py` を実行して指定した文章と似ている文章を探します。movieと書いてますが、特に気にしないで良いです。

## 解説動画
以下の動画でコードの内容と各手法について解説しています。
- https://www.youtube.com/watch?v=cGLBdmjAq34
- https://www.youtube.com/watch?v=O0iuGjPcdTY
- https://www.youtube.com/watch?v=Lj7LzB6EFJI
- https://www.youtube.com/watch?v=GPe-xlySq-k
- https://www.youtube.com/watch?v=LDItgS9dmbI
- https://www.youtube.com/watch?v=11WobcsWn64
