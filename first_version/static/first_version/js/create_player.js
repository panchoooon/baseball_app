const mainPosition = document.querySelector('#id_main_position');

mainPosition.addEventListener('change', (event) => {
  const mainPosition = event.target.value;
  console.log('変更後の値：', mainPosition);
  alert('変更後の値：' + mainPosition);
  const id_change_position = '#id_' + mainPosition + '_appropriate';
  document.querySelector(id_change_position).value = '◎'
});