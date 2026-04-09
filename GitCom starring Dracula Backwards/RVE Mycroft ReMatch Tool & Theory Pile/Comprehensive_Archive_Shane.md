# Tar0tscepter Systems Lab

**Live Site:** [https://tar0tscepter.github.io/](https://tar0tscepter.github.io/)

## Project Overview

Tar0tscepter Systems Lab is the digital headquarters for **Re.Match**, an opportunity and resource matching engine designed specifically for individuals navigating the justice system, addiction recovery, and homelessness. 

The core philosophy of this application is constraint-based filtering: utilizing societal "red flags" (felonies, employment gaps, lack of documentation) as mathematical constraints to unlock highly specific, localized grants, employment, and resources.

## Technical Requirements (Next Chapter Admissions)

This project was built from the ground up to strictly adhere to the Next Chapter pre-course technical requirements:

*   **Strict Vanilla Constraints:** Built using exclusively pure HTML5, CSS3, and Vanilla JavaScript.
*   **Zero External Libraries:** No CSS frameworks (like Bootstrap or Tailwind) and no JS libraries (like React or jQuery) were used.
*   **Responsive Design:** Fully responsive layout that scales appropriately across mobile and desktop environments.
*   **Separation of Concerns:** Clean architecture utilizing distinct `.html`, `.css`, and `.js` files.

## Features

*   **Re.Match Intake Form:** A structured data collection system designed with cognitive load reduction in mind, enabling users to input their constraints for dossier generation.
*   **Accessible Design:** High-contrast aesthetic ("Systems Lab" theme) prioritizing readability and clear semantic HTML structure.
*   **Future Integration:** (Planned) Native web-audio recording for narrative intake.

## Version History

*   **v1.1.0** - Shifted narrative focus from "overcoming weakness" to "leveraging systemic constraints." Adjusted text to confidently present a tool that will help.
*   **v1.0.0** - Initial deployment. Established "Systems Lab" aesthetic, basic routing, and initial contact form structure.

## Learning Journey & Curriculum

As part of the development of this project, I am actively following open-source curriculums to understand the underlying architecture of the web. Below are the core concepts applied in this project and the corresponding open-source learning materials:

### 1. Document Structure & Semantic HTML
*The foundation of the site, ensuring accessibility and proper document flow.*
*   **Curriculum:** [freeCodeCamp - Basic HTML and HTML5](https://www.freecodecamp.org/learn/responsive-web-design/#basic-html-and-html5)
*   **Concepts Applied:** `<!DOCTYPE html>`, `<head>` metadata, viewport scaling for responsiveness, and semantic block elements (`<main>`, `<section>`, `<header>`).

### 2. Form Architecture & Data Collection
*Building the Re.Match intake system using native web standards.*
*   **Curriculum:** [MDN Web Docs - HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms)
*   **Concepts Applied:** Implicit labeling (nesting `<input>` inside `<label>`), structural grouping (`<fieldset>` and `<legend>`), and native input validation (`type="number"`, `min`, `max`, `required`).

### 3. Data Transmission (Without Backend Servers)
*Handling form submissions securely without relying on external JavaScript libraries.*
*   **Curriculum:** [MDN Web Docs - Sending form data](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data)
*   **Concepts Applied:** Utilizing the `<form action="...">` attribute, `method="POST"`, and `enctype="text/plain"` to interface directly with native client protocols (like `mailto:`).

### 4. Text Formatting & Semantic Emphasis
*Structuring the psychological copywriting for maximum readability and screen-reader accessibility.*
*   **Curriculum:** [freeCodeCamp - HTML Text Formatting](https://www.freecodecamp.org/news/html-formatting-tags-how-to-format-text-in-html/)
*   **Concepts Applied:** Differentiating between stylistic boldness (`<b>`) and semantic importance (`<strong>`), inline styling containers (`<span>`), and structured lists (`<ul>`, `<ol>`, `<li>`).

### 5. Documentation & Markdown
*Creating this README and documenting the project lifecycle.*
*   **Curriculum:** [GitHub Docs - Mastering Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
*   **Concepts Applied:** Version history tracking, header formatting, and hyperlink integration.

## Author

**Shane (tar0t)**
*In pursuit of systematic methods to help people.*


**Learning progression**
*   **v1.1.0** - Started using Codex and Gemini CLI for research and studying. Have an independent curriculum of open source materials for every component I work through.   
*   **v1.0.0** - Installed VS Code for the first time. Installed GitHub for the first time. Learned how to create the files, edit them, preview, and basic GitHub Push. 
 
RESOURCES UP TOP 
GIT 
https://www.w3schools.com/git/
HTML 
https://www.w3schools.com/tags/
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements

Starting from 0 skill
First order of business, Git/GitHub
Computer is up, both phones in front of me. 
I've installed VS Code
I've opened VS Code 
I've installed the Live Server plugin
I've installed the Prettier plugin 
---I will not use AI to generate code directly 
---I will have it teach me the principles and show me the relevant materials so that I can streamline this, since I have 6 hours to deliver a product. 
---Then test and iterate 
I've created 
-Index.html
-Script.js
-Style.css
Now commencing Git module on Circle 

NOTES - GIT MODULE - CIRCLE 
The Working Directory: Where  we actively edit files locally. This is our playground.
The Staging Area: Itâ€™s a temporary holding  spot for changes before committing.
The Local Repository: This is where  we store committed changes locally.
The Remote Repository: A server like  GitHub for sharing and backing up code.
Most git commands move files  between these four locations.
-Git is a version control system 
-There are 4 interaction points within the Git system. 
WORKING DIRECTORY ########### STAGING AREA ############ LOCAL REPO ########### REMOTE REPO 
-Git Add moves from working directory to staging area
-Git Commit moves from staging area to local repo 
-Git Push moves from local repo to remote repo 
-Git fetch pulls from remote repo to local repo 
-Git merge pulls from the local repo and merges into the working directory 
-Git pull pulls from remote repo to working directory 
	|->git pull, which fetches changes from the remote repository and merges  them into your local repository. 
		|-> It combines two commands: git fetch, which  grabs the latest updates, and git merge,  which integrates these updates with your work.
-Git clone pulls from remote repo to local repo (what's difference between fetch and pull?) 
									
-Git Init - Initialize an existing folder as a Git Repository 
-Git Clone - Retrieve an entire repository from an existing hosted location via URL

#####downloaded GitHub Desktop #####		--Downloaded Git Command Cheat Sheet--
|->Focus on using without GitHub Desktop to learn CLI stylo 
	|->Get savvy with CLI since coming from 0 makes that important. 
		|->Use AI, visual aid, and other highly useful tools last - focus on developing fundamentals 


username.github.io where username is your GitHub username. 
The important thing to keep in mind is that your website will be hosted on GitHub as well.
Hosting is a complicated topic, but for now just understand that GitHub allows you to host one site through their services for free and allows others to visit it, 
as long as you title your repository correctly!

As you can see on the GitHub Pages site - https://pages.github.com/ - you must create your repository with the name username.github.io where username is your GitHub username. Go ahead and follow the rest of this tutorial to initiate your repo and make sure you clone your repository to a folder on your computer that youâ€™ll be able to find easily.

I have 
-installed VS Code, 
-created the file directory tar0tscepter.github.io on my desktop 
-created a github repository using that directory 
-created 3 files within the directory 
-I am going to exclusively use the items mentioned within the assessment's curriculum
|-> particularly because I am new, I should be focusing on fundamentals and not trying anything beyond the curriculum's intended breadth 
	|-> this will catalyze my learning and give me a controllable scope 
This means I will only be using HTML, CSS, and JavaScript. 

I have decided to press my 0 knowledge, 0 skill, procrastination flavored project as an advantage instead of a constraint. 
This endeavor will serve myriad functions: 
1) I will document my learning process both in this notepad, 
as well as using Git versioning to both conduct standard versioning/branching advantagous fundamental operations as I learn them
I will iterate and branch as I move past each stage, starting with skeletons for everything and then progressively fleshing out a final product 

2) The final product will serve as a functional, real world application for the projects I've been theorycrafting in real life.
These projects are: 
The Tar0t Draw: A resource matching system designed to help homeless & incarcerated individuals match to opportunities that rate as close to 100/100 on Life Impact and 100/100 on Criteria Match 
while also including multiple other metrics such as probability, time to completion, sought category match count, and more 
The methodology I have right now is 
I create a form which asks the individual a series of questions designed to cover all possible match/barrier criteria found in resources. For instance, I found Next Chapter 
using this method by creating an expansive profile for myself in json by creating a MASSIVE questionaire (the one for public use will be more streamlined and less invasive) 
it covers items like types of barriers (Felony? Misdemeanor? No criminal history? Rental Debt? Type of felony [violent? theft? drugs?] sex offender barrier not covered (sorry) 
it asks what you want help with, what barriers you face, what your interests are, what type of work you've done, other stuff like that 
also has an option to include your resume 
offers categorical prompts as well, School, Career, Employment (seperate from career,) Housing, Social, Recreational, Physical, Hobby, Interest, Legal 
Presenting a completely comprehensive approach to identifying every possible improvement an individual could obtain 
For instance, my report led me to the following benefits by generating a "Dossier" which originally contained over 100 items, distilled it down to the best 3 per category, and yielded
an action plan for each 
I prototyped roughly on myself, which resulted in me initiating: 
-Worksource (Free laptop, covered my GED expenses, is covering my IT/CS classes so that I can allocate my remaining scholarships and grants more strategically) 
-PCC Adult Basic Education Classes 
-Multiple housing programs I'm enrolled in and now on waitlists for 
-Various other services that have escalated my priority 
-A method to obtain free glasses 
-A strategic wraparound for healthcare 
-Legal solutions for absolving apartment debt 
-Temporary housing solutions while I wait for waitlists 
-Emergency housing solutions as last resorts if it takes too long to get into a place 
-Next Chapter 
-Planet Fitness discount membership 
-RentWell program to absolve housing debt and aid me in getting into housing programs 
-Oregon Health Plan's Flex Fund fully covering Gym Membership, Combat training, a second laptop, a portable battery, and backup items in reserve 
-Oregon Health Plan's Housing Related Social Needs for various services - if I can get a down payment on housing and complete  
-And several more items but I'm rambling on 

SO the way it works is: 
Individual completes intake form 
They record an audio clip of themselves reading the questions out loud, then send the clip to my email. There is also an option to fill it out directly via text form and hit submit. 
The audio clip/text form is sent to a dedicated intake inbox 
Either Zapier or Make or similar automates the conversion of that file into a json 
The json is stored in a dedicated drive folder with the format M.D.YYYY.FirstName.LastName
I manually audit the json to ensure it's complete and doesn't have errors 
Currently I need to figure out how I want to automate it past there, likely via local LLM or REST API once I learn how to do that. 
Part of why I want to do NextChapter is to progress further in this and find a path to creating projects like this to help others 

other projects include Second Wind, a social collective designed to function as a social outlet that employs myriad scientific backed methods to go beyond 
simple mitigation of criminogenic recidivism and relapse factors, and focus on the potentiation of strengthening factors such as social outlet, hobbies, creative endeavors, and novel experience 
which all structurally reinforce and take advantage of the neuroplasticity window during acute addiction recovery 

I've designed a node system (not implemented still in theory phase) that makes this a replicatable entity
I will use 4D Recovery as a venue for intake events, as it is adjacent and affiliated with Washington County Community Corrections Center 
This will result in individuals ready to recover having the opportunity to indulge in a reoccuring event ran by Second Wind 
which will be casual video game tournaments with a 12 step opening, meditation closing, and dinner/snacks cooked by me and the homies 

I will also host my workout protocol, which is designed with recovery in mind, as well as mathematically including the vasoconstriction of nicotine use (most recovering individuals smoke cigarettes, like myself) 
to calculate their true 1 Rep Maximum (maximum amount of weight you can push one time) with the vasoconstriction mechanic included 
and also uses a few mechanisms to maximize gains without taxing the central nervous system more than can be recovered 

I will also include my productivity engine, which is possibly an overcomplicated version of the Eisenhower Matrix 
I will also include guides I've created for friends in treatment, such as my guide on utilizing the Flex Fund (our state's health insurance program which is designed to pay for items/servicesnot covered by traditional coverage as long as it can legitemately be contrived as being a boon to your medical diagnoses. If it is an indirect or complicated/unprecedented coorelation, they require you to provide Research Backed Studies/Clinical Trials. 
I've included with the guide an engine in which you upload the files in a drive folder to a Perplexity or ChatGPT thread along with your completed FlexFund form, and it generates a citation list of research backed studies that validate your request 
Included is examples of my final letter and instructions on ensuring that everything is tidy, and a guide to using AI enough to which they can follow the instructions 

PHWEW 
Anyway 
FOR NOW. I'm just going to create a landing page with a blank skeleton and slots for me to put all of those things, give it a cyberpunk/gritty Run The Jewels status styl0 and $wag it out 
Have a live intake form that's operational 
Have a live services offered (pay what you want if you want, free by nature) 
Have a live services offered (manual labor/other freelance work - manual labor paid, freelance work pay if you want so that i can learn by doing) 
Have a live bio 
Have a live blogpost section with at least one or two entries 
and I think that should be enough for now, I might be overshooting my capacity 
I'm going to learn as I go section by section, take notes, and start with the most basic iteration possible, then do branches as I add new components or revise items or integrate new concepts/techniques 
This document will also be uploaded to the site to function as my project notes and part of my bio in some way 

BACK TO THE PROJECT 

GitHub installed. 
Folder on desktop made.
Repository made. 
Project name is correct.
VS Code is open 
Live server plugin is installed 
Prettier plugin is installed 
 
I have created 3 files in the directory. 
First is index.html
Index.html functions as a blueprint that tells the browser :
|->	what to show on the page. 
|-> how to structure the page
|-> which other files to use (style.css and script.js in this case) to style it and make it 


MODULE NOTES 
PERSONAL NOTES 
First order of business - What the hell is HTML? 

###Hyper Text Markup Language###
index.html is a "markup language," not a "programming language" 
The browser reads this file top to bottom and builds the page layout from it 
https://www.w3schools.com/tags/
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements

What is XML?
HTML and XML are both markup (treeâ€‘shaped, tagâ€‘based structures) helps you later when you work with JSON, APIs, etc.
XML = eXtensible Markup Language.
Itâ€™s another markup language, like HTML, but:
HTML has predefined tags (<p>, <div>, <form>) designed for web pages.
XML lets you invent your own tags (<client>, <intakeForm>, <tarotDraw>) to structure data, not render pages.
Browsers donâ€™t display XML as a visual web page; itâ€™s mainly use to store and transport structured data between systems (older APIs, config files, etc.).
â€‹<intake>
  <name>John Doe</name>
  <date>2026-02-20</date>
  <service>Consultation</service>
  <notes>Wants help with resources.</notes>
</intake>

An example XML snippet for your intake JSON idea might look like:
I've created a skeleton using basic HTML 
<!DOCTYPE html>
Declaration that says: â€œThis is an HTML5 document.â€
Helps the browser render the page using modern rules.

<html lang="en">
Opens the root <html> element.
lang="en" tells the browser and screen readers the page language is English.

<head>
Start of the head section: invisible settings and metadata for the page.

  <meta charset="UTF-8" />
  Sets the character encoding to UTFâ€‘8 so you can safely use normal text, symbols, etc.
  
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
Tells mobile browsers to size the page properly on phones and tablets.

Critical for making pages responsive.

  <title>Tar0tscepter | Systems Lab</title>
Sets the tab title and what shows in bookmarks/search results.

<link rel="stylesheet" href="style.css" />
Connects this HTML file to your style.css file.
All your visual styling (colors, fonts, layout) will live there.

</head>
<body>
Closes the head, opens the body: everything inside <body> is what actually appears on the screen.

  <header>
Defines the top section of the page (usually logo, title, navigation).
    <h1>Tar0tscepter Systems Lab</h1>
Main heading for the whole page (only one <h1> recommended).

    <nav>
      <a href="#profile">Profile</a>
      <a href="#services">Services</a>
      <a href="#blog">Blog</a>
      <a href="#contact">Contact</a>
    </nav>

<nav> groups navigation links.

Each <a> is a link; href="#profile" means â€œscroll to the element whose id is profile.â€

This creates inâ€‘page navigation.
â€‹
  </header>

  <main>
Wraps the primary content of the page.

Helps with accessibility and SEO.
â€‹
    <section id="profile">
      <h2>Profile</h2>
      <p>Your story goes here.</p>
    </section>

<section> is a logical block of content.

id="profile" lets links (like the nav) and JavaScript refer to it directly.

<h2> is a subsection heading; <p> is a paragraph of text.
â€‹
    <section id="blog">
      <h2>Blog</h2>
      <p>Your guides and content go here.</p>
    </section>
Placeholder for your posts (later youâ€™ll swap this for multiple entries).

    <section id="contact">
      <h2>Contact</h2>
      <form id="intake-form">
        <label>Name: <input type="text" name="name" required /></label>
        <label>Email: <input type="email" name="email" required /></label>
        <label>Message: <textarea name="message" required></textarea></label>
        <button type="submit">Send Request</button>
      </form>
    </section>

Contact section that contains a form.

<form> will eventually be wired to send data to an email/API.

Each <label> describes a field.

<input> fields collect text and emails; required forces the user to fill them.

<textarea> is a multiâ€‘line input area.

<button type="submit"> triggers the form submission, which youâ€™ll intercept with JavaScript.
  </main>

  <footer>
    <p>&copy; 2026 Tar0tscepter Systems Lab</p>
  </footer>
Footer content at the bottom of the page.

&copy; is an HTML entity that displays the copyright symbol Â©.
â€‹
  <script src="script.js"></script>

Attaches your JavaScript file at the end of the body.

When the page loads, the browser loads and runs script.js to add behavior (validation, interactivity, etc.).
</body>
</html>
Closes the body and the root html element.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tar0tscepter | Systems Lab</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>

  <header>
    <h1>Tar0tscepter Systems Lab</h1>
    <nav>
      <a href="#profile">Profile</a>
      <a href="#services">Services</a>
      <a href="#blog">Blog</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <main>
    <section id="profile">
      <h2>Profile</h2>
      <p>Your story goes here.</p>
    </section>

    <section id="services">
      <h2>Services</h2>
      <p>Your services go here.</p>
    </section>

    <section id="blog">
      <h2>Blog</h2>
      <p>Your guides and content go here.</p>
    </section>

    <section id="contact">
      <h2>Contact</h2>
      <form id="intake-form">
        <label>Name: <input type="text" name="name" required /></label>
        <label>Email: <input type="email" name="email" required /></label>
        <label>Message: <textarea name="message" required></textarea></label>
        <button type="submit">Send Request</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2026 Tar0tscepter Systems Lab</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>


progression 

<main>
  <section id="profile">
    <h2>Profile</h2>
    <p>Hi! I go by <strong>tar0t</strong>. I'm four months sober, interested in physical fitness, cognitive progression, mental health, spiritual health, and in pursuit of systematic methods to help people.</p>
    <p>I'm going hard into physical training, martial arts, getting my GED, then starting Computer Science courses. My current ambition is to get accepted into <strong>Next Chapter's bootcamp</strong>.</p>
    <p>Next Chapter's coursework is guiding me through creating this website. <em>I am learning from the ground up with zero experience</em>, and intend to have a functional website before 1:00PM today. Here's to hoping!</p>
  </section>

  <section id="services">
    <h2>Services</h2>
    <h3>Manual Labor</h3>
    <p>Physical work, Portland area. Paid.</p>

    <h3>Digital Labor</h3>
    <p>Tar0t Draw: Opportunity/resource matching service â€” designed for homeless individuals and individuals leaving incarceration.</p>
    <p><em>Free by default, pay what you want (tips!)</em></p>

    <ul>
      <li><a href="#tarot">Tar0t Draw details</a></li>
      <li><a href="#flexfund">FlexFund guide</a></li>
    </ul>
  </section>

  <section id="blog">
    <h2>Projects & Guides</h2>
    <ul>
      <li><a href="#nextchapter">Next Chapter Technical Assessment Project Notes</a></li>
      <li><a href="#flexfund">FlexFund Citation Guide w/ examples + prompt</a></li>
      <li><a href="#tarot">Example Tar0t Draw Dossier</a></li>
      <li>Recovery Workout Protocol</li>
      <li>Productivity Engine</li>
      <li>Second Wind Social Collective</li>
    </ul>
  </section>

  <section id="contact">
    <h2>Contact / Intake</h2>
    <form id="intake-form">
      <label>Name: <input type="text" name="name" required /></label>
      <label>Email: <input type="email" name="email" required /></label>
      <label>Service:
        <select name="service" required>
          <option value="">Select...</option>
          <option value="tarot">Tar0t Draw</option>
          <option value="research">Research/FlexFund</option>
          <option value="labor">Manual Labor</option>
        </select>
      </label>
      <label>Message: <textarea name="message" rows="5" required></textarea></label>
      <button type="submit">Send Request</button>
    </form>
  </section>
</main>

Had to update windows 
OneDrive did some weird jank i think, it prompted me to backup and I foolishly decided to 
I have to tweak settings later, but I was able to get everything working again (copied folder from cloud to desktop, ensured cloud is read/write instead of read only, directly dumped 
folder into vs code 
Git seems good 
VS Code seems good 

Back to it, commencing CSS 

CyberPunk has always been my favorite stuff, even though I'm super not down for God-devouring-singularity or dystopian neurolink shananigans 
but moving on

Study every line. 

OK. For the next week, I'm going to work on further understanding and practicing HTML, CSS and Javascript. I will use Git versioning and progress. I will find online training through 
the platforms offered through the coursework assessment. I will acquire and implement as many techniques to further the development and launch of a final, v1 iteration of all of my projects. 
I will document my learning progress as I go. 

I will launch my project at all costs, but will use Next Chapter as a target to further my capabilities. 
Everything is hinging on Next Chapter. 

So to do this, I will document my progress, save my AI history, ensure that I understand every single line of code I use and can replicate it by hand. 
I will use Git to version control and test specific components before implementing them, then merge them together as I progress. 

If I can use the platforms they offered to learn more, and document my growth journey up to Next Chapter, then I will provide evidence of my grit, self teachability, and an honest and transparent 
showcase of the progression. 
If I leverage my past, my identity, my references, my ambition, my grit, my drive, my focus, my unrelenting nature - I am sure to succeed. I will not fail. 
From henceforth, everything will be: Combat training, working these projects, reading books, and progressing towards Next Chapter. 
I will complete my GED and ensure that I have that in the pocket in time. 
I will also find multiple online platforms to learn and acquire credible certifications through platforms, showcasing that I am capable of learning and seek to learn as much as possible 
as aggressively as possible. 
School might have to wait a term.
I need to start with Rolling Victory Engine so that I can track everything that I'm doing, integrate that into either Obsidian, Notion or both, have my profile snapshot complete 
Secure housing, comply with probation, continue treatment, and also start combat training once a day 

The project progression: 
#0 Second Wind (Highest impact, lowest technical effort to initialize)
Extraction from ChatLogs - Then complete my own intake profile 
#1 Profile Snapshot/Intake Form(name the profile snapshot component) 
#2 Rolling Victory Engine - Fine tune and complete Rolling Victory Engine (After snapshot is uploaded and task reservoir is complete. Complete this first so that I can track all skill/task/life goal progressions) 
#3 tar0t draw - After the profile snapshot and intake form are done, fine tune the resource acquisition in its cloud AI platform iteration. Eventually, it should be a standalone app and function API calls, either local AI or open source cloud AI 
#4 Workout protocol - Optimize it for recovery. Create an app out of it that has a glossary of adaptations, allows you to either select components to yield adaptations, or select adaptations to yield components. If I can atomize all of the proccesses of exercise programs by aggregating all of the methods used by top tier programs, then I can provide the ability to fine tune highly optimized programs for an individual by selecting components. 
#5 Knowledge base - 
#7 Content base - 
#8 Resource database 
#9 Self Training Methodology 
#10 AI Smart Tutor (better than what exists) 
#11 Content generation pipeline (Auto, semi auto, and manual. Generate content that can successfully standalone based on intake forms, forms i circulate in treatment, second wind, at the rc and in the street 
#12 Get 4D Recovery on board 
#14 Get The RC on board 
#15 Get my PO on board 
#17 Get Washington County Jail on board 
#DealSealer - Find a way to monetize this whole $chab@ng so that it can self sustain its progression, scaling and mutation 
##extra - Flex Fund Clinical Evidence Support Engine (Search pubmed etc., find supporting items, generate letter) 


LONGER TERM PROJECTS: UNRELATED TO NEXT CHAPTER 
~~Learning potentiation: use bineural beatz and sonic frequency properties to allocate certain resonance qualities that affect brainwave frequencies for audiobooks 
~~~Ideal method, possibly: Create a program that allows you to select the properties you want, up to x amount of frequency layers including the sonic properties of the voice 
~~~~Program then generates a audiobook from an ebook that has multiple clinically substantial resonant frequencies designed to potentiate retention and deep learning 
To optimize my chances of succeeding, 
The information video said that technical proficiency was only one of the relevant criteria for the admissions process. From what it sounds like, it's an aggregate of myriad datapoints; 
Your story 
Your work ethic 
Your resolve
Your character 
Your skill-less proficiency (your ability to acquire skills, learn, problem solve, and map out solutions to problems as you encounter them - your ability to progress regardless of the circumstances) 
I ace all of the criteria. My story kicks ass, I kick ass, my background kicks ass, and I'm a perfect fit. Justice involved like a mother fucker, and the fact that all of the projects i'm working on 
directly revolve around helping people like me, and the fact that I intend to use Next Chapter to perpetuate my abilities for this purpose - should be an ace for fuckin sure 

So to optimize, I think I need to: 
Present the progression of all of my ideas from concept to documentation to artifact to functional prototype to launched item 
Log the learning progression 
Learn thoroughly as I go, identifying new skills or target problems that mandate new skills to be acquired 

Taken a few day break from things 

Been pursuing setting up local automation pipelines to distill my conversation history into usable materials (content skeletons, artifact skeletons, cross-polinated hybrids of adjacent domains' top tier knowledge (IE top tier books in multiple combat physiology + anatomy + addiction recovery) or automations that identify potential cross-pollinations, or other novel methods of combining information and forming genuinely useful novel material or presenting existing information in progressively more useful ways) 

Current workflows i'd like to construct: 
on demand workflows 

ongoing passive workflows 

ongoing utilities 

Next Chapter Project Notes Sequence 2 
Hey! So it's been a while since I've actually been able to do more than theorycrafting, ideation refinement, getting my computer more equipped and getting familiar with the command line, 
and getting other pre-requisites out of the way. 
So, my name is Shane W. Johns and I am struck with faith in God at the timing and existence in general of Next Chapter. I stumbled onto it while hunting resources/opportunities while 
I was in custody. 
While in jail, I was able to get a month of sobriety under my belt, start working out, start treatment, get my social security card, get into a career development program, 
get two phones, get two laptops, get my ID, get my glasses, get on proper medication, 
get on housing lists, get some debts squared away, get signed up at Portland Community College, get my GED, and much, much more. 
I was taking Adult Basic Education classes at Portland Community College in preparation to start taking Computer Science classes to start. 
I ended up losing my lodging at Washington County Community Corrections Center because I couldn't be on time and I had a disagreement with a guard. I was invited to come back, but declined. 
So I had to get my GED, study and complete coursework, do my physical training, and everything else while homeless. 
I've been setting my computer up and training myself in some basics as best as I can while solidifying probation, treatment, getting my GED, keeping up with physical conditioning, and 
resource hunting to try to get my housing squared away. 
I'm happy to say, i have a tinyhome that I'll be able to stay in by the time Next Chapter's cohort begins. I have completed my GED in time to submit my letter of interest as well as 
get financial aid and take classes at Portland Community College this term. I might only take a physical training class so that I can focus on Next Chapter, however. 

So, that's kind of my life update. 
I've come to realize that documentation of my endeavors, activities, and now that I am in position - My training - will be a very powerful habit to begin. 
So this crude log is the very first in a series of daily logs that I will keep no matter what. 
I've been theorycrafting many systems and it is time to actually pull some into reality. 

So for Next Chapter, I want to create a website that will present a solid, marketable product. 
The website I am going to make will contain these aspects: 
1) An introduction/profile. Not too much, but enough to present context, character, and establish that I have experience that will yield result, and that I intend to help. 
2) Re.Match - Simplified: User fills out form I have on website, user recieves a "dossier," which is an action plan that categorically provides as-close-to-optimal-as-i-can-claim paths. 
The workflow : They fill out a form, either by recording a voice message and reading the form out loud and then the answers, or an unstructured voice message just stating what they need help 
with, or type it out. If the form is audio, it is transcribed and sent to an intake inbox. If it is not audio, it is sent to the intake inbox. From the intake inbox, it is converted 
to a json schema profile. I then, currently manually, run it through a scripted series of prompts that identifies the highest "life impact," 100% criteria matches for their given constraints, 
affinities, alignment, needs and interest. 
The form has been through a few iterations before I am ready to add it to the website.
The first version of the form, I did by hand and it was pretty good. I basically stated categories of aid they could pursue to guide them, left an open category, got basic demographics, 
a bit of alignment, interest and affinity information, and that was it. 
The next version was 80 questions long and I determined to have as much data as I could get without being invasive, which seems paradoxical when I type it outloud. 
Then I created by hand another version, which was pretty close to the first version. 
Finally, I used Gemini 3.0flash and Codex, had them each create an amalgamation of all of the versions with the intent of having the bare minimum amount of exactly "perfectly" functional
information. Too much information, too many fields - I am not experienced or skilled yet, but I imagine that would break the schema, result in bloat, pollute the context/token limits, 
be difficult to log to a database, and possibly obstruct retrieval instead of aid it. 
Then I wanted to make sure that the workflow was correct in using AI. As far as my reckoning goes, web scraping and scripting is highly effective for deterministic, specific, reoccurring,
targeted information harvests. AI is better for complex, abstract shit. So for acquiring "the d0pest sh1t my dawg can d0 to $wag his life up, yo," AI excels beyond a scraper. 
However, for maintaining the legitemacy of the vitality of objects in a database of the aforementioned d0pe sh1t, a scraper would be effective. 
So the concept at this point, now that I have a form that I'm willing to push - for the Re.Match project, which is the flagship content for the website - 
Form is complete. 
Now I get a version of the form, basic, typed, on the website with a working email submission. 
Then, I learn to use GitBranch.
To practice/learn Git Branching, 
I will iterate versions of this concept. 
First, I will push the vanilla form version. 
Then, I will branch push (or just branch?) a version of the form that contains a microphone button next to every response field. click the microphone and you can speak the field. 
Then, I will branch push a version that has a way to just record you reading the form outloud...this is sounding pretty weak as i type it. what happened...ill check the logs, i'm pretty 
sure i remember it being better. maybe the microphone button version is just that much better. the idea was that this version would allow more freeform, organic responses with more 
nuanced character to emerge, allowing for more abstract matching 
Then I will branch a version with a voice navigation feature that allows you to voice navigate to other fields. I dont know if this is even a thing, but the idea keeps coming to mind that 
my people, my street homies - have low attention span, low energy for anything that isn't gettin dope, gettin bread, or gettin laid, as unfortunate as it may be that is the state 
of the downward locale of the spiral 
I'll merge whichever branches don't suck after attempting to iterate into a fine tuned version of each of them. 

Once I have the form submission down, I will submit a test version using myself. 
Once the microphone button one submits clean, the audio clip one submits clean and transcribes to audio with no worries about length or rate limits, the voice navigation works, 
and it all sends to the intake funnel and converts to schema - Then its prompt engineering. 
My original method was SLOPPY. NOOB. GARBAGE. I was just a nooblet who liked AI a lot, which is still more or less what I am, but I just designed a cracked out prompt that kicked ass at finding 
things that matched the json profile i created for myself, created EIGHT threads on ChatGPT AND Perplexity, one for each category - 16 threads 
and i hit deep research, and kept typing "Continue, continue, continue, continue, more, more, more"  
I really came to an intimate understanding with the limits of those platforms with this and am so enamored with the command line versions oh my goodness. 
so my current epitomized version of this concept, to ensure no redundancy as a policy to increase the amount of opportunities i harvest 

the plan is to create a prompt that adds everything to a database file. the database file will be indexed with the attributes to which an individual can match, services offered, and metrics 
of evaluation/rating in certain categories, with the "life impact" metric being entirely dependent on the person and their circumstance. A 100/100 on the life impact metric essentially means 
that the opportunity/resource hits like 3 or 4 of your categories of interest. 
anyway, so as searches are run for every person, their results are added to a big fat database file - possibly multiple database files, categorically divided. 
they are indexed 
then every search moving forward is ran first against that database with a "no redundancy, do not list items in the database in your results or pursue them. add new items to database and index them." 
then after several runs, manual review, etc. 
A final search against the database only is ran 
Final output is 
The top 1 opportunity/resource per category in full detail with an action plan, what to do, how to do it, where to go, phone numbers, addresses, urls, time to fruition, difficulty barrier, 
end result, prerequisites, possibilities after completion  
Two follow ups  in full detail as well 
5 honorable mentions in short list format with a description of what they are and why they aren't in the top 3 
Then a link to the complete database. 

An issue I've percieved being possible is people being reluctant to post their data on some random dude's website - reasonably so. I don't have the ability to offer confident security yet. 
So I've contrived a solution which is still ambiguous but seems plausible where instead of their name they submit a code of their selection, an alphanumberic like SLICKDICKRICK69 or 1825932 
and I upload the dossier publicly with their constraint flags, none of their demographic information, and their identifier number - that way people with similar constraint flags can 
check it out as well as the person can access it without needing to offer their name. Alternatively, they use the service at their own risk and i offer scouts honor that i wont 
share their information and i do my best to keep it secure. 

PHEW. and that's the Re.Match system. 

ANOTHER COMPONENT for the website 
I'm currently distilling all of my conversation history from since I was in The RC to now into content, as best as i can with my current skills. 
i'm going to identify rock solid exerpts and put them up on the website. guides to resources, guides to being homeless, guides to recovery, recovery science, shit that's relevant 
open source books (if im allowed to) and links to resources and shit 

I have a few different versions in mind to try, and that's the step i'm on right now. I just finished ironing out what the form will contain.
I use the platforms for standard research, information aggregation, resource/opportunity aggregation, and then synthesize useful documents out of them or export my chat files to my computer. Once they are exported to my computer, I use Gemini CLI and Codex to deploy agents to normalize and consolidate my messy notes, downloads, personal documents, downloaded documents, and books into a structured "Information Base." I then parse the chat history, which is reflective of my journey as a homeless Justice Involved Individual who was just released from custody and is on probation, journeying with fervor and zeal through the early stages of recovery - By structuring and logging my inquiries, my notes, my thought process, the details of my life, the resources - everything - I am creating the raw material with which I can produce a great many things; Personal blog history, distilled information presented in a manner targeted to individuals in custody, resources for homeless people and JIIs, guides and tools - essentially providing everything that has led me to be able to confidently slaughter fentanyl addiction and become a high energy, disciplined, focused and excited-to-be-alive human being again. I am working on a few projects right now revolving around my experience in custody and in recovery. 

One is called "Re.Match," or "Resource Match." Please, read through all of this and not just the beginning. The first iteration of it was ugly and crude, but yielded what is a very high yield (in terms of positive world impact, I truly believe this) concept. It is inspired by my extremely sloppy early research waves that led me to all of the bewilderingly perfect opportunities available to me, such as Next Chapter. Back then, I was more proficient than a noob by an extremely large margin, but absolutely nowhere near the proficiency of real developers or coders, nor did I myself identify as such an individual.

 I was, however, absurdly good at actually utilizing AI platforms for real world scenarios. The system I initially created was as such: First, I designed a questionnaire for myself that would allow me to create as complete of a snapshot of me as an individual as I could. Then, I converted that to JSON. Then, I used a no-redundancy policy to iterate multiple deep research threads on multiple platforms, harvesting everything I could that was a 100% Criteria Match (or nearly matched if I completed something in progress, like getting my ID) and as close to 100/100 on a subjective metric called "Life Impact," which I explained to the AI as "Life Impact is measured by increase to liberty, societal freedom of movement, sufficient resource to meet all needs, and aligning with an individual's interest, alignment, affinities and needs." Similar to the Japanese concept of Ikegai, which is embedded into the design of the current version. So what I had then was about 300 pages of resources, a lot of redundancy, no consistency in quality. I sloppily made multiple "dossiers," some of them coming close to what I output now. I then uploaded those, processed them into a bunch of reports, then combined them into one final report. The final report was amazing, it was exactly what I was hoping for, but the process was ugly and needed work. 

I have since refined the process majorly, having learned an immense amount from the experience of the first iteration. Now I have a more simple form, using myself as the prototype because I am exactly the demographic that I am trying to help, which makes it easy to iterate on. It is designed to have the minimum amount of questions to have maximum yield, so as to not dissuade individuals possibly in recovery, still regaining their attention span and discipline. Also accounting for time, for situations where JIIs might be in a program where they have access to a computer for a brief amount of time periodically, as was the case while I was in custody. 

I'm finishing the design for the form right now and learning about what I'm doing as I go but the working concept is: For the form, I include the option to either record voice and submit an audio recording, which will then transcribe automatically and parse to JSON. I will manually review and infer or clarify mistranscriptions, A microphone button next to every field to fill out the fields with voice. I figure having a more freeform option will allow an individual to get more relaxed, revealing more character and nuance which will help in identifying matchable traits. The more structured method will be more accurate and appeal to certain individual types. 

Form responses go to an intake email I've sent up, then I manually grab them, verify they're all coherent, then feed it into an agentic split. An agent per category hunts opportunities/resources, matching them to the attributes with a no-redundancy policy - For every subsequent run, if it encounters a match it has already logged or analyzed, it will pass over it instead of blowing resources and time. 

I decided that it would be effective if all opportunity harvests added to an ongoing database, which each search matched against to save resource and time. I could also, as the database expanded, index it by establishing attributes and metadata to every item in the database, such as types of offenders it matches to (Currently in prison, post-prison, post-jail, probation, felon, misdemeanor, drug related offense, theft, etc.)  which is essentially the whole principle of Re.Match. I noticed that a lot of individuals view their legal status as a limitation, but my philosophy has always been converting weaknesses into strengths instead of A) Patching them up by mitigating the weakness, or B) Ignoring your weaknesses and playing to your strengths. I've met so many non-offenders who are frustrated and jealous of some of the opportunities present for JIIs. So introducing those opportunities and helping people slay their demons, fall in love with their selves, and find a path that is honest to who they are at their core is something I am heavily interested in. 

Beyond THAT, I'm using it to generate content out of my chat history, organize my plans, projects, tasks, schoolwork, notes, etc., research in depth literally anything and everything I can, I used it to study for my GED test by creating practice exams, doing them, uploading the completed practice exam, then having it assess my weaknesses and drilling me on them. I've used it to teach me HTML,JSS and CS, I've used it to work through extremely stressful personal situations - situations where another individual might have relapsed, but I used it to psychoanalyze the shit out of myself and work through it. 

I use each platform for different things, Perplexity for research and aggregation, ChatGPT for researching anything that needs to be interacted with like a human (Agent Mode, searching medical databases for providers covered by my health insurance in the specialty im looking for, creating a list of them, and providing me with their professional history, educational background and specialty, for example. ChatGPT also for synthesis, and I'm about to disable memory on it now that I'm getting a bit more savvy and learn to use the custom MCP feature) I use Gemini for Google integration, phone commands, and also Gemini CLI because it's really good and I don't think its possible at my skill level to hit rate limits with Gemini Google AI Pro. I really want to expand my skills and knowledge and have my eyes set on a few tools and frameworks, but I don't want to speak on speculation. Open Interpreter, local models, and OpenClaw are interesting to me - It would be pretty cool to have a multidevice setup where a voice interface could query intelligently, write and execute a script as needed, offload queries that need a smarter model to a cloud model, feed that back into the local model, and execute. Speculative, and I don't even know what I want to do with it, and I'm not there yet.

That said, I know that I am a noob and I have an infinite wealth of knowledge to learn - that is not daunting to me, it is hugely driving because I know that even at my low skill level, I am capable of applying the skill that I /do/ have in genuinely high impact ways. So, imagining the amount of positive impact I could have if I had proper training and education, it gives me hope for truly transmuting my life and turning everything around. 

If I were able to be provided with such support, it would almost feel like Divine Providence that I ended up here - By suffering well through these last 5 years on the street and in and out of jail, I have learned humility like I never knew before, I've learned the ins and outs of the reality of addiction and hopelessness. I can truly make a difference, and I ask that you bet on me. I am unmolded clay, I am humble, I know that I do not know, I am eager to learn, I take criticism well, I enjoy learning very much, and I am relentless when an objective is set. 

Apologies for going too hard on this question, but I feel as though illustrating that my heart is open and being completely transparent is important.
Git can seem confusing at first, but understanding  a few key concepts makes it much clearer.
0:13
In this video, weâ€™ll walk through the basic  
0:15
Git command workflow and clear  up some common misconceptions.
0:20
I'm Sahn, co-author of best-selling  system design interview books.
0:24
We explain complex system design  concepts clearly through animations.
0:28
Let's get started.
0:30
Before we dive into the commands, letâ€™s  identify where our code is stored in Git.
0:35
The common assumption is that  there are only two locations,  
0:38
but our code doesnâ€™t only exist  on GitHub or our local machine.
0:43
There are four main locations  where your code lives in Git:
0:47
The Working Directory: Where  we actively edit files locally.
0:51
This is our playground.
0:53
The Staging Area: Itâ€™s a temporary holding  spot for changes before committing.
0:59
The Local Repository: This is where  we store committed changes locally.
1:04
The Remote Repository: A server like  GitHub for sharing and backing up code.
1:10
With these zones in mind, letâ€™s visualize  where our code travels throughout its journey.
1:16
Most git commands move files  between these four locations.
1:20
The first step is to git clone an  existing repository so you have a  
1:24
local version of the project to work  on, complete with all its history.
1:29
With the repo cloned locally,  let's look at where the code lives.
1:34
When you start working on a file,  you're in the Working Directory.
1:37
This is your local development environment  where you make changes to your code.
1:43
Now, when youâ€™re ready to commit your changes,  
1:45
you'll use git add to stage a snapshot  of those files in the Staging Area.
1:51
Think of this as a checkpoint, where your changes  are gathered up and ready to be finalized.
1:57
The next step is to use git commit,  
2:00
which takes a snapshot of the staging area  and saves it to your Local Repository.
2:06
This locks in those staged changes  by creating a permanent record that  
2:10
you can refer back to, like a snapshot in time.
2:14
Your code doesn't just stay on your local machine.
2:17
When you're ready to share your progress  with the team or back up your work,  
2:21
you use git push to send your  commits to the Remote Repository.
2:26
This is often a shared server where your team  can collaborate, like GitHub or Bitbucket.
2:33
Collaboration in Git is a two-way exchange.
2:35
To integrate your teammates' work, you  use git pull, which fetches changes from  
2:40
the remote repository and merges  them into your local repository.
2:45
It combines two commands: git fetch, which  grabs the latest updates, and git merge,  
2:51
which integrates these updates with your work.
2:54
There are times when you need to switch  contexts, perhaps to fix a bug on another branch.
2:59
That's where git checkout or git switch comes in.
3:03
It allows you to switch between different  branches to work on specific features.
3:08
Git branching allows you to diverge from the main  
3:11
codebase to develop a new feature  without impacting the main code.
3:15
Some key concepts include creating  a new branch with git branch,  
3:19
switching between branches using git switch,  
3:22
merging branches together with git merge, and  resolving merge conflicts when changes overlap.
3:29
Branching enables isolated development  and collaboration workflows.
3:34
There are more nuance when merging or rebasing  changes from others or managing branches.
3:39
We have a dedicated video on merging and  rebasing that we encourage you to watch.
3:45
Many developers use graphical git tools  like GitHub Desktop and SourceTree.
3:51
These tools provide visual interfaces  and shortcuts for common commands.
3:55
They can help new users get  started with git more easily.
4:00
If you like our videos, you might like  our System Design newsletter, as well.
4:04
It covers topics in trends  and large-scale system design.
4:08
Trusted by 500,000 readers.
4:11
Subscribe at blog.bytebytego.com.

All

From the series

From ByteByteG
Hi, my name is Shane Johns. What follows is a letter broken up into multiple parts. 
First, I've written the shortest possible summary of the letter with as little personal narrative as possible, since I'm sure you're busy and a gigantic wall of text from some strange 
man is probably a daunting occurrence in your day of being a literal hero/heroin. Thank you for your work, by the way. 

#####SUMMARY##### 
Iâ€™m writing this because I have difficulty finding a way to put my circumstance into words whenever I meet with someone or talk to them on the phone, or they don't think to ask me. So I'm looking to clarify some important details and send this letter to both existing applications and new contacts, in hopes of getting connected with something as soon as possible. , 
There are several factors Iâ€™ve wanted to bring up in housing appointments that I havenâ€™t. 
I was talking with a friend and they said I should absolutely mention these things because they might have a direct impact on my well-being, and shouldnâ€™t be left out.
You are recieving this letter if you are affiliated with A) Housing/Reentry programs that provide non-congregate shelter/motel/hotel stays or might be able to help towards that goal. Or B) Can help me move forward in the extremely complex pipeline of things towards stability.
Iâ€™m writing to you because I am in an active housing and safety crisis and Iâ€™m trying to find a temporary non-congregate shelter, hotel, or motel situation that actually fits me so I can eliminate dangerous and unhealthy variables, stay sober, and focus on my probation, GED, college work, instead of spending all day every day just barely surviving and being treated like I'm not allowed to survive.
This email is going out to a lot of people at once because I need help quickly, it's been five years and the one chance I had was obliderated by factors outside my control at the time. 


