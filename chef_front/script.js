document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname.endsWith("index.html")) {
        fetchRecipes();
    } else if (window.location.pathname.endsWith("chef.html")) {
        fetchChefs();
    }
});

function fetchRecipes() {
    fetch('http://127.0.0.1:8000/api/recipes/')
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

    fetch('http://127.0.0.1:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token f3a7ffe43616de5d1ee11bb9c913174d6898206d'
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

        fetchRecipes();
    })
    .catch(error => console.error('Error adding recipe:', error));
}

function fetchChefs() {
    fetch('http://127.0.0.1:8000/api/chefs/')
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
