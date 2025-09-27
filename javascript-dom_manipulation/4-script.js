const addBtn = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');

addBtn.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