I'll explicity list these criteria up front, in a bulleted list format. This is the main deliverable of this email, is my qualification criteria. 
-I am homeless, have been for 5 years, with the exception of 1 year in an apartment. I've lived outside, not in shelters or on couches or in a car. 
-4 months sober 
-In treatment (CODA Hillsboro IOP) for Polysubstance Use Disorder\
|--> which is absolutely an officially, legally designated debilitating medical disorder.
-I also suffer from major depression. 
-I also suffer from ADHD. 
-I also suffer from psychosis induced-PTSD, from when I quit drinking alcohol for the first time over a decade ago. 
-I am a Portland Community College student on probation
-I am, by multiple official classifications and citations, absolutly a victim of victim of domestic and interpersonal violence 
|-->I have included citations that corroborate with my facts, and detail how and why I am stating and invoking this, and how and why it is legitemate both ethically, legally, and morally.
-Have issues related to the above (multiple items) that severely deteriorate the efficacy of congregate housing to the point that I prefer livin outside to it. 
|--> I do NOT enjoy living outside, and it is absolutely destroying my ability to maintain with probation, with treatment, with mental health sanity, with physical health, with personal safety, with education, with career development. 
|------> Essentially all of the hard work I did during and post incarceration is being unraveled at an extremely compounding pace. 
-My issue in terms of my sobriety isn't neccesarily being around drugs per-se, it's more about the escalating inability to keep up with any of the things I was doing to move my life in a positive direction. 
|-->Being within the homeless community won't compromise my sobriety if all of my mitigation strategies are running. They are all breaking right now due to my instability and lack of structure, though. 
|---->This is an addendum post-script, in case someone reading this were to consider "Well if he has issues being around drugs, he won't do well within the homeless community." or something like that. 

