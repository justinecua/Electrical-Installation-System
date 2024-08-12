let AddServiceBtn = document.getElementById('AddServiceBtn');
let ServiceOverlay = document.getElementById('Service-Overlay');
let containerService = document.querySelector('.containerService');
let ServiceIcon = document.getElementById('ServiceIcon');
let ServiceName = document.getElementById('ServiceName');
let ServiceDesc = document.getElementById('ServiceDesc');
let ServicePrice = document.getElementById('ServicePrice');
let SubmitService = document.getElementById('SubmitService');

AddServiceBtn.addEventListener('click', function(event){
  event.stopPropagation();
  containerService.classList.add('show');
  ServiceOverlay.style.display = "flex";
})

document.addEventListener('click', function(event) {

  if (!containerService.contains(event.target)) {
      ServiceOverlay.style.display = "none";
      containerService.classList.remove('show');
  }

});

SubmitService.addEventListener('click', function(){

    let ServiceObject = {
      serviceIcon: ServiceIcon.files[0],
      serviceName: ServiceName.value,
      serviceDesc: ServiceDesc.value,
      servicePrice: ServicePrice.value,
    }
    console.log(ServiceObject);
})
