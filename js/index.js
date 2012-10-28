(function() {
  var date, fav, key, post, posted, timer, txt, txt_val;

  txt = $('#txt');

  date = new Date();

  posted = true;

  timer = 0;

  txt_val = '';

  fav = function(href) {
    var link;
    $('#favicon').remove();
    link = document.createElement('link');
    link.type = 'image/gif';
    link.rel = 'shortcut icon';
    link.id = 'favicon';
    link.href = href;
    return document.getElementsByTagName('head')[0].appendChild(link);
  };

  post = function() {
    if (!posted && (txt_val !== txt.val())) {
      posted = false;
      fav("/css/img/load.gif");
      $.post(location.href, {
        txt: txt.val()
      }, function() {
        fav("/css/img/fav.gif");
        posted = true;
        return txt_val = txt.val();
      });
    }
    timer && clearTimeout(timer);
    return timer = setTimeout(post, 3000);
  };

  key = function() {
    if (posted) {
      fav('/css/img/favicon.gif');
    }
    posted = false;
    return 1;
  };

  txt.keydown(key);

  txt.keyup(key);

  post();

  focus(txt[0]);

}).call(this);
