# $^: liste des dependances
# $< premiere dependance 
# $@: cible

#CXX = pandoc --self-contained --toc -N 
#CSSFLAGS = -c $(CSSFILE)/pandoc.css
#CSSFLAGS = -c $(CSSFILE)/pandoc2.css
#CSSFILE = css

##### Creation du pdf/html au mm endroit que la source
# %.pdf: %.ipynb
# 	$(CXX) $(OPTPDF)  $<

# %.html: %.ipynb
# 	$(CXX) $(OPTHTML) $< 

##### La suite pour l'arborescence L1-Algo-Prog

# Generer tout html ou webpdf
#all: pdf
#all: html
all:book

# notebook par notebook
#NAME = 0-presentation-2022
#NAME = 1-fonctions
#NAME = 2-boucles-avancees
#NAME = 3-ES-fichiers
#NAME = 5-types_composes
#NAME = 6-recursivite
#NAME = 7-fonctions-avancees
#NAME = 8-rechercher
#NAME = 9-ES-avancees
#NAME = 10-trier
#NAME = 11-modules-utiles
#NAME = Competences-2021
#NAME = Complements-2021

# changer si necessaire
BOOKDIR = algoprog2023

# tous d'un coup
ALLSRC = $(wildcard  $(BOOKDIR)/cm/*.ipynb $(BOOKDIR)/cm/*.md $(BOOKDIR)/td/*.ipynb $(BOOKDIR)/td/*.md)

#--------------------------------------------------------------------
book: $(ALLSRC)
	@cd /Users/langlois/2023/ens/L1-Algo-Prog
	@jupyter-book build $(BOOKDIR)

enligne: $(ALLSRC)
	@cd /Users/langlois/2023/ens/L1-Algo-Prog
	@jupyter-book build $(BOOKDIR)
	@ghp-import -n -p -f $(BOOKDIR)/_build/html -m "version en ligne : maj"

tp: $(BOOKDIR)/$(wildcard tp2022/*.ipynb)
	@cd /Users/langlois/2023/ens/L1-Algo-Prog
	@run jupyter-book build tp2023
#--------------------------------------------------------------------

SRCDIR = cm
DESTDIRPDF = cm-webpdf
DESTDIRHTML = cm-html
SRC = $(SRCDIR)/$(NAME)

CXX = jupyter nbconvert 
OPTPDF =  --to webpdf --template classic --output-dir="$(DESTDIRPDF)"
OPTHTML= --to html_embed --HTMLExporter.theme=dark  --output-dir="$(DESTDIRHTML)"

$(SRC).pdf: $(SRC).ipynb
	@mkdir -p $(DESTDIRPDF)
	$(CXX) $(OPTPDF)  $< 

$(SRC).html: $(SRC).ipynb 
	@mkdir -p $(DESTDIRHTML)
	$(CXX) $(OPTHTML)  $<

%.pdf: $(SRCDIR)/%.ipynb
	@mkdir -p $(DESTDIRPDF)
	$(CXX) $(OPTPDF)  $<

%.html: $(SRCDIR)/%.ipynb
	@mkdir -p $(DESTDIRHTML)
	$(CXX) $(OPTHTML) $<

pdf: $(ALLSRC)
	@mkdir -p $(DESTDIRPDF)
	$(CXX) $(OPTPDF)  $^ 

html: $(ALLSRC)
	@mkdir -p $(DESTDIRHTML)
	$(CXX) $(OPTHTML)  $^ 

cleanpdf:
	@rm -rf $(DESTDIRPDF)

cleanhtml:
	@rm -rf $(DESTDIRHTML)

test:
	echo $(ALLSRC)
	echo $(ALLDESTDIRPDF)
	echo $(ALLPDF)

# $(DESTFILE): $(DESTNAME)
# 	@echo("fait")
# 	@mkdir -p $(DESTDIR)
# 	@mv $(DESTNAME) $(DESTDIR)
