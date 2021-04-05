---
layout: post
title:  "word_frequecy를 활용한 영단어 분리기 toy project"
subtitle:   "word_frequecy를 활용한 영단어 분리기 toy project"
categories: Project
tags: etc
comments: true
---

약 6개월 전에, 3일 동안 간단하게 만든 영어 단어 분리기입니다.

함수에 넣으면 최적의 경우의 수를 찾아서 영어 단어를 분리해주는 방식으로

애초에는 주어진 데이터로 정확도를 산출하는 것이었지만, 데이터가 비공개 이므로 예시로만 보여드리고

하도 블로그에 내용을 안 올린 것 같아서 깃허브와 캐글에 업로드 하는 김에

여기에도 업로드를 진행합니다.



<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="0-.-kaggle,-github-&#44172;&#49884;-&#47553;&#53356;">0 . kaggle, github &#44172;&#49884; &#47553;&#53356;<a class="anchor-link" href="#0-.-kaggle,-github-&#44172;&#49884;-&#47553;&#53356;">&#182;</a></h1><p>kaggle : <a href="https://www.kaggle.com/bluemumin/word-frequency-with-hashtag-split">https://www.kaggle.com/bluemumin/word-frequency-with-hashtag-split</a></p>
<p>github : <a href="https://github.com/bluemumin/word_frequency_with_hashtag_split">https://github.com/bluemumin/word_frequency_with_hashtag_split</a></p>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="1.-&#49324;&#51204;-&#49444;&#47749;-&#48143;-&#54056;&#53412;&#51648;-import">1. &#49324;&#51204; &#49444;&#47749; &#48143; &#54056;&#53412;&#51648; import<a class="anchor-link" href="#1.-&#49324;&#51204;-&#49444;&#47749;-&#48143;-&#54056;&#53412;&#51648;-import">&#182;</a></h1><p>해당 notebook의 경우, 복합적인 영어 단어를 단순한 단어로 분리를 시키는 과제에 대한 풀이입니다.</p>
<p>데이터는 비공개이기 때문에, 예시의 단어들로만 결과를 보여드리며,</p>
<p>실제 데이터를 가지고 한 결과에서는 해당 알고리즘만 가지고는 500개의 단어를 가지고</p>
<p>약 97%의 정확도를 가졌었습니다.</p>
<p>현재는 노트북에서 함수로만 실행이 가능하지만, 나중에는 class로 구현하여서</p>
<p>간편하게 불러오고, cmd 창에서 바로 실행이 가능하도록 알고리즘을 구현하는 것을 생각은 하고 있습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span> <span class="c1"># 데이터 전처리</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> <span class="c1"># 데이터 전처리</span>
<span class="kn">import</span> <span class="nn">random</span> <span class="c1">#데이터 전처리</span>

<span class="kn">from</span> <span class="nn">pandas</span> <span class="kn">import</span> <span class="n">DataFrame</span> <span class="c1">#데이터 전처리</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span> <span class="c1">#데이터 전처리</span>

