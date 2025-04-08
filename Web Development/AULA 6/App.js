const switchToggle = document.getElementById('switch-shadow');
const titleForm = document.getElementById('title-form');
const formFields = document.getElementById('form-fields');

function renderFormWithAnimation(isLogin) {
  // Aplica fade-out antes de trocar os campos
  formFields.classList.add('fade-out');

  setTimeout(() => {
    // Troca os campos
    if (isLogin) {
      titleForm.textContent = "Login";
      formFields.innerHTML = `
        <input type="email" name="email" placeholder="Seu email" required>
        <input type="password" name="senha" placeholder="Sua senha" required>
      `;
    } else {
      titleForm.textContent = "Cadastro";
      formFields.innerHTML = `
        <input type="text" name="nome" placeholder="Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <input type="password" name="senha" placeholder="Sua senha" required>
      `;
    }

    // Força reflow pra reiniciar animação (técnica comum)
    void formFields.offsetWidth;

    // Remove fade-out e adiciona fade-in
    formFields.classList.remove('fade-out');
    formFields.classList.add('fade-in');

    // Remove fade-in depois que terminar (pra evitar conflito)
    setTimeout(() => {
      formFields.classList.remove('fade-in');
    }, 300);
  }, 200);
}

// Listener do switch
switchToggle.addEventListener('change', () => {
  renderFormWithAnimation(switchToggle.checked);
});

// Inicializa com cadastro
renderFormWithAnimation(false);
