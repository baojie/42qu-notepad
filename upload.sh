PREFIX=$(cd "$(dirname "$0")"; pwd)

jitter $PREFIX/coffee $PREFIX/js &
python $PREFIX/css_js.py
svn add $PREFIX/build/*.css 
svn add $PREFIX/build/*.js 
svn ci -m f
ps x -u $USER|ack 'jitter'|awk  '{print $1}'|xargs kill -9 > /dev/null 2>&1
