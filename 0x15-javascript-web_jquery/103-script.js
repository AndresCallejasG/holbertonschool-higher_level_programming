$('document').ready(function () {
  $('input#btn_translate').on('click', getTranslation);
  $('input#language_code').on('keypress', function (event) {
    if (event.keyCode === 13) {
      getTranslation();
    }
  });

  function getTranslation () {
    const lCode = $('input#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lCode, function (data) {
      $('div#hello').text(data.hello);
    }, 'json');
  }
});
