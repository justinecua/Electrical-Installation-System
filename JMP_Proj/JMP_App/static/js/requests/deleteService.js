let DelServiceOverlay = document.getElementById('DelService-Overlay');
let DelcontainerService = document.querySelector('.DelcontainerService');
let message = document.getElementById('message-service');
let MSMessage = document.getElementById('MS-Message');
let loader = document.querySelector('.loader4');

export function deleteService(serviceId){
  loader.style.display = 'flex';

  fetch(`deleteService/${serviceId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }, 
    })
    .then(response => response.json())
    .then(response => {
        if (response.status === 'success') {
          loader.style.display = 'none';
          
          const serviceContainer = document.querySelector(`.Service-Container .SC-Delete[data-serviceId='${serviceId}']`).closest('.Service-Container');
          if (serviceContainer) {
            serviceContainer.remove();
          }
          
          DelServiceOverlay.style.display = "none";
          DelcontainerService.classList.remove('show');

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
