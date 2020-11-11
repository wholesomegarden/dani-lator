

doctype html
html(lang="en")
	head
		title= pageTitle
		script(type='text/javascript').
			if (foo) bar(1 + 5)
	body
		h1 Pug - node template engine
		#container.col
			if youAreUsingPug
				p You are amazing
			else
				p Get on it!
			p.
				Pug is a terse and simple templating language with a
				strong focus on performance and powerful features.


html = xo.html
html.head.title = pageTitle
html.head.script("javascript"):
	if (foo) bar(1+5)

html.title = PageTile

body = html.body
body.h1("Pug - node template engine")
if youAreUsingPug
	body.p("You are amazing")
else
	body.p("You are amazing")
body.p("""
				Pug is a terse and simple templating language with a
				strong focus on performance and powerful features.
			""")




html = xo.html(lang="en").title()
html.head.title = pageTitle
html.head.script("javascript"):
	if (foo) bar(1+5)

body = html.body
body.h1("Pug - node template engine")
if youAreUsingPug
		body.p("You are amazing")
else
	body.p("You are amazing")
body.p("""
				Pug is a terse and simple templating language with a
				strong focus on performance and powerful features.
			""")


