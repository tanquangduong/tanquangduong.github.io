.PHONY: render publish

render:
    quarto render

publish: render
    git add docs
    git commit -m "Publish site to docs/"
    git push