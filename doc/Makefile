DOC := proyecto.tex

all: doc

doc: $(DOC:.tex=.pdf)

all: proyecto.pdf

%.pdf: %.tex
	pdflatex -shell-escape $< && bibtex $* && \
	pdflatex -shell-escape $< && pdflatex -shell-escape $<

clean:
	rm  proyecto.pdf *.aux *.blg *.log *.bbl *.toc *.out *.glg \
					 *.glo *.gls *.ist *.lof *.lot *.fls *.fdb_latexmk
