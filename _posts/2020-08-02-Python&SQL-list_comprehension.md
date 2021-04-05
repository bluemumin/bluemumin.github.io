---
layout: post
title:  "python for문 사용과 list comprehension"
subtitle:   "python for문 사용과 list comprehension"
categories: PS
tags: Python
comments: true
---

#### python에서 for문과 자주 비교되서 사용되는 list comprehension 구조를 위한 포스팅입니다.

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>보통 루프문을 일반적으로 배울 때는 for, while문을 먼저 배운다.</p>
<p>그러면 이러한 루프문에서 나온 값을 바로 적용하기 위해서는</p>
<p>보통은 리스트를 미리 만들고 append를 하도록 배우는 것이 보편적이다.</p>
<p>하지만 이러한 방법은 미리 할당도 하여야되고 수가 기하급수적으로 많아지면 루프문이 매우 느리게 실행 되는 것을 볼 수 있다.</p>
<p>이러한 상황을 해결하기 위해서 그 다음으로 배우는 것이 바로 list comprehension이다.</p>
<p>일단 특정 패키지 없이 사용이 가능하다는 점에서 좋고 짧은 구조에서는 가독성도 나쁘지 않은 편이다.</p>
<p>속도의 경우는 생략하고 바로 사용 방법만 다뤄보기로 하겠다</p>
<p>바로 예시를 통해서 비교를 해보도록 하자.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>첫 번째로는 숫자 리스트의 숫자를 문자로만 바꿔서 문자 리스트로 바꾸는 작업이다</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># list comprehension</span>

<span class="n">name</span> <span class="o">=</span> <span class="p">[</span><span class="mi">123</span><span class="p">,</span> <span class="mi">456</span><span class="p">,</span> <span class="mi">789</span><span class="p">,</span> <span class="mi">101112</span><span class="p">]</span>

<span class="n">list1</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name</span><span class="p">:</span>
    <span class="n">list1</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="nb">str</span><span class="p">(</span><span class="n">first</span><span class="p">)</span> <span class="p">)</span>

<span class="n">list1</span>    
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[1]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;123&#39;, &#39;456&#39;, &#39;789&#39;, &#39;101112&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>일반 for문을 쓰면 보통은 빈 리스트를 만들고 이를 append하는 방식이지만</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">first</span><span class="p">)</span> <span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;123&#39;, &#39;456&#39;, &#39;789&#39;, &#39;101112&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>list comprehension은 그냥 리스트안에 for문을 집어넣어서 리스트 안에서 해당 방식이 실행이 되도록 하여서</p>
<p>집어넣는 과정을 생략하여서 속도가 훨씬 빠르게 된다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>이 방법을 보면 두 가지 생각이 들 것이다.</p>
<p>첫 번째는 도대체 뭔 구조로 이루어 진 것이고</p>
<p>두 번째는 이중 for 문으로 안되는거면 복잡한 경우에는 for문으로만 해야되는거네 라는 것이다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>첫 번째를 자세히 설명하자면</p>
<p>for first in name에서 name은 전체 항목이고 first에는 각 항목이 나와서 이를 전체적으로 실행하는 방식이다.</p>
<p>[str(first) for first in name] 에서 뒷 부분은 일반 for문과 동일한 것이다.</p>
<p>그렇다면 맨 앞의 str(first)는 무엇이냐면 for문에서 : 뒤에 나오는 것이다.</p>
<p>list comprehension은 실제 실행이 되어야되는 내용을 맨 앞에 두고 for문을 뒤에 두는 방식이다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>두 번째의 경우는 바로 다음 예시를 보도록 하겠다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">name2</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;123&#39;</span><span class="p">,</span> <span class="s1">&#39;456&#39;</span><span class="p">,</span> <span class="s1">&#39;789&#39;</span><span class="p">,</span> <span class="s1">&#39;101112&#39;</span><span class="p">]</span>

<span class="n">list2</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name2</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="n">first</span><span class="p">:</span>
        <span class="n">list2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="nb">str</span><span class="p">(</span><span class="n">second</span><span class="p">)</span> <span class="p">)</span>
        
<span class="n">list2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[3]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;, &#39;1&#39;, &#39;0&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;2&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>list comprehension에서도 이중 for문이 실행이 가능한데</p>
<p>바로 첫 번째로 실행이 되는 for문 다음에 이중 for문으로 또 들어가는 항목을 넣고</p>
<p>최종적으로 실제 실행이 되어야 되는 내용을 맨 앞에 놔두는 것이다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">name3</span> <span class="o">=</span> <span class="p">[</span> <span class="p">[</span><span class="s1">&#39;123&#39;</span><span class="p">,</span> <span class="s1">&#39;456&#39;</span><span class="p">,</span> <span class="s1">&#39;789&#39;</span><span class="p">,</span> <span class="s1">&#39;101112&#39;</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;123&#39;</span><span class="p">,</span> <span class="s1">&#39;456&#39;</span><span class="p">]</span> <span class="p">]</span>

