# main.py
import env
from graph import graph
import os

# --- PASTE YOUR LATEX HERE ---
# (Example: A snippet of a physics paper)
dummy_tex = r"""
%% Converted from AAAI 2026 template to ACM conference format
%% Original file: anonymous-submission-latex-2026.tex
%% Converted to ACM manuscript format with line numbering

%%
%% The first command in your LaTeX source must be the \documentclass
%% command.
%%
%% For submission and review of your manuscript please change the
%% command to \documentclass[manuscript, screen, review]{acmart}.
%%
%% When submitting camera ready or to TAPS, please change the command
%% to \documentclass[sigconf]{acmart} or whichever template is required
%% for your publication.
%%
\documentclass[manuscript,screen,review]{acmart}

%%
%% Mathematical packages (converted from AAAI)
%%
\usepackage{amsmath, amsfonts, amssymb, amsthm}

%%
%% Algorithm packages (kept from AAAI)
%%
\usepackage{algorithm}
\usepackage{algpseudocode}

%%
%% Additional packages (converted from AAAI)
%%
\usepackage[utf8]{inputenc}
\usepackage{textgreek}
\usepackage{xcolor}        % for colorbox support
\usepackage{float}
\usepackage{subcaption}
% for [H] positioning

%%
%% Listing support (converted from AAAI)
%%
\usepackage{newfloat}
\usepackage{listings}
\DeclareCaptionStyle{ruled}{labelfont=normalfont,labelsep=colon,strut=off}
\lstset{%
	basicstyle={\footnotesize\ttfamily},% footnotesize acceptable for monospace
	numbers=left,numberstyle=\footnotesize,xleftmargin=2em,% show line numbers
	aboveskip=0pt,belowskip=0pt,%
	showstringspaces=false,tabsize=2,breaklines=true}
\floatstyle{ruled}
\newfloat{listing}{tb}{lst}{}
\floatname{listing}{Listing}

%%
%% \BibTeX command to typeset BibTeX logo in the docs
%%
\AtBeginDocument{%
  \providecommand\BibTeX{{%
    Bib\TeX}}}

%%
%% Rights management information. Replace SAMPLE values with actual information
%% when you complete the rights form.
%%
\setcopyright{acmlicensed}
\copyrightyear{2026}
\acmYear{2026}
\acmDOI{XXXXXXX.XXXXXXX}

%%
%% These commands are for a PROCEEDINGS abstract or paper.
%% Replace with actual conference information
%%
\acmConference[Conference acronym 'XX]{Make sure to enter the correct
  conference title from your rights confirmation email}{Month DD--DD,
  2026}{City, Country}

%%
%% Uncomment \acmBooktitle if the title of the proceedings is different
%% from ``Proceedings of ...''!
%%
%\acmBooktitle{Conference '26: ACM Conference Name,
%  Month DD--DD, 2026, City, Country}

\acmISBN{978-1-4503-XXXX-X/2026/MM}

%%
%% Submission ID.
%% Use this when submitting an article to a sponsored event. You'll
%% receive a unique submission ID from the organizers
%% of the event, and this ID should be used as the parameter to this command.
%%
%\acmSubmissionID{123-A56-BU3}

%%
%% For managing citations, it is recommended to use bibliography
%% files in BibTeX format.
%%
%% You can then either use BibTeX with the ACM-Reference-Format style,
%% or BibLaTeX with the acmnumeric or acmauthoryear sytles, that include
%% support for advanced citation of software artefact from the
%% biblatex-software package, also separately available on CTAN.
%%

%%
%% The majority of ACM publications use numbered citations and
%% references.  The command \citestyle{authoryear} switches to the
%% "author year" style.
%%
%% If you are preparing content for an event
%% sponsored by ACM SIGGRAPH, you must use the "author year" style of
%% citations and references.
%% Uncommenting the next command will enable that style.
%%
%\citestyle{acmauthoryear}

%%
%% end of the preamble, start of the body of the document source.
%%
\begin{document}

%%
%% The "title" command has an optional parameter,
%% allowing the author to define a "short title" to be used in page headers.
%%
\title{Trust-proof Decentralized Learning to Collaborate}

%%
%% The "author" command and its associated commands are used to define
%% the authors and their affiliations.
%% Of note is the shared affiliation of the first two authors, and the
%% "authornote" and "authornotemark" commands
%% used to denote shared contribution to the research.
%%
% \author{First Author}
% \authornote{Both authors contributed equally to this research.}
% \email{first.author@institution.edu}
% \orcid{0000-0000-0000-0000}
% \author{Second Author}
% \authornotemark[1]
% \email{second.author@institution.edu}
% \affiliation{%
%   \institution{Institution Name}
%   \streetaddress{Street Address}
%   \city{City}
%   \state{State}
%   \country{Country}
%   \postcode{Postal Code}
% }

% \author{Third Author}
% \affiliation{%
%   \institution{Another Institution}
%   \streetaddress{Another Street Address}
%   \city{Another City}
%   \state{Another State}
%   \country{Another Country}
%   \postcode{Another Postal Code}
% }
% \email{third.author@another-institution.edu}

%%
%% By default, the full list of authors will be used in the page
%% headers. Often, this list is too long, and will overlap
%% other information printed in the page headers. This command allows
%% the author to define a more concise list
%% of authors' names for this purpose.
%%
\renewcommand{\shortauthors}{Author et al.}

%%
%% The abstract is a short summary of the work to be presented in the
%% article.
%%
\begin{abstract}
Traditional committee‐based blockchain consensus schemes either rely on stake‐weighted elections or on reputation systems, both of which struggle to remain fair when nodes contribute unequally heterogeneous compute and data.  We propose FairRank-L2C, a fully decentralised committee-selection framework that couples Learning-to-Collaborate (L2C) meta-learning with a gossip-based reputation protocol.  Each node trains a local model on its private, task-specific data, broadcasts only parameter deltas to randomly chosen neighbours, and aggregates received updates through a soft attention matrix alpha that is jointly optimised to maximise each node’s validation loss drop.  The loss-improvement achieved after every gossip round is accumulated into a scalar performance score; after T rounds the top-k scorers are deterministically elected to the next consensus committee.  Because scores derive from verifiable model behaviour rather than stake or identity, FairRank-L2C resists Sybil attacks, privileges genuinely useful contributors, and adapts as task distributions drift. 
\end{abstract}
\maketitle

\section{Introduction}
\input{sections/intro}

\section{Related Work}
\input{sections/related}


\section{Preliminaries and Model}
This section lays the groundwork for our proposed framework. The core architecture on which our system is built is a multi-layer blockchain architecture and decentralised machine learning.
\subsection{Dual Layer Consensus Architectures}
% \begin{enumerate}
% \item Dual-Layer Consensus refers to a consensus mechanism that operates in two coordinated phases, each designed to perform a distinct role in securing and finalizing the state of a distributed ledger.

% \item The first layer focuses on selection or sampling.
% This stage typically identifies which nodes, committees, or leaders will participate in block or model proposal.
% Common techniques include stake-weighted sampling, verifiable random functions (VRFs), or reputation-based filtering.
% Its purpose is to fairly and unpredictably choose a responsible subset of the network while reducing communication overhead.

% \item The second layer performs the agreement or finalization process.
% Once a proposer or committee is selected, this phase executes the actual consensus protocol—often a Byzantine Fault Tolerant (BFT) method—to validate, vote on, and finalize proposals.
% It ensures that all honest nodes reach the same ordering of events, blocks, or model updates.

% \item Both layers operate within a single blockchain or distributed ledger, meaning no separate L1/L2 chains are introduced.
% The layering occurs inside the consensus algorithm—not in the blockchain architecture.
% This internal separation allows the network to scale without compromising consistency or security.

% \item This design improves efficiency by reducing the number of nodes involved in communication-heavy finalization steps.
% By delegating the initial selection task to the first layer, the second layer works only with a smaller, representative set of nodes, lowering latency and bandwidth requirements.

% \item Dual-Layer Consensus also strengthens security and fairness.
% The selection layer prevents adversaries from predicting or influencing which nodes will participate, while the agreement layer guarantees deterministic or probabilistic finality.
% The separation of these roles makes coordinated attacks significantly harder.

% \item Many modern DLT systems use dual-layer designs, even if implemented differently.
% Examples include Algorand’s combination of VRF-based committee election with Byzantine Agreement, or Hedera’s separation of gossip propagation from virtual voting.
% Although their internal mechanisms vary, the conceptual two-layer structure is consistent.

% \item Dual-Layer Consensus is especially valuable for advanced applications such as AI-assisted consensus, federated learning, and model aggregation.
% The selection layer can identify suitable participants based on stake, reputation, or computational capability, while the finalization layer ensures that aggregated outputs are agreed upon and immutable.

% \end{enumerate}


Dual-layer consensus is a consensus design in which the agreement process is divided into two coordinated phases, each responsible for a different aspect of block production. The first layer focuses on selection—identifying which nodes, committees, or leaders are eligible to participate in a given round. This stage often uses mechanisms such as verifiable randomness, stake weighting, or reputation scores to ensure fairness and unpredictable participation.
The second layer performs the actual agreement on the proposed block or state update. This stage typically employs a Byzantine Fault Tolerant (BFT) protocol or a similar voting-based mechanism to finalize results in a secure and fault-tolerant manner. By separating selection from agreement, dual-layer consensus reduces communication overhead, improves scalability, and limits the influence of malicious participants.
Our framework is a dual-layer consensus architecture. This approach is inspired the Hedera consensus algorithm, which uses a "stem" chain for block production (L1) and a "leaf" committee (L2) to perform BFT for high transaction throughput. In our model, the L2C and ranking process (Layer 1) serves as the mechanism to elect the high-performance committee that will execute consensus (Layer 2).

Whereas a multi-layer blockchain architecture enhances scalability and efficiency by segregating tasks, where instead of putting all the heavy computation in one layer, we break it down into multiple layers, each doing its job quietly in the background.

% Typically, this involves:
% \begin{enumerate}
%     \item Layer 1 (L1): This is the primary blockchain that provides decentralisation and final settlement of transactions. It provides core consensus and on-chain data management. Some of the popular examples for Layer 1 blockchains are Bitcoin, Ethereum and Solana.
    
%     \item Layer 2 (L2): One or more secondary protocols or "off-chain" solutions that are built on top of Layer 1. L2S are designed to handle high-volume computations and transactions, which are processed quickly before anchoring a summary or proof back to the L1. Solutions like Polygon and Arbitrum are Layer 2 (L2) solutions, built on top of Ethereum (L1).
% \end{enumerate}

% Our framework is a dual-layer consensus architecture. This approach is inspired the Hedera consensus algorithm, which uses a "stem" chain for block production (L1) and a "leaf" committee (L2) to perform BFT for high transaction throughput. In our model, the L2C and ranking process (Layer 1) serves as the mechanism to elect the high-performance committee that will execute consensus (Layer 2).

\subsection{Decentralised Federated Learning (DFL)}
Decentralised Machine Learning, and particularly Decentralised Federated Learning (DFL), is a training process that removes the need for a central coordinating server. In this model the data remains on the private, local devices of each participant (or node) who  train a local model on their own data. Instead of sending raw data, nodes exchange model information (parameter updates or deltas) directly with their peers. Each node aggregates the information received from its peers to update and improve its own model. Unlike usual DML, here the aggregation is not a simple average instead, each node learns whom to trust based on their contribution to model performance.

\subsection{Layer 1 Model Explanation}
The diagrams below illustrate our model's Layer 1 operation.
\begin{itemize}
    \item \textbf{\ref{fig:local_training} Local Training Phase.}: Here, each client possesses its own private, local dataset ($D_i$). They use this data to train a local model (e.g., a CNN). The outcome of this local training, as described in \ref{alg:l2c-localtraining}, is the computation of ``delta'' ($\Delta_i$). This delta represents the changes to the model's parameters based on that client's unique data.

    \item \textbf{\ref{fig:decentralized_aggregation} Decentralised Aggregation Phase.} This diagram illustrates the collaborative, peer-to-peer interaction. The central node $i$ receives the parameter deltas ($\Delta_j$) from its neighbouring nodes $j$. Node $i$ then applies its own learned ``trust weights'' ($w_i[j]$) to each incoming delta. This process, detailed in \ref{alg:l2c-client}, is the core of the L2C mechanism: node $i$ is not treating all neighbours equally. It performs a weighted aggregation of the deltas ($\Delta_{agg,i}$) to create an improved model, learning to prioritise updates from peers that verifiably improve its performance.
\end{itemize}
% \begin{figure}[H]
%   \centering
%   \includegraphics[width=\linewidth/1.5]{L2C paper.png}
%   \caption{1907 Franklin Model D roadster. Photograph by Harris \&
%     Ewing, Inc. [Public domain], via Wikimedia
%     Commons. (\url{https://goo.gl/VLCRBB}).}
%   \Description{A woman and a girl in white dresses sit in an open car.}


%   \centering
%   \includegraphics[width=\linewidth]{L2C paper (1).png}
%   \caption{1907 Franklin Model D roadster. Photograph by Harris \&
%     Ewing, Inc. [Public domain], via Wikimedia
%     Commons. (\url{https://goo.gl/VLCRBB}).}
%   \Description{A woman and a girl in white dresses sit in an open car.}
% \end{figure}
% \begin{figure}[H]
%     \centering
    
%     % First Subfigure
%     \begin{subfigure}[b]{0.48\textwidth}
%         \centering
%         \includegraphics[width=\linewidth]{L2C paper.png}
%         \caption{Local Training Phase. Each client computes a parameter delta ($\Delta_i$) from its local data $D_i$.}
%         \Description{A diagram showing three clients, each with local data, training a CNN model to compute a parameter delta.}
%         \label{fig:local_training}
%     \end{subfigure}
%     \hfill % This adds a flexible horizontal space between the figures
    
%     % Second Subfigure
%     \begin{subfigure}[b]{0.48\textwidth}
%         \centering
%         \includegraphics[width=\linewidth]{L2C paper (1).png}
%         \caption{Decentralized Aggregation Phase. Node $i$ receives deltas ($\Delta_j$) from peers and applies learned trust weights ($w_i[j]$).}
%         \Description{A network graph showing a central node 'i' receiving deltas from neighboring nodes 'j' and applying weights to them.}
%         \label{fig:decentralized_aggregation}
%     \end{subfigure}
%     \label{fig:model_overview}
% \end{figure}
\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\linewidth]{L2C paper.png}
        \caption{Local Training Phase. Each client computes a parameter delta ($\Delta_i$) from its local data $D_i$.}
        \label{fig:local_training}
    \end{subfigure}
    \hspace{0.02\textwidth} % small space between the images
    \begin{subfigure}[b]{0.49\textwidth}
        \centering
        \includegraphics[width=\linewidth]{L2C paper (1).png}
        \caption{Decentralized Aggregation Phase. Node $i$ receives deltas ($\Delta_j$) from peers and applies learned trust weights ($w_i[j]$).}
        \label{fig:decentralized_aggregation}
    \end{subfigure}
    \caption{Model Overview}
    \label{fig:model_overview}
\end{figure}

\section{Convergence theory of decentralised FL}
\section{Lower Bound for Trust-proof Ranking}
\section{Trust-proof Learning to Collaborate}
% \section{Algorithm}
% \begin{algorithm}[H]
% \caption{\textsc{L2C} with \colorbox{red!20}{Lexicographic Committee}}
% \label{alg:trust-proof-l2c}
% \begin{algorithmic}[1]

% \Require 
% \Statex \hspace*{1em} $N (nodes), R (rounds), S (local epochs), K (committee size) \in \mathbb{N}$, $\eta, \beta > 0$
% \Statex \hspace*{1em} $\mathcal{D}^{train} = \{\mathcal{D}_i\}_{i=1}^N$ (non-IID)
% \Statex \hspace*{1em} SimpleCNN, $\mathcal{L} = \text{CrossEntropy}$
% \Ensure $\{\text{score}_i\}_{i=1}^N$, committee $\mathcal{C} \subset \{1,\ldots,N\}$, $|\mathcal{C}| = K$

% \State \textbf{Initialize} $\{\theta_i^{(0)}\}_{i=1}^N$ and $\{\alpha_i\}_{i=1}^N$
% \State $\theta_i^{(0)} \leftarrow \text{SimpleCNN}()$, $\forall i \in [N]$
% \State $\alpha \in \mathbb{R}^{N \times N}$ with $\alpha_{i,j} \sim \mathcal{N}(0,1)$  
% \State $\text{score}_i \leftarrow 0$, $\forall i \in [N]$

% \For{$t = 1 : R$}
%     \For{$i = 1 : N$} \Comment{Local training phase}
%         \State $L_{\text{before}}(i) \leftarrow \mathcal{L}(\theta_i^{(t-1)}, \mathcal{D}_i)$
%         \State $\theta_{\text{pre}}(i) \leftarrow \theta_i^{(t-1)}$
%         \For{$s = 1 : S$} \Comment{Local SGD steps}
%             \State $\theta_i^{(t-1)} \leftarrow \theta_i^{(t-1)} - \eta \cdot \nabla_\theta \mathcal{L}(\theta_i^{(t-1)}, \mathcal{D}_i)$
%         \EndFor
%         \State $\Delta(i) \leftarrow \theta_i^{(t-1)} - \theta_{\text{pre}}(i)$
%     \EndFor
    
%     \State \Comment{Trust weights calculation}
%     \For{$i = 1 : N$}
%         \For{$j = 1 : N$}
%             \State $w_{i,j} \leftarrow \frac{\exp(\alpha_{i,j})}{\sum_{k=1}^N \exp(\alpha_{i,k})}$
%         \EndFor
%     \EndFor
    
%     \State $\nabla_\alpha \leftarrow \mathbf{0}_{N \times N}$
%     \For{$i = 1 : N$} \Comment{Aggregation \& meta-update}
%         \State $\Delta_{\text{agg}}(i) \leftarrow \sum_{j=1}^N w_{i,j} \cdot \Delta(j)$
%         \State $\theta'(i) \leftarrow \theta_{\text{pre}}(i) + \Delta_{\text{agg}}(i)$
%         \State $L_{\text{after}}(i) \leftarrow \mathcal{L}(\theta'(i), \mathcal{D}_i)$
%         \State $\Delta L(i) \leftarrow L_{\text{before}}(i) - L_{\text{after}}(i)$
%         \State \colorbox{yellow!30}{$\text{score}_i \leftarrow \text{score}_i + \max(\Delta L(i), 0)$}
%         \For{$j = 1 : N$}
%             \State $\nabla_\alpha[i,j] \leftarrow \nabla_\alpha[i,j] - \Delta L(i) \cdot w_{i,j} \cdot (1 - w_{i,j})$
%         \EndFor
%     \EndFor
    
%     \State $\alpha \leftarrow \alpha - \beta \cdot \nabla_\alpha$ \Comment{Update trust parameters}
% \EndFor

% \State \Comment{Gossip score sharing}
% \State $\mathbf{S}_{\text{vec}} \leftarrow (\text{score}_1, \ldots, \text{score}_N)$

% \State \Comment{Preference vectors}
% \For{$i = 1 : N$}
%     \State $P_i \leftarrow \text{argsort}_{\text{desc}}(\mathbf{S}_{\text{vec}}) \in \{1,\ldots,N\}^N$
% \EndFor

% \State \Comment{Position vectors}
% \For{$j = 1 : N$}
%     \State $p_j \in \mathbb{N}^N$ with $p_{j,i} \leftarrow \text{rank of } j \text{ in } P_i$ (1-indexed)
%     \If{$j \notin P_i$}
%         \State $p_{j,i} \leftarrow |P_i| + 1$
%     \EndIf
% \EndFor

% \State \Comment{Lexicographic ordering}
% \State $\sigma \leftarrow \text{argsort}_{\text{lex}}(\{p_j\}_{j=1}^N)$
% \Statex \hspace*{1em} where $p_j \prec p_k$ iff $\exists r: p_{j,1}=p_{k,1},\ldots,p_{j,r-1}=p_{k,r-1}$ and $p_{j,r} < p_{k,r}$

% \State \Comment{Committee selection}
% \State $\mathcal{C} \leftarrow \text{first } K \text{ indices in } \sigma$

% \State \Return $\{\text{score}_i\}_{i=1}^N$, $\mathcal{C}$

% \end{algorithmic}
% \end{algorithm}
% \section{Algorithm}

% --- PART 1: Client Side (till score computation) ---
% \begin{algorithm}[H]
% \caption{\textsc{L2C} Client-Side: Local Training and Score Computation}
% \label{alg:l2c-client}
% \begin{algorithmic}[1]
% \Require 
%     $N$ (nodes), $R$ (rounds), $S$ (local epochs), $K$ (committee size) $\in \mathbb{N}$, $\eta, \beta > 0$ \\
%     $\mathcal{D}^{train} = \{\mathcal{D}_i\}_{i=1}^N$ (non-IID), \textbf{SimpleCNN}, $\mathcal{L} = \text{CrossEntropy}$
% \Ensure $\{\text{score}_i\}_{i=1}^N$
% \State \textbf{Initialize} $\{\theta_i^{(0)}\}_{i=1}^N$
%     \State $\theta_i^{(0)} \gets \text{SimpleCNN}()$
% \EndFor
% \State $\alpha \in \mathbb{R}^{N \times N}$ with $\alpha_{i,j} \sim \mathcal{N}(0,1)$
% \State $\text{score}_i \gets 0$ for all $i$
% \For{$t = 1 : R$}
%     \For{$i = 1 : N$} \Comment{Local training phase for all N}
%         \State $L_{\text{before}}(i) \gets \mathcal{L}(\theta_i^{(t-1)}, \mathcal{D}_i)$
%         \State $\theta_{\text{pre}}(i) \gets \theta_i^{(t-1)}$
%         \For{$s = 1 : S$} \Comment{Local SGD steps}
%             \State $\theta_i^{(t-1,s)} \gets \theta_i^{(t-1)} - \eta \cdot \nabla_\theta \mathcal{L}(\theta_i^{(t-1,s-1)}, \mathcal{D}_i)$
%         \EndFor
%         \State $\Delta(i) \gets \theta_i^{(t-1,S)} - \theta_{\text{pre}}(i)$

%     \EndFor

%     \For{$i = 1 : N$} \Comment{Trust weights calculation}
%         \For{$j = 1 : N$} (locally by client i)
%             \State $w_{i,j} \gets \dfrac{\exp(\alpha_{i,j})}{\sum_{k=1}^N \exp(\alpha_{i,k})}$
%         \EndFor
%     \EndFor

%     \State $\nabla_\alpha \gets \mathbf{0}_{N \times N}$
%     \For{$i = 1 : N$} \Comment{Aggregation \& meta-update}
%         \State $\Delta_{\mathrm{agg}}(i) \gets \sum_{j=1}^N w_{i,j} \cdot \Delta(j)$
%         \State $\theta'(i) \gets \theta_{\text{pre}}(i) + \Delta_{\mathrm{agg}}(i)$
%         \State $L_{\text{after}}(i) \gets \mathcal{L}(\theta'(i), \mathcal{D}_i)$
%         \State $\Delta L(i) \gets L_{\text{before}}(i) - L_{\text{after}}(i)$
%         \State \colorbox{yellow!30}{$\text{score}_i \gets \text{score}_i + \max(\Delta L(i), 0)$}
%         \For{$j = 1 : N$}
%             \State $\nabla_\alpha[i,j] \gets \nabla_\alpha[i,j] - \Delta L(i) \cdot w_{i,j} \cdot (1 - w_{i,j})$
%         \EndFor
%     \EndFor
%     \State $\alpha \gets \alpha - \beta \cdot \nabla_\alpha$ \Comment{Update trust parameters}
% \EndFor
% \end{algorithmic}
% \end{algorithm}






% \section{Algorithm}
% % --- PART 1: Client Side (till score computation) ---
% \begin{algorithm}[H]
% \caption{\textsc{L2C} Client-Side: Local Training and Score Computation}
% \label{alg:l2c-client}
% \begin{algorithmic}[1]
% \Require 
%     $N$ (nodes), $R$ (rounds), $S$ (local epochs), $K$ (committee size) $\in \mathbb{N}$, $\eta, \beta > 0$ \\
%     $\mathcal{D}^{train} = \{\mathcal{D}_i\}_{i=1}^N$ (non-IID), \textbf{SimpleCNN}, $\mathcal{L} = \text{CrossEntropy}$, $\mathcal{N}_i \subseteq \{1,2,\ldots,N\}$ (neighborhood of node $i$)
% \Ensure $\{\text{score}_i\}_{i=1}^N$
% \State \textbf{Initialize}
%     \State $\{\theta_i^{(0)}\}_{i=1}^N \gets \text{SimpleCNN}()$
%     \State $\boldsymbol{\alpha}_i \in \mathbb{R}^{|\mathcal{N}_i|}$ with $\alpha_{i,j} \sim \mathcal{N}(0,1)$ for $j \in \mathcal{N}_i$ \Comment{Local storage only}
%     \State $\mathbf{w}_i \gets \{\mathbf{0}\}^{|\mathcal{N}_i|}$ for all $i \in \{1,\ldots,N\}$ \Comment{Initialize trust weight vectors}
%     \State $\nabla_{\boldsymbol{\alpha}_i} \gets \mathbf{0}_{|\mathcal{N}_i|}$ for all $i \in \{1,\ldots,N\}$ \Comment{Zero vector initialization}
%     \State $\text{score}_i \gets 0$ for all $i \in \{1,\ldots,N\}$
% \For{$t = 1, 2, \ldots, R$}
%     \For{$i = 1, 2, \ldots, N$} \Comment{Local training phase}
%         \State $[L_{\text{before}}(i), \theta_{\text{pre}}(i), \Delta_i] \gets $ \Call{LocalTrainingPhase}{$i, t, S$} \Comment{See Algorithm~\ref{alg:l2c-localtraining}}
%     \EndFor
%     \For{$i = 1, 2, \ldots, N$} \Comment{Trust weights and aggregation}
%         \State $Z_i \gets \sum_{k \in \mathcal{N}_i} \exp(\alpha_{i,k})$ \Comment{Normalization constant}
%         \For{$j \in \mathcal{N}_i$}
%             \State $\mathbf{w}_i[j] \gets \frac{\exp(\alpha_{i,j})}{Z_i}$ \Comment{Softmax weights}
%         \EndFor
%         \State \textbf{Receive} $\Delta_j$ \textbf{from all} $j \in \mathcal{N}_i$ \Comment{Receive local model updates from neighbors}
%         \State $\Delta_{\mathrm{agg},i} \gets \sum_{j \in \mathcal{N}_i} w_{i,j} \cdot \Delta_j$
%         \State $\theta'_i \gets \theta_{\text{pre}}(i) + \Delta_{\mathrm{agg},i}$
%         \State $L_{\text{after}}(i) \gets \mathcal{L}(\theta'_i, \mathcal{D}_i)$
%         \State $\Delta L_i \gets L_{\text{before}}(i) - L_{\text{after}}(i)$
%         \State \colorbox{yellow!30}{$\text{score}_i \gets \text{score}_i + \max(\Delta L_i, 0)$}
%         \For{$j \in \mathcal{N}_i$} \Comment{Gradient computation}
%             \State $\nabla_{\boldsymbol{\alpha}_i}[j] \leftarrow \nabla_{\boldsymbol{\alpha}_i}[j] - \Delta L_i \cdot w_{i,j} \cdot (1 - w_{i,j})$
%         \EndFor
%     \EndFor
%     \State $\boldsymbol{\alpha}_i \gets \boldsymbol{\alpha}_i - \beta \cdot \nabla_{\boldsymbol{\alpha}_i}$ for all $i \in \{1,\ldots,N\}$ \Comment{Vector update}
% \EndFor
% \end{algorithmic}
% \end{algorithm}

% % --- PART 1a: Local Training Phase ---
% \begin{algorithm}[H]
% \caption{Local Training Phase}
% \label{alg:l2c-localtraining}
% \begin{algorithmic}[1]
% \Require $i \in \{1,\ldots,N\}$, $t \in \{1,\ldots,R\}$, $S \in \mathbb{N}$
% \Ensure $L_{\text{before}}(i)$, $\theta_{\text{pre}}(i)$, $\Delta_i$
% \State $L_{\text{before}}(i) \gets \mathcal{L}(\theta_i^{(t-1)}, \mathcal{D}_i)$
% \State $\theta_{\text{pre}}(i) \gets \theta_i^{(t-1)}$
% \State $\theta_{\text{temp}} \gets \theta_i^{(t-1)}$
% \For{$s = 1, 2, \ldots, S$} \Comment{Local SGD iterations}
%     \State $\theta_{\text{temp}} \gets \theta_{\text{temp}} - \eta \cdot \nabla_\theta \mathcal{L}(\theta_{\text{temp}}, \mathcal{D}_i)$
% \EndFor
% \State $\Delta_i \gets \theta_{\text{temp}} - \theta_{\text{pre}}(i)$
% \State \Return $L_{\text{before}}(i), \theta_{\text{pre}}(i), \Delta_i$
% \end{algorithmic}
% \end{algorithm}




\section{Algorithm}
% --- PART 1: Client Side (till score computation) ---
\begin{algorithm}[H]
\caption{\textsc{L2C} Client-Side: Local Training and Score Computation}
\label{alg:l2c-client}
\begin{algorithmic}[1]
\Require 
    $N$ (nodes), $R$ (rounds), $S$ (local epochs), $K$ (committee size) $\in \mathbb{N}$, $\eta, \beta > 0$ \\
    $\mathcal{D}^{train} = \{\mathcal{D}_i\}_{i=1}^N$ (non-IID), \textbf{SimpleCNN}, $\mathcal{L} = \text{CrossEntropy}$, $\mathcal{N}_i \subseteq \{1,2,\ldots,N\}$ (neighborhood of node $i$)
\Ensure $\{\text{score}_i\}_{i=1}^N$
\State \textbf{Initialize}
    \State $\{\theta_i^{(0)}\}_{i=1}^N \gets \text{SimpleCNN}()$
    \State $\boldsymbol{\alpha}_i \in \mathbb{R}^{|\mathcal{N}_i|}$ with $\alpha_{i,j} \sim \mathcal{N}(0,1)$ for $j \in \mathcal{N}_i$ \Comment{Local storage only}
    \State $\mathbf{w}_i \gets \{\mathbf{0}\}^{|\mathcal{N}_i|}$ for all $i \in \{1,\ldots,N\}$ \Comment{Initialize trust weight vectors}
    \State $\nabla_{\boldsymbol{\alpha}_i} \gets \{\mathbf{0}\}^{|\mathcal{N}_i|}$ for all $i \in \{1,\ldots,N\}$ \Comment{Zero vector initialization}
    \State $\text{score}_i \gets 0$ for all $i \in \{1,\ldots,N\}$
\For{$t = 1, 2, \ldots, R$}
    \For{$i = 1, 2, \ldots, N$} \Comment{Local training phase}
        \State $[L_{\text{before}}(i), \theta_{\text{pre}}(i), \Delta_i] \gets $ \Call{LocalTrainingPhase}{$i, t, S$} \Comment{See Algorithm~\ref{alg:l2c-localtraining}}
    \EndFor
    \For{$i = 1, 2, \ldots, N$} \Comment{Trust weights and aggregation}
        \State $Z_i \gets \sum_{k \in \mathcal{N}_i} \exp(\alpha_{i,k})$ \Comment{Normalization constant}
        \For{$j \in \mathcal{N}_i$}
            \State $\mathbf{w}_i[j] \gets \frac{\exp(\alpha_{i,j})}{Z_i}$ \Comment{Softmax weights}
        \EndFor
        \State \textbf{Receive} $\Delta_j$ \textbf{from all} $j \in \mathcal{N}_i$ 
        \State $\Delta_{\mathrm{agg},i} \gets \sum_{j \in \mathcal{N}_i} \mathbf{w}_i[j] \cdot \Delta_j$
        \State $\theta'_i \gets \theta_{\text{pre}}(i) + \Delta_{\mathrm{agg},i}$
        \State $L_{\text{after}}(i) \gets \mathcal{L}(\theta'_i, \mathcal{D}_i)$
        \State $\Delta L_i \gets L_{\text{before}}(i) - L_{\text{after}}(i)$
        \State \colorbox{yellow!30}{$\text{score}_i \gets \text{score}_i + \max(\Delta L_i, 0)$}
        \For{$j \in \mathcal{N}_i$} \Comment{Gradient computation}
            \State $\nabla_{\boldsymbol{\alpha}_i}[j] \leftarrow \nabla_{\boldsymbol{\alpha}_i}[j] - \Delta L_i \cdot \mathbf{w}_i[j] \cdot (1 - \mathbf{w}_i[j])$
        \EndFor
    \State $\boldsymbol{\alpha}_i \gets \boldsymbol{\alpha}_i - \beta \cdot \nabla_{\boldsymbol{\alpha}_i}$ for all $i \in \{1,\ldots,N\}$ \Comment{Vector update}
    \EndFor
    \Comment{See Algorithm~\ref{alg:l2c-decentralized}}
\EndFor
\end{algorithmic}
\end{algorithm}

% --- PART 1a: Local Training Phase ---
\begin{algorithm}[H]
\caption{Local Training Phase}
\label{alg:l2c-localtraining}
\begin{algorithmic}[1]
\Require $i $, $\theta_i^{(t-1)}$, $\mathcal{D}_i$
\Ensure $L_{\text{before}}(i)$, $\theta_{\text{pre}}(i)$, $\Delta_i$
\State $L_{\text{before}}(i) \gets \mathcal{L}(\theta_i^{(t-1)}, \mathcal{D}_i)$
\State $\theta_{\text{pre}}(i) \gets \theta_i^{(t-1)}$
\State $\theta_{\text{temp}} \gets \theta_i^{(t-1)}$
\For{$s = 1, 2, \ldots, S$} \Comment{Local SGD iterations}
    \State $\theta_{\text{temp}} \gets \theta_{\text{temp}} - \eta \cdot \nabla_\theta \mathcal{L}(\theta_{\text{temp}}, \mathcal{D}_i)$
\EndFor
\State $\Delta_i \gets \theta_{\text{temp}} - \theta_{\text{pre}}(i)$
\State \Return $L_{\text{before}}(i), \theta_{\text{pre}}(i), \Delta_i$
\end{algorithmic}
\end{algorithm}




% --- PART 2: Decentralized Process (Gossip, Lexicographic Ordering, Committee Selection) ---
\begin{algorithm}[H]
\caption{\textsc{L2C} Decentralized Process: Committee Selection via Lexicographic Committee}
\label{alg:l2c-decentralized}
\begin{algorithmic}[1]
\Require $\{\text{score}_i\}_{i=1}^N$, $K$
\Ensure committee $\mathcal{C} \subset \{1, \ldots, N\}$, $|\mathcal{C}| = K$
\State $\mathbf{S}_{\text{vec}} \gets (\text{score}_1, \ldots, \text{score}_N)$  \Comment{Gossip score sharing}
\For{$i = 1 : N$}
    \State $P_i \gets \text{argsort}_{\text{desc}}(\mathbf{S}_{\text{vec}})$ \Comment{Preference vectors}
\EndFor
\For{$j = 1 : N$}
    \State $p_j \in \mathbb{N}^N$ with $p_{j,i} \gets \text{rank of } j \text{ in } P_i$ (1-indexed)
    \If{$j \notin P_i$}
        \State $p_{j,i} \gets |P_i| + 1$
    \EndIf
\EndFor
\State $\sigma \gets \text{argsort}_{\text{lex}}(\{p_j\}_{j=1}^N)$ \Comment{Lexicographic ordering}
\Statex \hspace*{1em} where $p_j \prec p_k$ iff $\exists r:~p_{j,1}=p_{k,1}, \ldots, p_{j,r-1}=p_{k,r-1}$ \& $p_{j,r} < p_{k,r}$
\State $\mathcal{C} \gets$ first $K$ indices in $\sigma$ \Comment{Committee selection}
\State \Return $\{\text{score}_i\}_{i=1}^N$, $\mathcal{C}$
\end{algorithmic}
\end{algorithm}

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \begin{algorithm}[H]
% \caption{Client Process (decentralized FL node)}
% \SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}
% \Input{$id,\, data,\, labels,\, model_0,\, R,\, K,\, B,\, \eta,\, dev$}
% \Output{final committee for node $id$}
% \BlankLine
% \textbf{Init:} $\texttt{loader}\leftarrow \texttt{DataLoader}(\texttt{TensorDataset}(data,labels),B,\texttt{shuffle}=True)$; 
% $M \leftarrow \texttt{clone}(model_0)\to dev$\;
% \For{$r \leftarrow 1$ \KwTo $R$}{
%   \tcp{Pre-train eval}
%   $\textit{val}_0 \leftarrow \texttt{AvgLoss}(M,\texttt{loader},3)$;\;
%   $\textit{acc}_0 \leftarrow \texttt{Acc}(M,\texttt{loader},3)$;\;
%   \tcp{Local SGD (3 epochs)}
%   $\texttt{opt} \leftarrow \texttt{SGD}(M.\texttt{params}(), \eta)$;\;
%   $S_0 \leftarrow \texttt{copy\_state}(M)$;\;
%   \For{$e \leftarrow 1$ \KwTo $3$}{
%     \ForEach{$(x,y)\in \texttt{loader}$}{
%       $x,y \leftarrow \texttt{to}(dev)$;\;
%       $\texttt{opt.zero\_grad}()$;\;
%       $o \leftarrow M(x)$;\;
%       $\ell \leftarrow \texttt{CE}(o,y)$;\;
%       $\ell.\texttt{backward}();\ \texttt{opt.step}()$;\;
%     }
%   }
%   $S_1 \leftarrow \texttt{copy\_state}(M)$;\;
%   \tcp{Form delta and send}
%   $\Delta \leftarrow S_1 - S_0$;\;
%   \texttt{send}$(id,\Delta,\textit{val}_0,\textit{acc}_0)$;\;
%   $(w,\Delta^{\mathrm{agg}}) \leftarrow \texttt{recv}(id)$;\;
%   \tcp{Apply aggregated update}
%   $M.\texttt{load\_state}(S_0 + \Delta^{\mathrm{agg}})$;\;
%   \tcp{Post-agg eval and report}
%   $\textit{val}_1 \leftarrow \texttt{AvgLoss}(M,\texttt{loader},3)$;\;
%   $\textit{acc}_1 \leftarrow \texttt{Acc}(M,\texttt{loader},3)$;\;
%   \texttt{sendMetrics}$(id,\textit{val}_1,\textit{acc}_1)$;\;
% }
% \tcp{Decentralized committee selection}
% \texttt{shareScores}$(id,\texttt{score})$;\;
% \texttt{broadcastVec}$(id,\texttt{recScores})$;\;
% \texttt{collectVecs}(id);\;
% \Return $\texttt{lexSelect}(id,\texttt{allVecs},K)$\;
% \end{algorithm}
\subsection{BFT Consensus}

\section{Experiments}
This work presents a two-layer federated learning protocol combined with a distributed lexicographical committee selection mechanism.  
Layer~1 focuses on collaborative model training and adaptive trust-based aggregation. Layer~2 executes decentralized selection of a leaf committee using true lexicographical ordering of peer-shared performance rankings.

\subsection{Layer 1: Adaptive Collaborative Training}

\subsubsection{Data Partitioning and Local Task Assignment}
Each of $N$ nodes with a non-IID local dataset and random classes for a classification problem. No centralized data repository is used; nodes train exclusively on private data.

\subsubsection{Model and Trust Initialization}
\textbf{Model Architecture:} All nodes instantiate an identical convolutional neural network.

\textbf{Trust Matrix:} A trainable square matrix $\boldsymbol{\alpha}_i \in \mathbb{R}^{|\mathcal{N}_i|}$ is initialized with random values. Applying row-wise softmax to $\alpha$ generates collaboration weights $\mathbf{w}_i[j]$ that govern how much node $i$ trusts updates from node $j$.

\subsubsection{Local Training and Delta Computation}
For each communication round:
\begin{enumerate}
    \item \textbf{Evaluation Before Training:} Compute local validation loss $L_{\text{before}}(i)$ and accuracy on the node’s own dataloader.
    \item \textbf{Inner-Loop Training:} Node $i$ trains its model for $S$ local epochs using SGD (learning rate $\eta$), producing post-training weights $\theta_{\text{pre}}(i)$.
    \item \textbf{Update Extraction:}  
    \[
        \Delta_i \gets \theta_{\text{temp}} - \theta_{\text{pre}}(i)
    \]
\end{enumerate}

\subsubsection{Weighted Aggregation and Score Update}
\textbf{Weight Computation:}
\[
    \mathbf{w}_i[j] \gets \frac{\exp(\alpha_{i,j})}{Z_i}.
\]
where
\[
    Z_i \gets \sum_{k \in \mathcal{N}_i} \exp(\alpha_{i,k})
\]
\textbf{Aggregated Update:}
\[
    \Delta_{\mathrm{agg},i} \gets \sum_{j \in \mathcal{N}_i} \mathbf{w}_i[j] \cdot \Delta_j
\]

\textbf{Model Update:} Apply $\Delta_{\mathrm{agg},i}$ to the pre-training weights $\theta_{\text{pre}}(i)$ to obtain $\theta'(i)$.

\textbf{Post-Aggregation Evaluation:} Recompute validation loss $L^{\text{after}}(i)$ and accuracy using $\theta'(i)$.

% \textbf{Contribution Scoring:}
% \[
%     \Delta L(i) = L^{\text{before}}(i) - L^{\text{after}}(i), \quad 
%     \text{score}_i \;+=\; \max(\Delta L(i), 0).
% \]

\noindent\textbf{Contribution Scoring.}
\begin{align}
\Delta L_i \gets L_{\text{before}}(i) - L_{\text{after}}(i), \\
\text{score}_i &\mathrel{+}= \max\!\left(\Delta L(i),\, 0\right).
\end{align}


\subsubsection{Trust Matrix Update}
Compute gradients for $\alpha$ based on the loss reduction:
\[
    \frac{\partial \Delta L(i)}{\partial \alpha_{i,j}} \propto -(1-w_{i,j})w_{i,j},
\]
then perform a gradient step with learning rate $\beta$:
\[
    \alpha \leftarrow \alpha - \beta \nabla_{\alpha}.
\]

\subsection{Layer 2: Decentralized Lexicographical Committee Selection}

\subsubsection{Peer Score Exchange}
Each node broadcasts its cumulative contribution score $\text{score}_i$ to all other nodes in a fully connected topology.

\subsubsection{Local Ranking}
Upon receiving scores, node $i$ sorts peer scores in descending order, forming its local preference vector of node IDs.

\subsubsection{Vector Broadcast}
Nodes broadcast their preference vectors so that every participant obtains all $N$ sorted lists.

\subsubsection{Lexicographical Ordering for Committee Formation}
\textbf{Position Vector:} For each candidate node $j$, construct its position vector $p_j \in \mathbb{N}^N$, where $p_{j,i}$ is the rank of node $j$ in node $i$’s preference list ($1=$ top).

\textbf{Lexicographical Comparison:} Sort all nodes by comparing their position vectors lexicographically (smaller vectors rank higher).

\textbf{Committee Selection:} Choose the top-$K$ nodes ($K=6$) as the leaf committee. This deterministic process ensures consensus without additional rounds or a central authority.
\subsubsection{BFT Consensus}
\section{Committee Switching}
\section{Conclusion}


\cite{c:85} \cite{c:86} \cite{c:87} \cite{c:88} \cite{c:89} \cite{c:90} \cite{c:91} \cite{c:92} \cite{c:95} \cite{c:96}
 \cite{c:97} \cite{c:98} \cite{c:99} \cite{c:100} \cite{c:101} \cite{c:102} \cite{c:103} \cite{c:104} \cite{c:105} \cite{c:106} \cite{c:107} \cite{c:108} \cite{c:109} \cite{c:110} \cite{c:111}

% \bibliography{aaai2026} 
% \bibliographystyle{ieeetr}   % IEEE style [1], [2], etc.
\bibliographystyle{plainnat}
\bibliography{aaai2026}    % your .bib file name
% \cite{c:84}
% \cite{c:85}
% \cite{c:86}
% % \cite{r:80x}



\end{document}

"""

state = {
    "tex_content": dummy_tex,   # <--- Put your real TeX here
    "output_format": "beamer",  # <--- Select 'beamer' or 'pptx'
    "audience": "PhD Researchers"
}

print(f"🚀 Parsing Paper & Building {state['output_format'].upper()} Presentation...")
final_state = graph.invoke(state)

print("\n✅ DONE!")
if state.get("output_format") == "pptx":
    print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
else:
    print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
    print("👉 Download 'presentation.tex' and compile it on Overleaf/LaTeX.")