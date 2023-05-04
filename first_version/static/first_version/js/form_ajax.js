// 「保存」ボタンがクリックされた時の処理
$('#save-btn').on('click', function() {

alert("in!!:$('#save-btn').on('click', function() ")
// プロフィールフォームの情報を取得
var profileFormData = $('#form_profile').serialize();
console.log("Profile form data: ", profileFormData);

// 投手フォームの情報を取得
var pitcherFormData = $('#form_pitcher').serialize();
console.log("Pitcher form data: ", pitcherFormData);

// 野手フォームの情報を取得
var fielderFormData = $('#form_fielder').serialize();
console.log("Fielder form data: ", fielderFormData);

// フォーム情報を送信する処理を記述する
$.ajax({
  type: "POST",
  url: '/first_version/create_player/',  // views.pyで定義されたURL
  beforeSend: function(xhr, settings) {
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  },
  data: {
    'profile': profileFormData,
    'pitcher': pitcherFormData,
    'fielder': fielderFormData
  },
  success: function(response) {
    // 成功した場合の処理
    alert("Success")
    // console.log(response);
  },
  error: function(xhr, status, error) {
    // エラーが発生した場合の処理
    alert("Error")
    console.log(xhr.responseText);
  }
});

});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');