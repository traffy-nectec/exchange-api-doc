// Traffy Fondue Exchange API - Single Page Interaction

document.addEventListener('DOMContentLoaded', () => {
  // Category Filter
  const tabs = document.querySelectorAll('.filter-tab');
  const cards = document.querySelectorAll('.api-card');
  const searchInput = document.getElementById('apiSearch');

  let activeCategory = 'all';
  let searchQuery = '';

  function filterCards() {
    cards.forEach(card => {
      const cardCategory = card.dataset.category || '';
      const cardKeywords = (card.dataset.keywords || '').toLowerCase();
      const cardText = card.innerText.toLowerCase();

      const matchesCategory = (activeCategory === 'all') || (cardCategory === activeCategory);
      const matchesSearch = !searchQuery || cardKeywords.includes(searchQuery) || cardText.includes(searchQuery);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');
      activeCategory = tab.dataset.category;
      filterCards();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      filterCards();
    });
  }

  // Active Navbar on Scroll
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
      const sectionHeight = section.offsetHeight;
      const sectionTop = section.offsetTop - 120;
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
});

// Global Copy Code Function
window.copyCode = function(button) {
  const codeBlock = button.closest('.code-block-wrap').querySelector('code');
  if (!codeBlock) return;

  const textToCopy = codeBlock.innerText;
  navigator.clipboard.writeText(textToCopy).then(() => {
    const originalText = button.innerText;
    button.innerText = 'Copied!';
    button.style.backgroundColor = '#553924';
    button.style.color = '#FFFFFF';

    setTimeout(() => {
      button.innerText = originalText;
      button.style.backgroundColor = '';
      button.style.color = '';
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy: ', err);
  });
};
