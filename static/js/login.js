document.getElementById('toggle-password').addEventListener('click', function () {
    const input = document.getElementById('password-input');
    const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
    input.setAttribute('type', type);
    this.textContent = type === 'password' ? '👁️' : '🙈';
});

window.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.querySelector('input[name="email"]');
    if(emailInput) emailInput.focus();
});

document.querySelector('form.form-style').addEventListener('submit', function (e) {
    const submitButton = this.querySelector('button[type="submit"]');
    // Deshabilitar el botón para evitar múltiples envíos
    submitButton.disabled = true;
    // Opcional: cambiar el texto para indicar que se está procesando
    submitButton.textContent = 'Processing...';
});