#####END OF SUMMARY##### 


#####CONTACT######
If you only read the summary, here is my contact information. 
Email1: Shane.Johns1@pcc.edu 
Email2: TarotAlucard7@gmail.com 
Phone: 971-494-5103 You can text or leave a voicemail without worrying about privacy or leaving information 
Mailing address : 34420 SW TV HWY - Cornelius - Oregon - 97123
Iâ€™m trying not to make another desperate decision. I fear that with congregate shelter or even a program like bridges to change, I might run into people connected to my ex and end up unsafe or relapsing again; 
Iâ€™m trying to buy enough time in a private, stable place to actually put thought, effort, love and care into choosing the best housing option for my future instead of watching my life break immediately all over again.
Further more, in terms of temporary stays- even a week or month right now would enable me to catch up on homework and finish my GED classes on time; 
there was a life changing bootcamp I was preparing to take and I only have two weeks to complete the pre-requisites. 

A bit about my unsafe situation: 
Iâ€™ve been homeless since the start of COVID, with the exception of an apartment I had for a year. This apartment was hostile overtaken by people that threatened me, messed with me, stole from me, messed with my girlfriends head and did bad things to both of us physically and mentally, and mind-fucked me into oblivion whilst keeping me on exactly enough fentanyl to constantly be in withdrawal. 
Going exactly the amount of time it takes to get through the withdrawal phase, then giving me just enough to get well or overdose once, then back to withdrawals. They would even dose me with NARCAN if I simply nodded off and wasn't overdosing, putting me into precipitated withdrawals and acting like I couldn't control my smoking. I confirmed this with an individual to be true. 
My sanity reached cripplingly low points. Then the girl I moved in with moved in with her ex and abandoned me, while ensuring no one would sell to me. I couldn't make it out of withdrawal long enough to take care of my place and I couldn't leave my place because my things weren't safe with a ton of people staying there uninvited. I couldn't call the cops because that's not a safe solution. 
After I lost the apartment, I started getting stalked and attacked. Iâ€™ve been assaulted and threatened with violence by people of relation to my ex on at least five occasions for certain. 
Iâ€™ve been stolen from by people affiliated with my ex over 15 times, including very recently. 
One of her friends threw a slushy in my face while they were driving towards me in oncoming traffic, which almost led to me dying. 
One of her partners or ex partners jumped on me while I was withdrawing in a â€œfriendâ€™sâ€ car and beat me bloody then stabbed me in the head with a pen. Turns out the â€œfriendâ€ sold out my location for $20. He was one of the individuals I had let live in my apartment who then refused to leave.
One of her friends or partners tricked me into coming into his house, and then told me to drop my belongings and get out or he was going to beat the shit out of me and take my shit anyway. I said "you're not taking my things." and proceeded to walk out. He tackled me into a glass table, I was cut in a few places, then he beat the shit out of me.
I was stolen from just a week or two ago outside and saw the person who stole my stuff, it was one of the same people. 
Police reporting is not an option. I just want to get off the streets and get away from all of this already. 

