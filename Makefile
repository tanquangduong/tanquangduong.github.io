.PHONY: render publish

render:
	quarto render
	python fix-sitemap.py

publish: render
	git add .
	git commit -m "Publish site to docs/"
	git push