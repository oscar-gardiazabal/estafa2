cd /var/www/estafa2/osqa/locale/es/LC_MESSAGES/

iconv -f latin1  -t utf-8 django.po > messages.po
msgfmt -o messages.po
rm messages.po
rm django.mo
mv messages.mo django.mo