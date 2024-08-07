let loader = document.querySelector('.loader2');
let message = document.getElementById('message-login');

export function validatelogin(loginObject) {
    loader.style.display = 'flex';
    fetch(`validatelogin/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: loginObject.email,
            password: loginObject.password,
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
