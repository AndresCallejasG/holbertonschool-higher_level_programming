$('document').ready(function () {
  $('input#btn_translate').click(function () {
    const lCode = $('input#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lCode, function (data) {
      $('div#hello').text(data.hello);
    }, 'json');
  });
});
