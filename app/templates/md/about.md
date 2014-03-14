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

<div class="white-box">
<h4>生成されたリンク済みの実際のテキスト</h4>
<p>クリックして試してみてください</p>
<hr>
<p><a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4780&amp;stg=2">Permission</a> is hereby <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1616&amp;stg=2">granted</a> , free of <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1049&amp;stg=2">charge</a> , to any <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=7527&amp;stg=2">person</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8200&amp;stg=2">obtaining</a> a copy<br>of this software and <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=7453&amp;stg=2">associated</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=2080&amp;stg=2">documentation</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=2648&amp;stg=2">files</a> ( the " Software "), to deal<br>in the Software without <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=7924&amp;stg=2">restriction</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1474&amp;stg=2">including</a> without <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4079&amp;stg=2">limitation</a> the <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6750&amp;stg=2">rights</a><br>to <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8709&amp;stg=2">use</a> , copy , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4825&amp;stg=2">modify</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4612&amp;stg=2">merge</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6215&amp;stg=2">publish</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8555&amp;stg=2">distribute</a> , sublicense , and / or sell<br>copies of the Software , and to <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4778&amp;stg=2">permit</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=7527&amp;stg=2">persons</a> to whom the Software is<br>furnished to do so , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=3697&amp;stg=2">subject</a> to the following <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=2013&amp;stg=2">conditions</a> :<br><br>The above copyright <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=5205&amp;stg=2">notice</a> and this <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4780&amp;stg=2">permission</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=5205&amp;stg=2">notice</a> shall be <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1473&amp;stg=2">included</a> in<br>all copies or <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=7838&amp;stg=2">substantial</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=5547&amp;stg=2">portions</a> of the Software .<br><br>THE SOFTWARE IS <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=9120&amp;stg=2">PROVIDED</a> " AS IS ", WITHOUT WARRANTY OF ANY KIND , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6365&amp;stg=2">EXPRESS</a> OR<br><a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6010&amp;stg=2">IMPLIED</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1474&amp;stg=2">INCLUDING</a> BUT NOT <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4081&amp;stg=2">LIMITED</a> TO THE WARRANTIES OF <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4591&amp;stg=2">MERCHANTABILITY</a> ,<br>FITNESS FOR A <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=5532&amp;stg=2">PARTICULAR</a> <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6182&amp;stg=2">PURPOSE</a> AND NONINFRINGEMENT . IN NO <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8881&amp;stg=2">EVENT</a> SHALL THE<br><a href="http://home.alc.co.jp/db/owa/etm_sch?unum=446&amp;stg=2">AUTHORS</a> OR COPYRIGHT HOLDERS BE <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4056&amp;stg=2">LIABLE</a> FOR ANY <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1401&amp;stg=2">CLAIM</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=1875&amp;stg=2">DAMAGES</a> OR OTHER<br><a href="http://home.alc.co.jp/db/owa/etm_sch?unum=4057&amp;stg=2">LIABILITY</a> , WHETHER IN AN <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=30&amp;stg=2">ACTION</a> OF <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8476&amp;stg=2">CONTRACT</a> , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8446&amp;stg=2">TORT</a> OR OTHERWISE , <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=6773&amp;stg=2">ARISING</a> FROM ,<br>OUT OF OR IN <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=5067&amp;stg=2">CONNECTION</a> WITH THE SOFTWARE OR THE <a href="http://home.alc.co.jp/db/owa/etm_sch?unum=8709&amp;stg=2">USE</a> OR OTHER DEALINGS IN<br>THE SOFTWARE .</p>
</div>

### 何が便利なの?

[語源辞典：スペースアルク](http://home.alc.co.jp/db/owa/etm_sch)の語源辞典のデータはすべての単語を網羅しているわけではなく、検索を試してはマッチせず落胆するということが多々あります。辞書データに存在するかどうかわからないにも関わらず、気になった単語をそれぞれ検索する作業は非常に骨が折れますよね?

この作業を改善するのが当サイトの[アルク語源辞典テキストリンカー](http://alc-etm-searcher.herokuapp.com/text_linker)です。

学習したい英文を入力すれば、予め一括で語源辞典のデータベースにマッチする単語だけをリンクし、辞書を引く時間を大幅に短縮、かつ快適に学習することが出来ます。

他にも、自分では検索しないような単語にも事前にマッチすることによって、思いもよらなかった新たな発見ができるというメリットもあります。


View on GitHub
--------------

当サイトが使用しているコードは[GitHub](https://github.com/)に上がっています。

Fork me on GitHub: [haya14busa/alc-etm-searcher](https://github.com/haya14busa/alc-etm-searcher)


Author
------
<div class="author-card">
  <div class="card-left">
    <img class="icon-image" src="https://0.gravatar.com/avatar/dca89778aa3e6bc49f0e100df1a1a1f0?s=240" alt="haya14busa_icon">
  </div>
  <div class="card-right">
    <div class="name">haya14busa</div>
    <div class="description">V!mm!shment Th!s World!</div>
  </div>
</div><!-- /div.author-card -->

<div class="social-flat">
  <ul>
    <li class="github"><a href="https://github.com/haya14busa">GitHub <span class="bottom-right">@haya14busa</span></a></li>
    <li class="twitter"><a href="https://twitter.com/haya14busa">Twitter <span class="bottom-right">@haya14busa</span></a></li>
    <li class="blog"><a href="http://haya14busa.com/">Blog <span class="bottom-right">http://haya14busa.com/</span></a></li>
  </ul>
</div>
<br>

*Please feel free to contact me!*

