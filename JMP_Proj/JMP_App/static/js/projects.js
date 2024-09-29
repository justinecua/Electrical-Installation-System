
let AddProjectsBtn = document.getElementById('AddProjectsBtn');
let ProjectOverlay = document.getElementById('Project-Overlay');
let containerProject = document.querySelector('.containerProject');
let SubmitCaption = document.getElementById('SubmitCaption');
let ProjectPhoto = document.getElementById('ProjectPhoto');
let ProjectCaption = document.getElementById('ProjectCaption');

AddProjectsBtn.addEventListener('click', function (event) {
  event.stopPropagation();
  containerProject.classList.add('show');
  ProjectOverlay.style.display = "flex";
});

const editButtons = document.querySelectorAll(".ProjectEdit-Btn");
const editModal = document.getElementById("EditProject-Overlay");
let containerEditProject = document.querySelector('.containerEditProject');

editButtons.forEach(button => {
  button.addEventListener("click", function (event) {
    event.stopPropagation();
    containerEditProject.classList.add('show');
    editModal.style.display = "flex";

    const projectId = this.getAttribute("data-id");
    const projectCaption = this.getAttribute("data-caption");

    document.getElementById("editProjectId").value = projectId;
    document.getElementById("editProjectCaption").value = projectCaption;
  });
});

const deleteButtons = document.querySelectorAll(".DeleteProjParent");
const deleteModal = document.getElementById("DeleteProject-Overlay"); 
let containerDeleteProject = document.querySelector('.containerDeleteProject');  
let confirmDeleteBtn = document.querySelector('.Del-Project'); 
let cancelDeleteBtn = document.querySelector('.Cancel-Delete-Proj');

deleteButtons.forEach(button => {
  button.addEventListener('click', function (event) {
    event.stopPropagation();
    containerDeleteProject.classList.add('show');
    deleteModal.style.display = "flex";

    const projectId = this.closest('.DeleteProjParent').getAttribute('data-id');

    document.getElementById('deleteProjectId').value = projectId;
    console.log(projectId);

    const form = document.getElementById("deleteProjectForm");
    form.action = `/adminProjects/delete_project/${projectId}/`;

  });
});

cancelDeleteBtn.addEventListener('click', function (event) {
  event.stopPropagation();
  containerDeleteProject.classList.remove('show');
  deleteModal.style.display = 'none';
});


document.addEventListener('click', function (event) {
  if (!containerProject.contains(event.target)) {
    ProjectOverlay.style.display = "none";
    containerProject.classList.remove('show');
  }

  if (!containerEditProject.contains(event.target)) {
    editModal.style.display = "none";
    containerEditProject.classList.remove('show');
  }

  if (!containerDeleteProject.contains(event.target)) {
    deleteModal.style.display = "none";
    containerDeleteProject.classList.remove('show');
  }
});
