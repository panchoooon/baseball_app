$(document).ready(function(){
  $('.nav-link').click(function(){
    $('.nav-link').removeClass('active');
    $(this).addClass('active');
    var tabId = $(this).attr('data-tab');
    $('.tab-pane').removeClass('show active'); // 修正点: 全てのタブの表示を非表示にする
    $('#' + tabId).addClass('show active'); // 修正点: 選択されたタブのコンテンツを表示
  });
});