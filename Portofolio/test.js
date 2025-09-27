// script.js
const filterButtons = document.querySelectorAll('.filter-btn');
const skillItems = document.querySelectorAll('.skill-item');

filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const category = btn.dataset.category;
        
        skillItems.forEach(item => {
            if (category === 'all' || item.classList.contains(category)) {
                item.style.display = 'flex'; // Gunakan 'flex' atau 'block'
            } else {
                item.style.display = 'none';
            }
        });
    });
});