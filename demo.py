from pytohtml import *

# ── Header & Navigation ──────────────────────────────────────────────────────
fnav_bar = cabecalho(
    linha(
        linha(
            imagem("https://www.python.org/static/favicon.ico", alt="Logo PYTOHTML", classes="h-8 w-8 drop-shadow-sm"),
            titulo("PYTOHTML", tamanho="grande", classes="text-xl font-black tracking-tighter bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-yellow-500"),
            distanciamento=3
        ),
        nav(
            botao("Início", variante="vazio", classes="text-slate-600 hover:text-blue-600 font-medium transition-colors duration-200"),
            botao("Documentação", variante="vazio", classes="text-slate-600 hover:text-blue-600 font-medium transition-colors duration-200"),
            botao("Começar", variante="primario", classes="bg-blue-600 hover:bg-blue-700 text-white shadow-md hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200 rounded-full px-6"),
        ),
        classes="w-full justify-between"
    ),
    classes="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm"
)

# ── Destaque Section ─────────────────────────────────────────────────────────
secao_destaque = destaque(
    "Design Simples. Resultados Poderosos.",
    "Uma biblioteca em Python puro para criar interfaces modernas, sem tocar em HTML, CSS ou Javascript. Perfeito para quem está começando.",
    botao("Iniciar Jornada 🚀", variante="primario", classes="bg-blue-600 hover:bg-blue-500 text-white shadow-xl hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 text-lg px-8 py-3 rounded-full border-none"),
    botao("Ver Documentação", variante="vazio", classes="border-2 border-slate-600 text-slate-300 hover:text-white hover:bg-slate-800 transition-all duration-300 text-lg px-8 py-3 rounded-full"),
    classes="bg-slate-950 text-white relative overflow-hidden"
)

# ── 1. Textos e Visualização Básica ──────────────────────────────────────────
secao_basicos = secao(
    container(
        titulo("1. Textos e Elementos Visuais", tamanho="grande", classes="mb-6"),
        grade(
            cartao(
                titulo("Tipografia Inteligente", tamanho="medio", classes="text-lg text-gray-800 mb-2"),
                paragrafo("Gerencie textos, negritos e cores de forma nativa e simples."),
                paragrafo("Este é um texto comum, mas ", classes="text-sm text-gray-600"),
                paragrafo("este tem destaque", classes="text-sm font-bold text-indigo-600"),
                classes="bg-white shadow-sm hover:shadow-md transition-shadow"
            ),
            cartao(
                titulo("Avatares e Badges", tamanho="medio", classes="text-lg text-gray-800 mb-2"),
                linha(
                    avatar(src="https://picsum.photos/id/1025/100/100", tamanho=12),
                    etiqueta("Premium", cor="roxo"),
                    etiqueta("Ativo", cor="verde"),
                    distanciamento=2
                ),
                classes="bg-white shadow-sm hover:shadow-md transition-shadow"
            ),
            cartao(
                titulo("Botões Diferentes", tamanho="medio", classes="text-lg text-gray-800 mb-2"),
                grade(
                    botao("Primário", variante="primario"),
                    botao("Secundário", variante="secundario"),
                    botao("Perigo", variante="perigo"),
                    botao("Sucesso", variante="sucesso"),
                    colunas=2, distanciamento=2
                ),
                classes="bg-white shadow-sm hover:shadow-md transition-shadow"
            ),
            colunas=3, distanciamento=6
        )
    ),
    classes="bg-gray-50"
)

