
let LoginBtn = document.getElementById('Login-btn');
let LoginOverlay = document.getElementById('Login-Overlay');
let container = document.querySelector('.container');
let containerSignUp = document.querySelector('.container-SignUp');
let SignUpBtn = document.getElementById('SignUp-btn');
let SignUpOverlay = document.getElementById('SignUp-Overlay');


LoginBtn.addEventListener('click', function(event){
  event.stopPropagation();
  container.classList.add('show');
  LoginOverlay.style.display = "flex";

})


SignUpBtn.addEventListener('click', function(event){
  event.stopPropagation();
  containerSignUp.classList.add('show');
  SignUpOverlay.style.display = "flex";

})

document.addEventListener('click', function(event) {

  if (!container.contains(event.target)) {
      LoginOverlay.style.display = "none";
      container.classList.remove('show');
  }

  if (!containerSignUp.contains(event.target)) {
    SignUpOverlay.style.display = "none";
    containerSignUp.classList.remove('show');

}

});
