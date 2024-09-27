let AddServiceBtn = document.getElementById('AddServiceBtn');
let ServiceOverlay = document.getElementById('Service-Overlay');
let containerService = document.querySelector('.containerService');
let ServiceIcon = document.getElementById('ServiceIcon');
let ServiceName = document.getElementById('ServiceName');
let ServiceDesc = document.getElementById('ServiceDesc');
let ServicePrice = document.getElementById('ServicePrice');
let SubmitService = document.getElementById('SubmitService');
let SCDelete = document.querySelectorAll('.SC-Delete');
let DelService = document.querySelectorAll('.Del-Service');
let DelServiceOverlay = document.getElementById('DelService-Overlay');
let DelcontainerService = document.querySelector('.DelcontainerService');
let EServiceOverlay = document.getElementById('EService-Overlay');
let EcontainerService = document.querySelector('.EcontainerService');
let CancelService = document.querySelectorAll('.Cancel-Service');
let SCEditBtn = document.querySelectorAll('.SC-Edit');
let EServiceIcon = document.getElementById('EServiceIcon');
let EServiceIconInput = document.getElementById('EServiceIconInput');
let EServiceName = document.getElementById('EServiceName');
let EServiceDesc = document.getElementById('EServiceDesc');
let EServicePrice = document.getElementById('EServicePrice');
let ESubmitService = document.getElementById('ESubmitService');

let selectedServiceId = null;
let selectedServiceIdE = null;

SCEditBtn.forEach((EditBtn) => {
    EditBtn.addEventListener('click', async function(event) {
        event.stopPropagation();
        selectedServiceIdE = EditBtn.getAttribute('data-serviceIdE');
        console.log(selectedServiceIdE);

        EServiceIcon.src = '';
        EServiceName.value = '';
        EServiceDesc.value = '';
        EServicePrice.value = '';

        EcontainerService.classList.add('show');
        EServiceOverlay.style.display = "flex";

        let { fetch4EditService } = await import ("./requests/fetch4EditService.js");
        if (selectedServiceIdE) {
            fetch4EditService(selectedServiceIdE);
        }
    });
});


AddServiceBtn.addEventListener('click', function(event){
  event.stopPropagation();
  containerService.classList.add('show');
  ServiceOverlay.style.display = "flex";
});

SCDelete.forEach((del) =>{
  del.addEventListener('click', function(event){
    event.stopPropagation();
    selectedServiceId = del.getAttribute('data-ServiceId');
    console.log(selectedServiceId);

    DelcontainerService.classList.add('show');
    DelServiceOverlay.style.display = "flex";
  });
});

DelService.forEach((delService) =>{
  delService.addEventListener('click', async function(event){
    event.stopPropagation();

    let { deleteService } = await import ("./requests/deleteService.js");
    if (selectedServiceId) {
      deleteService(selectedServiceId);
    }
  });
});

CancelService.forEach((cancel) => {
  cancel.addEventListener('click', function (event) {
    event.stopPropagation();

    DelcontainerService.classList.remove('show');
    DelServiceOverlay.style.display = "none";
  });
});

document.addEventListener('click', function(event) {

  if (!containerService.contains(event.target)) {
      ServiceOverlay.style.display = "none";
      containerService.classList.remove('show');
  }

   if (!DelcontainerService.contains(event.target)) {
      DelServiceOverlay.style.display = "none";
      DelcontainerService.classList.remove('show');
  }

  if (!EcontainerService.contains(event.target)) {
      EServiceOverlay.style.display = "none";
      EcontainerService.classList.remove('show');
  }

   if (!EcontainerService.contains(event.target)) {
      EServiceOverlay.style.display = "none";
      EcontainerService.classList.remove('show');

  }
});

SubmitService.addEventListener('click', async function(){

    let ServiceObject = {
      serviceIcon: ServiceIcon.files[0],
      serviceName: ServiceName.value,
      serviceDesc: ServiceDesc.value,
      servicePrice: ServicePrice.value,
    }

    let { saveService } = await import ("./requests/saveService.js");
    saveService(ServiceObject);

    console.log(ServiceObject);
});


/* --------FIX THISSSSSSSSSS-

ESubmitService.addEventListener('click', async function(event) {
  event.preventDefault();

  let NewEServiceIcon;
  let ServiceObject = {};

  if (EServiceIcon.src.indexOf("imagekit") !== -1) {
     ServiceObject = {
        serviceName: EServiceName.value,
        serviceDesc: EServiceDesc.value,
        servicePrice: EServicePrice.value,
    }
  } else  {

      NewEServiceIcon = EServiceIconInput.files[0];
      EServiceIcon.src = NewEServiceIcon;
      ServiceObject = {
        serviceIcon: NewEServiceIcon,
        serviceName: EServiceName.value,
        serviceDesc: EServiceDesc.value,
        servicePrice: EServicePrice.value,
    }
  }

  console.log(ServiceObject);
});



*/

