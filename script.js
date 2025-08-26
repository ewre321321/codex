async function loadProperties() {
    const response = await fetch('properties.json');
    const properties = await response.json();
    return properties;
}

function createCard(property) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
        <img src="${property.image}" alt="${property.title}" />
        <div class="card-content">
            <h3>${property.title}</h3>
            <p>${property.location}</p>
            <p>${property.price}</p>
            <button data-id="${property.id}" class="details-btn">Detaylar</button>
        </div>
    `;
    return card;
}

function renderProperties(list, container) {
    container.innerHTML = '';
    list.forEach(prop => {
        container.appendChild(createCard(prop));
    });
}

function openModal(property) {
    document.getElementById('modal-image').src = property.image;
    document.getElementById('modal-title').textContent = property.title;
    document.getElementById('modal-location').textContent = property.location;
    document.getElementById('modal-price').textContent = property.price;
    document.getElementById('modal-description').textContent = property.description;
    document.getElementById('modal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}

async function init() {
    const properties = await loadProperties();
    const listingsEl = document.getElementById('listings');
    renderProperties(properties, listingsEl);

    document.getElementById('search').addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const filtered = properties.filter(p =>
            p.title.toLowerCase().includes(term) ||
            p.location.toLowerCase().includes(term)
        );
        renderProperties(filtered, listingsEl);
    });

    listingsEl.addEventListener('click', (e) => {
        if (e.target.classList.contains('details-btn')) {
            const id = parseInt(e.target.getAttribute('data-id'));
            const property = properties.find(p => p.id === id);
            if (property) {
                openModal(property);
            }
        }
    });

    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('modal').addEventListener('click', (e) => {
        if (e.target.id === 'modal') {
            closeModal();
        }
    });
}

init();
