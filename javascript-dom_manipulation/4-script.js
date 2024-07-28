const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', () => {
  const ul = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  ul.appendChild(newItem);
});