I am homeless and have been for 5 years. 

I am a victim of domestic violence and interpersonal violence seeking safety, and I meet state, federal, nonprofit and international definitions. 
I am subject to multiple debilitating medical disorders which prevent me from successfully/reliably doing basic human needs 
(Poly Substance Use Disorder, Depression, ADHD, PTSD). 
I am a student of Portland Community College trying to get my life together.

I donâ€™t mean to absolve myself of any accountability in my situation. 
I am the architect of my own suffering, there is always something to learn from a situation and I do not intend to let any of this happen to me anymore. 
There are, however, a lot of factors that are not directly my fault or within my control that are ruining my ability to live. 
I wanted so badly to turn my life around with that apartment. Then I was cheated on, stolen from, mind-fucked, threatened, gaslighted, and made to look like an evil individual 
and even believed myself to be an evil individual, when I was absolutely being destroyed and targeted by some truly horrible individuals.

Recently, I was doing SO well. 
I was attending the gym daily, enrolled in classes at Portland Community College, making it to treatment every day, making all of my probation appointments.
I was excited to go visit my mom after probation ended and show her "look, not only am I sane and not in psychosis, but I'm a fricken tank, learning martial arts, in school, have started a non-profit, am sober, and have cut all ties to bad things!" 
That vector is deteriorating day by day.  

