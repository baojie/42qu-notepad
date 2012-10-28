(function() {



  if (!$('#note-list').children().length) {
    $('.paging').html('尚无内容 , <a href="/">点此新建</a>');
    $('#note_list_loading').css('background', 'none');
  }

}).call(this);