# ── 2. Componentes Prontos ───────────────────────────────────────────────────
secao_componentes = secao(
    container(
        titulo("2. Componentes Estruturais", tamanho="grande", classes="mb-6"),
        grade(
            # Alertas
            cartao(
                titulo("Alertas Estáticos", tamanho="pequeno", classes="text-md text-gray-700"),
                coluna(
                    aviso_estatico("Tudo funcionando perfeitamente!", tipo="sucesso"),
                    aviso_estatico("Seu disco está quase cheio.", tipo="aviso"),
                    aviso_estatico("Houve um erro no servidor nativo.", tipo="perigo"),
                    aviso_estatico("Nova notificação!", tipo="info"),
                    distanciamento=1,
                    centralizado=False
                )
            ),
            # Listas e Tabelas
            cartao(
                titulo("Listas e Tabelas", tamanho="pequeno", classes="text-md text-gray-700 mb-3"),
                lista(*["Primeiro item", "Segundo item", "Terceiro item"]),
                divisor(classes="my-4"),
                tabela(
                    dados=[
                        ["ID", "Nome", "Status"],
                        ["1", "Sistema Core", etiqueta("Ativo", cor="verde")],
                        ["2", "Banco de Dados", etiqueta("Manutenção", cor="amarelo")],
                    ],
                    cabecalho=True,
                    escapar=False
                )
            ),
            colunas=2
        ),
        divisor(classes="my-8"),
        grade(
            cartao(
                titulo("Accordion (Sanfona)", tamanho="pequeno", classes="mb-4"),
                accordion("O que é o componente accordion?", paragrafo("É um painel que se expande ao clicar para mostrar seu conteúdo oculto.")),
                accordion("Posso ter vários?", paragrafo("Sim, você pode empilhar quantos quiser criando layouts eficientes.")),
            ),
            cartao(
                titulo("Código e Skeletons", tamanho="pequeno", classes="mb-4"),
                codigo('print("Hello World!")'),
                divisor(classes="my-4"),
                paragrafo("Skeleton Loading:", classes="font-semibold mb-2"),
                animacao_carregando(tipo="texto", classes="h-8 w-3/4 mb-2"),
                animacao_carregando(tipo="texto", classes="h-4 w-full mb-2"),
                animacao_carregando(tipo="texto", classes="h-4 w-5/6")
            ),
            colunas=2
        )
    )
)

# ── 3. Formulários ───────────────────────────────────────────────────────────
secao_forms = secao(
    container(
        titulo("3. Formulários", tamanho="grande", classes="text-2xl text-gray-800 mb-6 font-bold"),
        formulario(
            cartao(
                grade(
                    coluna(rotulo("Nome Completo", para="nome"), entrada(tipo="text", nome="nome", placeholder="João Silva", obrigatorio=True), centralizado=False, distanciamento=1),
                    coluna(rotulo("Email Profissional", para="email"), entrada(tipo="email", nome="email", placeholder="joao@empresa.com", obrigatorio=True), centralizado=False, distanciamento=1),
                    coluna(rotulo("Senha", para="senha"), entrada(tipo="password", nome="senha", placeholder="••••••••", obrigatorio=True), centralizado=False, distanciamento=1),
                    coluna(rotulo("Data de Nascimento", para="data"), entrada(tipo="date", nome="data", obrigatorio=True), centralizado=False, distanciamento=1),
                    colunas=2
                ),
                coluna(rotulo("Biografia", para="bio"), textarea(nome="bio", linhas=3, placeholder="Fale um pouco sobre você..."), centralizado=False, distanciamento=1, classes="mt-4"),
                botao("Enviar Formulário", variante="primario", tipo="submit", classes="mt-6 w-full")
            )
        ),
        # Abstração de envio assíncrono real via motor Python: Captura o submit, 
        # transforma os inputs em JSON e envia via POST (tudo invisível ao usuário)
        enviar_formulario("form", "https://jsonplaceholder.typicode.com/posts", mensagem_sucesso="O cadastro simulado foi enviado com sucesso!")
    ),
    classes="bg-indigo-50"
)

