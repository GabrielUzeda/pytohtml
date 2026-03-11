# Guia Rápido: pytohtml 🐍

Este guia contém todas as funcionalidades da biblioteca agrupadas por categoria, com exemplos diretos de como usar cada uma.

---

## 🏗️ 1. Página e Estrutura Geral

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`html(...)`** | Monta e envelopa todos os seus elementos na estrutura HTML base (com Tailwind e Brython). | `pagina = html(meu_titulo, meu_botao, brython=True)` |
| **`salvar(...)`** | Salva a sua página HTML gerada num arquivo físico `.html`. | `salvar("index.html", pagina)` |

---

## 📐 2. Layout & Containers
Usados para agrupar e organizar outros elementos na tela.

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`container(...)`** | Centraliza o conteúdo (ideal para o corpo da página). | `container("Oi!", max_w="max-w-4xl")` |
| **`linha(...)` / `coluna(...)`** | Organiza itens lado a lado ou empilhados. | `linha(botao_1, botao_2, distanciamento=4)` |
| **`grade(...)`** | Organiza itens em grade estruturada (colunas). | `grade(item1, item2, item3, colunas=3)` |
| **`secao(...)`** | Cria uma área espaçada verticalmente (bloco principal). | `secao(meu_texto, bg="bg-gray-100")` |
| **`cabecalho(...)`** | Cria uma barra no topo da tela. | `cabecalho(logo, nav())` |
| **`rodape(...)`** | Cria uma barra no fim da tela. | `rodape("Copyright 2024")` |
| **`nav(...)`** | Cria um menu de navegação. | `nav(link_home, link_sobre)` |
| **`destaque(...)`** | Cria uma "capa" de destaque no topo. | `destaque("Bem-vindo!", subtitulo="O melhor site")` |

---

## 📝 3. Textos e Visualização Básica

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`titulo(...)`** | Cria títulos (H1 a H4). Tamanhos: "pequeno", "medio", "grande", "gigante". | `titulo("Minha Loja", tamanho="gigante")` |
| **`paragrafo(...)`** | Insere texto simples. | `paragrafo("Este é um texto normal.", cor="text-gray-600")` |
| **`imagem(...)`** | Exibe uma imagem da internet ou arquivo local. | `imagem("foto.jpg", alt="Foto de um gato")` |
| **`botao(...)`** | Cria um botão clicável. | `botao("Salvar", variante="sucesso", id="btn-salvar")` |
| **`link(...)`** | Um hiperlink para outra página. | `link("Clique aqui", url="https://google.com")` |
| **`divisor(...)`** | Cria uma linha horizontal separadora. | `divisor(margem_y="my-8")` |
| **`etiqueta(...)`** | Cria uma etiqueta pequena realçada. | `etiqueta("Novo!", cor="azul")` |

---

## 🧩 4. Componentes Prontos

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`cartao(...)`** | Uma caixa branca com borda/sombra para destacar conteúdo. | `cartao(titulo("Oi"), paragrafo("Conteúdo aqui."))` |
| **`tabela(...)`** | Uma tabela estruturada a partir de cabeçalhos e linhas. | `tabela(["Nome", "Idade"], [["João", 20], ["Maria", 30]])` |
| **`lista(...)`** | Uma lista com bolinhas pontilhadas. | `lista(["Maçã", "Pêra", "Uva"])` |
| **`aviso_estatico(...)`** | Uma caixa colorida estática na tela com aviso. | `aviso_estatico("Sistema fora do ar!", tipo="perigo")` |
| **`avatar(...)`** | Uma foto de perfil redonda (se sem foto, mostra as iniciais). | `avatar(nome="Elon Musk", src="perfil.png")` |
| **`accordion(...)`** | Painel que esconde/mostra conteúdo ao clicar (Sanfona). | `accordion("O que é?", "É uma lib legal.")` |
| **`codigo(...)`** | Mostra bloco de texto com fonte monoespaçada. | `codigo("print('Olá mudo')")` |
| **`animacao_carregando(...)`** | Efeito de "carregando". | `animacao_carregando(tipo="texto")` |
| **`modal(...)`** | Janela pop-up flutuante construída com Tailwind. | `modal("aviso", "Meu Modal", "Tem certeza?", botao_fechar="X")` |

