async function fetchTitle() {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    const movies = data.results;

    const list = document.getElementById('list_movies');

    movies.forEach(movie => {
      const node = document.createElement('li');
      const textnode = document.createTextNode(movie.title);
      node.appendChild(textnode);
      list.appendChild(node);
    });
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}

fetchTitle();
