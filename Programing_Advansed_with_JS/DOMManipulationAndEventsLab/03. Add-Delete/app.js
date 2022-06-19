function addItem() {
    let newElement = document.getElementById('newItemText');
    let list = document.getElementById('items');

    if ((newElement.value).length === 0) {
        return;
    }

    let listItem = document.createElement('li');
    listItem.textContent = newElement.value;

    let remove = document.createElement('a');
    let linkText = document.createTextNode('[Delete]');
    remove.appendChild(linkText);
    remove.href = '#';
    remove.addEventListener('click', deleteItem);

    listItem.appendChild(remove);
    list.appendChild(listItem);

    newElement.value = ''

    function deleteItem() {
       list.removeChild(listItem);
    }
}