I have a storage unit, two sleeping bags, and a bunch of warm clothes. People have been helping me with what they can, but my life is at stake and there has to be something more that can be done. 
So again, this letter is to outreach to people I've already made contact with to update my profile with all of the relevant factors, 
and also as outreach to individuals and entitites I have /not/ made contact with. 
If you could forward my information to someone that can help, forward my email to the appropriate intake line, or reply with any kind of critical information; 
Or better yet, if you can directly manuever the machinations and help me find the path forward here, 
I would be so grateful. 

Thank you so much for your time and the work you do, if you're recieving this email you do amazing work and I am grateul and glad that you are here in this world. 

I usually state that I am capable of performing the basic duties to take care of myself, but I've come to realize, after discussion with friends and professionals; I absolutely am not. 
I can't make appointments, it take astronomical effort to even get out of the bed and go to the bathroom, my motivation and focus have reached a point of corruption where they are deteriorating no matter what I do and my depression is devouring my soul. 
I can't even make it to appointments where my freedom is on the line, I can't make it to my classes, everything is slipping. 
I am not able to perform the duties required to take care of myself; it took me two weeks to sit down and get this one wave of effort towards housing done; and it probably isnt even going to help my position any, which will result in more hopelessness devouring me. 
My drive and motivation are fading away, I have to look out for my future self and for my son who I haven't even met yet do whatever it takes to get into a place, and then to turn my life
into a powerhouse success story, helping as many people as I can along the way. I don't want to slip through the cracks here.  

