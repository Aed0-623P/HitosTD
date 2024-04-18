window.addEventListener('DOMContentLoaded', () => {
  const content = document.getElementsByClassName('content');
  const footer = document.getElementsByClassName('footer');

  const checkContentOverlay = () => {
    if (content.getBoundingClientRect().bottom >= footer.getBoundingClientRect().top) {
      footer.classList.add('hidden-footer');
    } else {
      footer.classList.remove('hidden-footer');
    }
  };

  window.addEventListener('resize', checkContentOverlay);
  window.addEventListener('scroll', checkContentOverlay);
  checkContentOverlay();
});
