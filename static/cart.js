
document.querySelectorAll('.card-type').forEach(function(card) {
    card.addEventListener('click', function() {
        
        if (this.classList.contains('selected')) {
            this.classList.remove('selected');
        } else {
            
            document.querySelectorAll('.card-type').forEach(function(otherCard) {
                otherCard.classList.remove('selected');
            });
            
            this.classList.add('selected');
        }
    });
});

const cardTypes = document.querySelectorAll('.card-type');
const selectedCardInput = document.createElement('input');
selectedCardInput.type = 'hidden';
selectedCardInput.name = 'selected_card'; 
const form = document.querySelector('form');
form.addEventListener('submit', function() {
    const selectedCard = document.querySelector('.card-type.selected');
    if (selectedCard) {
        selectedCardInput.value = selectedCard.querySelector('img').src;
    } else {
        selectedCardInput.value = '';
    }
    form.appendChild(selectedCardInput);
});
