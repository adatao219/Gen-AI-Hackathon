portfolio_template1 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ada Tao GHC23 - Personal Portfolio</title>

    <!--
    - favicon
    - empty
  -->
    <link
      rel="shortcut icon"
      href="./assets/images/logo.ico"
      type="image/x-icon"
    /> 

    <!--
    - custom css link
  -->
    <link rel="stylesheet" href="./assets/css/style.css" />

    <!--
    - google font link
  -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap"
      rel="stylesheet"
    />
  </head>

  <body>
    <!--
    - #MAIN
  -->

    <main>
      <nav class="navbar">
        <ul class="navbar-list">
          <li class="navbar-item">
            <a class="navbar-link" href="#about">About</a>
          </li>
          <li class="navbar-item">
            <a class="navbar-link" href="#education-work-experience"
              >Education and Work Experience</a
            >
          </li>
          <li class="navbar-item">
            <a class="navbar-link" href="#projects">Projects</a>
          </li>
          <li class="navbar-item">
            <a class="navbar-link" href="#hobbies">Hobbies</a>
          </li>
        </ul>
      </nav>

      <!--
      - #SIDEBAR
    -->

      <aside class="sidebar" data-sidebar>
        <div class="sidebar-info">
          <figure class="avatar-box">
            <img src="./assets/images/my-pic.png" alt="Ada Tao" width="400" />
          </figure>

          <div class="info-content">
            <h1 class="name" title="Ada Tao">Ada Tao</h1>
          </div>
          <h4 class="h4 service-title">GHC'23| MCIT at UPenn | Rewriting the code ｜ AWS CloudUp for her </h4>

          <button class="info_more-btn" data-sidebar-btn>
            <span>Show Contacts</span>

            <ion-icon name="chevron-down"></ion-icon>
          </button>
        </div>

        <div class="sidebar-info_more">
          <div class="separator"></div>

          <ul class="contacts-list">
            <li class="contact-item">
              <div class="icon-box">
                <ion-icon name="mail-outline"></ion-icon>
              </div>

              <div class="contact-info">
                <p class="contact-title">Email</p>

                <a href="mailto:adatao@seas.upenn.edu" class="contact-link"
                  >adatao@seas.upenn.edu</a
                >
              </div>
            </li>

            <li class="contact-item">
              <div class="icon-box">
                <ion-icon name="phone-portrait-outline"></ion-icon>
              </div>

              <div class="contact-info">
                <p class="contact-title">Phone</p>

                <a href="tel:+6466561504" class="contact-link"
                  >+1 (646) 656-1504</a
                >
              </div>
            </li>

            <li class="contact-item">
              <div class="icon-box">
                <ion-icon name="calendar-outline"></ion-icon>
              </div>

              <div class="contact-info">
                <p class="contact-title">Birthday</p>

                <time datetime="1996-05-09">May 9, 1996</time>
              </div>
            </li>

            <li class="contact-item">
              <div class="icon-box">
                <ion-icon name="location-outline"></ion-icon>
              </div>

              <div class="contact-info">
                <p class="contact-title">Location</p>

                <address>Philadelphia, Pennsylvania, USA</address>
              </div>
            </li>

            <li class="contact-item">
              <div class="icon-box">
                <ion-icon name="mail-outline"></ion-icon>
              </div>

              <div class="contact-info">
                <p class="contact-title">Resume</p>

                <a href="https://drive.google.com/file/d/1WScxTKt5Ir2NpVb2PPbyqUfVtHTXl058/view?usp=sharing" class="contact-link"
                >CLICK ME</a
              >              
            </div>
            </li>

          </ul>

          <div class="separator"></div>

          <ul class="social-list"> 
            <li class="social-item">
              <a href="https://www.linkedin.com/in/ada-tao" class="social-link">
                <ion-icon name="logo-linkedin"></ion-icon>
              </a>
            </li>

            <li class="social-item">
              <a href="https://github.com/adatao219" class="social-link">
                <ion-icon name="logo-github"></ion-icon>
              </a>
            </li>

            <li class="social-item">
              <a href="https://instagram.com/ada.tao/" class="social-link">
                <ion-icon name="logo-instagram"></ion-icon>
              </a>
            </li>
          </ul>
        </div>
      </aside>

      <!--
      - #main-content
    -->
      <style>
        .intro-title {
          margin-top: 20px;  /* Adjust this value as needed for desired indent */
        }

        .service-content-box + .service-title {
          margin-top: 100px;  /* Adding 100px space */
        }

        .article-title {
          margin-top: 75px;
        }
      </style>

      <div class="main-content">

        <section id="about" class="about active" data-page="about">
          <img src="./assets/images/mypicwithcat.png" alt="Description of Image" class="right-float-img">

          <header>

            <h2 class="h2 article-title">About me</h2>

          </header>

          <div class="service-content-box">
            <h3 class="h3 highlight-title">
              Hi there! I'm Ada Tao. <br> 
              I'm Open to work full time from May 2024!
            </h3>


            <h5 class="h5 intro-title">
              A passionate Computer and Information Technology Graduate Student at UPenn who loves AWS and building applications from scratch. <br>
              I’m also a HipHop dancer and a cat mom ! <br>
              I live in Philadelphia, PA. Go birds!<br>
            </h5>
          </div>
          <!--
          - service
          -->

          <h3 class="h3 service-title">A glimpse of my skills</h3>

          <ul class="service-list">
            <li class="service-item">
              <div class="service-icon-box">
                <img
                  src="./assets/images/icon-design.svg
                "
                  alt="Web development icon"
                  width="40"
                />
              </div>

              <div class="service-content-box">
                <h4 class="h4 service-item-title">Full Stack</h4>

                <p class="service-item-text">
                  •  Proficient on web design and development. Learned web
                  development through online course, on site course and enhanced
                  by doing hands on project. <br>
                  •  Skills: Python, JavaScript, CSS, HTML, nodeJS, expressJS, MongoDB, REST API, Django <br>
                </p>
              </div>
            </li>

            <li class="service-item">
              <div class="service-icon-box">
                <img
                  src="./assets/images/icon-dev.svg"
                  alt="Web development icon"
                  width="40"
                />
              </div>

              <div class="service-content-box">
                <h4 class="h4 service-item-title">Cloud Operations</h4>

                <p class="service-item-text">
                  •  Currently working as a Associate CloudOps Engineer in Digital.AI. <br />
                  •  Implemented the robust CI/CD process in Github action, deployed images to cloud using ArgoCD, Kubernetes, Nexus and AWS EC2
                  •  LOVE AWS and pursuing the Solution Architect Certificate<br />
                  •  Skill: Kubernetes, AWS S3, AWS EC2, AWS route 53, Terraform, Docker, ArgoCD
                </p>
              </div>
            </li>

            <li class="service-item">
              <div class="service-icon-box">
                <img
                  src="./assets/images/icon-app.svg"
                  alt="mobile app icon"
                  width="40"
                />
              </div>

              <div class="service-content-box">
                <h4 class="h4 service-item-title">Mobile apps & AI</h4>

                <p class="service-item-text">
                  •  Proficient on develop of applications for iOS and
                  Android.<br />
                  •  Utilized OpenAI API to generate AI images and recipes for food <br />
                  •  Skill: Flutter, Microsoft Azure, Django, OpenAI API
                  •  Ex. Wizeats AI-powered food recipe app

                </p>
              </div>
            </li>

            <li class="service-item">
              <div class="service-icon-box">
                <img
                  src="./assets/images/icon-dev.svg"
                  alt="camera icon"
                  width="40"
                />
              </div>

              <div class="service-content-box">
                <h4 class="h4 service-item-title">Algorithm & Database</h4>

                <p class="service-item-text">
                  •  I love solving backend problems using Algorithm. Different
                  data structures are fascinating. <br>
                  •  I love brainstorming what's the optimized datastructure for each task to increase the efficiency.
                  •  Ex. Facebook Haystack Database
                </p>
              </div>
            </li>
          </ul>
        </section>

        <!--
        - #Education and Work Experience
        -->
        <section
          id="education-work-experience"
          class="education-work-experience"
          data-page="education-work-experience"
        >
          <header>
            <h2 class="h2 article-title">Education and Work Experience</h2>
          </header>

            <div class="title-wrapper">
              <div class="icon-box">
                <ion-icon name="book-outline"></ion-icon>
              </div>

              <h3 class="h3">Education</h3>
            </div>

            <ol class="timeline-list">
              <li class="timeline-item">
                <h4 class="h4 timeline-item-title">
                  University of Pennsylvania, Philadelphia, PA
                </h4>

                <span>Aug 2022 — May 2024</span>

                <p class="timeline-text">
                  •  M.S. in Computer and Information Technology<br>

                  •  Coursework: Artificial Intelligence(Python), Data Structure & Software Design (Java), Computer Systems Programming (C/C++), Algorithms, Database (SQL), Programming for the web (SaaS)<br />
                  •  GPA: 3.76/4.00<br />
                  •  President in MMDC dance crew at Penn, lead 20+ students to perform on stage!


                </p>
              </li>

              <li class="timeline-item">
                <h4 class="h4 timeline-item-title">Lehigh University, Bethlehem, PA</h4>

                <span>2015 — 2019</span>

                <p class="timeline-text">
                  •  B.S in Business Information Systems<br />
                  •  Coursework: Information Systems (SQL), Application Development for Business (Java), Cloud Computing<br />
                  •  GPA: 3.67/4.00<br />
                  •  President of Business Information Systems club, arranged trips of 30+ student and faculty to visit Tech companies in NYC
                </p>
              </li>


            </ol>


            <div class="title-wrapper">
              <div class="icon-box">
                <ion-icon name="book-outline"></ion-icon>
              </div>

              <h3 class="h3">Work Experience</h3>
            </div>

            <ol class="timeline-list">
              <li class="timeline-item">
                <h4 class="h4 timeline-item-title">
                  Part-Time Associate CloudOps Engineer
                </h4>
                <h5 class="h5 company-item-title">
                  Digital.ai Lafayette, IN
                </h5 >

                <span>Sep 2023 — Present</span>

                <p class="timeline-text"></p>
              </li>

              <li class="timeline-item">
                <h4 class="h4 timeline-item-title">Cloud Operations Intern</h4>
                <h5 class="h5 company-item-title">
                  Digital.ai Lafayette, IN
                </h5 >
                <span>May 2023 — Aug 2023</span>

                <p class="timeline-text">
                  •  Implemented the robust CI/CD process, automated the creation, testing and deployment of Docker Images to private repository and public domains, resulting in a 40% reduction in errors and improved release stability<br />
                  •	 Leveraged Kubernetes to deploy cloud services, used dynamic routing and load balancing to support scalability<br />
                  •	 Championed Agile methodologies within the Cloud operations team, facilitated daily stand-ups, sprint planning, and retrospectives, resulting in a 25% increase in project delivery speed and enhancing team collaboration<br />
                  •	 Troubleshot 3 cloud service requests monthly, provided detailed root cause analysis, and implemented permanent solutions
                </p>
              </li>

            </ol>
          </section>
        </section>

        <!--
        - #Projects
        -->

        <section id="projects" class="projects" data-page="projects">

          <header>
            <h2 class="h2 article-title">Projects</h2>
          </header>

          <ul class="project-list">
            <a href="https://blitzat.com">
              <figure class="project-img">
                <div class="project-item-icon-box">
                  <ion-icon name="eye-outline"></ion-icon>
                </div>
                <img
                  src="./assets/images/project2.png"
                  alt="finance"
                  loading="lazy"
                />
              </figure>

              <div class="project-info">
                <h2 class="project-title">BlitzAt Food Truck Ordering</h2>
                <p class="project-category">
                  Food Truck Ordering Web Application
                </p>
                <div class="project-blurb">
                  <p style="color: white;"></pp>
                    •  This web application, BlitzAt, makes it easy to order from
                    your favorite food trucks online. Browse through menus,
                    place orders, and enjoy delicious meals with just a few
                    clicks! <br>
                    •  Currently serve 100+ weekly orders
                  </p>
                </div>
              </div>
            </a>

            <a href="https://www.wizeats.com/">
              <figure class="project-img">
                <div class="project-item-icon-box">
                  <ion-icon name="eye-outline"></ion-icon>
                </div>
                <img
                  src="./assets/images/project1.png"
                  alt="finance"
                  loading="lazy"
                />
              </figure>

              <div class="project-info">
                <h2 class="project-title">Wizeats App</h2>
                <p class="project-category">
                  AI-powered food recipe app
                </p>
                <div class="project-blurb">
                  <p style="color: white;"></pp>
                    •  The app utilized OpenAI API and is launched on iOS, Android App Store
                    and Google App. <br>
                    •  The app makes recommendations based on user’s preference, currently serving 50 daily users
                  </p>
                </div>
              </div>
            </a>
              <a href="https://github.com/cit5940-23sp/Haystack_Database">
                <figure class="project-img">
                  <div class="project-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/project3.png"
                    alt="finance"
                    loading="lazy"
                  />
                </figure>

                <div class="project-info">
                  <h2 class="project-title">Facebook Haystack Database</h2>
                  <p class="project-category">
                    Efficient photo storage application 
                  </p>
                  <div class="project-blurb">
                    <p style="color: white;"></pp>
                      •  This database replicated the Facebook's photo storage feature that optimized storage, enabled efficient retrieval and reduced metadata overhead by 80%<br>
                      •  Added in a recommended friend search algorithm using heuristic and graph techniques<br>

                    </p>
                  </div>
                </div>
              </a>
              <a href="https://still-stream-71646.herokuapp.com/">
                <figure class="project-img">
                  <div class="project-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/project4.png"
                    alt="finance"
                    loading="lazy"
                  />
                </figure>

                <div class="project-info">
                  <h2 class="project-title">Photo:D Cloud Photo Sharing Platform (Full Stack)</h2>
                  <p class="project-category">
                    Photo sharing Platform
                  </p>
                  <div class="project-blurb">
                    <p style="color: white;"></pp>
                      •  The platform supports user log-
                      in, posting reviews and comments, editing and deleting submissions <br>
                      •  Utilized two database for the most cost effective. Used MongoDB for user identity information and saved image data to Cloudinary <br>
                      •  The platform has interactive front-end user interface and supported viewing on computer and phone screens
                    </p>
                  </div>
                </div>
              </a>
              <a href="https://github.com/Elenalalala/web_scraping_hackathon">
                <figure class="project-img">
                  <div class="project-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/project5.jpeg"
                    alt="finance"
                    loading="lazy"
                  />
                </figure>

                <div class="project-info">
                  <h2 class="project-title">Investment made possible</h2>
                  <p class="project-category">
                    Stock Recommendation Platform
                  </p>
                  <div class="project-blurb">
                    <p style="color: white;"></pp>
                    •  The platform tells users the stock price and key insights for public companies <br>
                    •  Derived key insights from statistical analysis, Regression and multivariate analysis based on company industry and size
                  </p>
                  </div>
                </div>
              </a>  
          </ul>

        </section>


        <section id="hobbies" class="hobbies" data-page="hobbies">

          <header>
            <h2 class="h2 article-title">Ada's Hobbies</h2>
          </header>

          <ul class="hobbies-list">
            <li
              class="hobbies-item active"
              data-filter-item
              data-category="web development"
            >
              <a href="#" class="hobbies-item-wrapper">
                <figure class="hobbies-img">
                  <div class="hobbies-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/hobbies1.jpg"
                    alt="Dancing"
                    loading="lazy"
                  />
                </figure>
                <div class="hobbies-info">
                  <h3 class="hobbies-title">Dancing</h3>
                  <p class="hobbies-category">
                    •  Dancing is in my blood. I love hiphop, kpop and jazz. Always trying out new things,
                    like Waacking and house.
                  </p>
                </div>
              </a>
            </li>
            <li
              class="hobbies-item"
              data-filter-item
              data-category="web development"
            >
              <a href="#" class="hobbies-item-wrapper">
                <figure class="hobbies-img">
                  <div class="hobbies-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/hobbies2.png"
                    alt="Organizing events"
                    loading="lazy"
                  />
                </figure>
                <div class="hobbies-info">
                  <h3 class="hobbies-title">Organizing events</h3>
                  <p class="hobbies-category">
                    •  I love to utilize my connections and contribute back
                    to the community. While being the BIS president in college,
                    I took 30 club members to
                    Amazon and E&Y’s New York City offices.
                  </p>
                </div>
              </a>
            </li>
            <li
              class="hobbies-item"
              data-filter-item
              data-category="web development"
            >
              <a href="#" class="hobbies-item-wrapper">
                <figure class="hobbies-img">
                  <div class="hobbies-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/hobbies3.jpg"
                    alt="Pottery"
                    loading="lazy"
                  />
                </figure>
                <div class="hobbies-info">
                  <h3 class="hobbies-title">Pottery</h3>
                  <p class="hobbies-category">
                    •  I am very passionate about wheel throwing, trying out new clay/glaze
                    is my favorite thing!
                  </p>
                </div>
              </a>
            </li>
            <li
              class="hobbies-item"
              data-filter-item
              data-category="web development"
            >
              <a href="#" class="hobbies-item-wrapper">
                <figure class="hobbies-img">
                  <div class="hobbies-item-icon-box">
                    <ion-icon name="eye-outline"></ion-icon>
                  </div>
                  <img
                    src="./assets/images/hobbies4.jpg"
                    alt="Spend time with my cat"
                    loading="lazy"
                  />
                </figure>
                <div class="hobbies-info">
                  <h3 class="hobbies-title">Spend time with my cat</h3>
                  <p class="hobbies-category">
                    •  I am so lucky to have my cat's company during grad school. <br>
                    Her name is Bubbles. She comes to the door to welcome me
                    home every day.
                  </p>
                </div>
              </a>
            </li>
          </ul>
        </section>
      </div>

      <!--
    - custom js link
  -->
      <script src="./assets/js/script.js"></script>

      <!--
    - ionicon link
  -->
      <script
        type="module"
        src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"
      ></script>
      <script
        nomodule
        src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"
      ></script>
    </main>
  </body>
</html>
"""