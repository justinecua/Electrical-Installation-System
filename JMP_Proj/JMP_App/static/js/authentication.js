
let username = document.getElementById('username');
let email = document.getElementById('email');
let password = document.getElementById('password');
let conpassword = document.getElementById('conpass');
let registerbtn = document.getElementById('register-btn');
let emaillgn = document.getElementById('Email-lgn');
let passlgn = document.getElementById('Pass-lgn');
let signInbtn = document.getElementById('SignIn-btn');

registerbtn.addEventListener('click', async(event) =>{
   event.preventDefault();

  if (username.checkValidity() && email.checkValidity() && password.checkValidity() && conpassword.checkValidity()){
    let signupObject = {
      username: username.value,
      email: email.value,
      password1: password.value,
      password2: conpassword.value,
    };
    console.log(signupObject);

    const { signup } = await import ("./requests/signup.js");
    signup(signupObject);

  } else {
    if (!username.checkValidity()) {
      username.reportValidity();
    }
    else if(!email.checkValidity()){
      email.reportValidity();
    }
    else if (!password.checkValidity()) {
      password.reportValidity();
    } else if (!conpassword.checkValidity()) {
      conpassword.reportValidity();
    }
  }
   
});


signInbtn.addEventListener('click', async(event)=>{
  event.preventDefault();
  if (emaillgn.checkValidity() && passlgn.checkValidity()) {
    let loginObject = {
      email: emaillgn.value,
      password: passlgn.value
    };
    console.log(loginObject);
    
    const { validatelogin } = await import ("./requests/login.js");
    validatelogin(loginObject);

  } else {
  if (!emaillgn.checkValidity()) {
    emaillgn.reportValidity();
  } else if (!passlgn.checkValidity()) {
    passlgn.reportValidity();
  }
  }
})
