# 素数神経衰弱

素数大富豪は、複数人で遊べるトランプゲームです。今回は2人対戦のみです。

## 使い方

python3でデフォルトで使えるモジュールのみを使っていますので、python3の使える環境で起動できると思います。

  ※tkinterのバージョンによっては多少配置等が変わってしまう場合があります。
- Pyhon3のインストール及び実行について: https://www.python.jp/install/windows/install_py3.html

## ルール

通常の神経衰弱と同じように52枚のカードをすべて裏側にして並べます。
ターンプレイヤーは1枚以上のカードを順番にめくり、数字を作ります。
  (例: 1枚目が「１」、2枚目が「7」、3枚目が「2」、4枚目が「9」の場合は「1729」となります)
その数字が素数の場合、使用したカードをすべてターンプレイヤーの持ち札とします。素数ではない場合そのまま裏側に戻します。
素数、素数ではない問わず、ターンは次のプレイヤーに移ります。
場に1枚で素数のカード(2,3,5,7,11,13)がなくなった場合、ゲームを終了します。
１番多くカードを持っているプレイヤーの勝ちです。

jokerを加える、終了条件や勝利条件の変更等、改善案はたくさんあると思います。

## 結び

トランプ画像として無料素材クラブ様(http://sozai.7gates.net)
の画像を使用させていただきました。

作成者　松石大輝




