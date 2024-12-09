// Seleciona todos os itens do projeto/serviço
const projectItems = document.querySelectorAll('.project-item, .service-item');

// Seleciona o modal e a sobreposição
const modal = document.querySelector('.modal');
const modalOverlay = document.querySelector('.modal-overlay');
const modalCloseBtn = document.querySelector('.modal .close-btn');

// Função para abrir o modal
function openModal(content) {
    modal.querySelector('h3').textContent = content.title;
    modal.querySelector('p').textContent = content.description;
    modal.querySelector('img').src = content.image;
    modal.style.display = 'block';
    modalOverlay.style.display = 'block';
}

// Função para fechar o modal
function closeModal() {
    modal.style.display = 'none';
    modalOverlay.style.display = 'none';
}

// Adiciona evento de clique nos itens
projectItems.forEach((item, index) => {
    item.addEventListener('click', () => {
        const content = {
            title: `Título do Projeto ${index + 1}`, // Substituir pelo conteúdo real
            description: `Descrição detalhada do projeto/serviço ${index + 1}.`,
            image: `https://via.placeholder.com/300` // Substituir pela URL real
        };
        openModal(content);
    });
});

// Fecha o modal quando clicar no botão fechar ou fora do modal
modalCloseBtn.addEventListener('click', closeModal);
modalOverlay.addEventListener('click', closeModal);
