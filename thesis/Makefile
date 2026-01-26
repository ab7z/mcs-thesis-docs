# Makefile for LaTeX thesis
# UDP Transport Options (RFC 9868) - Master's Thesis

MAIN = main
LATEX = pdflatex
BIBTEX = bibtex
MAKEGLOSSARIES = makeglossaries

# LaTeX flags
LATEXFLAGS = -interaction=nonstopmode -halt-on-error

# Auxiliary file extensions to clean
AUX_EXT = aux bbl blg fls fdb_latexmk log out run.xml toc lof lot \
          synctex.gz acn acr alg glo gls glg ist nav snm vrb bcf

.PHONY: all pdf quick clean distclean view help

# Default target: full build
all: pdf

# Full build with bibliography and abbreviations
pdf: $(MAIN).tex
	@echo "=== First LaTeX pass ==="
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	@echo "=== Running BibTeX ==="
	-$(BIBTEX) $(MAIN)
	@echo "=== Running makeglossaries ==="
	-$(MAKEGLOSSARIES) $(MAIN)
	@echo "=== Second LaTeX pass ==="
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	@echo "=== Third LaTeX pass ==="
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	@echo "=== Build complete: $(MAIN).pdf ==="

# Quick build (single pass, no bibliography/glossary update)
quick: $(MAIN).tex
	@echo "=== Quick LaTeX build ==="
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex

# Clean auxiliary files
clean:
	@echo "=== Cleaning auxiliary files ==="
	rm -f $(foreach ext,$(AUX_EXT),$(MAIN).$(ext))
	rm -f $(MAIN)-blx.bib
	rm -f chapters/*.aux
	@echo "=== Clean complete ==="

# Full clean including PDF
distclean: clean
	@echo "=== Removing PDF ==="
	rm -f $(MAIN).pdf
	@echo "=== Distclean complete ==="

# Open PDF (macOS)
view: $(MAIN).pdf
	@open $(MAIN).pdf

# Help
help:
	@echo "LaTeX Thesis Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  all       - Full build with bibliography (default)"
	@echo "  pdf       - Same as 'all'"
	@echo "  quick     - Single LaTeX pass (fast, no bib update)"
	@echo "  clean     - Remove auxiliary files"
	@echo "  distclean - Remove auxiliary files and PDF"
	@echo "  view      - Open PDF in default viewer (macOS)"
	@echo "  help      - Show this help"
