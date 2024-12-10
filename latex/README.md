# UniforTeX2 - O que é?

O **UniforTeX2** é um projeto baseado no [abnTeX2] desenvolvido para auxiliar os alunos da Universidade de Fortaleza em seus trabalhos de monografias de graduação, dissertações de mestrado e teses de doutorado. Embora tenha sido escrita para ser utilizada principalmente pelos alunos da Computação, o UniforTeX2 é suficientemente configurável e facilmente adaptável para ser utilizada em praticamente todos os cursos da UNIFOR. Espera-se que o projeto seja um modelo de trabalho acadêmico que implemente todas as exigências das normas da ABNT sem a necessidade de se preocupar com o estilo ou formatação do documento.

### Modelos Disponíveis

**Trabalhos Acadêmicos**

 - Trabalho de Conclusão de Curso de Graduação
 - Trabalho de Conclusão de Curso de Especialização
 - Dissertação de Mestrado Acadêmico e Profissional
 - Tese de Doutorado
 
# Por onde começo?
Para utilizar o UniforTeX2 você precisa seguir os seguintes passos:
1. Crie uma conta no editor online de LaTeX [Overleaf](https://www.overleaf.com/);
2. Após criar a conta, clique [AQUI](https://www.overleaf.com/docs?snip_uri=https://github.com/bruno-unifor/unifortex2/archive/master.zip) para criar um novo template na sua conta Overleaf;

# Dicas
Veja a seguir como inserir alguns elementos no seu texto.

### Como inserir uma Tabela
```tex
\begin{table}[h!]	
	\centering
	\Caption{\label{tab:label_da_tabela} Legenda da Tabela}
	\UNIFORtab{}{
		\begin{tabular}{ccll}
			\toprule
	    		Quisque & pharetra & tempus & vulputate \\
			\midrule \midrule
				E1 & Complete coverage & Both splice sites \\
				E2 & Complete coverage & Both splice sites \\
				E3 & Partial coverage & Both splice sites & Both \\
				E4 & Partial coverage & One splice site & Both \\
				E5 & Complete or coverage & No splice & Both \\
				E6 & No coverage & No splice sites\\
			\bottomrule
		\end{tabular}
	}{
		\Fonte{Elaborado pelo autor}
    }
\end{table}
```

### Como inserir um Quadro
```tex
\begin{quadro}[h!]	
	\centering
	\Caption{\label{qua:label_do_quadro} Legenda do Quadro}
	\UNIFORqua{}{
		\begin{tabular}{|c|c|}
			\hline
			Quisque & pharetra \\
			\hline
			E1 & Complete coverage  \\
			\hline
			E2 & Complete coverage \\
			\hline
		\end{tabular}
	}{
		\Fonte{Elaborado pelo autor}
	}
\end{quadro}
```

### Como inserir uma figura
```tex
\begin{figure}[h!]
	\centering
	\UNIFORfig{
	    \Caption{\label{fig:label_da_figura} Legenda da Figura}	
	}{
	    \includegraphics[width=8cm]{figuras/figura-1}
	}{
	    \Fonte{Elaborado pelo autor}
	}	
\end{figure}
```

### Como inserir uma alínea
```tex
\begin{alineas}
	\item Lorem ipsum dolor sit amet;
    \item Praesent vitae nulla varius;
	\item Praesent quis erat eleifend;
	\item Mauris facilisis odio eu:
	\begin{subalineas}
		\item Integer non lacinia magna;
		\item Proin mattis placerat risus.
	\end{subalineas}
\end{alineas}
```

### Como criar Capítulos
```tex
\chapter{Fundamentação Teórica}
\label{cap:fundamentacao-teorica}
```

### Como criar Seções
```tex
% Seções Secundárias
\section{Objetivo Geral 2}
\label{sec:objetivo-geral-2}

% Seções Terciárias
\subsection{Objetivo Geral 3}
\label{sec:objetivo-geral-3}

% Seções Quaternárias
\subsubsection{Objetivo Geral 4}
\label{sec:objetivo-geral-4}

% Seções Quinárias
\subsubsubsection{Objetivo Geral 5}
\label{sec:objetivo-geral-5}
```

### Como inserir um algoritmo
```tex
\begin{algorithm}[h!]
	\SetSpacedAlgorithm
	\caption{\label{alg:algoritmo_de_colonica_de_formigas}Algoritmo de Otimização por Colônia de Formiga}
	\Entrada{Entrada do Algoritmo}
	\Saida{Saida do Algoritmo}
	\Inicio{
		Atribua os valores dos parâmetros\;
		Inicialize as trilhas de feromônios\;
		\Enqto{não atingir o critério de parada}{
			\Para{cada formiga}{
				Construa as Soluções\;
			}
			Aplique Busca Local (Opcional)\;
			Atualize o Feromônio\;
		}	
	}
\end{algorithm}
```

# Atenção

O UniforTeX2 é fornecido gratuitamente e sem garantias e pode ser redistribuído livremente para fins acadêmicos. O UniforTeX2 é um produto extra-oficial e não está oficialmente vinculada à Universidade de Fortaleza - Unifor.
