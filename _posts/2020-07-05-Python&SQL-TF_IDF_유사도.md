---
layout: post
title:  "TF-IDF와 유사도 그리고 상관관계"
subtitle:   "TF-IDF와 유사도 그리고 상관관계"
categories: PS
tags: Python
comments: true
---

#### TF-IDF와 유사도 그리고 상관관계에 대해서 설명을 하기 위한 포스팅입니다.

<br/>

실제 실행된 결과를 ipynb 파일로 보고 싶으시다면 다음 링크로 이동해주시면 됩니다!

<https://github.com/bluemumin/bluemumin.github.io/blob/master/_posts/html/tfidf%20%ED%8F%AC%EC%8A%A4%ED%8C%85%EC%9A%A9.ipynb>

<br/>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="n">action</span><span class="o">=</span><span class="s1">&#39;ignore&#39;</span><span class="p">)</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn.feature_extraction.text</span> <span class="kn">import</span> <span class="n">TfidfVectorizer</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics.pairwise</span> <span class="kn">import</span> <span class="n">linear_kernel</span><span class="p">,</span> <span class="n">cosine_similarity</span>
</pre></div>

    </div>
</div>
</div>

<br/>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="&#44592;&#48376;&#51201;&#51064;-TF-IDF">&#44592;&#48376;&#51201;&#51064; TF-IDF<a class="anchor-link" href="#&#44592;&#48376;&#51201;&#51064;-TF-IDF">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>TF-IDF에 대한 이론적으로 좋은 블로그는 다음과 같다고 생각됩니다.</p>
<p><a href="https://euriion.com/?p=548">https://euriion.com/?p=548</a></p>

<br/>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf</span> <span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list1</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;I like apple and this monitor and this ground&#39;</span><span class="p">,</span> <span class="s1">&#39;I like this ground and this ground is 100m&#39;</span><span class="p">,</span>
        <span class="s1">&#39;I am looking this ground at the monitor&#39;</span><span class="p">,</span> <span class="s1">&#39;I am looking this ground at the television&#39;</span><span class="p">,</span>
        <span class="s1">&#39;pen pineapple apple pen&#39;</span><span class="p">]</span>

<span class="n">tfidf_matrix</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list1</span><span class="p">)</span>
<span class="n">tfidf_matrix</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>

<br/>


<div class="output_text output_subarea output_execute_result">
<pre>&lt;5x34 sparse matrix of type &#39;&lt;class &#39;numpy.float64&#39;&gt;&#39;
	with 56 stored elements in Compressed Sparse Row format&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>5개의 행이 34개의 단어로 이루어져 있으며 0이 아닌 값은 총 56개가 존재한다는 뜻입니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tfidf_matrix</span><span class="o">.</span><span class="n">toarray</span><span class="p">()[</span><span class="mi">0</span><span class="p">],</span> <span class="n">tfidf_matrix</span><span class="o">.</span><span class="n">toarray</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([0.        , 0.        , 0.        , 0.44642293, 0.44642293,
        0.22321146, 0.27666486, 0.        , 0.        , 0.        ,
        0.15586815, 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.22321146, 0.27666486, 0.        , 0.        ,
        0.        , 0.22321146, 0.27666486, 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.31173631, 0.15586815, 0.27666486]),
 (34,))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>첫 번째 행 안에 34개의 단어들이 array 안에서 값이 채워져 있는 모습입니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cosine_sim</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tfidf_matrix</span><span class="p">,</span> <span class="n">tfidf_matrix</span><span class="p">)</span>
