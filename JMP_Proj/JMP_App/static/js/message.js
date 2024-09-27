document.addEventListener('DOMContentLoaded', function() {
    const messageService = document.getElementById('message-service2');

    if (messageService) { 
        
        setTimeout(() => {
            messageService.style.opacity = "1";
        }, 100); 
                
        setTimeout(() => {
            messageService.style.opacity = "0";
        }, 4000); 
    }
});

