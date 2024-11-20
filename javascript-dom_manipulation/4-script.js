const addList = document.getElementById('add_item');

addList.addEventListener('click', function () {
  const node = document.createElement('li');

  const textnode = document.createTextNode('Item');

  const list = document.querySelector('.my_list');

  node.appendChild(textnode);

  list.appendChild(node);

})
