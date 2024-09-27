let EServiceIcon = document.getElementById('EServiceIcon');
let ServiceName = document.getElementById('EServiceName');
let ServiceDesc = document.getElementById('EServiceDesc');
let ServicePrice = document.getElementById('EServicePrice');

export function fetch4EditService(serviceId) {
    fetch(`fetch4editService/${serviceId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }, 
    })
    .then(response => response.json())
    .then(response => {
        if (response.status === 'success') {
            const context = response.context;              
            console.log(response);

            ServiceName.value = context.name;
            ServiceDesc.value = context.description;
            ServicePrice.value = context.price;
            EServiceIcon.src = context.icon;
        } else {
            console.error('Failed to fetch service details');
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}


