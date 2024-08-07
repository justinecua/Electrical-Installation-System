let loader = document.querySelector('.loader');
let message = document.getElementById('message-signup');

export function signup(signupObject) {
    loader.style.display = 'flex';
    fetch(`signup/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: signupObject.username,
            email: signupObject.email,
            pass: signupObject.password1,
            pass2: signupObject.password2,
        })
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            window.location.href = result.redirect;
        } else {
            loader.style.display = 'none';
            message.innerHTML = result.message;
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

}