I am subject to several debilitating mental disorders: Severe depression, severe ADHD, 
and I am 4 months sober in treatment for polysubstance use disorder, dr...u.g of choice being fentanyl.
I am a victim of domestic violence and interpersonal violence seeking stable and private safety.
I am a student of Portland Community College trying to get my life together.
There is $15,000 in damages I need to pay before I can even rent again. 
Someone told me there might be possible avenues to get my debt dismissed or consolidated or helped with, that's another area I'm pursuing other than direct temporary housing ASAP. 

I was told that if I start a payment plan on the damages and make a payment, I can rent again. Iâ€™m also working on the RentWell program.

Addenum, Iâ€™m working on designing a non-profit or grassroots community group to get people together to do fun sober activities, instill healthy habits, create a forum for healthy discussion and peer networking, as well as get some free classes and activities covered for the group. Iâ€™m also designing a simple to use productivity engine, a system to match people to the highest life impact 100% match possible opportunities that are available to them given their criteria, credentials, demographic information, barriers, desires and affinities. Iâ€™m working on a lot of things that I believe could change the world for the better. Not that anyone should need to meet some sort of performance criteria to be housed.

Please, point me towards any non-conjugate shelter options, ideally hotel/motel so that I can be alone and work on schoolwork without getting kicked out of every place I try to sit down on my computer at. Iâ€™m applying to housing related social needs, non-profits, community connect, and every email I can find that might be able to directly or indirectly help me.
If there is some way you can help that I haven't concieved, I am all ears. 
I am so grateful for your time and hopefully this email wasnâ€™t too exhaustive and you donâ€™t mind the spam. Iâ€™m not looking for sympathy or special treatment, I just need help. The point of this letter is to clearly and concisely explain my story, situation, and clearly state, itemized and clear, the criteria that should elevate my priority. Iâ€™ve been turned down by multiple Domestic Violence advocates who refused to even look at my citations regarding the nature of domestic violence and its legal classification that it can absolutely be carried out by an individual who is not your ex but is connected to your ex. I am in fear for my safety regularly, and my psyche is bleeding out from a million different holes and Iâ€™m trying to stablize the wounds. I have difficulty with phone calls and in person interactions because I usually just say â€œiâ€™m fine,â€ and am embarrassed to say that I am absolutely not fine and ask for help. Through this same issue, I have myriad physical conditions I need to see a doctor about as well - so iâ€™m performing a similar activity to hopefully get all of my medical issues taken care of.