<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">nltk</span>
<span class="n">nltk</span><span class="o">.</span><span class="n">download</span><span class="p">(</span><span class="s1">&#39;words&#39;</span><span class="p">)</span>
<span class="kn">from</span> <span class="nn">nltk.corpus</span> <span class="kn">import</span> <span class="n">words</span><span class="p">,</span> <span class="n">brown</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>[nltk_data] Downloading package words to
[nltk_data]     C:\Users\user\AppData\Roaming\nltk_data...
[nltk_data]   Package words is already up-to-date!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="2.-&#54645;&#49900;-&#50508;&#44256;&#47532;&#51608;">2. &#54645;&#49900; &#50508;&#44256;&#47532;&#51608;<a class="anchor-link" href="#2.-&#54645;&#49900;-&#50508;&#44256;&#47532;&#51608;">&#182;</a></h1><p>인터넷에서 찾은 hashtag splitter의 함수입니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">word_dictionary</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">words</span><span class="o">.</span><span class="n">words</span><span class="p">()))</span>
<span class="k">for</span> <span class="n">alphabet</span> <span class="ow">in</span> <span class="s2">&quot;bcdefghjklmnopqrstuvwxyz&quot;</span><span class="p">:</span>
    <span class="n">word_dictionary</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">alphabet</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">hashtag</span><span class="p">):</span>
    <span class="n">all_possibilities</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">split_posibility</span> <span class="o">=</span> <span class="p">[</span><span class="n">hashtag</span><span class="p">[:</span><span class="n">i</span><span class="p">]</span> <span class="ow">in</span> <span class="n">word_dictionary</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">hashtag</span><span class="p">)</span><span class="o">+</span><span class="mi">1</span><span class="p">))]</span>
    <span class="n">possible_split_positions</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">split_posibility</span><span class="p">)</span> <span class="k">if</span> <span class="n">x</span> <span class="o">==</span> <span class="kc">True</span><span class="p">]</span>

    <span class="k">for</span> <span class="n">split_pos</span> <span class="ow">in</span> <span class="n">possible_split_positions</span><span class="p">:</span>
        <span class="n">split_words</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">word_1</span><span class="p">,</span> <span class="n">word_2</span> <span class="o">=</span> <span class="n">hashtag</span><span class="p">[:</span><span class="nb">len</span><span class="p">(</span><span class="n">hashtag</span><span class="p">)</span><span class="o">-</span><span class="n">split_pos</span><span class="p">],</span> <span class="n">hashtag</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">hashtag</span><span class="p">)</span><span class="o">-</span><span class="n">split_pos</span><span class="p">:]</span>

        <span class="k">if</span> <span class="n">word_2</span> <span class="ow">in</span> <span class="n">word_dictionary</span><span class="p">:</span>
            <span class="n">split_words</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">word_1</span><span class="p">)</span>
            <span class="n">split_words</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">word_2</span><span class="p">)</span>
            <span class="n">all_possibilities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">split_words</span><span class="p">)</span>

            <span class="n">another_round</span> <span class="o">=</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">word_2</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">another_round</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">all_possibilities</span> <span class="o">=</span> <span class="n">all_possibilities</span> <span class="o">+</span> <span class="p">[[</span><span class="n">a1</span><span class="p">]</span> <span class="o">+</span> <span class="n">a2</span> <span class="k">for</span> <span class="n">a1</span><span class="p">,</span> <span class="n">a2</span><span class="p">,</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">([</span><span class="n">word_1</span><span class="p">]</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">another_round</span><span class="p">),</span> <span class="n">another_round</span><span class="p">)]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">another_round</span> <span class="o">=</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">word_2</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">another_round</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">all_possibilities</span> <span class="o">=</span> <span class="n">all_possibilities</span> <span class="o">+</span> <span class="p">[[</span><span class="n">a1</span><span class="p">]</span> <span class="o">+</span> <span class="n">a2</span> <span class="k">for</span> <span class="n">a1</span><span class="p">,</span> <span class="n">a2</span><span class="p">,</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">([</span><span class="n">word_1</span><span class="p">]</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">another_round</span><span class="p">),</span> <span class="n">another_round</span><span class="p">)]</span>
                
    <span class="k">return</span> <span class="n">all_possibilities</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="3.-&#45800;&#50612;-&#54056;&#53556;-&#44396;&#48516;">3. &#45800;&#50612; &#54056;&#53556; &#44396;&#48516;<a class="anchor-link" href="#3.-&#45800;&#50612;-&#54056;&#53556;-&#44396;&#48516;">&#182;</a></h1><p>하지만 이를 이대로 사용하기에는 무리 였던 점이,</p>
<p>해당 함수는 모든 경우의 수를 반환해주기 때문에, 매번 사용자가 확인도 해줘야되고 만약에 단어의 갯수가 엄청나게 많다면</p>
<p>이를 제대로 활용하지 못하게 됩니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">print_3</span><span class="p">(</span><span class="n">original</span><span class="p">):</span>
    <span class="n">word_space</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">original</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="o">&lt;=</span><span class="mi">3</span><span class="p">:</span>
            <span class="n">word_space</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">word_space</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>그렇기 때문에, 최적의 경우의 수를 찾는 것을 생각하였고,</p>
<p>가장 좋은 경우는 단어가 최대 3개로 나누어지고, 마지막 글자에 따라서 패턴만 조정하는 방식을 선택하였습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">print_er</span><span class="p">(</span><span class="n">original_word</span><span class="p">):</span>
    <span class="n">word_space2</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">original_word</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">)</span><span class="o">==</span><span class="mi">3</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span><span class="o">&lt;=</span><span class="mi">3</span> <span class="p">):</span>
            <span class="n">temp</span><span class="o">=</span><span class="p">[]</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="n">j</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>
    <span class="n">word_space</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">word_space2</span><span class="p">:</span>
        <span class="k">if</span> <span class="s1">&#39;er&#39;</span> <span class="ow">in</span> <span class="n">i</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">word_space</span><span class="p">)]</span>

