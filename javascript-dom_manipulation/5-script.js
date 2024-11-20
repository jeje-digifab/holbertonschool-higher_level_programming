const modifyText = document.getElementById('update_header');


modifyText.addEventListener('click', function () {

  const header = document.querySelector('header');


  header.innerHTML = 'New Header!!!';

})
