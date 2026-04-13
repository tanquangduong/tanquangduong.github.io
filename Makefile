.PHONY: render publish

render:
	quarto render

publish: render
	git add .
	git commit -m "Publish site to docs/"
	git push