<span class="n">cosine_sim</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.46739466, 0.19012271, 0.12296691, 0.0612277 ],
       [0.46739466, 1.        , 0.19869546, 0.19439867, 0.        ],
       [0.19012271, 0.19869546, 1.        , 0.77157306, 0.        ],
       [0.12296691, 0.19439867, 0.77157306, 1.        , 0.        ],
       [0.0612277 , 0.        , 0.        , 0.        , 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>sklearn.metrics.pairwise의 linear_kernel을 통해서 기존에 만들어 놓은 tfidf_matrix를 넣으면 코사인 유사도가 계산됩니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tfidf_matrix</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">c2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        ,  0.20136947, -0.23671414, -0.33755445, -0.21502735],
       [ 0.20136947,  1.        , -0.25287475, -0.25771132, -0.31606925],
       [-0.23671414, -0.25287475,  1.        ,  0.63630574, -0.33344966],
       [-0.33755445, -0.25771132,  0.63630574,  1.        , -0.33205463],
       [-0.21502735, -0.31606925, -0.33344966, -0.33205463,  1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>이 array를 corr를 계산하는 np.corrcoef를 이용해 계산하면 상관관계가 일단은 계산이 됩니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>여기서 유사도와 상관관계에서의 가장 큰 차이점은 음수의 존재 여부입니다.</p>
<p>코사인 유사도의 경우, 결론적으로 빈도의 분포를 활용하기 때문에 일반적인 코사인 유사도의 값인 -1 ~ 1 사이가 아닌 0 ~ 1 사이입니다.</p>

<br/>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="&#44060;&#48324;-&#50696;&#49884;&#50752;-&#54633;&#52432;&#51652;-&#50696;&#49884;&#51032;-&#52264;&#51060;">&#44060;&#48324; &#50696;&#49884;&#50752; &#54633;&#52432;&#51652; &#50696;&#49884;&#51032; &#52264;&#51060;<a class="anchor-link" href="#&#44060;&#48324;-&#50696;&#49884;&#50752;-&#54633;&#52432;&#51652;-&#50696;&#49884;&#51032;-&#52264;&#51060;">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>다음은 하나의 리스트를 이용해 계산한 결과와 각각으로 나누어서 계산한 결과를 통해서</p>
<p>코사인 유사도의 계산과 상관관계의 계산 결과를 살펴보려고 합니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="&#54633;&#52432;&#51652;-&#50696;&#49884;">&#54633;&#52432;&#51652; &#50696;&#49884;<a class="anchor-link" href="#&#54633;&#52432;&#51652;-&#50696;&#49884;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 예시1</span>
<span class="n">tf2</span> <span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list2</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;I like apple and this monitor and this ground&#39;</span><span class="p">,</span> <span class="s1">&#39;I like this ground and this ground is 100m&#39;</span><span class="p">,</span>
        <span class="s1">&#39;I am looking this ground at the monitor&#39;</span><span class="p">,</span> <span class="s1">&#39;I am looking this ground at the television&#39;</span><span class="p">]</span>

<span class="n">tfidf_matrix2</span> <span class="o">=</span> <span class="n">tf2</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list2</span><span class="p">)</span>
<span class="n">tfidf_matrix2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;4x29 sparse matrix of type &#39;&lt;class &#39;numpy.float64&#39;&gt;&#39;
	with 50 stored elements in Compressed Sparse Row format&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cosine_sim2</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tfidf_matrix2</span><span class="p">,</span> <span class="n">tfidf_matrix2</span><span class="p">)</span>
