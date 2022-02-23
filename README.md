<h2 class="code-line" data-line-start=0 data-line-end=1 ><a id="Instalao_0"></a>Instalação</h2>
<p class="has-line-data" data-line-start="2" data-line-end="3">Para instalar o programa, siga esses passos:</p>
<pre><code class="has-line-data" data-line-start="4" data-line-end="8" class="language-sh">git <span class="hljs-built_in">clone</span> https://github.com/clauds-macedo/ProjetoRedes.git
<span class="hljs-built_in">cd</span> ProjetosRedes
pip install -r requirements.txt
</code></pre>
<p class="has-line-data" data-line-start="8" data-line-end="9"><code>Nota: Em alguns computadores a biblioteca &quot;Cryptography&quot; não instala corretamente em conjunto ao &quot;requirements.txt&quot;. Caso ocorra, utilize o comando: pip install cryptography</code></p>
<p class="has-line-data" data-line-start="10" data-line-end="11">Após ter instalado as bibliotecas, abra um terminal para o servidor e execute seu arquivo:</p>
<pre><code class="has-line-data" data-line-start="13" data-line-end="15">python .\server.py
</code></pre>
<p class="has-line-data" data-line-start="15" data-line-end="16">Ou</p>
<pre><code class="has-line-data" data-line-start="17" data-line-end="19">python3 .\server.py
</code></pre>
<p class="has-line-data" data-line-start="20" data-line-end="21">Com o servidor inicializado, abra mais um terminal agora está apto para iniciar o cliente:</p>
<pre><code class="has-line-data" data-line-start="22" data-line-end="24">python .\tela_principal.py
</code></pre>
<p class="has-line-data" data-line-start="25" data-line-end="26">Ou</p>
<pre><code class="has-line-data" data-line-start="27" data-line-end="29">python3 .\tela_principal.py
</code></pre>
<ul>
  Passos
  <li>Ao executar o arquivo "tela_principal.py", escolha a opção de criptografia e insira uma mensagem qualquer.</li>
  <li>Após ter dado OK, feche a janela e vá na opção de descriptografar, insira o código que foi automaticamente copiado para sua área de transferência e, novamente, clique em OK.</li>
  Com isso, a mensagem será descriptografada.
</ul>