<span class="k">def</span> <span class="nf">print_ing</span><span class="p">(</span><span class="n">original_word</span><span class="p">):</span>
    <span class="n">q</span><span class="o">=</span><span class="n">p</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s1">&#39;ing$&#39;</span><span class="p">)</span>
    <span class="n">word_space2</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">original_word</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">)</span><span class="o">==</span><span class="mi">3</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span><span class="o">&lt;=</span><span class="mi">4</span> <span class="p">):</span>
            <span class="n">temp</span><span class="o">=</span><span class="p">[]</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="n">j</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>
        <span class="k">elif</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">)</span><span class="o">==</span><span class="mi">3</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="n">q</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span><span class="o">==</span><span class="p">[</span><span class="s1">&#39;ing&#39;</span><span class="p">]</span> <span class="p">):</span>
            <span class="n">temp</span><span class="o">=</span><span class="p">[]</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">+</span><span class="n">j</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="p">)</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>
    <span class="n">word_space</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">word_space2</span><span class="p">:</span>
        <span class="k">if</span> <span class="s1">&#39;ing&#39;</span> <span class="ow">in</span> <span class="n">i</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">word_space</span><span class="p">)]</span>

<span class="k">def</span> <span class="nf">print_ed</span><span class="p">(</span><span class="n">original_word</span><span class="p">):</span>
    <span class="n">word_space2</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">original_word</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">)</span><span class="o">==</span><span class="mi">3</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span><span class="o">&lt;=</span><span class="mi">3</span> <span class="p">):</span>
            <span class="n">temp</span><span class="o">=</span><span class="p">[]</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span>
            <span class="n">temp</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">j</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="n">j</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">j</span><span class="p">)</span>
    <span class="n">word_space</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">word_space2</span><span class="p">:</span>
        <span class="k">if</span> <span class="s1">&#39;ed&#39;</span> <span class="ow">in</span> <span class="n">i</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">word_space</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">word_space</span><span class="p">)]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>최대 3개만 선택하게 한 이후에는, er, ing, ed로 끝나는 단어에 대한 구분을 추가하였고</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">print_man</span><span class="p">(</span><span class="n">original_word</span><span class="p">):</span>
    <span class="n">raw</span><span class="o">=</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">original_word</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">original_word</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">[</span> <span class="n">raw</span><span class="p">[:</span><span class="o">-</span><span class="mi">3</span><span class="p">],</span><span class="n">raw</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span> <span class="p">]</span>  <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">original_word</span><span class="p">)]</span>

<span class="k">def</span> <span class="nf">print_wm</span><span class="p">(</span><span class="n">original_word</span><span class="p">):</span>
    <span class="n">raw</span><span class="o">=</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">original_word</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">original_word</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">[</span> <span class="n">raw</span><span class="p">[:</span><span class="o">-</span><span class="mi">5</span><span class="p">],</span><span class="n">raw</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:]</span> <span class="p">]</span>  <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="nb">list</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">element</span><span class="p">)</span> <span class="k">for</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">original_word</span><span class="p">)]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>나중에는 man, woman이라는 단어로 끝나는 경우에 대한 구분도 추가하였습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="4.-English-Word-Frequency-&#54876;&#50857;">4. English Word Frequency &#54876;&#50857;<a class="anchor-link" href="#4.-English-Word-Frequency-&#54876;&#50857;">&#182;</a></h1><p>하지만, 그렇게 하더라도 최적의 경우가 나오지 않는 경우가 있었는데</p>