# ── 4. Interatividade, SweetAlert2 e Brython ─────────────────────────────────
secao_interatividade = secao(
    container(
        titulo("4. Popups e Interatividade Nativa", tamanho="grande", classes="mb-6"),
        paragrafo("Usando as funções de alerta intuitivo e o motor Python integrado, tudo roda perfeitamente no cliente.", classes="mb-6 text-gray-600"),
        grade(
            cartao(
                etiqueta("Popups", cor="azul"),
                titulo("Alertas Centrais", tamanho="pequeno", classes="text-lg text-gray-800 mt-2 mb-4"),
                coluna(
                    botao("Sucesso", variante="sucesso", classes="id-btn-suc w-full"),
                    botao("Erro", variante="perigo", classes="id-btn-err w-full"),
                    botao("Aviso", variante="aviso", classes="id-btn-avi w-full"),
                    distanciamento=2
                ),
                classes="bg-white shadow-sm"
            ),
            cartao(
                etiqueta("Ações", cor="amarelo"),
                titulo("Toast & Confirmação", tamanho="pequeno", classes="text-lg text-gray-800 mt-2 mb-4"),
                coluna(
                    botao("Mostrar Toast 🎉", variante="sucesso", classes="id-btn-toast w-full"),
                    botao("Deletar Conta 🗑️", variante="perigo", classes="id-btn-del w-full"),
                    distanciamento=4
                ),
                classes="bg-white shadow-sm"
            ),
            cartao(
                etiqueta("Motor Web", cor="verde"),
                titulo("Python Assíncrono", tamanho="pequeno", classes="text-lg text-gray-800 mt-2 mb-4"),
                paragrafo("Busca de API externa feita 100% no cliente com o Python:", classes="text-sm text-gray-600 mb-4"),
                botao("🌍 Buscar Dados Fakes", variante="secundario", classes="id-btn-fetch w-full mb-4"),
                div_resultado := espaco_dinamico("api-result"),
                classes="bg-white shadow-sm"
            ),
            colunas=3, distanciamento=6
        ),
        
        # Ações diretas das abstrações geradas:
        alerta_ao_clicar(".id-btn-suc", "Maravilha!", "", "success"),
        alerta_ao_clicar(".id-btn-err", "Oops!", "", "error"),
        alerta_ao_clicar(".id-btn-avi", "Atenção!", "", "warning"),

        alerta_ao_clicar(".id-btn-toast", "Toast Ativado!", "Operação rápida.", "success"), # Toast simplificado para didática
        
        pedir_confirmacao(".id-btn-del", titulo="Apagar tudo?", texto="Toda a base será perdida."),
        
        # Teste do buscar_dados abstraído em 1 única linha elegante para iniciantes:
        buscar_dados("https://dummyjson.com/users/1", seletor_resultado="#api-result", gatilho_clique=".id-btn-fetch")
    )
)


# ── Modais ───────────────────────────────────────────────────────────────────
secao_modais = secao(
    container(
        titulo("5. Modais HTML Puro (Tailwind)", tamanho="grande", classes="mb-6"),
        cartao(
            paragrafo("Além dos alertas interativos, o pytohtml suporta modais tradicionais de HTML escondidos pelo Tailwind.", classes="mb-4"),
            botao("Abrir Modal Padrão", variante="primario", classes="id-btn-abrir-modal"),
            modal(
                "meu-modal-demo",
                "Termos de Uso",
                "Este é um exemplo de modal nativo usando Tailwind estruturando os elementos.",
                botao("Aceitar e Fechar", variante="sucesso", classes="w-full mt-4")
            ),
            abrir_modal_ao_clicar(".id-btn-abrir-modal", "meu-modal-demo")
        )
    ),
    classes="bg-white"
)

# ── Footer ───────────────────────────────────────────────────────────────────
pe = rodape(
    coluna(
        paragrafo("© 2024 pytohtml", classes="text-gray-400"),
        linha(
            link("GitHub", href="#", classes="text-gray-400 hover:text-white mx-2"),
            link("Twitter", href="#", classes="text-gray-400 hover:text-white mx-2"),
        ),
        distanciamento=2, centralizado=True
    )
)

# ── Montar a Página ──────────────────────────────────────────────────────────
pagina = html(
    fnav_bar, 
    secao_destaque, 
    secao_basicos, 
    secao_componentes, 
    secao_forms, 
 
    secao_interatividade,
    secao_modais, 
    pe,
    titulo_pagina="pytohtml — Portfólio",
    brython=True,
    favicon="https://www.python.org/static/favicon.ico"
)

salvar("demo.html", pagina)
print("demo.html gerado com sucesso!")
