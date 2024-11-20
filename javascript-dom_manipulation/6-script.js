async function fetchCharacterName() {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    const characterName = data.name;

    const characterElement = document.getElementById('character');
    characterElement.textContent = characterName;
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}

fetchCharacterName();
