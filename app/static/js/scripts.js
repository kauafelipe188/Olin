// Seleciona todos os itens do projeto
const projectItems = document.querySelectorAll('.project-item');

// Seleciona o modal e a sobreposição
const modal = document.querySelector('.modal');
const modalOverlay = document.querySelector('.modal-overlay');
const modalCloseBtn = document.querySelector('.modal .close-btn');

// Função para abrir o modal
function openModal(title, description, startDate, endDate) {
    document.getElementById("modal-title").textContent = title;
    document.getElementById("modal-description").textContent = description;
    document.getElementById("modal-start-date").textContent = startDate;
    document.getElementById("modal-end-date").textContent = endDate;
    modal.style.display = 'block';
    modalOverlay.style.display = 'block';
}

// Função para fechar o modal
function closeModal() {
    modal.style.display = 'none';
    modalOverlay.style.display = 'none';
}

// Adiciona evento de clique nos itens do projeto
projectItems.forEach((item) => {
    item.addEventListener('click', () => {
        const title = item.querySelector('h2').textContent;
        const description = item.querySelector('p').textContent;
        const startDate = item.querySelector('.start-date').textContent;
        const endDate = item.querySelector('.end-date').textContent;

        openModal(title, description, startDate, endDate);
    });
});

// Fecha o modal quando clicar no botão fechar ou fora do modal
modalCloseBtn.addEventListener('click', closeModal);
modalOverlay.addEventListener('click', closeModal);
