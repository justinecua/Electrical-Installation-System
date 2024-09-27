let EServiceOverlay = document.getElementById('EService-Overlay');
let EcontainerService = document.querySelector('.EcontainerService');
let message = document.getElementById('message-service');
let MSMessage = document.getElementById('MS-Message');
let loader = document.querySelector('.loader4');

export function editService(serviceId){
  loader.style.display = 'flex';

  fetch(`editService/${serviceId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        if (response.status === 'success') {
          loader.style.display = 'none';


          EServiceOverlay.style.display = "none";

          message.classList.add('show');
          message.style.display = "flex";
          MSMessage.innerHTML = response.message;

          setTimeout(() => {
              message.classList.remove('show');
              message.style.display = "none";
          }, 2000);
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

}