---

## 📩 5. Formulários

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`formulario(...)`** | A tag raiz de um formulário. | `formulario(ent1, ent2, btn_submit)` |
| **`entrada(...)`** | Adiciona um input. Pode ter obrigatorio=True. | `entrada(tipo="email", obrigatorio=True)` |
| **`textarea(...)`** | Campo grande para texto. Pode ser obrigatorio. | `textarea(linhas=4, obrigatorio=True)` |
| **`rotulo(...)`** | Texto descritivo acima de input. | `rotulo("Seu Nome:", para="campo_nome")` |

---

## ⚡ 6. Interatividade e Dados (Python no Navegador)
*Requer que o motor `brython=True` esteja ligado no `html()`.*

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`ao_clicar(...)`** | Roda código Python assim que um elemento for clicado. | `ao_clicar("#botao_1", 'print("Clicou!")')` |
| **`escutar_evento(...)`** | O mesmo que o de cima, mas ao terminar de digitar algo (mudança, focos, teclas etc). | `escutar_evento("#meu-campo", "change", ...)` |
| **`ao_carregar(...)`** | Roda o código sozinho, apenas uma vez, assim que a página abrir. | `ao_carregar('print("Carregou")')` |
| **`espaco_dinamico(...)`** | Cria um espaço em branco invisível, preparado para receber texto depois. | `espaco_dinamico("resultado-aqui")` |
| **`inserir_html(...)`** | Mostra/Insere conteúdo dentro do `espaco_dinamico()`. | `inserir_html("#resultado-aqui", 'html_resultado="Foi!"')` |
| **`buscar_dados(...)`** | Baixa informações secretas de outra página da internet. | `buscar_dados("https://site.com/dados", callback_nome="on_done")` |
| **`estado(...)`** | Variável com magia: toda vez que você altera o `valor`, todos os textos da página que dependem dessa variável mudam automaticamente. | `estado("placar", "0", seletor_bind="#meu-score")` |
| **`script_python(...)`** | Cria a tag oficial de inserção de blocos livres em código Python puro. | `script_python("print('oi')")` |

---

## 🎉 7. Popups e Alertas Rápidos (SweetAlert2)
Formato mais fácil para avisar algo na cara do usuário, sem ele se perder.

| Função | O que faz | Exemplo de uso |
| :--- | :--- | :--- |
| **`alerta(...)`** | Abstração geral para exibir um popup nativo (SweetAlert) flexível via script. | `alerta("Oops!", "Erro 404", icone="warning")` |
| **`alerta_sucesso(...)`** | Mostra um popup central verde de tudo ok! (Abre sozinho ao carregar) | `alerta_sucesso("Salvo!", "Tudo ótimo.")` |
| **`alerta_erro(...)`** | Mostra um popup vermelho de fracasso. | `alerta_erro("Ops", "Aconteceu um erro grave")` |
| **`alerta_aviso(...)`** | Um popup amarelo indicando atenção. | `alerta_aviso("Atenção", "Seu tempo esgotou.")` |
| **`alerta_info(...)`** | Um popup azulzinho apenas informativo. | `alerta_info("Info", "O arquivo já foi lido.")` |
| **`pedir_confirmacao(...)`** | Interrompe e pergunta ao usuário "Você tá certo que quer fazer isso?". | `pedir_confirmacao("#btn-deletar", titulo="Confirmar exclusão?", texto="...")` |
| **`notificacao_rapida(...)`** | Aquele alerta que aparece sutilmente no canto superior sem travar a tela e some sozinho. | `notificacao_rapida("E-mail enviado!", icone="success")` |
| **`alerta_ao_clicar(...)`** | Mesma coisa de cima, mas é engatilhado no instante que você clica num botão específico. | `alerta_ao_clicar("#btn-x", "Surpresa!")` |
| **`alerta_ao_enviar(...)`** | Intercepta o comportamento normal do formulário de *recarregar a tela em branco*, e exibe só um aviso. | `alerta_ao_enviar("#meu_formulario", "Enviado com sucesso!")` |
