% mins.sty
% Take minutes of meetings
% 2005-Sept-01 Jim Hefferon jhefferon (at) smcvt.edu
% --- Class structure: identification part
% ---
\ProvidesClass{application_note}[2005/09/01 version 1.00 Minutes of meetings]
\NeedsTeXFormat{LaTeX2e}
\LoadClass[a4paper]{article}
\RequirePackage[a4paper,bindingoffset=0.2in,%
            left=1in,right=1in,top=1.5in,bottom=1in,%
            footskip=.25in, headheight=100pt]{geometry}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{wallpaper}
\RequirePackage{graphicx} %this package used for importing images
\RequirePackage[]{hyperref}
\hypersetup{
    linkbordercolor = {blue},
    linkcolor=[rgb]{0,0.5, 0},
    colorlinks = True,
}
\RequirePackage{fancyhdr}
\RequirePackage{amsmath}

\fancypagestyle{followingpage}{%
\fancyhf{} % clear all six fields
\lhead{\includegraphics[width=5cm]{logo.jpg}} %puts in dataray logo
\rhead{\bfseries Application Note} %puts in dataray logo
\fancyheadoffset[L]{.1\textwidth}% changes the left-right location of the dataray logo


\rfoot{\thepage} %puts in the page number
\cfoot{1675 Market Street, Redding, CA 96001 USA\\
\href{http://www.dataray.com/}{dataray.com} | Tel +1 530 776 0843} %puts in the center footer
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\makeatletter
\let\ps@plain\ps@fancy 
\makeatother

}
\setlength\headsep {10\p@}
\pagestyle{followingpage}
\AtBeginDocument{\thispagestyle{followingpage}}
\LRCornerWallPaper{1}{dataray_footer.png} 
\setlength{\headsep}{0.65in} %sets space between header and text

\makeatletter
\renewcommand{\maketitle}{%
  %\begin{titlepage}
  \begin{center}
    \bfseries \Large \@title \vspace{6ex}
    \end{center}
  %\end{titlepage}
}
\makeatother
\setcounter{secnumdepth}{0}
%\makeatletter
%\renewcommand\section{\@startsection {section}{0}{\z@}%
%                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
%                                   {-1em}%
%                                   {\normalfont\Large\bfseries}}
%\makeatother




