(function() {
  var date, key, post, posted, timer, txt, txt_val;

  txt = $('#txt');

  date = new Date();

  posted = true;

  timer = 0;

  txt_val = '';

  post = function() {
    if (!posted && (txt_val !== txt.val())) {
      posted = false;
      $.post(location.href, {
        txt: txt.val()
      }, function() {
        posted = true;
        return txt_val = txt.val();
      });
    }
    timer && clearTimeout(timer);
    return timer = setTimeout(post, 3000);
  };

  key = function() {
    posted = false;
    return 1;
  };

  txt.keydown(key);

  txt.keyup(key);

  post();

  focus(txt[0]);

}).call(this);