<span class="n">list3</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name3</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="n">first</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">third</span> <span class="ow">in</span> <span class="n">second</span><span class="p">:</span>
            <span class="n">list3</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="nb">str</span><span class="p">(</span><span class="n">third</span><span class="p">)</span> <span class="p">)</span>
        
<span class="nb">print</span><span class="p">(</span> <span class="n">list3</span> <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">third</span><span class="p">)</span> <span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name3</span> <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="n">first</span> <span class="k">for</span> <span class="n">third</span> <span class="ow">in</span> <span class="n">second</span><span class="p">]</span> <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;, &#39;1&#39;, &#39;0&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;2&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;]
[&#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;, &#39;1&#39;, &#39;0&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;2&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">third</span><span class="p">)</span> <span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name3</span> <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="n">first</span> <span class="k">for</span> <span class="n">third</span> <span class="ow">in</span> <span class="n">second</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[5]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;1&#39;,
 &#39;2&#39;,
 &#39;3&#39;,
 &#39;4&#39;,
 &#39;5&#39;,
 &#39;6&#39;,
 &#39;7&#39;,
 &#39;8&#39;,
 &#39;9&#39;,
 &#39;1&#39;,
 &#39;0&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;2&#39;,
 &#39;1&#39;,
 &#39;2&#39;,
 &#39;3&#39;,
 &#39;4&#39;,
 &#39;5&#39;,
 &#39;6&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>삼중으로 실행 시키는 경우도 비슷하게 하면 된다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>단 중간에 실제 실행하는 내용이 들어가는 경우, 경우에 따라 이중 for문으로만 해도 되는 경우가</p>
<p>3중 list comprehension으로 구성하여야되는 경우도 있다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">list2</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name2</span><span class="p">:</span>
    <span class="n">first</span> <span class="o">=</span> <span class="n">first</span> <span class="o">+</span> <span class="s1">&#39;a&#39;</span>
    <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="n">first</span><span class="p">:</span>
        <span class="n">list2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="nb">str</span><span class="p">(</span><span class="n">second</span><span class="p">)</span> <span class="p">)</span>
        
<span class="n">list2</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[6]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;1&#39;,
 &#39;2&#39;,
 &#39;3&#39;,
 &#39;a&#39;,
 &#39;4&#39;,
 &#39;5&#39;,
 &#39;6&#39;,
 &#39;a&#39;,
 &#39;7&#39;,
 &#39;8&#39;,
 &#39;9&#39;,
 &#39;a&#39;,
 &#39;1&#39;,
 &#39;0&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;2&#39;,
 &#39;a&#39;]</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">third</span><span class="p">)</span> <span class="k">for</span> <span class="n">second</span> <span class="ow">in</span> <span class="p">[</span><span class="n">first</span> <span class="o">+</span> <span class="s1">&#39;a&#39;</span> <span class="k">for</span> <span class="n">first</span> <span class="ow">in</span> <span class="n">name2</span> <span class="p">]</span> <span class="k">for</span> <span class="n">third</span> <span class="ow">in</span> <span class="n">second</span> <span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[7]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>[&#39;1&#39;,
 &#39;2&#39;,
 &#39;3&#39;,
 &#39;a&#39;,
 &#39;4&#39;,
 &#39;5&#39;,
 &#39;6&#39;,
 &#39;a&#39;,
 &#39;7&#39;,
 &#39;8&#39;,
 &#39;9&#39;,
 &#39;a&#39;,
 &#39;1&#39;,
 &#39;0&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;1&#39;,
 &#39;2&#39;,
 &#39;a&#39;]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>list comprehension은 짧은 구조에 간단히 사용하면 좋지만,</p>
<p>23중으로 가는 경우와 복잡한 경우 그리고 특히 다른 사람이 코드를 보고 나중에 수정을 할 필요가 있는 내용이라면</p>
<p>이러한 방식으로 구현을 절대 하지 않는 것을 권한다.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>가장 큰 이유는 가독성이 떨어지며, 코드 특성 상 몇 달만 지나도 본인조차 까먹기 때문에</p>
<p>코드를 해석하기 위해서라면 알아두면 좋지만, 굳이 권장은 하지 않는다.</p>
<p>함수에 넣어서 자주 사용을 할거라면 덕 타이핑으로 해당 설명을 필수적으로 넣어줘야된다고 본다.</p>

</div>
</div>
</div>