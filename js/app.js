// Traffy Fondue Exchange API Portal Script

document.addEventListener('DOMContentLoaded', () => {
  // 1. Search Filter on Docs Page
  const docSearch = document.getElementById('docSearch');
  if (docSearch) {
    docSearch.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const cards = document.querySelectorAll('.api-card');
      
      cards.forEach(card => {
        const text = (card.innerText + ' ' + (card.dataset.keywords || '')).toLowerCase();
        if (text.includes(q)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }

  // 2. Mobile Endpoint Dropdown Select Jump
  const mobileSelect = document.getElementById('mobileEndpointSelect');
  if (mobileSelect) {
    mobileSelect.addEventListener('change', (e) => {
      const targetId = e.target.value;
      if (targetId) {
        const targetEl = document.querySelector(targetId);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }

  // 3. Active Sidebar Link Tracking (ScrollSpy)
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  if (sidebarLinks.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '-20% 0px -65% 0px',
      threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          sidebarLinks.forEach(link => {
            if (link.getAttribute('href') === `#${id}`) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
          if (mobileSelect) {
            mobileSelect.value = `#${id}`;
          }
        }
      });
    }, observerOptions);

    document.querySelectorAll('.api-card, .docs-section-group').forEach(el => {
      if (el.id) observer.observe(el);
    });
  }
});

// 4. Global Copy Code Function
window.copyCode = function(button) {
  const codeBlock = button.closest('.code-block-wrap').querySelector('pre code');
  if (!codeBlock) return;

  const textToCopy = codeBlock.innerText;
  navigator.clipboard.writeText(textToCopy).then(() => {
    const origText = button.innerText;
    button.innerText = 'Copied! ✓';
    button.style.color = '#4ADE80';
    setTimeout(() => {
      button.innerText = origText;
      button.style.color = '';
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy: ', err);
  });
};

// 5. Copy Plain Text (e.g. Base URL)
window.copyText = function(text, button) {
  navigator.clipboard.writeText(text).then(() => {
    const origText = button.innerText;
    button.innerText = 'Copied! ✓';
    setTimeout(() => {
      button.innerText = origText;
    }, 2000);
  });
};
