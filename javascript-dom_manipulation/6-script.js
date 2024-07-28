fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const character = document.querySelector('#character');
    character.textContent = data.name;
  })
  .catch(error => console.error('Error fetching data:', error));
