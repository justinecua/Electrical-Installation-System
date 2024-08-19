let loader = document.querySelector('.loader3');
let message = document.getElementById('message-service');
let MSMessage = document.getElementById('MS-Message');
let ServiceOverlay = document.getElementById('Service-Overlay');
let PLMMMid = document.querySelector('.PLMM-Mid');
let DelService = document.querySelectorAll('.Del-Service');
let DelServiceOverlay = document.getElementById('DelService-Overlay');
let DelcontainerService = document.querySelector('.DelcontainerService');

export function saveService(serviceObject) {
   loader.style.display = 'flex';

    const formData = new FormData();
    formData.append('serviceIcon', serviceObject.serviceIcon);
    formData.append('data', JSON.stringify({
        serviceName: serviceObject.serviceName,
        serviceDesc: serviceObject.serviceDesc,
        servicePrice: serviceObject.servicePrice,
    }));

    const options = {
        method: 'POST',
        body: formData,
    };

    fetch("saveService/", options)
        .then(response => {

            return response.json();
        })
        .then(response => {
            if (response.status === 'success') {
               console.log(response.message);
              loader.style.display = "none";
              ServiceOverlay.style.display = "none";
             
              message.classList.add('show');
              message.style.display = "flex"; 
              MSMessage.innerHTML = response.message;  
    
              setTimeout(() => {
                  message.classList.remove('show');
                  message.style.display = "none"; 
              }, 2000);
              
              let ServiceContainer = document.createElement('div');
              ServiceContainer.className = "Service-Container";
              let SCOptions = document.createElement('div'); 
              SCOptions.className = "SC-Options";
              let SCEdit = document.createElement('img');
              SCEdit.className = 'SC-Edit';
              SCEdit.src = "../../static/images/Edit-4-Line--Streamline-Mingcute.png";
              let SCDelete = document.createElement('img');
              SCDelete.className = 'SC-Delete';
              SCDelete.src = "../../static/images/Delete-3-Line--Streamline-Mingcute.png";
              SCDelete.setAttribute('data-serviceId', response.service.serviceId);
              SCOptions.appendChild(SCEdit);
              SCOptions.appendChild(SCDelete);
              ServiceContainer.appendChild(SCOptions);

              let SCImg = document.createElement('img');
              SCImg.className = "SC-Icon";
              SCImg.src = response.service.serviceIcon;
              let SCH3 = document.createElement('h3');
              SCH3.innerHTML = response.service.serviceName;
              let SCP = document.createElement('p');
              SCP.innerHTML = response.service.serviceDesc;
              ServiceContainer.appendChild(SCImg); 
              ServiceContainer.appendChild(SCH3);
              ServiceContainer.appendChild(SCP);
              
              let PLMMMidSub = document.createElement('div');
              PLMMMidSub.className = 'PLMM-MidSub';
              let PLMSpan1 = document.createElement('span');
              let PLMSpan2 = document.createElement('span');
              PLMSpan1.innerHTML = "Price: ₱" + response.service.servicePrice;
              PLMSpan2.innerHTML = "On: " + response.service.serviceDate;
              PLMSpan1.className = 'SC-Price';
              PLMSpan2.className = 'SC-Price';
              PLMMMidSub.appendChild(PLMSpan1);
              PLMMMidSub.appendChild(PLMSpan2);
              ServiceContainer.appendChild(PLMMMidSub);
              PLMMMid.appendChild(ServiceContainer);

              SCDelete.addEventListener('click', function(event) {
                  event.stopPropagation();
                  let ServiceId = SCDelete.getAttribute('data-serviceId');
                  console.log(ServiceId);

                  ServiceDelete(ServiceId);

                  DelcontainerService.classList.add('show');
                  DelServiceOverlay.style.display = "flex";
              });

              function ServiceDelete(serviceId) {
                  DelService.forEach((delService) => {
                      delService.addEventListener('click', async function(event) {
                          event.stopPropagation();

                          let { deleteService } = await import("./deleteService.js");
                          deleteService(serviceId);
                      });
                  });
              }

            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });

}
