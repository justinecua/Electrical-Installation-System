let AddProjectsBtn = document.getElementById('AddProjectsBtn');
let ProjectOverlay = document.getElementById('Project-Overlay');
let containerProject = document.querySelector('.containerProject');

AddProjectsBtn.addEventListener('click', function (event) {
  event.stopPropagation();
  containerProject.classList.add('show');
  ProjectOverlay.style.display = "flex";
});


document.addEventListener('click', function (event) {

  if (!containerProject.contains(event.target)) {
    ProjectOverlay.style.display = "none";
    containerProject.classList.remove('show');

  }
});