My name is Shane Walter Johns, 15 year Oregon resident. 
HealthShare of Oregon OHP/Medicaid member. 
Mailing Address: 34420 SW TV Hwy, Cornelius, OR 97123
Phone number: 971-494-5103 (I am hesitant of unfamiliar numbers by habit due to my unsafe situation but I try to answer every call I see right now for housing. Sometimes I miss calls because it is insanely chaotic. 
If email can be the method we communicate and perhaps meet up in person to discuss any opportunities, or I can call at a scheduled time, or I can try harder to not miss phone calls.
My email address is 
Shane.Johns1@pcc.edu 
or 
TarotAlucard7@gmail.com 

Thank you if you read all of this or even the first part. 
What is Notepad++?
******************

Notepad++ is a free (as in "free speech" and also as in "free beer") source code editor and Notepad replacement (https://npp-user-manual.org/docs/other-resources/#notepad-replacement) that supports several programming languages and natural languages. Running in the MS Windows environment, its use is governed by GPL (GNU General Public License).


Why another source code editor?
*******************************

The company I worked for used JEXT (another open source code editor in Java) as the production tool. Due to its poor performance, I began an investigation to find another solution (in C++ instead of in Java) in September 2003. I found Scintilla and built a prototype. This solution was not accepted. I removed the specific part and continued to develop it in my leisure time. On the 25th November 2003 it was made available on Sourceforge, hence the birth of Notepad++.


How to install:
***************

From the installer:
	Just follow the installation instructions.
From the zip/7z package:
	Unzip all the files into a directory you want then launch "notepad++.exe".

	
Web sites:
***********

Notepad++ official site:
	https://notepad-plus-plus.org/

Notepad++ project site:
	https://github.com/notepad-plus-plus/notepad-plus-plus/

Notepad++ user manual:
	https://npp-user-manual.org/

Notepad++ forum:
	https://community.notepad-plus-plus.org/


Author:
*******

Don Ho <don.h@free.fr>
	https://notepad-plus-plus.org/author/
Hi! I go by Shane. So, my name is Shane W. Johns, 15 year Oregon resident. I am a homeless Justice Involved Individual who was just released from custody and is on probation, journeying with fervor and zeal through the early stages of recovery. I'm 5 months sober. Just got my GED with flying colors. Enrolled in college. Signed up for financial aids and grants, have a full ride ahead of me. Training at the gym daily. Start martial arts classes next week. All of this while living outside, recovering from extreme mental illness, and processing my self inflicted trauma with replicatable successful integration of my fractured psyche.

By suffering well through these last 5 years on the street and in and out of jail, I have learned humility like I never knew before. I had at this point lost literally everything and the only option left was to recover my honor and rebuild with discipline, focus, and unrelenting faith that through honor, discipline, integrity and compassion - anything is possible. I am the architect of my own suffering, there is always something to learn from a situation and I do not intend to let any of this happen to me anymore. I am proud to say that I was not full of shit all these years and astounding results are approaching, so long as my humility, discipline, focus, integrity, honor and compassion remain intact. I will make up for my dishonor in spades and hearts.

I have about 15 years of working in restaurants I've been a manager at every job I've worked at... I've been a trainer at every job I'm highly capable of hard work focused work disciplined work and I've learned a lot of skills over the years through employment and that doesn't even cover my personal skill pursuits. My goal: Find a way to get a full ride to complete competency in the fields I want, go to school as much as I want, create a freelance business unique to me using my identity as power, and empowering my identity, and sustaining myself and not just surviving but thriving - for FREE. Introducing those opportunities and helping people slay their demons, fall in love with their selves, and find a path that is honest to who they are at their core is something I am heavily interested in. I will help people who are coming out of constellations of circumstance similar to my own, which will function as my medium, metric, anchor and fuel.

I am working on a few projects right now revolving around my experience in custody and in recovery. One is called 'Re.Match,' or 'Resource Match.' Individual submits a form that the creator has made, form contains all information required to find user exact matches to their circumstance. Other projects include Second Wind, a social collective designed to function as a social outlet that employs myriad scientific backed methods to go beyond simple mitigation of criminogenic recidivism and relapse factors, and focus on the potentiation of strengthening factors... Rolling Victory Engine... I will also host my workout protocol, which is designed with recovery in mind.

I noticed that a lot of individuals view their legal status as a limitation, but my philosophy has always been converting weaknesses into strengths instead of A) Patching them up by mitigating the weakness, or B) Ignoring your weaknesses and playing to your strengths. By structuring and logging my inquiries, my notes, my thought process, the details of my life, the resources - everything - I am creating the raw material with which I can produce a great many things... essentially providing everything that has led me to be able to confidently slaughter fentanyl addiction and become a high energy, disciplined, focused and excited-to-be-alive human being again. 

I can only hope that by driving ahead at full velocity at my current vector, with persistent calibration to ensure I'm upholding what I stand for in as many of my activities as possible ; hopefully I can mend any wounds I've caused alleviate the suffering of anyone I can, and teach individuals as I learn to integrate their suffering into power through healing - the power of unconditional love. With honor, respect, and adoration for all beings, I do these things. I will engage the pressure until it crumbles. For Love and Justice, in the name of the Moon! Lux Illuminate Destiny.
Hi! I go by Shane. So, my name is Shane W. Johns, 15 year Oregon resident. I am a homeless Justice Involved Individual who was just released from custody and is on probation, journeying with fervor and zeal through the early stages of recovery. I'm 5 months sober. Just got my GED with flying colors. Enrolled in college. Signed up for financial aids and grants, have a full ride ahead of me. Training at the gym daily. Start martial arts classes next week. All of this while living outside, recovering from extreme mental illness, and processing my self inflicted trauma with replicatable successful integration of my fractured psyche.

By suffering well through these last 5 years on the street and in and out of jail, I have learned humility like I never knew before. I had at this point lost literally everything and the only option left was to recover my honor and rebuild with discipline, focus, and unrelenting faith that through honor, discipline, integrity and compassion - anything is possible. I am the architect of my own suffering, there is always something to learn from a situation and I do not intend to let any of this happen to me anymore. I am proud to say that I was not full of shit all these years and astounding results are approaching, so long as my humility, discipline, focus, integrity, honor and compassion remain intact. I will make up for my dishonor in spades and hearts.

I have about 15 years of working in restaurants I've been a manager at every job I've worked at... I've been a trainer at every job I'm highly capable of hard work focused work disciplined work and I've learned a lot of skills over the years through employment and that doesn't even cover my personal skill pursuits. My goal: Find a way to get a full ride to complete competency in the fields I want, go to school as much as I want, create a freelance business unique to me using my identity as power, and empowering my identity, and sustaining myself and not just surviving but thriving - for FREE. Introducing those opportunities and helping people slay their demons, fall in love with their selves, and find a path that is honest to who they are at their core is something I am heavily interested in. I will help people who are coming out of constellations of circumstance similar to my own, which will function as my medium, metric, anchor and fuel.

I am working on a few projects right now revolving around my experience in custody and in recovery. One is called 'Re.Match,' or 'Resource Match.' Individual submits a form that the creator has made, form contains all information required to find user exact matches to their circumstance. Other projects include Second Wind, a social collective designed to function as a social outlet that employs myriad scientific backed methods to go beyond simple mitigation of criminogenic recidivism and relapse factors, and focus on the potentiation of strengthening factors... Rolling Victory Engine... I will also host my workout protocol, which is designed with recovery in mind.

I am struck with faith in God at the timing and existence in general of Next Chapter. I stumbled onto it while hunting resources/opportunities while I was in custody. My current ambition is to get accepted into Next Chapter's bootcamp. Next Chapter's coursework is guiding me through creating this website. I am learning from the ground up with zero experience. Part of why I want to do NextChapter is to progress further in this and find a path to creating projects like this to help others. All of the projects i'm working on directly revolve around helping people like me, and the fact that I intend to use Next Chapter to perpetuate my abilities for this purpose - should be an ace for fuckin sure. If I leverage my past, my identity, my references, my ambition, my grit, my drive, my focus, my unrelenting nature - I am sure to succeed. I will not fail.

