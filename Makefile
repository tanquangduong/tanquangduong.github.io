.PHONY: render publish

render:
	quarto render

publish: 
	git add .
	git commit -m "Publish site to docs/"
	git push