$(document).ready(function(){
  $('.nav-link').click(function(){
    $('.nav-link').removeClass('active');
    $(this).addClass('active');
    var tabId = $(this).attr('data-tab');
    $('.tab-pane').removeClass('show active'); // 修正点: 全てのタブの表示を非表示にする
    $('#' + tabId).addClass('show active'); // 修正点: 選択されたタブのコンテンツを表示
  });
});

// 「野手基本能力チャート」ここから
let fielderBasicAbility = document.getElementById('fielder_basic').value;
fielderBasicAbility = JSON.parse(fielderBasicAbility); //オブジェクト型配列へパースする

var mydata = {
  labels: ["ミート", "パワー", "選球眼", "走力", "肩力","送球","打球反応", "捕球精度"],
  datasets: [
    {
      label: '野手能力',
      hoverBackgroundColor: "rgba(255,99,132,0.3)",
      // data: [525, 910, 676, 350, 710, 510, 590],
      data: fielderBasicAbility,

      backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)',
      ],
      borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
      ],
      borderWidth: 1
    }
  ]
};

//「オプション設定」
var options = {
  title: {    
    display: true,
    text: 'サンプルチャート'
  }
};

var ctx = document.getElementById('fielderAbility_chart');
var myChart = new Chart(ctx, {
  type: 'bar', //棒グラフ
  data:mydata, //データ設定 
  options:options  //オプション設定,
});

// 「野手基本能力チャート」ここまで
////////////////////////////////////////////////////////////////
// 「野手基本能力チャート」ここから
let fielderSpecialAbility = document.getElementById('fielder_special').value;
fielderSpecialAbility = JSON.parse(fielderSpecialAbility); //オブジェクト型配列へパースする

document.getElementById('chance').
  style.backgroundColor = 'pink';

// 「野手基本能力チャート」ここまで