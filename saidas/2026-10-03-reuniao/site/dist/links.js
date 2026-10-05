(() => {
  const button = document.querySelector('.copy-address');
  const address = document.querySelector('#clinic-address');
  const status = document.querySelector('.copy-status');
  if (!button || !address || !status) return;
  button.addEventListener('click', async () => {
    const text = address.innerText.replace(/\n/g, ', ');
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      status.textContent = 'Endereço copiado!';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(address);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Endereço selecionado. Use a opção Copiar do seu dispositivo.';
    }
  });
})();
