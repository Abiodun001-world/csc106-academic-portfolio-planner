/* 
   COS 106 Academic Portfolio & Planner — vanilla JavaScript
   Modules: mobile nav, academic planner (localStorage), contact form validation
 */

document.addEventListener("DOMContentLoaded", function () {
  initMobileNav();
  initPlanner();
  initContactForm();
});

/* 
   Mobile hamburger menu
   Toggles the shared .site-nav on small screens.
 */
function initMobileNav() {
  let toggle = document.querySelector(".nav-toggle");
  let nav = document.querySelector(".site-nav");

  if (!toggle || !nav) {
    return;
  }

  toggle.addEventListener("click", function () {
    let isOpen = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

/* 
   Academic Planner — Task / To-Do manager
   Data model: array of { id, title, course, dueDate, priority, completed }
   Persistence: localStorage key "cos106-planner-tasks"
 */
let STORAGE_KEY = "cos106-planner-tasks";
let tasks = [];

function initPlanner() {
  let form = document.getElementById("task-form");
  if (!form) {
    return;
  }

  tasks = loadTasks();
  renderTasks();

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    addTaskFromForm(form);
  });

  document.getElementById("task-list").addEventListener("click", function (event) {
    let button = event.target.closest("[data-action]");
    if (!button) {
      return;
    }

    let id = button.getAttribute("data-id");
    let action = button.getAttribute("data-action");

    if (action === "toggle") {
      toggleTask(id);
    } else if (action === "delete") {
      deleteTask(id);
    }
  });
}

function loadTasks() {
  try {
    let raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch (error) {
    return [];
  }
}

function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function addTaskFromForm(form) {
  let titleInput = document.getElementById("task-title");
  let title = titleInput.value.trim();

  if (!title) {
    titleInput.focus();
    return;
  }

  let task = {
    id: String(Date.now()),
    title: title,
    course: document.getElementById("task-course").value.trim() || "General",
    dueDate: document.getElementById("task-due").value,
    priority: document.getElementById("task-priority").value,
    completed: false
  };

  tasks.unshift(task);
  saveTasks();
  form.reset();
  renderTasks();
}

function toggleTask(id) {
  tasks = tasks.map(function (task) {
    if (task.id === id) {
      return Object.assign({}, task, { completed: !task.completed });
    }
    return task;
  });
  saveTasks();
  renderTasks();
}

function deleteTask(id) {
  tasks = tasks.filter(function (task) {
    return task.id !== id;
  });
  saveTasks();
  renderTasks();
}

function renderTasks() {
  let list = document.getElementById("task-list");
  let empty = document.getElementById("empty-state");
  let totalEl = document.getElementById("stat-total");
  let doneEl = document.getElementById("stat-done");
  let openEl = document.getElementById("stat-open");

  let completedCount = tasks.filter(function (task) {
    return task.completed;
  }).length;

  totalEl.textContent = String(tasks.length);
  doneEl.textContent = String(completedCount);
  openEl.textContent = String(tasks.length - completedCount);

  list.innerHTML = "";

  if (tasks.length === 0) {
    empty.hidden = false;
    return;
  }

  empty.hidden = true;

  tasks.forEach(function (task) {
    let item = document.createElement("li");
    item.className = "task-item priority-" + task.priority + (task.completed ? " completed" : "");

    let dueLabel = task.dueDate ? formatDate(task.dueDate) : "No due date";

    item.innerHTML =
      '<input type="checkbox" data-action="toggle" data-id="' +
      task.id +
      '" ' +
      (task.completed ? "checked" : "") +
      ' aria-label="Mark task complete">' +
      "<div>" +
      '<p class="task-title"><strong>' +
      escapeHtml(task.title) +
      "</strong></p>" +
      '<p class="task-meta">' +
      escapeHtml(task.course) +
      " · " +
      dueLabel +
      " · " +
      task.priority +
      " priority</p>" +
      "</div>" +
      '<button type="button" class="btn btn-ghost" data-action="delete" data-id="' +
      task.id +
      '">Delete</button>';

    list.appendChild(item);
  });
}

function formatDate(isoDate) {
  let parts = isoDate.split("-");
  if (parts.length !== 3) {
    return isoDate;
  }
  return parts[2] + "/" + parts[1] + "/" + parts[0];
}

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function initContactForm() {
  let form = document.getElementById("contact-form");
  if (!form) {
    return;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    validateContactForm(form);
  });

  form.querySelectorAll(".control").forEach(function (field) {
    field.addEventListener("input", function () {
      field.classList.remove("error");
    });
  });
}

function validateContactForm(form) {
  let name = document.getElementById("contact-name");
  let email = document.getElementById("contact-email");
  let phone = document.getElementById("contact-phone");
  let message = document.getElementById("contact-message");
  let feedback = document.getElementById("form-feedback");
  let errors = [];

  [name, email, phone, message].forEach(function (field) {
    field.classList.remove("error");
  });

  if (!name.value.trim()) {
    errors.push("Name cannot be empty.");
    name.classList.add("error");
  }

  if (!email.value.trim()) {
    errors.push("Email address cannot be empty.");
    email.classList.add("error");
  } else if (!isValidEmail(email.value.trim())) {
    errors.push("Please enter a valid email address (example: name@school.edu).");
    email.classList.add("error");
  }

  if (!phone.value.trim()) {
    errors.push("Phone number cannot be empty.");
    phone.classList.add("error");
  } else if (!isDigitsOnly(phone.value.trim())) {
    errors.push("Phone number must contain digits only (no letters, spaces, or symbols).");
    phone.classList.add("error");
  }

  if (!message.value.trim()) {
    errors.push("Message cannot be empty.");
    message.classList.add("error");
  }

  if (errors.length > 0) {
    showFeedback(feedback, errors.join(" "), "error");
    return;
  }

  showFeedback(
    feedback,
    "Thank you, " + name.value.trim() + ". Your message has been validated successfully.",
    "success"
  );
  form.reset();
}

function isValidEmail(value) {
  let emailPattern = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
  return emailPattern.test(value);
}

function isDigitsOnly(value) {
  return /^\d+$/.test(value);
}

function showFeedback(element, text, type) {
  element.textContent = text;
  element.className = "form-message show " + type;
  element.setAttribute("role", type === "error" ? "alert" : "status");
}
