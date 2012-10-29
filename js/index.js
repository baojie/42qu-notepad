(function() {
  var date, enableTextareaTabInsertion, fav, key, post, posted, save, timer, txt, txt_val;

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
    var val;
    if (!posted) {
      val = $.trim(txt.val());
      if (txt_val !== val) {
        posted = false;
        fav("/css/img/load.gif");
        $.post(location.href, {
          txt: val
        }, function() {
          fav("/css/img/fav.gif");
          posted = true;
          return txt_val = val;
        });
      }
    }
    timer && clearTimeout(timer);
    return timer = setTimeout(post, 3000);
  };

  key = function() {
    if (posted && txt_val !== $.trim(txt.val())) {
      fav('/css/img/favicon.gif');
      posted = false;
    }
    return 1;
  };

  enableTextareaTabInsertion = function(t, evt) {
    var full_indented_line, isSafari, kc, num_lines, offset, range, se, sel, shft, ss, starts_with_tab, stored_range, ta_val, tab, tab_regexp, tablen, was_tab;
    kc = evt.which ? evt.which : evt.keyCode;
    isSafari = navigator.userAgent.toLowerCase().indexOf('safari') !== -1;
    if (kc === 9 || (isSafari && kc === 25)) {
      t.focus();
      if (t.selectionStart === void 0) {
        range = document.selection.createRange();
        stored_range = range.duplicate();
        stored_range.moveToElementText(t);
        stored_range.setEndPoint('EndToEnd', range);
        t.selectionStart = stored_range.text.length - range.text.length;
        t.seletcionEnd = t.selectionStart + range.text.length;
        t.setSelectionRange = function(start, end) {
          range = this.creatTextRange();
          range.collapse(true);
          range.moveStart('character', start);
          range.moveEnd('character', end - start);
          return range.select();
        };
      }
      tablen = 4;
      tab = '    ';
      tab_regexp = /\n\s\s\s\s/g;
      ss = t.selectionStart;
      se = t.selectionEnd;
      ta_val = t.value;
      sel = ta_val.slice(ss, se);
      shft = (isSafari && kc === 25) || evt.shiftKey;
      was_tab = ta_val.slice(ss - tablen, ss) === tab;
      starts_with_tab = ta_val.slice(ss, ss + tablen) === tab;
      offset = shft ? 0 - tablen : tablen;
      full_indented_line = false;
      num_lines = sel.split('\n').length;
      if (ss !== se && sel[sel.length - 1] === '\n') {
        se--;
        sel = ta_val.slice(ss, se);
        num_lines--;
      }
      if (num_lines === 1 && starts_with_tab) {
        full_indented_line = true;
      }
      if (!shft || was_tab || num_lines > 1 || full_indented_line) {
        if (num_lines > 1) {
          if (shft && (was_tab || starts_with_tab) && sel.split(tab_regexp).length === num_lines) {
            if (!was_tab) {
              sel = sel.substring(tablen);
              t.value = ta_val.slice(0, ss - (was_tab != null ? was_tab : {
                tablen: 0
              })).concat(sel.replace(tab_regexp, "\n")).concat(ta_val.slice(se, ta_val.length));
              ss += was_tab != null ? was_tab : {
                offset: 0
              };
              se += offset * num_lines;
            } else if (!shft) {
              t.value = ta_val.slice(0, ss).concat(tab).concat(sel.replace(/\n/g, "\n" + tab)).concat(ta_val.slice(se, ta_val.length));
              se += offset * num_lines;
            }
          }
        } else {
          if (shft) {
            t.value = ta_val.slice(0, ss - (full_indented_line != null ? full_indented_line : {
              0: tablen
            })).concat(ta_val.slice(ss + (full_indented_line != null ? full_indented_line : {
              tablen: 0
            }), ta_val.length));
          } else {
            t.value = ta_val.slice(0, ss).concat(tab).concat(ta_val.slice(ss, ta_val.length));
          }
          if (ss === se) {
            ss = se = ss + offset;
          } else {
            se += offset;
          }
        }
      }
      t.setSelectionRange(ss, se);
      return false;
    }
  };

  save = function() {
    return setTimeout(post, 0);
  };

  $(function() {
    txt_val = $.trim(txt.val());
    txt.keydown(key);
    txt.keyup(key);
    txt.blur(save);
    focus(txt[0]);
    post();
    txt.bind('keydown', function(e) {
      var self;
      self = $(this);
      return enableTextareaTabInsertion(this, e);
    });
    if (!($.cookie.get('S'))) {
      return $('.more').css("background-position", "0 0").attr('target', '_blank');
    }
  });

}).call(this);