<span class="n">cosine_sim2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.44199978, 0.17531557, 0.10887498],
       [0.44199978, 1.        , 0.17988015, 0.17545666],
       [0.17531557, 0.17988015, 1.        , 0.76198892],
       [0.10887498, 0.17545666, 0.76198892, 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c22</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tfidf_matrix2</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">c22</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[8]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        ,  0.08277906, -0.38357704, -0.49188749],
       [ 0.08277906,  1.        , -0.41825066, -0.42250346],
       [-0.38357704, -0.41825066,  1.        ,  0.58031978],
       [-0.49188749, -0.42250346,  0.58031978,  1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="&#44060;&#48324;-&#50696;&#49884;">&#44060;&#48324; &#50696;&#49884;<a class="anchor-link" href="#&#44060;&#48324;-&#50696;&#49884;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf3</span><span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list3</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;I like apple and this monitor and this ground&#39;</span><span class="p">,</span> <span class="s1">&#39;I like this ground and this ground is 100m&#39;</span><span class="p">]</span>

<span class="n">tfidf_matrix3</span> <span class="o">=</span> <span class="n">tf3</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list3</span><span class="p">)</span>

<span class="n">cosine_sim3</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tfidf_matrix3</span><span class="p">,</span> <span class="n">tfidf_matrix3</span><span class="p">)</span>
<span class="n">cosine_sim3</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[9]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.48413539],
       [0.48413539, 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c3</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tfidf_matrix3</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">c3</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        , -0.38957117],
       [-0.38957117,  1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf4</span><span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list4</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;I like apple and this monitor and this ground&#39;</span><span class="p">,</span> <span class="s1">&#39;I am looking this ground at the monitor&#39;</span><span class="p">]</span>

<span class="n">tfidf_matrix4</span> <span class="o">=</span> <span class="n">tf4</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list4</span><span class="p">)</span>

<span class="n">cosine_sim4</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tfidf_matrix4</span><span class="p">,</span> <span class="n">tfidf_matrix4</span><span class="p">)</span>
<span class="n">cosine_sim4</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[11]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.18200376],
       [0.18200376, 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c4</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tfidf_matrix4</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">c4</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        , -0.82809385],
       [-0.82809385,  1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf5</span><span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list5</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;I like apple and this monitor and this ground&#39;</span><span class="p">,</span> <span class="s1">&#39;I am looking this ground at the television&#39;</span><span class="p">]</span>

<span class="n">tfidf_matrix5</span> <span class="o">=</span> <span class="n">tf5</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list5</span><span class="p">)</span>

<span class="n">cosine_sim5</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tfidf_matrix5</span><span class="p">,</span> <span class="n">tfidf_matrix5</span><span class="p">)</span>
<span class="n">cosine_sim5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.14048494],
       [0.14048494, 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c5</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tfidf_matrix5</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">c5</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        , -0.83667967],
       [-0.83667967,  1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>네 개의 리스트가 합쳐진 케이스와 첫 번째 항목과 나머지 항목이 각각 나뉘어진 상태에서의</p>
<p>코사인 유사도와 상관관계의 값의 결과입니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">cosine_sim2</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span> <span class="n">cosine_sim3</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">cosine_sim4</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">:],</span> <span class="n">cosine_sim5</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span> <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[1.         0.44199978 0.17531557 0.10887498]
[1.         0.48413539] [0.18200376] [0.14048494]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">c22</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span> <span class="n">c3</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">c4</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">:],</span> <span class="n">c5</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span> <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[ 1.          0.08277906 -0.38357704 -0.49188749]
[ 1.         -0.38957117] [-0.82809385] [-0.83667967]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>일반적인 자연어에서의 경우가 아닌, 숫자와 숫자간의 경우라면</p>
<p>일단 상관관계에서는 이렇게 분리가 되더라도 값이 동일하여야 합니다,</p>
<p>하지만, 상관관계의 결과를 보면, 값이 바뀌고 있다는 것이 자연어에서의 상관관계는 상대적인 것이라는 것을 확인할 수 있습니다.</p>
<p>즉, 일반적인 변수와 변수간의 관계에서 상관관계를 보는 것과 다르게 자연어 처리를 할 때에는</p>
<p>코사인 유사도를 보든간에 상관관계를 보든간에 상대적이라는 것을 확인할 수 있습니다.</p>

<br/>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="&#48324;&#44060;-&#52992;&#51060;&#49828;-&#50857;">&#48324;&#44060; &#52992;&#51060;&#49828; &#50857;<a class="anchor-link" href="#&#48324;&#44060;-&#52992;&#51060;&#49828;-&#50857;">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>다음은 리스트를 하나 더 추가하여, TF-IDF를 활용할 경우, 값이 어떻게 변화되는지 확인해보고자 합니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf6</span><span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list_case2</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;In this case, we have no choice&#39;</span><span class="p">,</span> <span class="s1">&#39;Life is choice between birth and death&#39;</span><span class="p">,</span>
             <span class="s1">&#39;Sometimes i watching youtube for 10 times&#39;</span><span class="p">,</span> <span class="s1">&#39;google</span><span class="se">\&#39;</span><span class="s1">s youtube has grown significantly in 10 years&#39;</span><span class="p">]</span>

<span class="n">tf_matrix</span> <span class="o">=</span> <span class="n">tf6</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list_case2</span><span class="p">)</span>
<span class="n">tf_matrix</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[17]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;4x48 sparse matrix of type &#39;&lt;class &#39;numpy.float64&#39;&gt;&#39;
	with 52 stored elements in Compressed Sparse Row format&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cos_sim</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tf_matrix</span><span class="p">,</span> <span class="n">tf_matrix</span><span class="p">)</span>
<span class="n">cos_sim</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[18]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[1.        , 0.05000364, 0.        , 0.04770921],
       [0.05000364, 1.        , 0.        , 0.        ],
       [0.        , 0.        , 1.        , 0.10431864],
       [0.04770921, 0.        , 0.10431864, 1.        ]])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coef2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span> <span class="n">tf_matrix</span><span class="o">.</span><span class="n">toarray</span><span class="p">()</span> <span class="p">)</span>
