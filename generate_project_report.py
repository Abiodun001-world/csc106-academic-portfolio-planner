from fpdf import FPDF

OUTPUT = "CSC106-Project-Report.pdf"


def clean_text(value):
    return (
        value.replace("’", "'")
        .replace("–", "-")
        .replace("—", "-")
        .replace("“", '"')
        .replace("”", '"')
    )


class PDFReport(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(27, 58, 75)
        self.cell(0, 12, "CSC 106 Academic Portfolio & Planner", ln=True)
        self.ln(2)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(15, 118, 110)
        self.cell(0, 10, clean_text(title), ln=True)
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(18, 35, 46)
        self.multi_cell(0, 6, clean_text(text))
        self.ln(2)

    def code_block(self, code):
        self.set_font("Courier", "", 8)
        self.set_fill_color(245, 245, 245)
        self.multi_cell(0, 5, clean_text(code), border=1, fill=True)
        self.ln(3)


def build_report():
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.body_text(
        "This project report explains the structure, purpose, and interactivity of the academic portfolio site developed for CSC 106. The portfolio is a multi-page static website that presents the student’s identity, academic path, sample projects, and contact information. It was built using Cursor IDE, which supported rapid drafting, iterating, and debugging of the HTML, CSS, and JavaScript across the pages."
    )

    pdf.chapter_title("1. Overview of the project")
    pdf.body_text(
        "The site includes a Home page, About page, Projects page, Planner page, and Contact page. It uses shared navigation and footer sections across the site, plus a common stylesheet for design consistency. The project uses semantic HTML for structure, CSS Grid and Flexbox for layout, and vanilla JavaScript for the interactive features."
    )
    pdf.body_text(
        "The main files are index.html, about.html, projects.html, planner.html, contact.html, styles.css, and script.js. The build is intentionally lightweight and easy to understand, which makes it a strong teaching example for front-end web development fundamentals."
    )

    pdf.chapter_title("2. Home page")
    pdf.body_text(
        "The Home page is the landing page and introduction to the student portfolio. It contains a hero section with a profile image, the student’s name, role description, and a short introduction to the site. This gives the portfolio a strong first impression and establishes its purpose immediately."
    )
    pdf.code_block(
        "<section class=\"hero\" aria-labelledby=\"student-name\">\n  <img class=\"hero-photo\" src=\"images/profile.jpg\" alt=\"Portrait of Abiodun Adekunle\" />\n  <div>\n    <p class=\"kicker\">Welcome</p>\n    <h1 id=\"student-name\">Abiodun Adekunle</h1>\n    <p class=\"hero-role\">Software Engineering Student · CSC 106 Term Project</p>\n  </div>\n</section>"
    )
    pdf.body_text(
        "This section uses CSS classes such as hero, hero-photo, and hero-role to shape the appearance and spacing. The design keeps the student profile front and center, reinforcing the academic and personal identity of the site. The page also includes a short course introduction and a video player, which helps present the student’s work in a more engaging format."
    )

    pdf.chapter_title("3. About page")
    pdf.body_text(
        "The About page explains the student’s educational background, technical skills, and interests. It includes an academic table showing programme information, key focus areas, and programme periods. It also describes career goals and personal interests, giving the visitor a fuller picture of the student beyond the portfolio itself."
    )
    pdf.code_block(
        "<table class=\"edu-table\">\n  <thead>\n    <tr>\n      <th scope=\"col\">Institution</th>\n      <th scope=\"col\">Programme</th>\n      <th scope=\"col\">Focus</th>\n      <th scope=\"col\">Years</th>\n    </tr>\n  </thead>\n</table>"
    )
    pdf.body_text(
        "This layout makes academic history readable and professional. The skills list highlights abilities gained through coursework, including HTML, CSS, JavaScript, responsive design, and form validation. The hobbies section humanizes the page and shows that the student has broader interests beyond coding."
    )

    pdf.chapter_title("4. Projects page")
    pdf.body_text(
        "The Projects page presents work in a card-based grid. Each project card includes an image, a project title, a summary, technology tags, and links to a live demo or repository. This format is ideal for a portfolio because it communicates each project quickly and consistently."
    )
    pdf.code_block(
        "<article class=\"project-card\">\n  <img src=\"images/project1.png\" alt=\"StudyFlow dashboard preview\" />\n  <div class=\"project-body\">\n    <h2>StudyFlow Dashboard</h2>\n    <p>A course overview board that groups weekly lectures, lab hours, and assignment checkpoints.</p>\n    <div class=\"tags\">\n      <span class=\"tag\">HTML</span>\n      <span class=\"tag\">CSS Grid</span>\n      <span class=\"tag\">JavaScript</span>\n    </div>\n  </div>\n</article>"
    )
    pdf.body_text(
        "The project cards are responsive and adapt to smaller screens, which makes the page usable on mobile devices. This is especially important for student portfolios because recruiters and visitors often browse from phones."
    )

    pdf.chapter_title("5. Contact page")
    pdf.body_text(
        "The Contact page contains a message form and an aside that lists other ways to reach the student. The form collects the user’s name, email, phone number, and message. This makes it easy for potential collaborators or instructors to get in touch."
    )
    pdf.code_block(
        "<form id=\"contact-form\" novalidate>\n  <input class=\"control\" id=\"contact-name\" type=\"text\" />\n  <input class=\"control\" id=\"contact-email\" type=\"email\" />\n  <input class=\"control\" id=\"contact-phone\" type=\"tel\" />\n  <textarea class=\"control\" id=\"contact-message\"></textarea>\n  <button class=\"btn btn-primary\" type=\"submit\">Send message</button>\n</form>"
    )
    pdf.body_text(
        "The page intentionally reminds the user that the message is checked in the browser before acceptance. This demonstrates front-end validation and improves the user experience by preventing incomplete or malformed submission."
    )

    pdf.chapter_title("6. Interactivity added and how it works")
    pdf.body_text(
        "Several interactive behaviors were added to make the site feel modern and functional. The JavaScript file initializes the following features when the document is ready: the mobile menu, task planner, and contact-form validation. This setup prevents race conditions and ensures the elements exist before behavior is attached."
    )
    pdf.code_block(
        "document.addEventListener(\"DOMContentLoaded\", function () {\n  initMobileNav();\n  initPlanner();\n  initContactForm();\n});"
    )
    pdf.body_text(
        "This pattern is standard in vanilla JavaScript because it prevents errors that might happen if the script runs before the HTML is loaded. Once the DOM is ready, the functions attach event listeners and update the page dynamically."
    )

    pdf.chapter_title("Mobile menu")
    pdf.code_block(
        "function initMobileNav() {\n  let toggle = document.querySelector(\".nav-toggle\");\n  let nav = document.querySelector(\".site-nav\");\n\n  toggle.addEventListener(\"click\", function () {\n    let isOpen = nav.classList.toggle(\"open\");\n    toggle.setAttribute(\"aria-expanded\", isOpen ? \"true\" : \"false\");\n  });\n}"
    )
    pdf.body_text(
        "The mobile menu hides the navigation on smaller screens and reveals it when the user taps the hamburger button. The CSS class .site-nav.open controls the visibility, while aria-expanded keeps the button state meaningful for accessibility tools and assistive technology."
    )

    pdf.chapter_title("Academic planner")
    pdf.code_block(
        "let STORAGE_KEY = \"cos106-planner-tasks\";\n\nfunction saveTasks() {\n  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));\n}\n\nfunction loadTasks() {\n  let raw = localStorage.getItem(STORAGE_KEY);\n  return raw ? JSON.parse(raw) : [];\n}\n\nfunction toggleTask(id) {\n  tasks = tasks.map(function (task) {\n    if (task.id === id) {\n      return Object.assign({}, task, { completed: !task.completed });\n    }\n    return task;\n  });\n  saveTasks();\n  renderTasks();\n}"
    )
    pdf.body_text(
        "The planner allows students to keep track of assignments or study tasks. Each task includes a title, course, due date, priority, and completion status. Because the app stores items in localStorage, the list persists during browser refreshes and can act as a simple personal study dashboard."
    )

    pdf.chapter_title("Form validation")
    pdf.code_block(
        "function validateContactForm(form) {\n  let name = document.getElementById(\"contact-name\");\n  let email = document.getElementById(\"contact-email\");\n  let phone = document.getElementById(\"contact-phone\");\n\n  if (!name.value.trim()) {\n    errors.push(\"Name cannot be empty.\");\n    name.classList.add(\"error\");\n  }\n\n  if (!email.value.trim()) {\n    errors.push(\"Email address cannot be empty.\");\n  } else if (!isValidEmail(email.value.trim())) {\n    errors.push(\"Please enter a valid email address.\");\n  }\n}"
    )
    pdf.body_text(
        "The validation logic checks for missing fields, invalid email addresses, and phone numbers that contain letters or symbols. It also updates the interface with visual feedback to show whether the user’s input passed or failed validation. This is an important pattern for modern web forms because it reduces frustration and improves accuracy."
    )

    pdf.chapter_title("7. Styling and responsiveness")
    pdf.body_text(
        "The stylesheet uses CSS variables, grid layouts, and media queries to keep the site cohesive and responsive. The colour palette, typography, and card treatments are consistent across all pages, while responsive rules ensure the layout collapses gracefully on smaller screens."
    )
    pdf.code_block(
        ":root {\n  --color-ink: #12232e;\n  --color-navy: #1b3a4b;\n  --color-teal: #0f766e;\n  --color-gold: #c4a35a;\n  --color-cream: #f8f4ef;\n}\n\n.hero {\n  display: grid;\n  grid-template-columns: 280px 1fr;\n  gap: 2.5rem;\n}\n\n@media (max-width: 900px) {\n  .hero, .bio-grid, .project-grid {\n    grid-template-columns: 1fr;\n  }\n}"
    )
    pdf.body_text(
        "This CSS design keeps the site readable and professional without relying on external frameworks. It highlights the importance of semantic HTML pairing with thoughtful CSS for creating a polished front-end experience."
    )

    pdf.chapter_title("8. Cursor IDE and workflow")
    pdf.body_text(
        "This project was built using Cursor IDE, an AI-assisted coding environment. Cursor helped with generating initial markup, refining the design, troubleshooting JavaScript errors, and iterating on small improvements across the site. The workflow was efficient because changes could be tested quickly and adjusted without losing momentum."
    )
    pdf.body_text(
        "In a classroom assignment, using Cursor IDE demonstrated how AI-assisted development can support learning and iteration. It is especially helpful when designing a small portfolio project with several different page layouts and interactive features."
    )

    pdf.chapter_title("9. Conclusion")
    pdf.body_text(
        "This project is a comprehensive front-end portfolio that shows both design skill and coding understanding. The Home, About, Projects, and Contact sections each serve a distinct purpose, while the interactive JavaScript features add usability and real-world learning value. The result is a polished academic portfolio that reflects strong web development fundamentals and thoughtful user experience design."
    )
    pdf.body_text(
        "Overall, the project demonstrates how HTML structure, CSS styling, and JavaScript interactivity can work together to create a functional and professional portfolio website. It is accessible, responsive, and practical—qualities that are essential in modern front-end development."
    )

    pdf.output(OUTPUT)
    print(f"Generated PDF: {OUTPUT}")


if __name__ == "__main__":
    build_report()
