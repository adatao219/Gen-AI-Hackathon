# Gen-AI-Hackathon

This is a project for the Gen-AI Hackathon. The project is a web application that uses machine learning to predict the price of a house based on its features. The application is built using Flask and React.

## Functionality: 

It's a service helping job seekers formulate a resume from raw description quickly.
The user just input raw information they want to insert into the resume, 
and the service will generate the LaTeX code for their resume.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8 or later
- pip (Python package installer)

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/projectname.git
cd projectname
```
    
Then, install the required Python packages:

```bash
pip install -r requirements.txt
npm install
```

Configure .env with credentials:
Inside .env, add the following:

```
GPT_API_KEY=sk-... (your GPT-4 APT key)
```

Finally, run the application:

```bash
python app.py
npm start
```

The backend runs on port 5000, and the frontend runs on port 3000.


## Example
example input:
```John Whiteman
1234567890
john_w@notreal.com
https://www.linkedin.com/in/john-whiteman
Master of Science in Information Science, University of Pennsylvania, May 2020
machine learning; safety ai club.
Bachelor of Engineering in Software Engineering, Brown University, April 2018
gpa 3.9/4.0
Software Engineer at Apple, inc July 2022 till now
Led team to develop new features in app store
design new projects; create plans, checkpoints; manage teams
machine learning platform development, to support ml engineers
machine learning algorithm design, innovation and implementation
Engineering Intern at Brave software company, May 2019 - Aug 2019
engaged in developing backend ednpoints for an ios app
developed functions supporting voice command, use aws for transcribing recording to text
trained a ml model help filtering important information from text
projects:
Game recommendation algorithm, Apple, inc. May 2023
worked with frontend team and crafted a new panel in appstore to support customized user recommendation on games
designed and trained machine learning model to rank games
after it's online, 75% users click and view the recommended games, boosted 5% more total installations
ML platform, University of Pennsylvania, Nov 2019
designed and developed a distributed platform for ml model training
support collaborations; boosted by gpu; use kuberflow, hdfs & spark,  minio to store output
skills: Flask, SpringBoot, Node.js, React.js, Python, Java, C++, TypeScript
```

example output:
\documentclass[a4paper,10pt]{article}
\usepackage[left=1in, right=1in, top=1in, bottom=1in]{geometry}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{parskip}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage[hidelinks]{hyperref}

\definecolor{verdeolivo}{RGB}{85,107,47}
\titleformat{\section}{\large\bfseries\color{verdeolivo}}{}{0em}{}[\titlerule]
\titleformat{\subsection}[runin]{\bfseries\color{verdeolivo}}{}{0em}{}[:]

\begin{document}

\pagestyle{empty}

\begin{center}
    \textbf{\Huge John Whiteman} \\
\end{center}

\vspace{2mm}

\begin{center}
    \faIcon{phone} (123) 456-7890 \hspace{1cm}
    \faIcon{envelope} \href{john_w@notreal.com}{john_w@notreal.com} \hspace{1cm}
    \faIcon{linkedin} \href{https://www.linkedin.com/in/john-whiteman}{John Whiteman}
\end{center}


\section*{\faIcon{user} Professional Profile}
Expert software engineer specializing in machine learning, with a keen interest in developing innovative algorithms for practical applications and enhancing existing platforms. 

\section*{\faIcon{building} Work Experience}

\subsection*{Software Engineer}  \hfill Apple Inc., July 2022 - Present
\begin{itemize}
  \item Spearheaded the development of feature-rich applications in app store, driving user engagement and enhancing the user experience.
 \item Led teams in the ideation and execution of new projects, ensuring efficient management and delivery.
 \item Developed novel machine learning algorithms and platforms to support other ML engineers in their tasks.
\end{itemize}

\subsection*{Engineering Intern}  \hfill Brave Software Company, May 2019 - Aug 2019
\begin{itemize}
    \item Involved in crafting backend endpoints for an iOS application, successfully handled data traffic and user interactions.
    \item Implemented voice command functionalities leveraging AWS services for transcription.
    \item Trained a machine learning model for context extraction from transcribed texts, improving the overall performance of the application.
\end{itemize}

\section*{\faIcon{project-diagram} Project Experience}

\subsection*{Game Recommendation Algorithm}  \hfill Apple Inc., May 2023
\begin{itemize}
    \item Collaborated with the frontend team to introduce a new gaming recommendation panel in the app store.
    \item Designed and trained a machine learning model for ranked game suggestions, leading to 75\% of users interacting with the recommended games and boosting total game installations by 5\%.
\end{itemize}

\subsection*{ML Platform}  \hfill University of Pennsylvania, Nov 2019
\begin{itemize}
    \item Designed and developed a robust distributed platform for ML model training, fostering collaborations among the team.
    \item Implemented a GPU-accelerated pipeline with Kubernetes, HDFS & Spark, Minio for persistent output storage.
\end{itemize}

\section*{\faIcon{graduation-cap} Education}
\subsection*{University of Pennsylvania}  \textbf{Master of Science in Information Science} \hfill May 2020
Specialization in Machine Learning; Participated in the Safety AI club.

\subsection*{Brown University}  \textbf{Bachelor of Engineering in Software Engineering} \hfill   April 2018
Academic performance: GPA 3.9/4.0.

\section*{\faIcon{cogs} Technical Skills}
\begin{center}
    \begin{itemize}[itemsep=-3pt]
        \item Backend Development: Flask, SpringBoot, Node.js
        \item Frontend Development:React.js
        \item Programming Languages: Python, Java, C++, TypeScript
    \end{itemize}
\end{center}

\end{document}
