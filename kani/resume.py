# /kani/resume.py

from kani import ChatMessage


example_input_1 = """
"""

example_output_1 = """
"""

example_input_2 = """
Jamie Parker
9876543210
jamie_parker_email@notreal.com
https://www.linkedin.com/in/jamie-parker
Master of Science in Electrical Engineering, University of AAA, April 2022
renewable energy systems; university's Innovation Lab.
Bachelor of Engineering in Electronics, BBB University, May 2019
honors, top 10%
Electrical Engineer at Dynamic Solutions Ltd. July 2022 till now
create advanced electrical systems that incorporate smart tech to enhance both efficiency and how users interact with our products. 
work together with teams of different disciplinary, reduce cost and be more enviroment friendly. 
I shaped an innovative energy management system that's currently awaiting patent approval. 
I used machine learning techniques to forecast and fine-tune the way energy is consumed.
Engineering Intern at Creative Tech Innovations, June 2019 - June 2020
I  participated in product development, from initial concept, 
work together to design and test a smart irrigation system. 
boasts a 20% reduction in water usage.
projects
Solar-Powered Charging Station, Dynamic Solutions Ltd., March 2023
design, develop, and deploy environment friendly solar charging station
work across teams,  with suppliers and manufacturers
IoT-Based Home Automation System, Dynamic Solutions Ltd., December 2022
design, implement, and test a IoT-based home automation system, reduce energy used
skills: Flask, SpringBoot, Node.js, React.js, Python, Java, C++, TypeScript
"""

example_output_2 = """
\\documentclass[a4paper,10pt]{article}
\\usepackage[left=1in, right=1in, top=1in, bottom=1in]{geometry}
\\usepackage{enumitem}
\\usepackage{titlesec}
\\usepackage{parskip}
\\usepackage{xcolor}
\\usepackage{fontawesome5}
\\usepackage[hidelinks]{hyperref}

\\definecolor{verdeolivo}{RGB}{85,107,47}
\\titleformat{\\section}{\\large\\bfseries\\color{verdeolivo}}{}{0em}{}[\\titlerule]
\\titleformat{\\subsection}[runin]{\\bfseries\\color{verdeolivo}}{}{0em}{}[:]

\\begin{document}

\\pagestyle{empty}

%\section*{\\faIcon{address-card} Contact Information}
\\begin{center}
    \\textbf{\\Huge Jamie Parker} \\
\\end{center}

\\vspace{2mm}

\\begin{center}
    \\faIcon{phone} (123) 456-7890 \\hspace{1cm}
    \\faIcon{envelope} \\href{mailto:jamie_parker_email@notreal.com}{john.doe@example.com} \\hspace{1cm}
    \\faIcon{linkedin} \\href{https://www.linkedin.com/in/jamie-parker}{Jamie Parker}
\\end{center}


\\space
\\section*{\faIcon{user} Professional Profile}
Innovative Electrical Engineer with a Master's degree and hands-on experience in developing sustainable energy solutions, adept at leveraging IoT technologies to drive efficiency and user engagement.


\\section*{\\faIcon{building} Work Experience}

\\subsection*{Electrical Engineer}  \\hfill Dynamic Solutions Ltd., July 2022 - Present

\\begin{itemize}
  \\item Spearheaded the development of cutting-edge electrical systems, focusing on the integration of smart technologies to improve product efficiency and user experience.
 \\item Played a key role in a multidisciplinary team to conceptualize, design, and deploy sustainable energy solutions, significantly reducing energy costs and carbon footprint for our clients.
 \\item Contributed to the development of a patent-pending energy management system that predicts and optimizes energy consumption patterns using machine learning algorithms.length.
\\end{itemize}

\\subsection*{Engineering Intern}  \\hfill Creative Tech Innovations, June 2019 - June 2020

\\begin{itemize}
    \\item Supported senior engineers in the R\&D of pioneering technology solutions, with a particular focus on the development of IoT-enabled devices for smart environments.
    \\item Assisted in the entire lifecycle of product development from concept to prototype for a smart irrigation system, which resulted in a 20\% reduction in water usage for our test clients.
\\end{itemize}

\\section*{\faIcon{building} Project Experience}

\\subsection*{Solar-Powered Charging Station}  \\hfill Dynamic Solutions Ltd., March 2023

\\begin{itemize}
  \\item Led the engineering design and development of an eco-friendly solar-powered charging station, from initial concept through to successful deployment.
 \\item Managed cross-functional team efforts, including coordination with suppliers and manufacturers, to meet project deadlines and budget constraints.
\\end{itemize}

\\subsection*{IoT-Based Home Automation System}  \\hfill Dynamic Solutions Ltd., December 2022

\\begin{itemize}
    \\item Directed the design, implementation, and testing phases of a sophisticated IoT-based home automation system aimed at optimizing energy consumption.
\\end{itemize}

\\section*{\\faIcon{graduation-cap} Education}

\\subsection*{University of AAA}  \\textbf{Master of Science in Electrical} \\hfill  April 2022

Specialization in renewable energy systems; Participated in the university's Innovation Lab.

\\subsection*{BBB University}  \\textbf{Bachelor of Engineering in Electronics} \\hfill  May 2019

Graduated with honors, ranking in the top 10\\% of the class.


\\section*{\\faIcon{cogs} Technical Skills}
\\begin{center}
    \\begin{itemize}[itemsep=-3pt]
        \\item Backend Development: Flask, SpringBoot, Node.js
        \\item Frontend Development: React.js
        \\item Programming Languages: Python, Java, C++, TypeScript
    \\end{itemize}
\\end{center}

\\end{document}
"""


async def generate_resume(engine, raw_text: str) -> str:
    """
    Takes raw text including unstructured personal information, sorts out the information,
    and returns it as a well-structured string with bullet-pointed work and project experiences.
    """
    # # Few-shot examples to guide the model
    # shots = [
    #     ChatMessage.user(example_input_2),
    #     ChatMessage.assistant(example_output_2),
    # ]
    #
    # # Incorporate the user's raw input as part of the few-shot learning
    # shots.append(ChatMessage.user(raw_text))
    #
    # # Since the function 'chat_round' expects an asynchronous call, ensure your framework supports async operations
    # # or adjust according to your application's architecture
    # response = await engine.chat_round(ChatMessage.assistant(""), always_included_messages=shots)

    prompt = f"""
        example input:
        {example_input_2}
        ---
        example output resume latex code:
        {example_output_2}
        ---
        generate resume latex code for this input (return just the latex code):
        {raw_text}
        """
    # Use the prepared prompt in a chat round without adding additional ChatMessage instances for few-shot
    response = await engine.chat_round(prompt)

    # Return the GPT-3 formatted text
    return response.content


# Example usage (this part should be in an async context)
if __name__ == "__main__":
    import asyncio

    raw_input = """
    John Whiteman
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
    """

    # Since sort_and_structure_personal_info is an async function, we need to run it inside an event loop
    structured_info = asyncio.run(generate_resume(raw_input))
    print(structured_info)