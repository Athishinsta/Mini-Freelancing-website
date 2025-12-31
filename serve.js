document.addEventListener('DOMContentLoaded', () => {
    const readMoreButtons = document.querySelectorAll('.read-more');
  
    readMoreButtons.forEach(button => {
        button.addEventListener('click', () => {
            document.querySelectorAll('.details-section').forEach(section => {
                section.style.display = 'none';
            });
  
            const targetId = button.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.style.display = 'block';
  
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
  });