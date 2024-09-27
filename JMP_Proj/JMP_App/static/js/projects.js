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


document.addEventListener('click', function (event) {

  if (!containerProject.contains(event.target)) {
    ProjectOverlay.style.display = "none";
    containerProject.classList.remove('show');

  }
});

/*
SubmitCaption.addEventListener('click', async function(){
    let ProjectObject = {
      project: ProjectPhoto.files[0],
      projectCaption: ProjectCaption.value, 
    }
    
    console.log(ProjectObject);
    
});
*/

