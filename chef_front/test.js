const authToken = 'YOUR_TOKEN_HERE'; // Replace with the actual token

document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname.endsWith("index.html")) {
        fetchRecipes();
    } else if (window.location.pathname.endsWith("chef.html")) {
        fetchChefs();
    }
});

function fetchRecipes() {
    fetch('http://localhost:8000/recipes/', {
        headers: {
            'Authorization': `Token ${authToken}`
        }
    })
    .then(response => response.json())
    .then(data => displayRecipes(data))
    .catch(error => console.error('Error fetching recipes:', error));
}

function displayRecipes(recipes) {
    const list = document.getElementById('recipes-list');
    list.innerHTML = '';
    recipes.forEach(recipe => {
        const item = document.createElement('div');
        item.classList.add('item');
        item.innerHTML = `<h3>${recipe.title}</h3><p>${recipe.description}</p>`;
        list.appendChild(item);
    });
}

function addRecipe() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const chef = document.getElementById('chef').value;

    fetch('http://localhost:8000/recipes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${authToken}`
        },
        body: JSON.stringify({ title, description, chef: parseInt(chef, 10) })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('title').value = '';
        document.getElementById('description').value = '';
        document.getElementById('chef').value = '';
        fetchRecipes(); // Refresh the list
    })
    .catch(error => console.error('Error adding recipe:', error));
}

function fetchChefs() {
    fetch('http://localhost:8000/chefs/', {
        headers: {
            'Authorization': `Token ${authToken}`
        }
    })
    .then(response => response.json())
    .then(data => displayChefs(data))
    .catch(error => console.error('Error fetching chefs:', error));
}

function displayChefs(chefs) {
    const list = document.getElementById('chefs-list');
    list.innerHTML = '';
    chefs.forEach(chef => {
        const item = document.createElement('div');
        item.classList.add('item');
        item.innerHTML = `<h3>${chef.name}</h3><p>Specialty: ${chef.specialty}</p>`;
        list.appendChild(item);
    });
}
