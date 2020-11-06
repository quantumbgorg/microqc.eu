TD_STRING = """
	<td style="padding: 5px 50px 5px 5px;">

		<div id="editablecontent">
			<div align="justify">
				<h1 style=font-size:16px>
					<a href="linkarticle">title</a>
				</h1>
			</div>
		
			<a href="linkarticle">
				<img alt="Qries" src="pictlink" width=500">
			</a>

		</div>
	</td>
"""

TR_STRING1 = """
<tr align="left" valign="top">"""
TR_STRING2 = """
</tr>
"""

TABLE_STRING_OPEN = "<table>"
TABLE_STRING_CLOSE = "</table>"


def replace_many(_str, dct):
	for old, new in dct.items():
		_str = _str.replace(old, new)
	return _str


def list_get(lst, idx, default=''):
	try:
		return lst[idx]
	except IndexError:
		return default


N_COLS = 3
# from news.sussex import TITLES, ARTICLE_LINKS, PICTURE_LINKS
# from news.leibnits import TITLES, ARTICLE_LINKS, PICTURE_LINKS
# from news.jerusalem import TITLES, ARTICLE_LINKS, PICTURE_LINKS
from news.siegen import TITLES, ARTICLE_LINKS, PICTURE_LINKS

html = ''
html += TABLE_STRING_OPEN
for idx in range(len(TITLES)):
	col = idx % N_COLS
	if col == 0:
		html += TR_STRING1
	html += replace_many(
		TD_STRING,
		{'title': list_get(TITLES, idx),
		'linkarticle': list_get(ARTICLE_LINKS, idx),
		'pictlink': list_get(PICTURE_LINKS, idx)}
		)
	if col == N_COLS - 1:
		html += TR_STRING2
html += TABLE_STRING_CLOSE

with open("NewsSiegen.html", "w") as text_file:
    print(html, file=text_file)