<p>가장 큰 것은 3개의 단어로 구분을 할 경우, 경우의 수가 2가지가 나오는 것이었습니다.</p>
<p>예를들어 blueberrycake라는 단어의 경우,</p>
<p>blue berry cake, blueberry cake로 나뉠 수가 있는데</p>
<p>어떠한 것이 최적의 경우인지 찾는 요소로 <a href="https://www.kaggle.com/rtatman/english-word-frequency">https://www.kaggle.com/rtatman/english-word-frequency</a> 의 단어 빈도 데이터를 활용하였습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">count_v</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;unigram_freq.csv&quot;</span><span class="p">)</span>
<span class="n">count_v</span><span class="p">[</span><span class="s1">&#39;type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="nb">type</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">count_v</span><span class="p">[</span><span class="s1">&#39;word&#39;</span><span class="p">]]</span>
<span class="n">count_v2</span><span class="o">=</span><span class="n">count_v</span><span class="p">[</span><span class="n">count_v</span><span class="p">[</span><span class="s1">&#39;type&#39;</span><span class="p">]</span><span class="o">==</span><span class="nb">str</span><span class="p">]</span>
<span class="n">count_v2</span><span class="p">[</span><span class="s1">&#39;len&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">count_v2</span><span class="p">[</span><span class="s1">&#39;word&#39;</span><span class="p">]]</span>

<span class="n">count_v2</span><span class="o">=</span><span class="n">count_v2</span><span class="p">[</span><span class="n">count_v2</span><span class="p">[</span><span class="s1">&#39;len&#39;</span><span class="p">]</span><span class="o">&gt;=</span><span class="mi">2</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>a, b, c 와 같은 한 글자 단어는 제외하고 사용하며,</p>
<p>to, in, by 등과 같은 전치사, 접속사 등의 단어들은 remove_list를 만들어서 제외하는 방식을 사용하였습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">remove_list</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;to&#39;</span><span class="p">,</span><span class="s1">&#39;in&#39;</span><span class="p">,</span><span class="s1">&#39;by&#39;</span><span class="p">,</span><span class="s1">&#39;go&#39;</span><span class="p">,</span><span class="s1">&#39;of&#39;</span><span class="p">,</span><span class="s1">&#39;in&#39;</span><span class="p">,</span><span class="s1">&#39;on&#39;</span><span class="p">,</span><span class="s1">&#39;as&#39;</span><span class="p">,</span><span class="s1">&#39;the&#39;</span><span class="p">,</span><span class="s1">&#39;and&#39;</span><span class="p">,</span><span class="s1">&#39;up&#39;</span><span class="p">]</span>
<span class="k">def</span> <span class="nf">regulatoin_list</span><span class="p">(</span><span class="n">next_word</span><span class="p">):</span>
    <span class="n">word_space</span><span class="o">=</span><span class="p">[]</span>
    <span class="k">if</span> <span class="n">next_word</span><span class="o">==</span><span class="p">[]:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">next_word</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">list1</span> <span class="ow">in</span> <span class="n">next_word</span><span class="p">:</span>
            <span class="n">word_space2</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">list1</span><span class="p">]</span>
            <span class="k">if</span> <span class="p">(</span><span class="mi">1</span> <span class="ow">in</span> <span class="n">word_space2</span><span class="p">)</span> <span class="p">:</span>  <span class="c1">#길이가 하나라도 1인 경우</span>
                <span class="k">pass</span>
            <span class="k">elif</span> <span class="p">(</span><span class="n">word_space2</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="o">==</span><span class="mi">2</span><span class="p">)</span> <span class="p">:</span>  <span class="c1"># 2개 단어의 길이가 2인 경우는 비정상적이므로 제외</span>
                <span class="k">pass</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">word_space</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">list1</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">word_space</span><span class="p">)</span><span class="o">&gt;=</span><span class="mi">2</span><span class="p">:</span>
            <span class="n">sum_list</span><span class="o">=</span><span class="p">[]</span>
            <span class="n">real_list</span><span class="o">=</span><span class="p">[]</span>
            <span class="k">for</span> <span class="n">splitting</span> <span class="ow">in</span> <span class="n">word_space</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">)</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span>
                    <span class="k">if</span> <span class="p">(</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span><span class="o">==</span><span class="mi">2</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">remove_list</span> <span class="p">)</span> <span class="p">)</span> <span class="o">|</span> <span class="p">(</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span><span class="o">==</span><span class="mi">2</span> <span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">remove_list</span> <span class="p">)</span> <span class="p">)</span> <span class="p">:</span>
                        <span class="k">pass</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">real_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">splitting</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">if</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span><span class="o">==</span><span class="mi">2</span> <span class="p">)</span> <span class="o">|</span> <span class="p">(</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">])</span><span class="o">==</span><span class="mi">2</span> <span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">remove_list</span> <span class="p">)</span> <span class="p">)</span> <span class="o">|</span> <span class="p">(</span> <span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">])</span><span class="o">==</span><span class="mi">2</span> <span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span> <span class="n">splitting</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">remove_list</span> <span class="p">)</span> <span class="p">)</span> <span class="p">:</span>
                        <span class="k">pass</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">real_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">splitting</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">real_list</span><span class="p">:</span>
                <span class="n">sum1</span> <span class="o">=</span> <span class="mi">1</span>
                <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">j</span><span class="p">)):</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">sum1</span> <span class="o">+=</span> <span class="n">count_v</span><span class="p">[</span><span class="n">count_v</span><span class="p">[</span><span class="s1">&#39;word&#39;</span><span class="p">]</span><span class="o">==</span><span class="n">j</span><span class="p">[</span><span class="n">y</span><span class="p">]]</span><span class="o">.</span><span class="n">index</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                    <span class="k">except</span><span class="p">:</span>
                        <span class="n">sum1</span> <span class="o">+=</span> <span class="mi">99999999</span>
                <span class="n">sum_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sum1</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">real_list</span><span class="p">[</span> <span class="n">sum_list</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">sum_list</span><span class="p">))</span> <span class="p">]</span>
            
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">word_space</span><span class="p">)</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">word_space</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>해당 알고리즘의 핵심은, 이미 단어가 분리가 된 상태에서</p>
<p>remove_list에 있는 단어들로는 분리가 되지 않으면서, word_frequecy 데이터의 빈도를 활용하여서</p>
<p>최대한 가장 잘 사용이 되는 단어가 최적의 경우의 수가 되도록 분리를 하는 방식을 사용한 것입니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="5.-word_frequecy-&#50500;&#51060;&#46356;&#50612;-&#51201;&#50857;">5. word_frequecy &#50500;&#51060;&#46356;&#50612; &#51201;&#50857;<a class="anchor-link" href="#5.-word_frequecy-&#50500;&#51060;&#46356;&#50612;-&#51201;&#50857;">&#182;</a></h1><p>해당 함수들을 만든 다음에, 끝에 끝나는 글자들을을 통해서 각각 다른 함수가 적용이 되도록 하였습니다.</p>
<p>중간에 내용을 추가하다보니 불필요하게 if, elif 등으로 반복되는 내용이 들어가긴 했지만</p>
<p>3일안에 해당 알고리즘을 처리를 하여야 됬기 때문에 구현에만 초점을 두었습니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">word_space</span><span class="p">(</span><span class="n">j</span><span class="p">):</span>
    <span class="n">p</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s1">&#39;er$&#39;</span><span class="p">)</span>
    
    <span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">j</span><span class="p">)</span><span class="o">==</span><span class="p">[</span><span class="s1">&#39;er&#39;</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_er</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">j</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span> 
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>

    <span class="k">elif</span> <span class="n">j</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">&quot;ing&quot;</span><span class="p">)</span><span class="o">&gt;</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_ing</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">j</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>

    <span class="k">elif</span> <span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:]</span><span class="o">==</span><span class="s2">&quot;woman&quot;</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_wm</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">j</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>

    <span class="k">elif</span> <span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">:]</span><span class="o">==</span><span class="s2">&quot;man&quot;</span><span class="p">)</span> <span class="o">&amp;</span>  <span class="p">(</span><span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:]</span><span class="o">!=</span><span class="s2">&quot;woman&quot;</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_man</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">j</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>
    <span class="k">elif</span> <span class="n">j</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span><span class="o">==</span><span class="s2">&quot;ed&quot;</span> <span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_ed</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span><span class="n">j</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>
    
    <span class="k">else</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">regulatoin_list</span><span class="p">(</span> <span class="n">print_3</span><span class="p">(</span> <span class="n">split_hashtag_to_words_all_possibilities</span><span class="p">(</span> <span class="n">j</span> <span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">except</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">j</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="6.-&#44208;&#44284;-&#54869;&#51064;">6. &#44208;&#44284; &#54869;&#51064;<a class="anchor-link" href="#6.-&#44208;&#44284;-&#54869;&#51064;">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;snowman&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;longwinded&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;hashtagsplit&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;strawberry&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;strawberrycake&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;blueberrycake&#39;</span><span class="p">)</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;watermelonsugar&#39;</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;watermelonsugarsalt&#39;</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span> <span class="n">word_space</span><span class="p">(</span><span class="s1">&#39;themselves&#39;</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;snow&#39;, &#39;man&#39;]
[&#39;long&#39;, &#39;winded&#39;]
[&#39;hash&#39;, &#39;tag&#39;, &#39;split&#39;]
[&#39;straw&#39;, &#39;berry&#39;]
[&#39;strawberry&#39;, &#39;cake&#39;]
[&#39;blue&#39;, &#39;berry&#39;, &#39;cake&#39;]
[&#39;water&#39;, &#39;melon&#39;, &#39;sugar&#39;]
[&#39;watermelon&#39;, &#39;sugar&#39;, &#39;salt&#39;]
[[]]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>일단 단어가 들어가면 무조건 분리가 일어나도록 진행이 되었으며,</p>
<p>단어 4개 이상으로 분리되는 경우는 어쩔수 없이 최대 3개가 되도록 처리를 하였으며</p>
<p>분리가 불가능한, 즉 아예 경우의 수가 없는 경우에는 빈 값이 나오도록 되어있습니다.</p>
<p>빈 값이 나오게 한 이유는 해당 단어는 직접 처리를 해야됨을 의미하며,</p>
<p>이는 함수 적용시 [[]]가 나오면 원본을 반환하도록 하는 것을 구현하면</p>
<p>간단하게 해결이 가능합니다.</p>

</div>
</div>
</div>