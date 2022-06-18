function addItem() {
    let newItem = document.getElementById('newItemText');
    let newElement = document.createElement('li');
    newElement.textContent = newItem.value;
    let parent = document.getElementById('items');

    if (newElement.textContent) {
        parent.appendChild(newElement);
    }
    
    newItem.value = '';
}