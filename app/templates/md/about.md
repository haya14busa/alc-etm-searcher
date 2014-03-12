このサイトについて
==================

このサイトは[スペースアルク](http://www.alc.co.jp/)の[語源辞典](http://home.alc.co.jp/db/owa/etm_sch)の検索機能を拡張し、より柔軟に使えるようにした**非公式**サイトです。


語源辞典自体のデータの著作権は一切保持せず、辞書データは監修者の[松澤喜好](http://www.alc.co.jp/lec-profile/matsuzawa/)氏に帰属しており、このサイトからはリンクを生成、またはリダイレクトするだけとなっております。


このサイトはより快適に語源辞典を使用できるように拡張し、もっとたくさんの学習者が語源について興味を持ち、簡単に勉強できるようにすることを目指しています。


検索機能の拡張について
----------------------

Link: [アルク語源辞典Searcher](http://alc-etm-searcher.herokuapp.com/)

[語源辞典：スペースアルク](http://home.alc.co.jp/db/owa/etm_sch)の検索機能はおそらく前方一致検索しか実装されておらずあいまい検索や、サジェスト機能を持っていません。

例えば`polish`には正しくマッチしますが、`polished`,`polishing`など本来ならマッチしたほうがより便利な検索語でもマッチせず、「もしかして: polish」などと言ったサジェスト機能もありません。


そこでこのサイトではその機能を改善し`polish`,`polished`,`polishing`などはすべて`polish`にマッチするように実装し、同語幹、同語源の検索ワードには貪欲にマッチするようになっています。

(よってまれに全く関係ない単語のページに飛んでしまう場合がありますがご了承ください。)


ブックマークレット
------------------

ブックマークレットによってわざわざ当サイトにアクセスせずとも、手軽に検索機能を使うことができるようになります。

<a href="javascript:(function(){var text=encodeURIComponent(window.getSelection());text=(!text)?encodeURIComponent(window.prompt('アルク語源辞典Searcher')):text;if(text=='null'||text=='')return;URL='http://alc-etm-searcher.herokuapp.com/send_word?search_word='+text;window.open(URL,'_blank');})();">アルク語源辞典SearcherBookMarklet</a>

上記リンクをブックマークバーにドラッグ&ドロップして登録してください。

またはこの<a href="http://alc-etm-searcher.herokuapp.com/about?javascript:(function(){var text=encodeURIComponent(window.getSelection());text=(!text)?encodeURIComponent(window.prompt('アルク語源辞典Searcher')):text;if(text=='null'||text=='')return;URL='http://alc-etm-searcher.herokuapp.com/send_word?search_word='+text;window.open(URL,'_blank');})();">リンク</a>にアクセスし(ページは変わりません)、ブックマークに登録したあと、URL内の`?javascript:`の`?`以前を削除してください。

### 使い方
ブックマークにおいておけば、他のサイトでも好きなときにクリックすることで検索プロンプトが開き、当サイトのアルク語源辞典Searcherを利用することが出来ます。また、事前に調べたい単語を選択した状態でクリックすると、その単語を検索語として検索を実行します。


一括テキストリンカー
--------------------

Link: [アルク語源辞典テキストリンカー](http://alc-etm-searcher.herokuapp.com/text_linker)

また、当サイトではテキストからの一括検索機能を提供しています。

上記URLのテキストエリアに任意の長さのテキストを入力し、`Generate`ボタンを押すと、[語源辞典](http://home.alc.co.jp/db/owa/etm_sch)にマッチするワードだけ語源辞典のページへリンクしたHTMLのテキストを吐き出します。

### 例
テキストエリアに文章を入力し...

![text_linker_before]({{ url_for('static', filename='images/text_linker_before.png') }})

`Generate`ボタンを押すと語源辞典へリンクされたテキストが表示されます

![text_linker_after]({{ url_for('static', filename='images/text_linker_after.png') }})

### 何が便利なの?

[語源辞典：スペースアルク](http://home.alc.co.jp/db/owa/etm_sch)の語源辞典のデータはすべての単語を網羅しているわけではなく、語源があるはずなのにマッチしないということが多々あり、毎回検索を試してはマッチせず落胆するということがあります。

そこで当サイトの[アルク語源辞典テキストリンカー](http://alc-etm-searcher.herokuapp.com/text_linker)を利用して学習したい英文を入力すれば、予め一括で語源辞典のデータベースにマッチする単語だけをリンクすることができ、辞書を引く時間を大幅に時間を短縮しながら学習することが出来ます。


View on GitHub
--------------

当サイトが使用しているコードは[GitHub](https://github.com/)に上がっています。

Fork me on GitHub!: [haya14busa/alc-etm-searcher](https://github.com/haya14busa/alc-etm-searcher)


Author
------

haya14busa

- Github: [haya14busa](https://github.com/haya14busa)
- Twitter: [haya14busa](https://twitter.com/haya14busa)
- Blog: [haya14busa « haya14busa's memo](http://haya14busa.com/)
