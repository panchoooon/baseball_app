// メインポジションが変更されたら、変更先のポジション適正を◎に変更する。
const mainPosition = document.querySelector('#id_main_position');


mainPosition.addEventListener('change', (event) => {
  const mainPosition = event.target.value;
  console.log('変更後の値：', mainPosition);
  alert('変更後の値：' + mainPosition);
  const id_change_position = '#id_' + mainPosition + '_appropriate';
  document.querySelector(id_change_position).value = '◎'
});

// フォームの値が変更されたら実行される関数
function updateRank() {
  // 変更された値を取得
  var contact = $('#id_contact').val();

  // Ajaxリクエストを送信
  $.ajax({
    type: 'POST',
    url: 'create_player/',
    data: {
      'contact': contact,
    },
    success: function(data) {
      // サーバーから返されたJSONデータを解析
      var rank = data.rank;

      // ランクを表示する要素を更新
      $('#rank').text(rank);
    }
  });
}