I can only hope that by driving ahead at full velocity at my current vector, with persistent calibration to ensure I'm upholding what I stand for in as many of my activities as possible ; hopefully I can mend any wounds I've caused alleviate the suffering of anyone I can, and teach individuals as I learn to integrate their suffering into power through healing - the power of unconditional love. With honor, respect, and adoration for all beings, I do these things. I will engage the pressure until it crumbles. My story kicks ass, I kick ass, my background kicks ass, and I'm a perfect fit. For Love and Justice, in the name of the Moon! Lux Illuminate Destiny.
Skill progression: 

July 2025-Before custody - Basic knowledge/understanding of ChatGPT & Perplexity. No idea how to get started in making a program or website or script or anything. 
September 2025-During custody - Deepened knowledge of the limits of ChatGPT Plus, Perplexity Pro, Gemini Pro, and myself. Started to have a refined understanding, expanded my knowledge of limitations, 
nuances, and what I needed to learn. Took an immense amount of repeated, redundant actions for me to obtain a result. Very sloppy, very ugly. 
January 2026-Skill progression post custody, pre Next Chapter preparation - Put on the backburner for physical training. I put my effort into designing a training program suited to me by (using AI) 
to decompose several of the most tried and true existing formats (Combat training, military holistic health, sports training) and comparing them to standard programs. I decomposed them 
into "atomic" components, a concept which would bleed into my future modus operandi. By identifying the actual scientific components and action points (IE What can be configured? What can be 
adjusted to yield a different result?) and identifying the adaptations that occur from certain exercises, I was able to configure a very good workout program that takes advantage of my 
ability to recover, my full nutrition/nourishment, etc. with a focus on recovery (both meanings of the word - drug recovery and recovery from training) combat mobilty, and military derived 
fundamentals (Marine Corps, Ranger and Navy Seals manuals and more) 
January 2026 At this point I'm doing treatment, Adult Basic Education classes through Portland Community College, training twice a day, and finding a place to sleep outside every day. 
Feburary 2026 Flash forward to Next Chapter - The day of the Information Session - So I thought that our websites were due by the day of the Information Session - Not with certainty, but I wanted to have 
mine done by then just in case. I finished it at exactly the start of the Information Session, but because I was at CODA (my outpatient clinic) and excited telling my counselor about 
completing it in time, I overlooked the fact that I had to ask in advance for a link to the Information Session. I was /CRUSHED/ but THEN it turned out that I had a LOT more time. 
So the day of the information session, I went to the Plaid Pantry i've frequented for 10 years, since before I was homeless - and hung out with the same graveyard homie I've been kickin it with 
since then. 
I focused on creating a quick curriculum using Perplexity to teach me how to create and deploy the website, I had it show me where to learn the code, tell me what I was looking for, etc. 
I installed VS Code, I created Index.HTML, Style.CSS, Script.JS and proceeded to create the skeleton for a cyberpunk styled website that I wanted to be the host of my future endeavors 
to help my peers and also offer my freelance services. 
March 2026 - I've gotten familiar with Powershell a little bit, running Gemini and Codex from the command line and using them to perform operations on my computer. I've started doing some 
pretty cool stuff and use them for actual action instead of just knowledge acquisition. 
Next goal: Focus on website. Get Re.Match live. Populate website with content. Ensure actual website fits the assignment rubric 100% and does not exceed the constraints of the assignment. 
That means anything beyond that has to happen outside the context of the website. 
# MySituationSpeaks: The Architecture of the Pivot
## A Manifesto on Sovereign Recovery & Systemic Reconstruction

### I. The Fragility of the Reborn
If you are recently sober, you are an extremely fragile being. You are essentially a reborn newborn, seeing a world that is objectively insane for the first time without a filter. You have spent years subduing your true self, replacing it with survival mechanisms and drug-altered perceptions of reality. 

Early recovery is not the time to "prove your worth" by crushing yourself under the weight of old obligations. If you jump into three jobs and eighty hours of overtime to provide for your family, you will alienate your support network and make your sobriety contingent on your employment. When you inevitably take an emotional blow, you will use. Do not betray your long-term reconstruction by rushing your short-term optics. The slower you learn, the deeper you learn.

### II. Sovereign Autonomy vs. Co-dependency
I believe in Love above all, but I believe more in the necessity of **Sovereign Autonomy.** In a coupling, both individuals must be capable of independent survival and growth. If one of you falls, the other should not die from ineptitude or sorrow. 

Washington County doesn't hand out No-Contact orders because they are money-hungry; they do it because they know that without separation, there is no space for individual fortification. Unless you and your partner are perfectly synergizedâ€”flowing seamlessly as one mindâ€”you must pursue your own growth at your own pace. It is extremely dangerous to have your recovery contingent upon someone else's possibly conditional love. Unconditional self-love is the only key that unlocks unconditional love for others.

### III. The Neurology of Habit: Muscle Memory and the "Bliss Point"
Your brain is a machine designed to automate as much as possible. This is "Muscle Memory." When you first learned to back out of a driveway, you had to consciously check every mirror and calibrate every movement. Now, you do it without thinking. 

This same automation is what kills you in recovery. When you bump into the homie you smoked with every day for five years at the same basketball court, your brain fires off a longing for "Bliss-Point." Your mind recognizes the context, the person, and the location as a state where you were once "safe" and "well." It will encourage you to pursue that neurotransmitter reconfiguration even when it is factually wrong. You must identify these subconscious triggers and intentionally rewire them through the **Neuroplasticity Window.**

### IV. Fundamental Disciplines: Resisting the Impulse
In addiction, you eschew every **Fundamental Discipline**â€”the things you know you should do that require force of will. Your only discipline becomes "get well at all costs." Your body-mind associates the absence of the drug with total annihilation.

By resisting every single impulseâ€”waking up at 5:00 AM without the snooze button, hitting a liter of water every three hours, attending treatment 20 minutes earlyâ€”you build the muscle of resistance. Every impulse resisted increases your ability to focus and think strategically. You are teaching your brain that it is no longer a slave to its own chemical whims.

### V. The Physical Engine: Hacking the Baseline
Early recovery is a fight-or-flight state. You feel like you are always on a mission; silence is awkward, and non-productive interactions feel empty. You can hack this baseline through specific physical conditioning:

1.  **Zone 2 Cardio:** 60% of your maximum heart rate. This increases the amount of **Mitochondria** in your systemâ€”the engines that metabolize energy. This increases your capacity for work and elevates your average mood.
2.  **HIIT (High-Intensity Interval Training):** Alternating between Zone 2 and Zone 4/5. This forces the body to synthesize the chemicals required for high-tier performance without the aid of stimulants.
3.  **Novel Experiences:** New neural pathways only grow when you experience new things. Martial arts, coding, and creative hobbies aren't just "fun"; they are neurological requirements for a brain that has been deadened by impulsive hedonism.

### VI. The ASDR Envelope of Dopamine
In sound engineering, every waveform has an envelope: **Attack, Sustain, Decay, and Release.** 
*   **Attack:** How fast the sound hits peak frequency.
*   **Sustain:** How long it holds that peak.
*   **Decay:** The drop from peak to a steady level.
*   **Release:** How long it lingers before returning to zero.

Drug use is a high-attack, high-decay waveform. It aggressively spikes dopamine and then crashes you into a negative baseline, leaving you with a desperate longing to return to the origin point. The goal of a "Synergistic Recovery" is to find activities with a **Slow Attack and a Gradual Release.** A steady increase to a moderate peak that returns you to a baseline equal to or higher than where you started. This is the difference between addiction and fulfillment.

### VII. Systemic Leverage: The WCCC and Treatment
The Washington County Community Corrections Center (WCCC) is a scientifically calibrated environment for recovery. It forces the earliest "feats" of capability: getting out of bed to eat when your brain just wants to sleep and die. It provides the social calibration of peers with a similar trajectory. 

Treatment is the mandatory baseline. It provides the safe space for calibration and ensures you are making moves for the **Long Term**, not just the short-term hit of "instant gratification" success.

### VIII. The Pivot: My Story
I am five months sober. Before this, I hadn't been clean in 17 years. I lost my social circle, my relationship, and my old life. I chose to use drugs, and I am grateful for itâ€”because by overcoming them, I acquired a force of will I never could have imagined. 

I am now using this period of isolation to iterate upon myself relentlessly. My current routine is a 15-hour daily push:
*   **07:00:** Wake up.
*   **08:00:** Gym (1hr Cardio, 15m Strength).
*   **09:30:** Treatment (20 mins early).
*   **10:00 - 13:00:** Recovery Groups.
*   **13:00 - 16:00:** School / Coding.
*   **17:00:** Gym Session 2 (Strength & HIIT).
*   **19:00:** Project Development / Systems Building.

**The Goal:** Synergize every factorâ€”Treatment, Physical Conditioning, Skill Acquisition, and Career Growthâ€”into a parallel engine. If one falters, the others sustain me. I am no longer a victim of circumstance; I am a laser, selecting my targets and slaughtering every objective in my path. 

**Let's find your jackpot.**


---

## Second Wind plus overall Mission Statement


--- Document: 0ProjectFolder\Second Wind\Second Wind plus overall Mission Statement.docx ---
Error reading 0ProjectFolder\Second Wind\Second Wind plus overall Mission Statement.docx: 'charmap' codec can't encode character '\u200b' in position 408: character maps to <undefined>

========================================