<span class="n">coef2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[19]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([[ 1.        , -0.30056629, -0.32935693, -0.33965525],
       [-0.30056629,  1.        , -0.33001768, -0.40765924],
       [-0.32935693, -0.33001768,  1.        , -0.22094461],
       [-0.33965525, -0.40765924, -0.22094461,  1.        ]])</pre>
</div>

</div>

</div>
</div>

<br/>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="&#47532;&#49828;&#53944;-&#52628;&#44032;-&#54980;-&#44208;&#44284;-&#48372;&#44592;">&#47532;&#49828;&#53944; &#52628;&#44032; &#54980; &#44208;&#44284; &#48372;&#44592;<a class="anchor-link" href="#&#47532;&#49828;&#53944;-&#52628;&#44032;-&#54980;-&#44208;&#44284;-&#48372;&#44592;">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">tf7</span><span class="o">=</span> <span class="n">TfidfVectorizer</span><span class="p">(</span><span class="n">analyzer</span> <span class="o">=</span> <span class="s1">&#39;word&#39;</span><span class="p">,</span> <span class="n">ngram_range</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">min_df</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>

<span class="n">list_case3</span> <span class="o">=</span> <span class="n">list2</span> <span class="o">+</span> <span class="n">list_case2</span>

<span class="n">tf_matrix3</span> <span class="o">=</span> <span class="n">tf7</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">list_case3</span><span class="p">,</span> <span class="n">list_case3</span><span class="p">)</span>
<span class="n">tf_matrix3</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;8x74 sparse matrix of type &#39;&lt;class &#39;numpy.float64&#39;&gt;&#39;
	with 102 stored elements in Compressed Sparse Row format&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cos_sim3</span> <span class="o">=</span> <span class="n">linear_kernel</span><span class="p">(</span><span class="n">tf_matrix3</span><span class="p">,</span> <span class="n">tf_matrix3</span><span class="p">)</span>

<span class="n">coef3</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">corrcoef</span><span class="p">(</span><span class="n">tf_matrix3</span><span class="o">.</span><span class="n">toarray</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[21]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([ 1.        ,  0.37740849,  0.04803899, -0.03319176])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cosine_sim2</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">cos_sim</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[31]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([1.        , 0.44199978, 0.17531557, 0.10887498]),
 array([1.        , 0.05000364, 0.        , 0.04770921]))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cos_sim3</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">:</span><span class="mi">4</span><span class="p">],</span> <span class="n">cos_sim3</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="mi">4</span><span class="p">:]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[28]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([1.        , 0.4732777 , 0.20111892, 0.13268325]),
 array([1.        , 0.05940594, 0.        , 0.05462482]))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>코사인 유사도의 경우, 별개의 경우와 합쳐진 경우에서 해당되는 경우를 가지고 와서 비교를 해본 결과</p>
<p>값의 차이가 존재는 하지만, 이는 애초에 유사도 자체가 상대적인 것이기 때문에 상관이 없으며,</p>
<p>첫 번째와 나머지를 비교했을 때의 결과도 얼마나 유사한지를 잘 보여주고 있다고 생각됩니다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c22</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">coef2</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[32]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([ 1.        ,  0.08277906, -0.38357704, -0.49188749]),
 array([ 1.        , -0.30056629, -0.32935693, -0.33965525]))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">coef3</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">:</span><span class="mi">4</span><span class="p">],</span> <span class="n">coef3</span><span class="p">[</span><span class="mi">4</span><span class="p">][</span><span class="mi">4</span><span class="p">:]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[27]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(array([ 1.        ,  0.37740849,  0.04803899, -0.03319176]),
 array([ 1.        , -0.1379455 , -0.19043601, -0.16249011]))</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>반면에 상관관계의 경우, TF-IDF라는 상대적인 값을 통해서 상관관계를 구했기 때문에,</p>
<p>일단 일반적으로 생각되는 것처럼 값이 고정되지 않는 것을 볼 수 있었습니다.</p>
<p>첫 번째와 나머지를 비교한 결과에서는 추가로 생성된 리스트에서</p>
<p>원래는 -0.3293, -0.3396의 차이를 가지던 것이 -0.1904, -0.1624로 값의 차이가 바뀐 것을 볼 수 있습니다.</p>
<p>이렇게 작은 추가만으로도 값이 크게 바뀌는데다가 순위까지 바뀌는 것을 볼 수 있었기 때문에</p>
<p>TF-IDF를 사용할 때는 상관관계가 아닌 유사도를 사용하는 것이 순위를 매기기에는 좋다고 생각됩니다.</p>
